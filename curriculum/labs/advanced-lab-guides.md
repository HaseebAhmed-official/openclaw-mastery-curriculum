# Advanced Lab Guides

## Common Production Evidence

Every advanced lab preserves requirements, architecture, source/version baseline, failure injection, trace and end state, security/privacy review, rollback or recovery, measured result, and residual risk. Use bounded disposable environments for attack labs.

The reference harness supplies bounded starting fixtures, not completed advanced labs:

| Labs | Starting code | Learner must still add and prove |
| --- | --- | --- |
| LAB-C1 | `reference-harness/src/agent_harness/orchestration.py` | a second real pattern, timing/cost evidence, concurrency where claimed, authority propagation, and comparative ablation |
| LAB-C3 | `reference-harness/src/agent_harness/memory.py` | durable/indexed retrieval, contamination corpus, privacy/deletion propagation, quality metrics, and unavailable-store behavior |
| LAB-C4 through LAB-C5 | `reference-harness/src/agent_harness/integration.py` | pinned MCP/A2A implementation, protocol traces, auth/transport behavior, malformed content, timeout, cancellation, and compatibility tests |
| LAB-C7 | `reference-harness/src/agent_harness/testing.py` | representative corpus, valid graders, repeated nondeterministic trials, uncertainty, leakage controls, latency/cost, and release rationale |
| LAB-C8 | attempt-correlated runtime events plus `integration.py` | timestamps, trace/span model, metrics/logs, exporter/version pin, redaction, SLOs, alerts, and incident reconstruction |

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
