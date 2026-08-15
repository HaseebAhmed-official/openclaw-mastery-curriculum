# Reference Harness

This is the curriculum's minimal executable model of a single-agent harness. It exists so learners can trace stable contracts before using a framework.

It includes:

- a provider protocol and deterministic scripted provider
- bounded turns, tool-call budgets, cancellation, and explicit stop reasons
- typed tool registration with a small JSON-Schema subset
- exact-argument approval binding for side-effecting tools
- append-only session messages and lifecycle events
- repeated-call no-progress detection
- a small repeated-trial evaluation runner

It intentionally does **not** claim production readiness. It does not provide process isolation, network egress control, durable database transactions, distributed leases, cryptographic identity, real JSON Schema coverage, or a network model client. Those become explicit Semester 2 extensions rather than hidden dependencies.

Run the tests without installing dependencies:

```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -v
```

Learners should first pass the tests, then add a changed requirement while preserving contract, policy, event, and evaluation evidence.
