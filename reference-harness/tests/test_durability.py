from __future__ import annotations

import sqlite3
import tempfile
import unittest
from dataclasses import dataclass
from pathlib import Path

from agent_harness.durability import (
    AmbiguousEffectFailure,
    DurableTaskStore,
    IdempotencyConflictError,
    LeaseError,
    PermanentFailure,
    RetryableFailure,
    RetryPolicy,
    TaskState,
)


@dataclass
class MutableClock:
    value: float = 100.0

    def __call__(self) -> float:
        return self.value

    def advance(self, seconds: float) -> None:
        self.value += seconds


class DurableTaskStoreTests(unittest.TestCase):
    def test_duplicate_delivery_reuses_identity_and_rejects_changed_intent(self):
        with (
            tempfile.TemporaryDirectory() as directory,
            DurableTaskStore(Path(directory) / "tasks.sqlite3") as store,
        ):
            first = store.submit("request-1", {"amount": 10})
            duplicate = store.submit("request-1", {"amount": 10})

            self.assertEqual(first.task_id, duplicate.task_id)
            self.assertEqual(1, len(store.transitions(first.task_id)))
            with self.assertRaises(IdempotencyConflictError):
                store.submit("request-1", {"amount": 11})
            with self.assertRaises(IdempotencyConflictError):
                store.submit(
                    "request-1",
                    {"amount": 10},
                    retry_policy=RetryPolicy(max_attempts=4),
                )

    def test_retryable_timeout_waits_then_succeeds(self):
        clock = MutableClock()
        calls: list[int] = []
        with tempfile.TemporaryDirectory() as directory, DurableTaskStore(
            Path(directory) / "tasks.sqlite3", clock=clock
        ) as store:
            task = store.submit(
                "retry-1",
                {"prompt": "bounded"},
                retry_policy=RetryPolicy(initial_delay=2),
            )

            def activity(work):
                calls.append(work.attempt)
                if work.attempt == 1:
                    raise RetryableFailure("provider timeout")
                return {"answer": "complete"}

            waiting = store.run_once("worker-a", activity)
            assert waiting is not None
            self.assertEqual(TaskState.WAITING_RETRY, waiting.state)
            self.assertIsNone(store.run_once("worker-a", activity))

            clock.advance(2)
            completed = store.run_once("worker-a", activity)
            assert completed is not None

            self.assertEqual(TaskState.SUCCEEDED, completed.state)
            self.assertEqual([1, 2], calls)
            self.assertEqual({"answer": "complete"}, completed.result)
            self.assertEqual(
                [
                    "pending",
                    "running",
                    "waiting_retry",
                    "running",
                    "succeeded",
                ],
                [transition.to_state for transition in store.transitions(task.task_id)],
            )

    def test_permanent_validation_failure_is_not_retried(self):
        with (
            tempfile.TemporaryDirectory() as directory,
            DurableTaskStore(Path(directory) / "tasks.sqlite3") as store,
        ):
            task = store.submit("invalid-1", {"amount": -1})

            failed = store.run_once(
                "worker-a",
                lambda _: (_ for _ in ()).throw(
                    PermanentFailure("amount must be positive")
                ),
            )
            assert failed is not None

            self.assertEqual(TaskState.FAILED, failed.state)
            self.assertEqual(1, failed.attempt)
            self.assertIsNone(store.claim("worker-a"))
            error = store.task(task.task_id).error
            assert error is not None
            self.assertIn("PermanentFailure", error)

    def test_retry_exhaustion_fails_at_the_predeclared_attempt_limit(self):
        with (
            tempfile.TemporaryDirectory() as directory,
            DurableTaskStore(Path(directory) / "tasks.sqlite3") as store,
        ):
            task = store.submit(
                "retry-exhausted",
                {"provider": "unavailable"},
                retry_policy=RetryPolicy(max_attempts=2, initial_delay=0),
            )

            first = store.run_once(
                "worker-a",
                lambda _: (_ for _ in ()).throw(RetryableFailure("timeout")),
            )
            second = store.run_once(
                "worker-a",
                lambda _: (_ for _ in ()).throw(RetryableFailure("timeout")),
            )

            assert first is not None
            assert second is not None
            self.assertEqual(TaskState.WAITING_RETRY, first.state)
            self.assertEqual(TaskState.FAILED, second.state)
            self.assertEqual(2, second.attempt)
            self.assertIsNone(store.claim("worker-a"))
            self.assertEqual(
                "activity.retries_exhausted",
                store.transitions(task.task_id)[-1].reason,
            )

    def test_process_loss_recovers_expired_lease_and_fences_stale_work(self):
        clock = MutableClock()
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "tasks.sqlite3"
            with DurableTaskStore(path, clock=clock) as first_store:
                task = first_store.submit(
                    "crash-1",
                    {"operation": "index"},
                    retry_policy=RetryPolicy(initial_delay=1),
                )
                stale_work = first_store.claim("worker-before-crash", lease_seconds=5)
                assert stale_work is not None

            clock.advance(6)
            with DurableTaskStore(path, clock=clock) as recovered_store:
                recovered = recovered_store.recover_expired_leases()
                self.assertEqual(1, len(recovered))
                self.assertEqual(TaskState.WAITING_RETRY, recovered[0].state)
                with self.assertRaises(LeaseError):
                    recovered_store.complete(stale_work, {"unsafe": True})

                clock.advance(1)
                completed = recovered_store.run_once(
                    "worker-after-crash", lambda _: {"indexed": True}
                )
                assert completed is not None

                self.assertEqual(TaskState.SUCCEEDED, completed.state)
                self.assertEqual(2, completed.attempt)
                reasons = [
                    transition.reason
                    for transition in recovered_store.transitions(task.task_id)
                ]
                self.assertIn("lease.expired_retry", reasons)

    def test_two_connections_cannot_claim_the_same_task(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "tasks.sqlite3"
            with (
                DurableTaskStore(path) as first_store,
                DurableTaskStore(path) as second_store,
            ):
                task = first_store.submit("claim-1", {"work": "once"})

                first_claim = first_store.claim("worker-a")
                second_claim = second_store.claim("worker-b")

                assert first_claim is not None
                self.assertEqual(task.task_id, first_claim.task_id)
                self.assertIsNone(second_claim)
                self.assertEqual(
                    "worker-a", second_store.task(task.task_id).lease_owner
                )

    def test_idempotent_external_effect_survives_lost_response(self):
        clock = MutableClock()
        effects: dict[str, str] = {}
        invocations = 0
        with tempfile.TemporaryDirectory() as directory, DurableTaskStore(
            Path(directory) / "tasks.sqlite3", clock=clock
        ) as store:
            store.submit(
                "effect-1",
                {"recipient": "learner"},
                retry_policy=RetryPolicy(initial_delay=0),
            )

            def activity(work):
                nonlocal invocations
                invocations += 1
                if work.idempotency_key not in effects:
                    effects[work.idempotency_key] = "receipt-1"
                    raise RetryableFailure("response lost after effect")
                return {"receipt": effects[work.idempotency_key]}

            first = store.run_once("worker-a", activity)
            second = store.run_once("worker-a", activity)
            assert first is not None
            assert second is not None

            self.assertEqual(TaskState.WAITING_RETRY, first.state)
            self.assertEqual(TaskState.SUCCEEDED, second.state)
            self.assertEqual(2, invocations)
            self.assertEqual(1, len(effects))

    def test_ambiguous_effect_requires_documented_manual_resolution(self):
        with (
            tempfile.TemporaryDirectory() as directory,
            DurableTaskStore(Path(directory) / "tasks.sqlite3") as store,
        ):
            task = store.submit("ambiguous-1", {"operation": "charge"})

            needs_repair = store.run_once(
                "worker-a",
                lambda _: (_ for _ in ()).throw(
                    AmbiguousEffectFailure("connection lost after send")
                ),
            )
            assert needs_repair is not None
            resolved = store.resolve_manual(
                task.task_id,
                outcome=TaskState.COMPENSATED,
                note="verified charge then issued refund receipt R-1",
            )

            self.assertEqual(TaskState.NEEDS_REPAIR, needs_repair.state)
            self.assertEqual(TaskState.COMPENSATED, resolved.state)
            transition = store.transitions(task.task_id)[-1]
            self.assertEqual("manual.resolution", transition.reason)
            self.assertIn("refund receipt", transition.metadata["note"])

    def test_pending_and_running_cancellation_are_explicit(self):
        with (
            tempfile.TemporaryDirectory() as directory,
            DurableTaskStore(Path(directory) / "tasks.sqlite3") as store,
        ):
            pending = store.submit("cancel-pending", {"work": 1})
            cancelled = store.request_cancel(
                pending.task_id, reason="learner requested stop"
            )
            self.assertEqual(TaskState.CANCELLED, cancelled.state)

            running = store.submit("cancel-running", {"work": 2})
            work = store.claim("worker-a")
            assert work is not None
            requested = store.request_cancel(
                running.task_id, reason="operator revoked authority"
            )
            acknowledged = store.acknowledge_cancellation(work)

            self.assertEqual(TaskState.RUNNING, requested.state)
            self.assertTrue(requested.cancel_requested)
            self.assertEqual(TaskState.CANCELLED, acknowledged.state)

    def test_incompatible_state_is_quarantined_not_executed(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "tasks.sqlite3"
            with DurableTaskStore(path) as store:
                task = store.submit("version-1", {"work": "migrate"})

            connection = sqlite3.connect(path)
            connection.execute(
                "UPDATE durable_tasks SET state_version = 999 WHERE task_id = ?",
                (task.task_id,),
            )
            connection.commit()
            connection.close()

            with DurableTaskStore(path) as store:
                self.assertIsNone(store.claim("worker-a"))
                quarantined = store.quarantine_incompatible()

                self.assertEqual(1, len(quarantined))
                self.assertEqual(TaskState.NEEDS_REPAIR, quarantined[0].state)
                error = quarantined[0].error
                assert error is not None
                self.assertIn("reader version", error)
                self.assertEqual(
                    "state.incompatible", store.transitions(task.task_id)[-1].reason
                )


if __name__ == "__main__":
    unittest.main()
