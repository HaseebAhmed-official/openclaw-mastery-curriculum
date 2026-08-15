"""Bounded, optional proofs against pinned interoperability SDKs.

These fixtures exercise real SDK behavior without claiming network transport,
production authentication, protocol certification, or stable GenAI telemetry
conformance. Optional imports stay inside functions so the base harness remains
standard-library only.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from importlib.metadata import PackageNotFoundError, version
from typing import Any

PINNED_PACKAGES = {
    "a2a-sdk": "1.1.2",
    "mcp": "2.0.0",
    "opentelemetry-sdk": "1.44.0",
}
MCP_PROTOCOL_VERSION = "2026-07-28"
A2A_PROTOCOL_VERSION = "1.0"
OTEL_GENAI_SOURCE_COMMIT = "a685613a207a580163353b8e48a7ad88967e7b42"
OTEL_GENAI_SCHEMA_URL = "https://opentelemetry.io/schemas/gen-ai-dev/1.42.0-dev"


class OptionalInteropError(RuntimeError):
    """Raised when the optional interoperability lane cannot run as pinned."""


@dataclass(frozen=True)
class McpProof:
    sdk_version: str
    protocol_version: str
    tools: tuple[str, ...]
    output: int
    malformed_rejected: bool


@dataclass(frozen=True)
class A2AProof:
    sdk_version: str
    protocol_binding: str
    protocol_version: str
    card_status: int
    task_state: int
    completed_state: int
    artifact_text: str
    unauthorized_status: int


@dataclass(frozen=True)
class SpanSnapshot:
    name: str
    attributes: tuple[tuple[str, Any], ...]
    span_id: int
    parent_span_id: int | None
    schema_url: str


@dataclass(frozen=True)
class OtelProof:
    sdk_version: str
    source_commit: str
    schema_url: str
    spans: tuple[SpanSnapshot, ...]
    parent_child_linked: bool


def installed_interop_versions() -> Mapping[str, str]:
    """Return exact versions or reject an absent/drifted optional lane."""

    observed: dict[str, str] = {}
    for package, expected in PINNED_PACKAGES.items():
        try:
            actual = version(package)
        except PackageNotFoundError as exc:
            raise OptionalInteropError(
                "install the reference harness with the 'interop' extra"
            ) from exc
        if actual != expected:
            raise OptionalInteropError(
                f"{package} must be {expected}; observed {actual}"
            )
        observed[package] = actual
    return observed


async def run_mcp_proof(
    *, allowed_tools: frozenset[str] = frozenset({"add"})
) -> McpProof:
    """Exercise discovery, local authorization, success, and schema failure."""

    versions = installed_interop_versions()
    from mcp import Client
    from mcp.server import MCPServer

    server = MCPServer("Curriculum MCP Proof", version="1.0.0")

    @server.tool()
    def add(a: int, b: int) -> int:
        """Add two integers."""

        return a + b

    denied = False
    proof: McpProof | None = None
    async with Client(server, raise_exceptions=True) as client:
        listed = await client.list_tools()
        tools = tuple(sorted(tool.name for tool in listed.tools))
        if "add" not in tools:
            raise OptionalInteropError("the proof server did not advertise add")
        if "add" not in allowed_tools:
            denied = True
        else:
            successful = await client.call_tool("add", {"a": 2, "b": 3})
            malformed = await client.call_tool(
                "add", {"a": "not-an-integer", "b": 3}
            )
            structured = successful.structured_content
            if successful.is_error or not isinstance(structured, Mapping):
                raise OptionalInteropError("MCP success response was not structured")
            output = structured.get("result")
            if not isinstance(output, int):
                raise OptionalInteropError(
                    "MCP result did not preserve the integer contract"
                )
            proof = McpProof(
                sdk_version=versions["mcp"],
                protocol_version=client.protocol_version,
                tools=tools,
                output=output,
                malformed_rejected=malformed.is_error,
            )

    if denied:
        raise PermissionError("local policy denied the MCP tool before invocation")
    if proof is None:
        raise OptionalInteropError("MCP proof exited without a result")
    return proof


async def run_a2a_proof() -> A2AProof:
    """Exercise an authenticated A2A JSON-RPC task over in-process ASGI."""

    versions = installed_interop_versions()
    import httpx
    from a2a.client.client import ClientConfig
    from a2a.client.client_factory import ClientFactory
    from a2a.helpers import (
        get_artifact_text,
        new_task_from_user_message,
        new_text_message,
        new_text_part,
    )
    from a2a.server.agent_execution import AgentExecutor
    from a2a.server.events.in_memory_queue_manager import InMemoryQueueManager
    from a2a.server.request_handlers import DefaultRequestHandler
    from a2a.server.routes import create_agent_card_routes, create_jsonrpc_routes
    from a2a.server.tasks import TaskUpdater
    from a2a.server.tasks.inmemory_task_store import InMemoryTaskStore
    from a2a.types import (
        AgentCapabilities,
        AgentCard,
        AgentInterface,
        Role,
        SendMessageConfiguration,
        SendMessageRequest,
        TaskState,
    )
    from a2a.utils import TransportProtocol
    from starlette.applications import Starlette
    from starlette.responses import PlainTextResponse

    class EchoExecutor(AgentExecutor):
        async def execute(self, context: Any, event_queue: Any) -> None:
            task = new_task_from_user_message(context.message)
            await event_queue.enqueue_event(task)
            updater = TaskUpdater(event_queue, task.id, task.context_id)
            await updater.start_work()
            await updater.add_artifact(
                parts=[new_text_part(f"echo:{context.get_user_input()}")],
                name="result",
            )
            await updater.complete()

        async def cancel(self, context: Any, event_queue: Any) -> None:
            if not context.task_id or not context.context_id:
                raise OptionalInteropError("A2A cancellation lacked task identity")
            await TaskUpdater(event_queue, context.task_id, context.context_id).cancel()

    class BearerBoundary:
        def __init__(self, app: Any) -> None:
            self.app = app

        async def __call__(self, scope: Any, receive: Any, send: Any) -> None:
            headers = dict(scope.get("headers", []))
            authorized = headers.get(b"authorization") == b"Bearer curriculum-proof"
            if scope["type"] == "http" and not authorized:
                response = PlainTextResponse("unauthorized", status_code=401)
                await response(scope, receive, send)
                return
            await self.app(scope, receive, send)

    binding = TransportProtocol.JSONRPC.value
    card = AgentCard(
        name="Curriculum Echo",
        description="Bounded A2A interoperability proof",
        version="1.0.0",
        capabilities=AgentCapabilities(streaming=False),
        supported_interfaces=[
            AgentInterface(
                url="http://testserver/rpc",
                protocol_binding=binding,
                protocol_version=A2A_PROTOCOL_VERSION,
            )
        ],
        default_input_modes=["text/plain"],
        default_output_modes=["text/plain"],
        skills=[],
    )
    handler = DefaultRequestHandler(
        agent_executor=EchoExecutor(),
        task_store=InMemoryTaskStore(),
        queue_manager=InMemoryQueueManager(),
        agent_card=card,
    )
    app = BearerBoundary(
        Starlette(
            routes=[
                *create_agent_card_routes(card),
                *create_jsonrpc_routes(handler, rpc_url="/rpc"),
            ]
        )
    )
    transport = httpx.ASGITransport(app=app)

    async with httpx.AsyncClient(
        transport=transport,
        base_url="http://testserver",
        headers={"Authorization": "Bearer curriculum-proof"},
    ) as authorized_http:
        card_response = await authorized_http.get("/.well-known/agent-card.json")
        if card_response.status_code != 200:
            raise OptionalInteropError("authenticated AgentCard retrieval failed")
        published_card = card_response.json()
        if published_card.get("name") != card.name:
            raise OptionalInteropError("published AgentCard identity did not match")
        client = ClientFactory(
            ClientConfig(
                streaming=False,
                httpx_client=authorized_http,
                supported_protocol_bindings=[TransportProtocol.JSONRPC],
            )
        ).create(card)
        request = SendMessageRequest(
            message=new_text_message("hello", role=Role.ROLE_USER),
            configuration=SendMessageConfiguration(return_immediately=False),
        )
        try:
            events = [event async for event in client.send_message(request)]
        finally:
            await client.close()

    if len(events) != 1 or events[0].WhichOneof("payload") != "task":
        raise OptionalInteropError("A2A blocking exchange did not return one task")
    task = events[0].task
    if len(task.artifacts) != 1:
        raise OptionalInteropError("A2A task did not return one artifact")

    async with httpx.AsyncClient(
        transport=transport, base_url="http://testserver"
    ) as unauthorized_http:
        unauthorized = await unauthorized_http.post("/rpc", json={})

    return A2AProof(
        sdk_version=versions["a2a-sdk"],
        protocol_binding=binding,
        protocol_version=A2A_PROTOCOL_VERSION,
        card_status=card_response.status_code,
        task_state=task.status.state,
        completed_state=TaskState.TASK_STATE_COMPLETED,
        artifact_text=get_artifact_text(task.artifacts[0]),
        unauthorized_status=unauthorized.status_code,
    )


def run_otel_proof(*, sensitive_input: str, sensitive_arguments: str) -> OtelProof:
    """Export in-memory spans while deliberately excluding sensitive content."""

    versions = installed_interop_versions()
    if not sensitive_input or not sensitive_arguments:
        raise ValueError("sensitive proof values must be non-empty")

    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import SimpleSpanProcessor
    from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
        InMemorySpanExporter,
    )

    exporter = InMemorySpanExporter()
    provider = TracerProvider()
    provider.add_span_processor(SimpleSpanProcessor(exporter))
    tracer = provider.get_tracer(__name__, schema_url=OTEL_GENAI_SCHEMA_URL)

    with tracer.start_as_current_span("invoke_agent curriculum_reference") as root:
        root.set_attribute("gen_ai.operation.name", "invoke_agent")
        root.set_attribute("gen_ai.agent.name", "curriculum_reference")
        with tracer.start_as_current_span("execute_tool add") as tool:
            tool.set_attribute("gen_ai.operation.name", "execute_tool")
            tool.set_attribute("gen_ai.tool.name", "add")
            # Inputs remain local variables; arguments/results are opt-in and omitted.
            _ = len(sensitive_input) + len(sensitive_arguments)

    provider.force_flush()
    snapshots = tuple(
        SpanSnapshot(
            name=span.name,
            attributes=tuple(sorted(span.attributes.items())),
            span_id=span.context.span_id,
            parent_span_id=span.parent.span_id if span.parent else None,
            schema_url=span.instrumentation_scope.schema_url or "",
        )
        for span in exporter.get_finished_spans()
    )
    roots = [span for span in snapshots if span.name.startswith("invoke_agent")]
    tools = [span for span in snapshots if span.name.startswith("execute_tool")]
    linked = (
        len(roots) == 1
        and len(tools) == 1
        and tools[0].parent_span_id == roots[0].span_id
    )
    return OtelProof(
        sdk_version=versions["opentelemetry-sdk"],
        source_commit=OTEL_GENAI_SOURCE_COMMIT,
        schema_url=OTEL_GENAI_SCHEMA_URL,
        spans=snapshots,
        parent_child_linked=linked,
    )
