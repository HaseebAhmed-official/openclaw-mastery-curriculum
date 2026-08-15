from __future__ import annotations

import unittest

from agent_harness import (
    Approval,
    Harness,
    ModelTurn,
    Policy,
    RunLimits,
    ScriptedProvider,
    StopReason,
    ToolCall,
    ToolRegistry,
    ToolSpec,
)
from agent_harness.runtime import canonical_fingerprint


def calculator(arguments):
    return arguments["a"] + arguments["b"]


def registry_with_calculator(side_effect: bool = False) -> ToolRegistry:
    registry = ToolRegistry()
    registry.register(
        ToolSpec(
            name="add",
            description="Add two integers.",
            input_schema={
                "type": "object",
                "properties": {
                    "a": {"type": "integer"},
                    "b": {"type": "integer"},
                },
                "required": ["a", "b"],
                "additionalProperties": False,
            },
            handler=calculator,
            side_effect=side_effect,
            idempotent=True,
        )
    )
    return registry


class HarnessTests(unittest.TestCase):
    def test_final_response_has_explicit_stop_reason(self):
        harness = Harness(ScriptedProvider([ModelTurn(content="complete")]))

        result = harness.run("s1", "work")

        self.assertEqual(StopReason.FINAL, result.stop_reason)
        self.assertEqual("complete", result.output)
        self.assertEqual("run.finished", result.events[-1].kind)

    def test_malformed_provider_turn_becomes_provider_error(self):
        harness = Harness(ScriptedProvider(["not-a-model-turn"]))

        result = harness.run("malformed", "work")

        self.assertEqual(StopReason.PROVIDER_ERROR, result.stop_reason)
        self.assertEqual("model.failed", result.events[-2].kind)

    def test_valid_tool_call_is_recorded_and_returned_to_provider(self):
        provider = ScriptedProvider(
            [
                ModelTurn(tool_calls=(ToolCall("c1", "add", {"a": 2, "b": 3}),)),
                ModelTurn(content="5"),
            ]
        )
        harness = Harness(provider, registry=registry_with_calculator())

        result = harness.run("s2", "add")

        self.assertEqual(StopReason.FINAL, result.stop_reason)
        self.assertEqual(1, result.tool_calls)
        second_request = provider.requests[1][0]
        self.assertEqual("tool", second_request[-1].role)
        self.assertIn('"output": 5', second_request[-1].content)

    def test_schema_rejection_can_be_repaired_by_next_turn(self):
        provider = ScriptedProvider(
            [
                ModelTurn(tool_calls=(ToolCall("bad", "add", {"a": 2}),)),
                ModelTurn(tool_calls=(ToolCall("good", "add", {"a": 2, "b": 3}),)),
                ModelTurn(content="5"),
            ]
        )
        harness = Harness(provider, registry=registry_with_calculator())

        result = harness.run("s3", "add")

        self.assertEqual(StopReason.FINAL, result.stop_reason)
        rejected = [event for event in result.events if event.kind == "tool.rejected"]
        self.assertEqual(1, len(rejected))
        self.assertIn("missing required fields", rejected[0].data["error"])

    def test_side_effect_requires_exact_session_and_arguments(self):
        call = ToolCall("c1", "add", {"a": 2, "b": 3})
        provider = ScriptedProvider([ModelTurn(tool_calls=(call,))])
        harness = Harness(provider, registry=registry_with_calculator(side_effect=True))

        denied = harness.run("s4", "add")

        self.assertEqual(StopReason.POLICY_DENIED, denied.stop_reason)

        approval = Approval("s5", "add", canonical_fingerprint("add", call.arguments))
        provider = ScriptedProvider(
            [ModelTurn(tool_calls=(call,)), ModelTurn(content="approved")]
        )
        harness = Harness(
            provider,
            registry=registry_with_calculator(side_effect=True),
            policy=Policy(approvals={approval}),
        )

        allowed = harness.run("s5", "add")

        self.assertEqual(StopReason.FINAL, allowed.stop_reason)

    def test_repeated_identical_call_stops_no_progress(self):
        provider = ScriptedProvider(
            [
                ModelTurn(tool_calls=(ToolCall(f"call-{index}", "missing", {}),))
                for index in range(3)
            ]
        )
        harness = Harness(provider)

        result = harness.run(
            "s6", "loop", RunLimits(max_turns=5, max_repeated_call=2)
        )

        self.assertEqual(StopReason.NO_PROGRESS, result.stop_reason)

    def test_provider_cannot_reuse_tool_call_identity(self):
        provider = ScriptedProvider(
            [
                ModelTurn(tool_calls=(ToolCall("duplicate", "add", {"a": 1, "b": 2}),)),
                ModelTurn(tool_calls=(ToolCall("duplicate", "add", {"a": 3, "b": 4}),)),
            ]
        )
        harness = Harness(provider, registry=registry_with_calculator())

        result = harness.run("duplicate-call-id", "add twice")

        self.assertEqual(StopReason.PROVIDER_ERROR, result.stop_reason)
        self.assertEqual(1, result.tool_calls)
        self.assertIn("reused a tool-call identity", result.events[-2].data["error"])

    def test_turn_budget_and_checkpoint_are_explicit(self):
        provider = ScriptedProvider(
            [ModelTurn(tool_calls=(ToolCall(str(i), "missing", {"n": i}),)) for i in range(3)]
        )
        harness = Harness(provider)

        result = harness.run("s7", "loop", RunLimits(max_turns=2))
        checkpoint = harness.store.checkpoint("s7")

        self.assertEqual(StopReason.TURN_BUDGET, result.stop_reason)
        self.assertGreaterEqual(len(checkpoint["messages"]), 3)
        self.assertEqual("run.finished", checkpoint["events"][-1]["kind"])


if __name__ == "__main__":
    unittest.main()
