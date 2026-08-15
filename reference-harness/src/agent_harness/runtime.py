"""Minimal bounded harness runtime with explicit policy and event evidence."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from typing import Any, Callable, Mapping, Protocol, Sequence

from .contracts import (
    Approval,
    ContextBuilder,
    Event,
    JsonObject,
    Message,
    Provider,
    RunLimits,
    RunResult,
    StopReason,
    ToolCall,
    ToolSpec,
)
from .context import AllContextBuilder


class SchemaError(ValueError):
    """Raised when tool arguments violate the supported schema subset."""


def canonical_fingerprint(tool_name: str, arguments: JsonObject) -> str:
    payload = json.dumps(
        {"tool": tool_name, "arguments": arguments},
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def validate_arguments(schema: JsonObject, arguments: JsonObject) -> None:
    """Validate the object/required/properties/type subset used in core labs."""

    if schema.get("type", "object") != "object":
        raise SchemaError("the reference harness accepts object schemas only")
    if not isinstance(arguments, Mapping):
        raise SchemaError("tool arguments must be an object")

    properties = schema.get("properties", {})
    required = schema.get("required", [])
    missing = [name for name in required if name not in arguments]
    if missing:
        raise SchemaError(f"missing required fields: {', '.join(sorted(missing))}")

    if schema.get("additionalProperties") is False:
        extra = sorted(set(arguments) - set(properties))
        if extra:
            raise SchemaError(f"unexpected fields: {', '.join(extra)}")

    expected_types: dict[str, tuple[type[Any], ...]] = {
        "string": (str,),
        "integer": (int,),
        "number": (int, float),
        "boolean": (bool,),
        "object": (Mapping,),
        "array": (list, tuple),
    }
    for name, value in arguments.items():
        declared = properties.get(name, {}).get("type")
        if declared is None:
            continue
        accepted = expected_types.get(declared)
        if accepted is None:
            raise SchemaError(f"unsupported schema type for {name}: {declared}")
        if declared in {"integer", "number"} and isinstance(value, bool):
            raise SchemaError(f"field {name} must be {declared}")
        if not isinstance(value, accepted):
            raise SchemaError(f"field {name} must be {declared}")


@dataclass
class ToolRegistry:
    _tools: dict[str, ToolSpec] = field(default_factory=dict)

    def register(self, spec: ToolSpec) -> None:
        if not spec.name or spec.name in self._tools:
            raise ValueError(f"invalid or duplicate tool name: {spec.name!r}")
        self._tools[spec.name] = spec

    def get(self, name: str) -> ToolSpec | None:
        return self._tools.get(name)

    def manifest(self) -> tuple[JsonObject, ...]:
        return tuple(
            {
                "name": spec.name,
                "description": spec.description,
                "input_schema": spec.input_schema,
                "side_effect": spec.side_effect,
                "idempotent": spec.idempotent,
            }
            for spec in sorted(self._tools.values(), key=lambda item: item.name)
        )


@dataclass
class Policy:
    allowed_tools: frozenset[str] | None = None
    require_side_effect_approval: bool = True
    approvals: set[Approval] = field(default_factory=set)

    def authorize(
        self, session_id: str, spec: ToolSpec, call: ToolCall
    ) -> tuple[bool, str]:
        if self.allowed_tools is not None and spec.name not in self.allowed_tools:
            return False, "tool is not in the session allowlist"
        if not spec.side_effect or not self.require_side_effect_approval:
            return True, "allowed by policy"

        required = Approval(
            session_id=session_id,
            tool_name=spec.name,
            arguments_fingerprint=canonical_fingerprint(spec.name, call.arguments),
        )
        if required not in self.approvals:
            return False, "side effect requires approval bound to exact arguments"
        return True, "exact approval matched"


@dataclass
class Session:
    messages: list[Message] = field(default_factory=list)
    events: list[Event] = field(default_factory=list)


@dataclass
class InMemorySessionStore:
    _sessions: dict[str, Session] = field(default_factory=dict)

    def session(self, session_id: str) -> Session:
        return self._sessions.setdefault(session_id, Session())

    def messages(self, session_id: str) -> tuple[Message, ...]:
        return tuple(self.session(session_id).messages)

    def events(self, session_id: str) -> tuple[Event, ...]:
        return tuple(self.session(session_id).events)

    def append_message(self, session_id: str, message: Message) -> None:
        self.session(session_id).messages.append(message)

    def append_event(self, session_id: str, kind: str, data: JsonObject) -> Event:
        session = self.session(session_id)
        event = Event(len(session.events) + 1, session_id, kind, dict(data))
        session.events.append(event)
        return event

    def checkpoint(self, session_id: str) -> JsonObject:
        session = self.session(session_id)
        return {
            "messages": [message.__dict__ for message in session.messages],
            "events": [
                {
                    "sequence": event.sequence,
                    "session_id": event.session_id,
                    "kind": event.kind,
                    "data": dict(event.data),
                }
                for event in session.events
            ],
        }


class SessionStore(Protocol):
    def messages(self, session_id: str) -> tuple[Message, ...]: ...

    def events(self, session_id: str) -> tuple[Event, ...]: ...

    def append_message(self, session_id: str, message: Message) -> None: ...

    def append_event(self, session_id: str, kind: str, data: JsonObject) -> Event: ...

    def checkpoint(self, session_id: str) -> JsonObject: ...


class Harness:
    def __init__(
        self,
        provider: Provider,
        registry: ToolRegistry | None = None,
        policy: Policy | None = None,
        store: SessionStore | None = None,
        context_builder: ContextBuilder | None = None,
        system_instruction: str = "Act within the available tools and policy.",
    ) -> None:
        self.provider = provider
        self.registry = registry or ToolRegistry()
        self.policy = policy or Policy()
        self.store = store or InMemorySessionStore()
        self.context_builder = context_builder or AllContextBuilder()
        self.system_instruction = system_instruction

    def run(
        self,
        session_id: str,
        user_input: str,
        limits: RunLimits | None = None,
        cancelled: Callable[[], bool] | None = None,
    ) -> RunResult:
        limits = limits or RunLimits()
        cancelled = cancelled or (lambda: False)
        if not self.store.messages(session_id):
            self.store.append_message(
                session_id, Message("system", self.system_instruction)
            )
        self.store.append_message(session_id, Message("user", user_input))
        self.store.append_event(session_id, "run.started", {"input": user_input})

        turns = 0
        tool_count = 0
        repeated_calls: dict[str, int] = {}

        while turns < limits.max_turns:
            if cancelled():
                return self._finish(
                    session_id, StopReason.CANCELLED, "", turns, tool_count
                )

            turns += 1
            try:
                context = self.context_builder.build(self.store.messages(session_id))
                self.store.append_event(
                    session_id,
                    "context.built",
                    {
                        "turn": turns,
                        "used_characters": context.used_characters,
                        "dropped_messages": context.dropped_messages,
                    },
                )
            except Exception as exc:
                self.store.append_event(
                    session_id,
                    "context.failed",
                    {"turn": turns, "error": f"{type(exc).__name__}: {exc}"},
                )
                return self._finish(
                    session_id, StopReason.CONTEXT_ERROR, "", turns, tool_count
                )
            self.store.append_event(session_id, "model.requested", {"turn": turns})
            try:
                turn = self.provider.complete(
                    context.messages, self.registry.manifest()
                )
            except Exception as exc:  # Provider errors are evidence, not crashes.
                self.store.append_event(
                    session_id,
                    "model.failed",
                    {"turn": turns, "error": f"{type(exc).__name__}: {exc}"},
                )
                return self._finish(
                    session_id, StopReason.PROVIDER_ERROR, "", turns, tool_count
                )

            self.store.append_event(
                session_id,
                "model.completed",
                {"turn": turns, "tool_calls": len(turn.tool_calls)},
            )
            if not turn.tool_calls:
                self.store.append_message(session_id, Message("assistant", turn.content))
                return self._finish(
                    session_id, StopReason.FINAL, turn.content, turns, tool_count
                )

            if turn.content:
                self.store.append_message(session_id, Message("assistant", turn.content))

            for call in turn.tool_calls:
                if tool_count >= limits.max_tool_calls:
                    return self._finish(
                        session_id, StopReason.TOOL_BUDGET, "", turns, tool_count
                    )
                tool_count += 1

                fingerprint = canonical_fingerprint(call.name, call.arguments)
                repeated_calls[fingerprint] = repeated_calls.get(fingerprint, 0) + 1
                if repeated_calls[fingerprint] > limits.max_repeated_call:
                    self.store.append_event(
                        session_id,
                        "run.no_progress",
                        {"tool": call.name, "call_id": call.call_id},
                    )
                    return self._finish(
                        session_id, StopReason.NO_PROGRESS, "", turns, tool_count
                    )

                spec = self.registry.get(call.name)
                if spec is None:
                    self._record_tool_error(session_id, call, "unknown tool")
                    continue
                try:
                    validate_arguments(spec.input_schema, call.arguments)
                except SchemaError as exc:
                    self._record_tool_error(session_id, call, str(exc))
                    continue

                allowed, reason = self.policy.authorize(session_id, spec, call)
                self.store.append_event(
                    session_id,
                    "policy.decided",
                    {
                        "tool": call.name,
                        "call_id": call.call_id,
                        "allowed": allowed,
                        "reason": reason,
                    },
                )
                if not allowed:
                    self._record_tool_error(session_id, call, reason)
                    return self._finish(
                        session_id, StopReason.POLICY_DENIED, "", turns, tool_count
                    )

                self.store.append_event(
                    session_id,
                    "tool.started",
                    {"tool": call.name, "call_id": call.call_id},
                )
                try:
                    output = spec.handler(call.arguments)
                    payload = {"ok": True, "output": output}
                    self.store.append_event(
                        session_id,
                        "tool.completed",
                        {"tool": call.name, "call_id": call.call_id},
                    )
                except Exception as exc:
                    payload = {
                        "ok": False,
                        "error": f"{type(exc).__name__}: {exc}",
                    }
                    self.store.append_event(
                        session_id,
                        "tool.failed",
                        {
                            "tool": call.name,
                            "call_id": call.call_id,
                            "error": payload["error"],
                        },
                    )
                self.store.append_message(
                    session_id,
                    Message(
                        "tool",
                        json.dumps(payload, sort_keys=True, default=str),
                        name=call.name,
                        call_id=call.call_id,
                    ),
                )

        return self._finish(
            session_id, StopReason.TURN_BUDGET, "", turns, tool_count
        )

    def _record_tool_error(
        self, session_id: str, call: ToolCall, error: str
    ) -> None:
        self.store.append_event(
            session_id,
            "tool.rejected",
            {"tool": call.name, "call_id": call.call_id, "error": error},
        )
        self.store.append_message(
            session_id,
            Message(
                "tool",
                json.dumps({"ok": False, "error": error}, sort_keys=True),
                name=call.name,
                call_id=call.call_id,
            ),
        )

    def _finish(
        self,
        session_id: str,
        reason: StopReason,
        output: str,
        turns: int,
        tool_calls: int,
    ) -> RunResult:
        self.store.append_event(
            session_id,
            "run.finished",
            {
                "stop_reason": reason.value,
                "turns": turns,
                "tool_calls": tool_calls,
            },
        )
        return RunResult(
            session_id=session_id,
            stop_reason=reason,
            output=output,
            turns=turns,
            tool_calls=tool_calls,
            events=self.store.events(session_id),
        )
