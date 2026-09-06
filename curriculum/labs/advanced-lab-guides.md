# Advanced Lab Guides

## Common Production Evidence

Every advanced lab preserves requirements, architecture, source/version baseline, failure injection, trace and end state, security/privacy review, rollback or recovery, measured result, and residual risk. Use bounded disposable environments for attack labs.

The reference harness supplies bounded starting fixtures, not completed advanced labs:

| Labs | Starting code | Learner must still add and prove |
| --- | --- | --- |
| LAB-C1 | `reference-harness/src/agent_harness/orchestration.py` | a second real pattern, timing/cost evidence, concurrency where claimed, authority propagation, and comparative ablation |
| LAB-C2 | `reference-harness/src/agent_harness/durability.py` | real process termination, actual timeout/cancellation boundary, queue/worker contention and heartbeat, external-service reconciliation, migration/backup/restore, chosen delivery semantics, and comparison with an approved durable engine |
| LAB-C3 | `reference-harness/src/agent_harness/memory.py` | durable/indexed retrieval, contamination corpus, privacy/deletion propagation, quality metrics, and unavailable-store behavior |
| LAB-C4 | `reference-harness/src/agent_harness/integration.py` plus the optional MCP proof in `protocol_proofs.py` | external transport, controlled side effect plus harness approval, returned-content injection, disconnect/timeout/retry, legacy compatibility if claimed, and safe protocol traces |
| LAB-C5 | `reference-harness/src/agent_harness/integration.py` plus the optional A2A JSON-RPC/ASGI proof in `protocol_proofs.py` | asynchronous or streaming transition, capability/authorization mismatch, duplicate handling, cancellation/timeout, malformed artifact, remote implementation swap, and safe protocol traces |
| LAB-C6 | `reference-harness/src/agent_harness/security.py` and `reference-harness/tests/test_security.py` | independently authored attack variants, real trust-boundary enforcement where claimed, memory/supply-chain path, detection and recovery evidence, and independent reproduction |
| LAB-C7 | `reference-harness/src/agent_harness/testing.py` | representative corpus, valid graders, repeated nondeterministic trials, uncertainty, leakage controls, latency/cost, and release rationale |
| LAB-C8 | attempt-correlated runtime events, `integration.py`, and the optional in-memory OpenTelemetry proof in `protocol_proofs.py` | production exporter/backend, metrics/logs, correlation contract, redaction verification, SLOs, alerts, injected degradation, and incident reconstruction |

Passing reference tests proves only the local contract examples. It cannot be submitted as advanced-lab evidence without the required extensions and measurements.

## LAB-C1: Orchestration Pattern Comparison

### Objective

Choose the simplest pattern that meets a measurable requirement.

### Task

Implement a deterministic baseline plus two patterns selected from routing, parallelization, manager/orchestrator, handoff, or evaluator-optimizer. Hold task corpus and acceptance criteria constant.

### Required Tests

- route ambiguity and misclassification
- partial parallel failure and slow worker
- delegated authority mismatch
- duplicated or conflicting result
- orchestrator/evaluator loop budget

### Evidence and Gate

Compare success, variance, latency, model/tool calls, cost proxy, failure propagation, trace complexity, and human intervention. Pass only if the selected pattern's added complexity is justified by evidence. Transfer: remove one agent and determine whether quality materially changes.

## LAB-C2: Durable Crash, Retry, and Recovery

### Objective

Preserve correct, auditable state across failures and retries.

### Task

Back the session/event contract with a durable store or approved workflow engine. Model transitions explicitly and inject crash before/after external side effects.

### Required Tests

- retryable provider timeout
- non-retryable validation failure
- duplicate task delivery
- process loss during work
- cancellation during pending work
- partial external side effect
- incompatible state/schema version

### Evidence and Gate

Pass with an idempotency strategy, transition log, checkpoint/recovery result, compensation or manual-repair path, and stated delivery semantics. “Exactly once” requires proof across the external boundary; otherwise reject the claim.

## LAB-C3: Memory Contamination and Deletion

### Objective

Measure whether memory improves tasks without violating isolation, freshness, privacy, or deletion requirements.

### Task

Implement a memory interface with write policy, provenance, retrieval, retention, and deletion. Build a corpus with useful, stale, irrelevant, malicious, and cross-user records.

### Required Tests

- retrieval precision and task effect
- stale contradiction
- injected instruction inside memory
- namespace/tenant isolation
- deletion and downstream cache/index cleanup
- unavailable memory store

### Evidence and Gate

Report benefit, contamination rate, privacy boundary, deletion evidence, failure behavior, and residual risk. Pass only if the system treats retrieved text as untrusted data and does not silently cross isolation boundaries.

