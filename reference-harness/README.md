# Reference Harness

This is the curriculum's minimal executable model of a single-agent harness. It exists so learners can trace stable contracts before using a framework.

It includes:

- a provider protocol and deterministic scripted provider
- bounded turns, tool-call budgets, cancellation, and explicit stop reasons
- typed tool registration with a small JSON-Schema subset
- exact-argument approval binding for side-effecting tools
- append-only session messages plus session- and attempt-correlated lifecycle events
- explicit context selection/budget evidence and fail-closed budget errors
- SQLite-backed single-process session/event persistence for reset-recovery labs
- a SQLite durable-task fixture with atomic claims, fenced leases, retry classification, idempotency-intent checks, cooperative cancellation, state-version quarantine, and manual compensation evidence
- repeated-call no-progress detection
- a bounded memory fixture with write policy, provenance, namespace isolation, expiry, retrieval, and deletion
- deterministic routing and sequential fan-out fixtures with budgets and visible partial failure
- pinned capability-adapter and event-exporter ports for protocol/telemetry contract tests
- an optional, exact-version interoperability lane with real MCP discovery/tool validation, A2A JSON-RPC task/artifact exchange plus an authentication boundary, and in-memory OpenTelemetry spans with sensitive content omitted
- repeated-trial evaluation with per-task thresholds and critical-failure release gates

It intentionally does **not** claim production readiness. It does not provide process isolation, handler timeouts, preemptive cancellation during a call, network egress control, cryptographic identity, one-time approval consumption, full event/log redaction, full JSON Schema, or a network model client. The durable-task fixture is a single-host SQLite teaching model: it has no queue service, worker heartbeat, distributed consensus/lease guarantee, real process-kill harness, or exactly-once external-effect guarantee. Memory is in-process lexical retrieval and fan-out is sequential. The optional interoperability proofs use in-process MCP, in-process ASGI for A2A, and an in-memory OpenTelemetry exporter. They do not prove external network transport, TLS/OAuth, resilient protocol retries, an OTLP backend, SLO operation, protocol certification, or stable GenAI-convention compliance.

Run the tests without installing dependencies:

```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -v
```

Run the exact optional interoperability lane in WSL/Linux:

```bash
uv run --extra interop --locked python -m unittest discover -s tests -v
```

Without the optional extra, four interoperability tests skip explicitly while the dependency-free base suite still runs. `uv.lock` freezes the optional lane's transitive resolution. A release-sensitive teaching run must preserve the Python version, lockfile, test output, and current source pins.

Learners should first pass the complete current suite, then add a changed requirement while preserving contract, policy, state, event, and evaluation evidence. Use the minimal runtime for Semester 1 and the bounded extension fixtures as starting points for LAB-C1 through LAB-C5, LAB-C7, and LAB-C8; passing these fixture tests is not the same as passing those labs.
