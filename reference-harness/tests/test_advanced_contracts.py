from __future__ import annotations

import unittest
from dataclasses import replace

from agent_harness import (
    AdapterContractError,
    BufferedEventExporter,
    CapabilityManifest,
    CapabilityRequest,
    CapabilityResponse,
    Harness,
    InMemoryMemoryStore,
    MemoryRecord,
    ModelTurn,
    ScriptedProvider,
    export_attempt,
    invoke_checked,
    run_fan_out_sequential,
    run_routed,
)


class MemoryTests(unittest.TestCase):
    def test_write_policy_namespace_expiry_and_deletion_are_explicit(self):
        store = InMemoryMemoryStore(
            lambda record: (
                record.source == "verified",
                "only verified records may be written",
            )
        )
        with self.assertRaises(PermissionError):
            store.put(MemoryRecord("denied", "user-a", "secret", "chat", 1))

        store.put(
            MemoryRecord(
                "fresh", "user-a", "deploy with rollback", "verified", 10
            )
        )
        store.put(
            MemoryRecord(
                "expired",
                "user-a",
                "deploy without tests",
                "verified",
                1,
                expires_at=5,
            )
        )
        store.put(
            MemoryRecord(
                "other-user",
                "user-b",
                "deploy private token",
                "verified",
                20,
            )
        )

        hits = store.search("user-a", "deploy rollback", now=20)

        self.assertEqual(["fresh"], [hit.record.memory_id for hit in hits])
        self.assertTrue(all(hit.trust == "untrusted" for hit in hits))
        self.assertTrue(store.delete("user-a", "fresh"))
        self.assertFalse(store.delete("user-a", "other-user"))
        self.assertEqual((), store.search("user-a", "deploy rollback", now=20))

        invalid_policy_store = InMemoryMemoryStore(lambda _record: ("yes", "wrong"))
        with self.assertRaises(TypeError):
            invalid_policy_store.put(
                MemoryRecord("invalid-policy", "user-a", "data", "verified", 1)
            )


class OrchestrationTests(unittest.TestCase):
    def test_routing_and_fan_out_failures_are_visible_and_bounded(self):
        workers = {
            "ok": lambda task: task.upper(),
            "broken": lambda _task: 1 / 0,
            "invalid-output": lambda _task: 42,
        }

        routed = run_routed("work", "ok", workers)
        fan_out = run_fan_out_sequential(
            "work", ["ok", "broken"], workers, max_workers=2
        )

        self.assertEqual("WORK", routed.results[0].output)
        self.assertEqual(("broken",), fan_out.failed_workers)
        self.assertIn("ZeroDivisionError", fan_out.results[1].error)
        invalid_output = run_routed("work", "invalid-output", workers)
        self.assertFalse(invalid_output.results[0].ok)
        self.assertIn("worker must return a string", invalid_output.results[0].error)
        with self.assertRaises(ValueError):
            run_fan_out_sequential(
                "work", ["ok", "broken"], workers, max_workers=1
            )
        with self.assertRaises(ValueError):
            run_routed("work", "missing", workers)
        with self.assertRaises(ValueError):
            run_fan_out_sequential("work", [], workers, max_workers=1)


class ScriptedAdapter:
    def __init__(self, version: str = "1", trust: str = "untrusted") -> None:
        self.version = version
        self.trust = trust

    def manifest(self) -> CapabilityManifest:
        return CapabilityManifest("fixture", self.version, frozenset({"read"}))

    def invoke(self, request: CapabilityRequest) -> CapabilityResponse:
        return CapabilityResponse(
            request.request_id, True, {"value": "untrusted"}, trust=self.trust
        )


class InvalidManifestAdapter(ScriptedAdapter):
    def manifest(self):
        return {"protocol": "fixture", "version": "1"}


class InvalidResponseAdapter(ScriptedAdapter):
    def invoke(self, request: CapabilityRequest):
        return {"request_id": request.request_id, "ok": True}


class IntegrationTests(unittest.TestCase):
    def test_adapter_pin_policy_and_response_identity_are_checked(self):
        request = CapabilityRequest("r1", "read", {})

        response = invoke_checked(
            ScriptedAdapter(),
            request,
            expected_protocol="fixture",
            expected_version="1",
            allowed_capabilities=frozenset({"read"}),
        )

        self.assertEqual("untrusted", response.trust)
        with self.assertRaises(AdapterContractError):
            invoke_checked(
                ScriptedAdapter("2"),
                request,
                expected_protocol="fixture",
                expected_version="1",
                allowed_capabilities=frozenset({"read"}),
            )
        with self.assertRaises(PermissionError):
            invoke_checked(
                ScriptedAdapter(),
                request,
                expected_protocol="fixture",
                expected_version="1",
                allowed_capabilities=frozenset(),
            )
        with self.assertRaises(AdapterContractError):
            invoke_checked(
                ScriptedAdapter(trust="trusted"),
                request,
                expected_protocol="fixture",
                expected_version="1",
                allowed_capabilities=frozenset({"read"}),
            )
        for invalid_adapter in (InvalidManifestAdapter(), InvalidResponseAdapter()):
            with self.assertRaises(AdapterContractError):
                invoke_checked(
                    invalid_adapter,
                    request,
                    expected_protocol="fixture",
                    expected_version="1",
                    allowed_capabilities=frozenset({"read"}),
                )

    def test_exporter_receives_only_the_current_attempt(self):
        harness = Harness(ScriptedProvider([ModelTurn(content="ok")]))
        run = harness.run("session", "work")
        exporter = BufferedEventExporter()

        export_attempt(run, exporter)

        self.assertEqual(1, len(exporter.batches))
        self.assertTrue(
            all(event.attempt_id == run.attempt_id for event in exporter.batches[0])
        )

        contaminated = replace(
            run,
            events=(replace(run.events[0], session_id="another-session"),)
            + run.events[1:],
        )
        with self.assertRaises(AdapterContractError):
            export_attempt(contaminated, exporter)


if __name__ == "__main__":
    unittest.main()
