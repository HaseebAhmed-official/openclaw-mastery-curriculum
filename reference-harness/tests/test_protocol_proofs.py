from __future__ import annotations

import asyncio
import importlib.util
import unittest

from agent_harness.protocol_proofs import (
    A2A_PROTOCOL_VERSION,
    MCP_PROTOCOL_VERSION,
    OTEL_GENAI_SCHEMA_URL,
    PINNED_PACKAGES,
    installed_interop_versions,
    run_a2a_proof,
    run_mcp_proof,
    run_otel_proof,
)


def module_available(module: str) -> bool:
    try:
        return importlib.util.find_spec(module) is not None
    except ModuleNotFoundError:
        return False


INTEROP_AVAILABLE = all(
    module_available(module) for module in ("a2a", "mcp", "opentelemetry.sdk")
)


@unittest.skipUnless(INTEROP_AVAILABLE, "install the 'interop' optional extra")
class ProtocolProofTests(unittest.TestCase):
    def test_exact_optional_dependency_versions_are_enforced(self):
        self.assertEqual(PINNED_PACKAGES, installed_interop_versions())

    def test_mcp_discovery_policy_success_and_schema_failure(self):
        proof = asyncio.run(run_mcp_proof())

        self.assertEqual("2.0.0", proof.sdk_version)
        self.assertEqual(MCP_PROTOCOL_VERSION, proof.protocol_version)
        self.assertEqual(("add",), proof.tools)
        self.assertEqual(5, proof.output)
        self.assertTrue(proof.malformed_rejected)

        with self.assertRaises(PermissionError):
            asyncio.run(run_mcp_proof(allowed_tools=frozenset()))

    def test_a2a_task_artifact_and_auth_boundary(self):
        proof = asyncio.run(run_a2a_proof())

        self.assertEqual("1.1.2", proof.sdk_version)
        self.assertEqual("JSONRPC", proof.protocol_binding)
        self.assertEqual(A2A_PROTOCOL_VERSION, proof.protocol_version)
        self.assertEqual(200, proof.card_status)
        self.assertEqual(proof.completed_state, proof.task_state)
        self.assertEqual("echo:hello", proof.artifact_text)
        self.assertEqual(401, proof.unauthorized_status)

    def test_otel_trace_is_linked_and_excludes_sensitive_content(self):
        secret_input = "learner-secret-input"
        secret_arguments = '{"token":"do-not-export"}'
        proof = run_otel_proof(
            sensitive_input=secret_input,
            sensitive_arguments=secret_arguments,
        )

        self.assertEqual("1.44.0", proof.sdk_version)
        self.assertEqual(OTEL_GENAI_SCHEMA_URL, proof.schema_url)
        self.assertTrue(proof.parent_child_linked)
        self.assertEqual(
            ["execute_tool add", "invoke_agent curriculum_reference"],
            sorted(span.name for span in proof.spans),
        )
        self.assertTrue(
            all(span.schema_url == OTEL_GENAI_SCHEMA_URL for span in proof.spans)
        )
        serialized = repr(proof.spans)
        self.assertNotIn(secret_input, serialized)
        self.assertNotIn(secret_arguments, serialized)
        self.assertNotIn("gen_ai.tool.call.arguments", serialized)
        self.assertNotIn("gen_ai.tool.call.result", serialized)


if __name__ == "__main__":
    unittest.main()
