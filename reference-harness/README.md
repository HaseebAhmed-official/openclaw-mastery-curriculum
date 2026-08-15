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
- repeated-call no-progress detection
- a bounded memory fixture with write policy, provenance, namespace isolation, expiry, retrieval, and deletion
- deterministic routing and sequential fan-out fixtures with budgets and visible partial failure
- pinned capability-adapter and event-exporter ports for protocol/telemetry contract tests
- repeated-trial evaluation with per-task thresholds and critical-failure release gates

It intentionally does **not** claim production readiness. It does not provide process isolation, handler timeouts, cancellation during a tool call, network egress control, distributed leases/workflow semantics, cryptographic identity, one-time approval consumption, event/log redaction, full JSON Schema, or a network model client. The SQLite store is single-process; memory is in-process lexical retrieval; fan-out is sequential; and the generic adapter/exporter ports do not implement or certify MCP, A2A, or OpenTelemetry. Those boundaries become explicit Semester 2 extensions rather than hidden dependencies.

Run the tests without installing dependencies:

```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -v
```

Learners should first pass the complete current suite, then add a changed requirement while preserving contract, policy, state, event, and evaluation evidence. Use the minimal runtime for Semester 1 and the bounded extension fixtures as starting points for LAB-C1, LAB-C3, LAB-C4, LAB-C5, LAB-C7, and LAB-C8; passing these fixture tests is not the same as passing those labs.