## LAB-C4: MCP Integration and Contract Test

### Objective

Integrate an MCP capability while preserving harness policy and observability.

### Task

Pin a current MCP specification/SDK version. Build or use a minimal server and connect it through the harness adapter. Expose one read capability and one controlled side effect.

### Required Tests

- modern per-request version/capability declarations and `server/discover`; if legacy support is claimed, test its initialization-era path separately
- unsupported capability/version behavior
- invalid arguments and server error
- authorization denial
- disconnect, timeout, and retry boundary
- prompt injection in returned content
- side effect still requiring harness approval

### Evidence and Gate

Preserve protocol messages or safe traces, contract tests, policy decisions, and end state. Pass when MCP discovery never bypasses local authority and version assumptions are explicit.

## LAB-C5: A2A Task and Artifact Exchange

### Objective

Exchange delegated work across an agent boundary with explicit identity, lifecycle, and artifacts.

### Task

Pin a current A2A specification/SDK version. Publish or consume an AgentCard, send a task/message, return an artifact, and handle one asynchronous or streaming transition.

### Required Tests

- capability mismatch
- identity/authentication failure
- authorization failure
- duplicate task/message
- cancellation and timeout
- malformed artifact
- untrusted content returned by remote agent

### Evidence and Gate

Pass with a task state diagram, protocol trace, artifact validation, duplicate handling, trust analysis, and local-policy enforcement. Transfer: replace the remote agent with a different implementation while preserving contract tests.

## LAB-C6: Agentic Attack and Mitigation

### Objective

Demonstrate exploitable authority paths and verify layered mitigation.

### Task

Select at least four scenarios spanning prompt injection, confused deputy, exfiltration, excessive agency, persistence/memory, supply chain, identity, or approval mismatch.

### Procedure

1. Declare authorization, data, and containment boundaries.
2. Write exploit success criteria before testing.
3. Capture preconditions, execution path, trace, end state, and blast radius.
4. Implement preventive and detective controls plus recovery.
5. Retest the original exploit and at least one variant.

### Starting Exercise: Compromised Model, Bounded Authority

Prerequisites: LAB-B2 tool validation, LAB-B5 policy, LAB-B6 event reconstruction, and a passing reference-harness base suite. Read `security.py` and `test_security.py` alongside the runtime's authorization-before-dispatch path. No paid model or external service is required. Use a disposable checkout, synthetic documents, and in-memory effects only.

Run from `reference-harness` in WSL/Linux:

```bash
PYTHONPATH=src python -m unittest discover -s tests -p test_security.py -v
```

On PowerShell, set `$env:PYTHONPATH = "src"` before the same `python -m unittest` command. The starting fixture contains 14 test methods; individual methods also exercise variants. Record the actual command, Python version, commit plus any dirty diff, elapsed time, pass/skip counts, and observed effects. Do not infer full lab completion from this count.

Threat model: an attacker controls a retrieved inbox document; assume the model follows its malicious instruction and emits an export call. The host owns session identity, capability scope, registry bindings, clock, and approvals. Handlers and the Python process remain trusted. The private canary is synthetic, and destinations are strings in a local list, never real network endpoints.

1. Before running the tests, predict the allowed operation, stolen resource, effect count, and terminal reason for both policies. Draw `retrieved text -> provider proposal -> schema -> capability -> approval -> handler -> evidence`.
2. Inspect `test_compromised_model_positive_control_and_resource_denial`. The deliberately permissive policy records one unauthorized synthetic export. Repeating the same proposed calls under `ScopedPolicy` must produce zero export effects, `policy_denied`, and no `tool.started` event for the denied call. Explain why a permissive positive control is necessary to show the attack path was reachable.
3. Trace the cross-resource read, unknown host session, changed destination, and model-supplied `approved` flag cases. A tool's read-only classification does not authorize every resource. Schema validity and human-looking text do not grant permission.
4. Trace the approved benign export. It must succeed once. Replay under a new call ID or run attempt, change arguments within an otherwise allowed scope, expire or revoke the grant, and check that authority is not reused. At the exact expiry instant the grant is invalid. The 32 competing authorization attempts must consume only one grant; this does not prove a thread-safe complete runtime.
5. Inspect the partial-effect failure test. The synthetic handler records an effect and then raises. The retry must not produce a second effect. Reconcile the local sink and event record before making a new approval decision; never interpret a failed handler response as proof that no effect occurred.
6. Inspect replacement-tool and schema-change denial. Explain why object/metadata binding can detect these changes but cannot establish package provenance, stop a compromised handler, or enforce OS isolation.

