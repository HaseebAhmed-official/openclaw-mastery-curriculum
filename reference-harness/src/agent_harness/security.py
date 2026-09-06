"""LAB-C6: host-issued capabilities and single-use approval, without external I/O.

The host, handlers, session identity, and clock are trusted. Model calls and tool
results are untrusted. This in-process policy is not a sandbox or an egress proxy.
"""

from __future__ import annotations

import json
import math
import time
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from threading import Lock
from uuid import uuid4

from .contracts import JsonObject, ToolCall, ToolSpec
from .runtime import canonical_fingerprint, validate_arguments


@dataclass(frozen=True)
class Capability:
    tool: ToolSpec
    # Each named argument must equal one host-allowed string; no prefix matching.
    argument_allowlists: Mapping[str, frozenset[str]]


@dataclass(frozen=True)
class _BoundCapability:
    tool: ToolSpec
    definition: str
    constraints: tuple[tuple[str, frozenset[str]], ...]


@dataclass(frozen=True)
class _Grant:
    session_id: str
    tool_name: str
    fingerprint: str
    expires_at: float


def _definition(spec: ToolSpec) -> str:
    return json.dumps(
        [
            spec.name,
            spec.description,
            spec.input_schema,
            spec.side_effect,
            spec.idempotent,
        ],
        sort_keys=True,
        allow_nan=False,
    )


def _fingerprint(name: str, arguments: JsonObject) -> str:
    # Reject non-JSON/NaN values rather than silently stringifying approval intent.
    serialized = json.dumps(dict(arguments), sort_keys=True, allow_nan=False)
    return canonical_fingerprint(name, json.loads(serialized))


class ScopedPolicy:
    """Freeze host scopes and bind approval to session, tool, and exact arguments.

    All side effects require a grant. Dispatch consumes it even if the handler
    fails: retries need reconciliation and fresh approval, not blind replay.
    Destination constraints check arguments only; handlers must honor them.
    """

    def __init__(
        self,
        scopes: Mapping[str, tuple[Capability, ...]],
        clock: Callable[[], float] = time.monotonic,
    ) -> None:
        self._capabilities: dict[tuple[str, str], _BoundCapability] = {}
        for session_id, capabilities in scopes.items():
            if not isinstance(session_id, str) or not session_id:
                raise ValueError("scope requires a nonempty host session identity")
            for capability in capabilities:
                spec = capability.tool
                key = (session_id, spec.name)
                if not spec.name or key in self._capabilities:
                    raise ValueError("duplicate or empty scoped tool")
                constraints = []
                for argument, allowed in capability.argument_allowlists.items():
                    if (
                        not isinstance(argument, str)
                        or not argument
                        or not isinstance(allowed, frozenset)
                        or not all(isinstance(value, str) for value in allowed)
                    ):
                        raise ValueError("constraints require named frozen string sets")
                    constraints.append((argument, allowed))
                self._capabilities[key] = _BoundCapability(
                    spec, _definition(spec), tuple(constraints)
                )
        self._clock = clock
        self._grants: dict[str, _Grant] = {}
        self._lock = Lock()

    def _check(self, session_id: str, spec: ToolSpec, call: ToolCall) -> str | None:
        bound = self._capabilities.get((session_id, call.name))
        if bound is None:
            return "session has no capability for this tool"
        if bound.tool is not spec or call.name != spec.name:
            return "tool implementation differs from the host-approved binding"
        try:
            if _definition(spec) != bound.definition:
                return "tool definition changed; host must rebind and reapprove"
            validate_arguments(spec.input_schema, call.arguments)
            _fingerprint(call.name, call.arguments)
        except (TypeError, ValueError):
            return "arguments or tool definition are invalid"
        for argument, allowed in bound.constraints:
            value = call.arguments.get(argument)
            if not isinstance(value, str) or value not in allowed:
                return "argument is outside the host-issued capability"
        return None

    def _now(self) -> float:
        now = self._clock()
        if not math.isfinite(now):
            raise ValueError("approval clock must be finite")
        return now

    def approve(self, session_id: str, call: ToolCall, ttl_seconds: float) -> str:
        """Trusted host API; never register this method as a model-visible tool."""
        if not math.isfinite(ttl_seconds) or ttl_seconds <= 0:
            raise ValueError("approval lifetime must be finite and positive")
        with self._lock:
            bound = self._capabilities.get((session_id, call.name))
            if bound is None or not bound.tool.side_effect:
                raise ValueError("approval requires a scoped side-effecting tool")
            reason = self._check(session_id, bound.tool, call)
            if reason:
                raise ValueError(reason)
            expiry = self._now() + ttl_seconds
            if not math.isfinite(expiry):
                raise ValueError("approval expiry must be finite")
            grant_id = uuid4().hex
            self._grants[grant_id] = _Grant(
                session_id, call.name, _fingerprint(call.name, call.arguments), expiry
            )
            return grant_id

    def revoke(self, grant_id: str) -> bool:
        with self._lock:
            return self._grants.pop(grant_id, None) is not None

    def authorize(
        self, session_id: str, spec: ToolSpec, call: ToolCall
    ) -> tuple[bool, str]:
        with self._lock:
            reason = self._check(session_id, spec, call)
            if reason:
                return False, reason
            if not spec.side_effect:
                return True, "host-issued capability matched"
            try:
                now = self._now()
            except (TypeError, ValueError):
                return False, "approval clock is invalid"
            self._grants = {
                key: grant
                for key, grant in self._grants.items()
                if now < grant.expires_at
            }
            fingerprint = _fingerprint(call.name, call.arguments)
            for key, grant in self._grants.items():
                if (grant.session_id, grant.tool_name, grant.fingerprint) == (
                    session_id,
                    call.name,
                    fingerprint,
                ):
                    del self._grants[key]
                    return True, "single-use exact approval consumed before dispatch"
            return False, "no live exact approval for this session and operation"
