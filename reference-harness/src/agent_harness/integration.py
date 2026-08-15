"""Protocol and telemetry ports without claiming MCP, A2A, or OTel compliance."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Protocol, Sequence

from .contracts import Event, JsonObject, RunResult


class AdapterContractError(RuntimeError):
    """Raised when an external adapter violates the pinned local contract."""


@dataclass(frozen=True)
class CapabilityManifest:
    protocol: str
    version: str
    capabilities: frozenset[str]

    def __post_init__(self) -> None:
        if (
            not isinstance(self.protocol, str)
            or not self.protocol
            or not isinstance(self.version, str)
            or not self.version
        ):
            raise ValueError("protocol and version are required")
        if not isinstance(self.capabilities, frozenset) or any(
            not isinstance(capability, str) or not capability
            for capability in self.capabilities
        ):
            raise ValueError("capability names must be non-empty")


@dataclass(frozen=True)
class CapabilityRequest:
    request_id: str
    capability: str
    payload: JsonObject

    def __post_init__(self) -> None:
        if (
            not isinstance(self.request_id, str)
            or not self.request_id
            or not isinstance(self.capability, str)
            or not self.capability
        ):
            raise ValueError("request identity and capability are required")
        if not isinstance(self.payload, Mapping):
            raise TypeError("request payload must be an object")


@dataclass(frozen=True)
class CapabilityResponse:
    request_id: str
    ok: bool
    payload: JsonObject
    error: str = ""
    trust: str = "untrusted"

    def __post_init__(self) -> None:
        if not isinstance(self.request_id, str) or not self.request_id:
            raise ValueError("response request identity is required")
        if not isinstance(self.ok, bool):
            raise TypeError("response status must be boolean")
        if not isinstance(self.payload, Mapping):
            raise TypeError("response payload must be an object")
        if not isinstance(self.error, str) or not isinstance(self.trust, str):
            raise TypeError("response error and trust labels must be strings")


class CapabilityAdapter(Protocol):
    def manifest(self) -> CapabilityManifest: ...

    def invoke(self, request: CapabilityRequest) -> CapabilityResponse: ...


def invoke_checked(
    adapter: CapabilityAdapter,
    request: CapabilityRequest,
    *,
    expected_protocol: str,
    expected_version: str,
    allowed_capabilities: frozenset[str],
) -> CapabilityResponse:
    manifest = adapter.manifest()
    if not isinstance(manifest, CapabilityManifest):
        raise AdapterContractError("adapter returned an invalid manifest")
    if manifest.protocol != expected_protocol or manifest.version != expected_version:
        raise AdapterContractError("adapter protocol or version does not match the pin")
    if request.capability not in manifest.capabilities:
        raise AdapterContractError("adapter did not advertise the requested capability")
    if request.capability not in allowed_capabilities:
        raise PermissionError("local policy does not allow the requested capability")

    response = adapter.invoke(request)
    if not isinstance(response, CapabilityResponse):
        raise AdapterContractError("adapter returned an invalid response")
    if response.request_id != request.request_id:
        raise AdapterContractError("response request identity mismatch")
    if response.trust != "untrusted":
        raise AdapterContractError("external content cannot self-declare trusted status")
    if response.ok and response.error:
        raise AdapterContractError("successful response cannot also contain an error")
    if not response.ok and not response.error:
        raise AdapterContractError("failed response must contain an error")
    return response


class EventExporter(Protocol):
    def export(self, events: Sequence[Event]) -> None: ...


@dataclass
class BufferedEventExporter:
    """Inspectable exporter test double for trace-adapter labs."""

    batches: list[tuple[Event, ...]]

    def __init__(self) -> None:
        self.batches = []

    def export(self, events: Sequence[Event]) -> None:
        self.batches.append(tuple(events))


def export_attempt(run: RunResult, exporter: EventExporter) -> None:
    if not run.events:
        raise AdapterContractError("run contains no attempt events")
    if any(event.attempt_id != run.attempt_id for event in run.events):
        raise AdapterContractError("run contains events from another attempt")
    if any(event.session_id != run.session_id for event in run.events):
        raise AdapterContractError("run contains events from another session")
    sequences = [event.sequence for event in run.events]
    if sequences != sorted(set(sequences)):
        raise AdapterContractError("run event sequence is duplicated or out of order")
    if run.events[-1].kind != "run.finished":
        raise AdapterContractError("run lacks a terminal event")
    exporter.export(run.events)
