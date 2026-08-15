"""SQLite durability fixture with explicit at-least-once semantics."""

from __future__ import annotations

import hashlib
import json
import sqlite3
import time
from collections.abc import Callable, Iterator, Mapping
from contextlib import contextmanager
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Self
from uuid import uuid4

CURRENT_STATE_VERSION = 1


class TaskState(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    WAITING_RETRY = "waiting_retry"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"
    NEEDS_REPAIR = "needs_repair"
    COMPENSATED = "compensated"


TERMINAL_STATES = frozenset(
    {
        TaskState.SUCCEEDED,
        TaskState.FAILED,
        TaskState.CANCELLED,
        TaskState.COMPENSATED,
    }
)


class IdempotencyConflictError(ValueError):
    """Raised when one idempotency key is reused for different intent."""


class LeaseError(RuntimeError):
    """Raised when a stale or different worker attempts a state change."""


class TransitionError(RuntimeError):
    """Raised when a requested task-state transition is invalid."""


class RetryableFailure(RuntimeError):
    """Known transient or intermittent failure that policy may retry."""


class PermanentFailure(RuntimeError):
    """Known failure that unchanged input or code cannot repair by retrying."""


class AmbiguousEffectFailure(RuntimeError):
    """Failure where an external effect may have happened and needs reconciliation."""


@dataclass(frozen=True)
class RetryPolicy:
    max_attempts: int = 3
    initial_delay: float = 1.0
    backoff_multiplier: float = 2.0
    max_delay: float = 60.0

    def __post_init__(self) -> None:
        if self.max_attempts < 1:
            raise ValueError("max_attempts must be positive")
        if min(self.initial_delay, self.max_delay) < 0:
            raise ValueError("retry delays cannot be negative")
        if self.backoff_multiplier < 1:
            raise ValueError("backoff_multiplier cannot be less than one")

    def delay_after(self, attempt: int) -> float:
        if attempt < 1:
            raise ValueError("attempt must be positive")
        return min(
            self.initial_delay * self.backoff_multiplier ** (attempt - 1),
            self.max_delay,
        )


@dataclass(frozen=True)
class WorkItem:
    task_id: str
    idempotency_key: str
    intent_hash: str
    payload: dict[str, Any]
    attempt: int
    lease_token: str


@dataclass(frozen=True)
class TaskSnapshot:
    task_id: str
    idempotency_key: str
    intent_hash: str
    payload: dict[str, Any]
    state: TaskState
    state_version: int
    attempt: int
    max_attempts: int
    available_at: float
    lease_owner: str | None
    lease_expires_at: float | None
    cancel_requested: bool
    result: Any | None
    error: str | None


@dataclass(frozen=True)
class Transition:
    sequence: int
    task_id: str
    from_state: str | None
    to_state: str
    reason: str
    attempt: int
    at: float
    metadata: dict[str, Any]


Activity = Callable[[WorkItem], Any]
Clock = Callable[[], float]


class DurableTaskStore:
    """Single-process teaching queue with durable state and fenced leases."""

    def __init__(self, path: str | Path, *, clock: Clock = time.time) -> None:
        self.path = Path(path)
        self._clock = clock
        self._connection = sqlite3.connect(self.path)
        self._connection.row_factory = sqlite3.Row
        self._connection.execute("PRAGMA foreign_keys = ON")
        self._connection.execute("PRAGMA busy_timeout = 5000")
        self._connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS durable_tasks (
                task_id TEXT PRIMARY KEY,
                idempotency_key TEXT NOT NULL UNIQUE,
                intent_hash TEXT NOT NULL,
                payload_json TEXT NOT NULL,
                state TEXT NOT NULL,
                state_version INTEGER NOT NULL,
                attempt INTEGER NOT NULL,
                max_attempts INTEGER NOT NULL,
                initial_delay REAL NOT NULL,
                backoff_multiplier REAL NOT NULL,
                max_delay REAL NOT NULL,
                available_at REAL NOT NULL,
                lease_owner TEXT,
                lease_token TEXT,
                lease_expires_at REAL,
                cancel_requested INTEGER NOT NULL,
                result_json TEXT,
                error TEXT,
                created_at REAL NOT NULL,
                updated_at REAL NOT NULL
            );
            CREATE TABLE IF NOT EXISTS durable_transitions (
                task_id TEXT NOT NULL,
                sequence INTEGER NOT NULL,
                from_state TEXT,
                to_state TEXT NOT NULL,
                reason TEXT NOT NULL,
                attempt INTEGER NOT NULL,
                at REAL NOT NULL,
                metadata_json TEXT NOT NULL,
                PRIMARY KEY (task_id, sequence),
                FOREIGN KEY (task_id) REFERENCES durable_tasks(task_id)
            );
            CREATE INDEX IF NOT EXISTS durable_tasks_ready
                ON durable_tasks(state, available_at, created_at);
            """
        )
        self._connection.commit()

    def close(self) -> None:
        self._connection.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()

    def submit(
        self,
        idempotency_key: str,
        payload: Mapping[str, Any],
        *,
        retry_policy: RetryPolicy | None = None,
    ) -> TaskSnapshot:
        if not idempotency_key.strip():
            raise ValueError("idempotency_key must be non-empty")
        if retry_policy is None:
            retry_policy = RetryPolicy()
        payload_json = _encode_payload(payload)
        intent_hash = _intent_hash(payload_json, retry_policy)
        now = self._clock()

        with self._immediate_transaction():
            existing = self._connection.execute(
                "SELECT * FROM durable_tasks WHERE idempotency_key = ?",
                (idempotency_key,),
            ).fetchone()
            if existing is not None:
                if existing["intent_hash"] != intent_hash:
                    raise IdempotencyConflictError(
                        "idempotency key was reused with different intent"
                    )
                return _snapshot(existing)

            task_id = str(uuid4())
            self._connection.execute(
                """
                INSERT INTO durable_tasks (
                    task_id, idempotency_key, intent_hash, payload_json,
                    state, state_version, attempt, max_attempts,
                    initial_delay, backoff_multiplier, max_delay, available_at,
                    lease_owner, lease_token, lease_expires_at, cancel_requested,
                    result_json, error, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, 0, ?, ?, ?, ?, ?, NULL, NULL,
                          NULL, 0, NULL, NULL, ?, ?)
                """,
                (
                    task_id,
                    idempotency_key,
                    intent_hash,
                    payload_json,
                    TaskState.PENDING.value,
                    CURRENT_STATE_VERSION,
                    retry_policy.max_attempts,
                    retry_policy.initial_delay,
                    retry_policy.backoff_multiplier,
                    retry_policy.max_delay,
                    now,
                    now,
                    now,
                ),
            )
            row = self._task_row(task_id)
            self._append_transition(
                row,
                from_state=None,
                to_state=TaskState.PENDING,
                reason="submitted",
                metadata={"state_version": CURRENT_STATE_VERSION},
                at=now,
            )
            return _snapshot(row)

    def task(self, task_id: str) -> TaskSnapshot:
        return _snapshot(self._task_row(task_id))

    def transitions(self, task_id: str) -> tuple[Transition, ...]:
        rows = self._connection.execute(
            """
            SELECT sequence, task_id, from_state, to_state, reason,
                   attempt, at, metadata_json
            FROM durable_transitions
            WHERE task_id = ?
            ORDER BY sequence
            """,
            (task_id,),
        ).fetchall()
        return tuple(
            Transition(
                sequence=int(row["sequence"]),
                task_id=str(row["task_id"]),
                from_state=row["from_state"],
                to_state=str(row["to_state"]),
                reason=str(row["reason"]),
                attempt=int(row["attempt"]),
                at=float(row["at"]),
                metadata=json.loads(row["metadata_json"]),
            )
            for row in rows
        )

    def claim(self, worker_id: str, *, lease_seconds: float = 30.0) -> WorkItem | None:
        if not worker_id.strip():
            raise ValueError("worker_id must be non-empty")
        if lease_seconds <= 0:
            raise ValueError("lease_seconds must be positive")
        now = self._clock()

        with self._immediate_transaction():
            row = self._connection.execute(
                """
                SELECT * FROM durable_tasks
                WHERE state_version = ?
                  AND state IN (?, ?)
                  AND available_at <= ?
                ORDER BY available_at, created_at, task_id
                LIMIT 1
                """,
                (
                    CURRENT_STATE_VERSION,
                    TaskState.PENDING.value,
                    TaskState.WAITING_RETRY.value,
                    now,
                ),
            ).fetchone()
            if row is None:
                return None

            lease_token = str(uuid4())
            attempt = int(row["attempt"]) + 1
            lease_expires_at = now + lease_seconds
            self._replace_mutable(
                row,
                state=TaskState.RUNNING,
                attempt=attempt,
                available_at=float(row["available_at"]),
                lease_owner=worker_id,
                lease_token=lease_token,
                lease_expires_at=lease_expires_at,
                cancel_requested=False,
                result_json=row["result_json"],
                error=None,
                updated_at=now,
            )
            self._append_transition(
                row,
                from_state=str(row["state"]),
                to_state=TaskState.RUNNING,
                reason="claimed",
                metadata={
                    "worker_id": worker_id,
                    "lease_expires_at": lease_expires_at,
                },
                at=now,
                attempt=attempt,
            )
            return WorkItem(
                task_id=str(row["task_id"]),
                idempotency_key=str(row["idempotency_key"]),
                intent_hash=str(row["intent_hash"]),
                payload=json.loads(row["payload_json"]),
                attempt=attempt,
                lease_token=lease_token,
            )

    def run_once(
        self,
        worker_id: str,
        activity: Activity,
        *,
        lease_seconds: float = 30.0,
    ) -> TaskSnapshot | None:
        work = self.claim(worker_id, lease_seconds=lease_seconds)
        if work is None:
            return None
        if self.task(work.task_id).cancel_requested:
            return self.acknowledge_cancellation(work)

        try:
            result = activity(work)
            return self.complete(work, result)
        except RetryableFailure as exc:
            return self._record_failure(work, exc, TaskState.WAITING_RETRY)
        except PermanentFailure as exc:
            return self._record_failure(work, exc, TaskState.FAILED)
        except AmbiguousEffectFailure as exc:
            return self._record_failure(work, exc, TaskState.NEEDS_REPAIR)
        except Exception as exc:  # noqa: BLE001 - unknown activity failures need repair.
            return self._record_failure(work, exc, TaskState.NEEDS_REPAIR)

    def complete(self, work: WorkItem, result: Any) -> TaskSnapshot:
        result_json = _encode_json(result)
        now = self._clock()
        with self._immediate_transaction():
            row = self._owned_running_row(work, now)
            cancel_requested = bool(row["cancel_requested"])
            self._replace_mutable(
                row,
                state=TaskState.SUCCEEDED,
                attempt=int(row["attempt"]),
                available_at=float(row["available_at"]),
                lease_owner=None,
                lease_token=None,
                lease_expires_at=None,
                cancel_requested=cancel_requested,
                result_json=result_json,
                error=None,
                updated_at=now,
            )
            self._append_transition(
                row,
                from_state=TaskState.RUNNING.value,
                to_state=TaskState.SUCCEEDED,
                reason=(
                    "completed_after_cancel_request"
                    if cancel_requested
                    else "completed"
                ),
                metadata={},
                at=now,
            )
            return _snapshot(self._task_row(work.task_id))

    def request_cancel(self, task_id: str, *, reason: str) -> TaskSnapshot:
        if not reason.strip():
            raise ValueError("cancellation reason must be non-empty")
        now = self._clock()
        with self._immediate_transaction():
            row = self._task_row(task_id)
            state = TaskState(row["state"])
            if state in TERMINAL_STATES or state is TaskState.NEEDS_REPAIR:
                return _snapshot(row)

            if state in {TaskState.PENDING, TaskState.WAITING_RETRY}:
                target = TaskState.CANCELLED
                lease_owner = None
                lease_token = None
                lease_expires_at = None
            elif state is TaskState.RUNNING:
                target = TaskState.RUNNING
                lease_owner = row["lease_owner"]
                lease_token = row["lease_token"]
                lease_expires_at = row["lease_expires_at"]
            else:
                raise TransitionError(f"cannot request cancellation from {state.value}")

            self._replace_mutable(
                row,
                state=target,
                attempt=int(row["attempt"]),
                available_at=float(row["available_at"]),
                lease_owner=lease_owner,
                lease_token=lease_token,
                lease_expires_at=lease_expires_at,
                cancel_requested=True,
                result_json=row["result_json"],
                error=row["error"],
                updated_at=now,
            )
            self._append_transition(
                row,
                from_state=state.value,
                to_state=target,
                reason="cancel.requested",
                metadata={"reason": reason},
                at=now,
            )
            return _snapshot(self._task_row(task_id))

    def acknowledge_cancellation(self, work: WorkItem) -> TaskSnapshot:
        now = self._clock()
        with self._immediate_transaction():
            row = self._owned_running_row(work, now)
            if not bool(row["cancel_requested"]):
                raise TransitionError("cancellation has not been requested")
            self._replace_mutable(
                row,
                state=TaskState.CANCELLED,
                attempt=int(row["attempt"]),
                available_at=float(row["available_at"]),
                lease_owner=None,
                lease_token=None,
                lease_expires_at=None,
                cancel_requested=True,
                result_json=row["result_json"],
                error=row["error"],
                updated_at=now,
            )
            self._append_transition(
                row,
                from_state=TaskState.RUNNING.value,
                to_state=TaskState.CANCELLED,
                reason="cancel.acknowledged",
                metadata={},
                at=now,
            )
            return _snapshot(self._task_row(work.task_id))

    def recover_expired_leases(self) -> tuple[TaskSnapshot, ...]:
        now = self._clock()
        recovered: list[TaskSnapshot] = []
        with self._immediate_transaction():
            rows = self._connection.execute(
                """
                SELECT * FROM durable_tasks
                WHERE state_version = ?
                  AND state = ?
                  AND lease_expires_at <= ?
                ORDER BY lease_expires_at, task_id
                """,
                (CURRENT_STATE_VERSION, TaskState.RUNNING.value, now),
            ).fetchall()
            for row in rows:
                attempt = int(row["attempt"])
                if bool(row["cancel_requested"]):
                    target = TaskState.CANCELLED
                    available_at = float(row["available_at"])
                    reason = "lease.expired_cancelled"
                elif attempt < int(row["max_attempts"]):
                    target = TaskState.WAITING_RETRY
                    available_at = now + _retry_delay(row, attempt)
                    reason = "lease.expired_retry"
                else:
                    target = TaskState.NEEDS_REPAIR
                    available_at = float(row["available_at"])
                    reason = "lease.expired_attempts_exhausted"

                self._replace_mutable(
                    row,
                    state=target,
                    attempt=attempt,
                    available_at=available_at,
                    lease_owner=None,
                    lease_token=None,
                    lease_expires_at=None,
                    cancel_requested=bool(row["cancel_requested"]),
                    result_json=row["result_json"],
                    error="worker lease expired before a durable outcome",
                    updated_at=now,
                )
                self._append_transition(
                    row,
                    from_state=TaskState.RUNNING.value,
                    to_state=target,
                    reason=reason,
                    metadata={"previous_worker": row["lease_owner"]},
                    at=now,
                )
                recovered.append(_snapshot(self._task_row(str(row["task_id"]))))
        return tuple(recovered)

    def quarantine_incompatible(self) -> tuple[TaskSnapshot, ...]:
        now = self._clock()
        quarantined: list[TaskSnapshot] = []
        with self._immediate_transaction():
            rows = self._connection.execute(
                """
                SELECT * FROM durable_tasks
                WHERE state_version <> ? AND state <> ?
                ORDER BY created_at, task_id
                """,
                (CURRENT_STATE_VERSION, TaskState.NEEDS_REPAIR.value),
            ).fetchall()
            for row in rows:
                self._replace_mutable(
                    row,
                    state=TaskState.NEEDS_REPAIR,
                    attempt=int(row["attempt"]),
                    available_at=float(row["available_at"]),
                    lease_owner=None,
                    lease_token=None,
                    lease_expires_at=None,
                    cancel_requested=bool(row["cancel_requested"]),
                    result_json=row["result_json"],
                    error=(
                        f"state version {row['state_version']} is incompatible with "
                        f"reader version {CURRENT_STATE_VERSION}"
                    ),
                    updated_at=now,
                )
                self._append_transition(
                    row,
                    from_state=str(row["state"]),
                    to_state=TaskState.NEEDS_REPAIR,
                    reason="state.incompatible",
                    metadata={
                        "observed_version": int(row["state_version"]),
                        "reader_version": CURRENT_STATE_VERSION,
                    },
                    at=now,
                )
                quarantined.append(_snapshot(self._task_row(str(row["task_id"]))))
        return tuple(quarantined)

    def resolve_manual(
        self, task_id: str, *, outcome: TaskState, note: str
    ) -> TaskSnapshot:
        if outcome not in {TaskState.COMPENSATED, TaskState.FAILED}:
            raise ValueError("manual outcome must be compensated or failed")
        if not note.strip():
            raise ValueError("manual resolution note must be non-empty")
        now = self._clock()
        with self._immediate_transaction():
            row = self._task_row(task_id)
            if TaskState(row["state"]) is not TaskState.NEEDS_REPAIR:
                raise TransitionError("manual resolution requires needs_repair state")
            self._replace_mutable(
                row,
                state=outcome,
                attempt=int(row["attempt"]),
                available_at=float(row["available_at"]),
                lease_owner=None,
                lease_token=None,
                lease_expires_at=None,
                cancel_requested=bool(row["cancel_requested"]),
                result_json=row["result_json"],
                error=row["error"],
                updated_at=now,
            )
            self._append_transition(
                row,
                from_state=TaskState.NEEDS_REPAIR.value,
                to_state=outcome,
                reason="manual.resolution",
                metadata={"note": note},
                at=now,
            )
            return _snapshot(self._task_row(task_id))

    def _record_failure(
        self, work: WorkItem, failure: Exception, target: TaskState
    ) -> TaskSnapshot:
        now = self._clock()
        with self._immediate_transaction():
            row = self._owned_running_row(work, now)
            attempt = int(row["attempt"])
            if target is TaskState.WAITING_RETRY:
                if attempt < int(row["max_attempts"]):
                    available_at = now + _retry_delay(row, attempt)
                    reason = "activity.retry_scheduled"
                else:
                    target = TaskState.FAILED
                    available_at = float(row["available_at"])
                    reason = "activity.retries_exhausted"
            elif target is TaskState.FAILED:
                available_at = float(row["available_at"])
                reason = "activity.permanent_failure"
            else:
                available_at = float(row["available_at"])
                reason = "activity.ambiguous_or_unknown_failure"

            error = f"{type(failure).__name__}: {failure}"
            self._replace_mutable(
                row,
                state=target,
                attempt=attempt,
                available_at=available_at,
                lease_owner=None,
                lease_token=None,
                lease_expires_at=None,
                cancel_requested=bool(row["cancel_requested"]),
                result_json=row["result_json"],
                error=error,
                updated_at=now,
            )
            self._append_transition(
                row,
                from_state=TaskState.RUNNING.value,
                to_state=target,
                reason=reason,
                metadata={"error_type": type(failure).__name__},
                at=now,
            )
            return _snapshot(self._task_row(work.task_id))

    def _owned_running_row(self, work: WorkItem, now: float) -> sqlite3.Row:
        row = self._task_row(work.task_id)
        if TaskState(row["state"]) is not TaskState.RUNNING:
            raise LeaseError("task is no longer running")
        if row["lease_token"] != work.lease_token:
            raise LeaseError("work item does not own the current lease")
        if float(row["lease_expires_at"]) <= now:
            raise LeaseError("work-item lease has expired")
        return row

    def _task_row(self, task_id: str) -> sqlite3.Row:
        row = self._connection.execute(
            "SELECT * FROM durable_tasks WHERE task_id = ?", (task_id,)
        ).fetchone()
        if row is None:
            raise KeyError(f"unknown task: {task_id}")
        return row

    def _replace_mutable(
        self,
        row: sqlite3.Row,
        *,
        state: TaskState,
        attempt: int,
        available_at: float,
        lease_owner: str | None,
        lease_token: str | None,
        lease_expires_at: float | None,
        cancel_requested: bool,
        result_json: str | None,
        error: str | None,
        updated_at: float,
    ) -> None:
        self._connection.execute(
            """
            UPDATE durable_tasks
            SET state = ?, attempt = ?, available_at = ?, lease_owner = ?,
                lease_token = ?, lease_expires_at = ?, cancel_requested = ?,
                result_json = ?, error = ?, updated_at = ?
            WHERE task_id = ?
            """,
            (
                state.value,
                attempt,
                available_at,
                lease_owner,
                lease_token,
                lease_expires_at,
                int(cancel_requested),
                result_json,
                error,
                updated_at,
                row["task_id"],
            ),
        )

    def _append_transition(
        self,
        row: sqlite3.Row,
        *,
        from_state: str | None,
        to_state: TaskState,
        reason: str,
        metadata: Mapping[str, Any],
        at: float,
        attempt: int | None = None,
    ) -> None:
        sequence_row = self._connection.execute(
            """
            SELECT COALESCE(MAX(sequence), 0) + 1
            FROM durable_transitions
            WHERE task_id = ?
            """,
            (row["task_id"],),
        ).fetchone()
        self._connection.execute(
            """
            INSERT INTO durable_transitions (
                task_id, sequence, from_state, to_state, reason,
                attempt, at, metadata_json
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                row["task_id"],
                int(sequence_row[0]),
                from_state,
                to_state.value,
                reason,
                int(row["attempt"]) if attempt is None else attempt,
                at,
                _encode_json(dict(metadata)),
            ),
        )

    @contextmanager
    def _immediate_transaction(self) -> Iterator[None]:
        self._connection.execute("BEGIN IMMEDIATE")
        try:
            yield
        except BaseException:
            self._connection.rollback()
            raise
        else:
            self._connection.commit()


