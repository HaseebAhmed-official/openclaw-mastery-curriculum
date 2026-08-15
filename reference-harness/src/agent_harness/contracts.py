"""Stable data contracts used by the educational harness."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable, Mapping, Protocol, Sequence


JsonObject = Mapping[str, Any]
ToolHandler = Callable[[JsonObject], Any]


@dataclass(frozen=True)
class Message:
    role: str
    content: str
    name: str | None = None
    call_id: str | None = None
    metadata: JsonObject = field(default_factory=dict)


@dataclass(frozen=True)
class ContextBundle:
    messages: tuple[Message, ...]
    used_characters: int
    dropped_messages: int


class ContextBuilder(Protocol):
    def build(self, messages: Sequence[Message]) -> ContextBundle:
        """Select the provider-visible working context."""


@dataclass(frozen=True)
class ToolCall:
    call_id: str
    name: str
    arguments: JsonObject


@dataclass(frozen=True)
class ModelTurn:
    content: str = ""
    tool_calls: tuple[ToolCall, ...] = ()


class Provider(Protocol):
    def complete(
        self, messages: Sequence[Message], tools: Sequence[JsonObject]
    ) -> ModelTurn:
        """Return the next model-directed turn."""


@dataclass(frozen=True)
class ToolSpec:
    name: str
    description: str
    input_schema: JsonObject
    handler: ToolHandler
    side_effect: bool = False
    idempotent: bool = False


@dataclass(frozen=True)
class Approval:
    session_id: str
    tool_name: str
    arguments_fingerprint: str


@dataclass(frozen=True)
class RunLimits:
    max_turns: int = 8
    max_tool_calls: int = 16
    max_repeated_call: int = 2

    def __post_init__(self) -> None:
        if min(self.max_turns, self.max_tool_calls, self.max_repeated_call) < 1:
            raise ValueError("run limits must be positive")


class StopReason(str, Enum):
    FINAL = "final"
    TURN_BUDGET = "turn_budget"
    TOOL_BUDGET = "tool_budget"
    POLICY_DENIED = "policy_denied"
    NO_PROGRESS = "no_progress"
    CANCELLED = "cancelled"
    CONTEXT_ERROR = "context_error"
    PROVIDER_ERROR = "provider_error"


@dataclass(frozen=True)
class Event:
    sequence: int
    session_id: str
    attempt_id: str
    kind: str
    data: JsonObject = field(default_factory=dict)


@dataclass(frozen=True)
class RunResult:
    session_id: str
    attempt_id: str
    stop_reason: StopReason
    output: str
    turns: int
    tool_calls: int
    events: tuple[Event, ...]