### Required Extensions and Assessment

Submit at least four attack families from the task above. The provided examples can supply a baseline, but at least one family must exercise a separately implemented memory/persistence, supply-chain, or identity path, and each family needs an unseen variant of your own.

| Evidence | Pass condition | Automatic failure |
| --- | --- | --- |
| Threat model and exploit | Controlled preconditions, reachable positive control, explicit attacker and trusted-host powers | Claims a model resisted injection when the provider was scripted |
| Preventive control and benign task | Original and variant denied before their forbidden effects; authorized task still succeeds | Relies only on refusal text or a prompt blacklist; prevents all useful tasks |
| Detection | Correlated attempt/call IDs, policy decisions, expected effect count, and a reproducible detection rule checked against benign traffic | Treats absence of an alert as absence of compromise |
| Recovery | Partial effect inspected, outstanding grants revoked, a fresh policy/restart tested, and new authority issued only after reconciliation | Automatically restores spent approvals or blindly retries ambiguous effects |
| Boundary and transfer | Student explains actual enforcement layer and implements a changed task while preserving evidence | Calls an argument allowlist a network firewall or treats session labels as authentication |

For a network-control claim, add a disposable local service/proxy and prove connection-level denial, redirects, DNS/IP handling, and permitted traffic separately. For a persistence claim, exercise the actual durable store and deletion/recovery path. Do not submit those properties as proven by this in-memory fixture.

Instructor sequence: demonstrate one positive control, ask for predictions before revealing the denial trace, let learners implement a different attack variant unaided, then conduct an oral defense. Record actual learner duration and assistance instead of assuming a timing budget. Oral prompts: Why can read-only tools leak data? What changes if session identity is attacker-controlled? What happens after the effect succeeds but its response is lost? Where must enforcement live if the tool handler itself is malicious?

Source rationale reviewed 2026-09-06: [OWASP AI Agent Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html) supports scoped tools, authorization, untrusted-content handling, approval integrity, and adversarial testing. [MCP security best practices](https://modelcontextprotocol.io/docs/draft/tutorials/security/security_best_practices) supplies a separate confused-deputy/authorization reference; it is a moving draft, not a protocol conformance claim. This fixture's design and results are local engineering evidence and require their own tests. Source sampling is sufficient for these bounded teaching claims; broad model-security effectiveness remains unmeasured.

### Evidence and Gate

Pass when critical paths are blocked or explicitly accepted by an authorized owner, detection evidence is reliable, recovery is rehearsed, and residual risk is not hidden. Do not use real credentials, targets, or third-party data.

## LAB-C7: Evaluation Corpus and Regression Gate

### Objective

Build an evaluation system that can support a release decision.

### Task

Create 20-50 realistic initial tasks or justify a smaller high-cost corpus. Separate capability, regression, security, and reliability subsets. Run repeated trials where behavior is nondeterministic.

### Required Analysis

- task coverage and representativeness
- contamination/leakage risk
- code/model/human grader validity
- trace versus end-state disagreements
- variance and confidence limits
- severity-weighted failure taxonomy
- latency, cost, tool failure, retry, and human override
- threshold selected before final release verdict

### Evidence and Gate

Pass when another reviewer can reproduce the report and the decision follows predeclared criteria. Averages cannot hide critical safety failures.

## LAB-C8: Observability, SLO, and Incident Simulation

### Objective

Operate the system through degradation and produce actionable learning.

### Task

Define availability, success, latency, recovery, cost, and human-override objectives. Inject provider latency/failure, tool degradation, queue pressure, or state inconsistency.

### Evidence and Gate

Preserve alerts, correlated timeline, diagnosis, mitigation, recovery, user impact, evidence gaps, and corrective actions. Pass when the learner identifies the actual failure layer, restores service within the exercise objective, and adds a regression/control test.

## LAB-C9: Deployment, Tenancy, and Rollback

### Objective

Defend a deployable architecture and its trust claims.

### Task

Deploy the harness in a bounded local, container, VM, or approved managed environment. Define configuration/secrets, network, filesystem, identity, storage, backup, migration, update, and rollback ownership.

### Required Tests

- missing or invalid configuration fails safely
- secret is absent from logs/artifacts
- migration success and failure
- rollback to a compatible version
- backup restore or declared alternative
- cross-session and, if claimed, cross-tenant isolation
- unavailable dependency behavior

### Evidence and Gate

Pass with deployment diagram, runbook, test evidence, rollback result, data lifecycle, and accurate single-user/team/multi-tenant boundary. Do not claim enterprise readiness from containerization alone.