def _encode_payload(payload: Mapping[str, Any]) -> str:
    encoded = _encode_json(dict(payload))
    decoded = json.loads(encoded)
    if not isinstance(decoded, dict):
        raise TypeError("task payload must be a JSON object")
    return encoded


def _intent_hash(payload_json: str, retry_policy: RetryPolicy) -> str:
    intent_json = _encode_json(
        {
            "payload": json.loads(payload_json),
            "retry_policy": {
                "max_attempts": retry_policy.max_attempts,
                "initial_delay": retry_policy.initial_delay,
                "backoff_multiplier": retry_policy.backoff_multiplier,
                "max_delay": retry_policy.max_delay,
            },
        }
    )
    return hashlib.sha256(intent_json.encode("utf-8")).hexdigest()


def _encode_json(value: Any) -> str:
    try:
        return json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=True,
            allow_nan=False,
        )
    except (TypeError, ValueError) as exc:
        raise ValueError("value must be deterministic JSON") from exc


def _snapshot(row: sqlite3.Row) -> TaskSnapshot:
    return TaskSnapshot(
        task_id=str(row["task_id"]),
        idempotency_key=str(row["idempotency_key"]),
        intent_hash=str(row["intent_hash"]),
        payload=json.loads(row["payload_json"]),
        state=TaskState(row["state"]),
        state_version=int(row["state_version"]),
        attempt=int(row["attempt"]),
        max_attempts=int(row["max_attempts"]),
        available_at=float(row["available_at"]),
        lease_owner=row["lease_owner"],
        lease_expires_at=(
            float(row["lease_expires_at"])
            if row["lease_expires_at"] is not None
            else None
        ),
        cancel_requested=bool(row["cancel_requested"]),
        result=(json.loads(row["result_json"]) if row["result_json"] else None),
        error=row["error"],
    )


def _retry_delay(row: sqlite3.Row, attempt: int) -> float:
    policy = RetryPolicy(
        max_attempts=int(row["max_attempts"]),
        initial_delay=float(row["initial_delay"]),
        backoff_multiplier=float(row["backoff_multiplier"]),
        max_delay=float(row["max_delay"]),
    )
    return policy.delay_after(attempt)
