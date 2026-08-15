"""Educational agent-harness contracts and runtime."""

from .contracts import (
    Approval,
    ContextBundle,
    Event,
    Message,
    ModelTurn,
    RunLimits,
    RunResult,
    StopReason,
    ToolCall,
    ToolSpec,
)
from .context import AllContextBuilder, ContextBudgetError, RecentContextBuilder
from .persistence import SQLiteSessionStore
from .runtime import Harness, InMemorySessionStore, Policy, ToolRegistry
from .testing import EvalReport, EvalTask, ScriptedProvider, run_eval

__all__ = [
    "Approval",
    "AllContextBuilder",
    "ContextBudgetError",
    "ContextBundle",
    "EvalReport",
    "EvalTask",
    "Event",
    "Harness",
    "InMemorySessionStore",
    "Message",
    "ModelTurn",
    "Policy",
    "RecentContextBuilder",
    "RunLimits",
    "RunResult",
    "ScriptedProvider",
    "SQLiteSessionStore",
    "StopReason",
    "ToolCall",
    "ToolRegistry",
    "ToolSpec",
    "run_eval",
]
