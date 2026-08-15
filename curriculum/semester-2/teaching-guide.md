# Semester 2 Teaching Guide

## Instructor Goal

Teach production judgment under uncertainty and failure. Feature count, autonomy, benchmark scores, and framework vocabulary are not substitutes for secure behavior, recovery, evaluation validity, or operational ownership.

## Delivery Pattern

Each week uses a production case:

1. State requirements, constraints, risk, and decision owner.
2. Predict failure modes before implementation.
3. Compare the simplest valid architectures.
4. Implement or operate one bounded slice.
5. Inject a failure or attack.
6. Inspect traces and end state.
7. Repair and rerun the evidence gate.
8. Defend tradeoffs and residual risk.

## Week-by-Week Guide

### Week 1: Production Requirements

- Teach SLOs, threat/data models, failure domains, capacity, cost, tenancy, and ownership as design inputs.
- Require measurable acceptance and rollback criteria.
- Reject “production-ready” when workload, operator, data, or trust assumptions are unstated.

### Week 2: Orchestration Patterns

- Compare deterministic workflows, routing, parallelization, manager, handoff, and evaluator-optimizer.
- Measure added quality against latency, cost, coordination failure, and observability burden.
- Require a simpler baseline and an explicit reason for every agent boundary.

### Week 3: Durable Execution

- Inject crash, duplicate delivery, timeout, partial side effect, and cancellation.
- Distinguish retryable, terminal, compensatable, and human-recovery states.
- Challenge exactly-once claims and require idempotency evidence.

### Week 4: Memory Systems

- Teach indexing, retrieval, reranking, retention, deletion, provenance, isolation, and contamination.
- Measure both benefit and harm; do not grade only retrieval recall.
- Include malicious and stale memories.

### Week 5: MCP

- Trace host/client/server responsibilities, modern per-request version/capability metadata, discovery, transport, authorization, and legacy-era compatibility boundaries.
- Test error and version behavior.
- Prevent learners from equating discovery with trust.

### Week 6: A2A

- Trace AgentCard, message, task, artifact, parts, streaming, asynchronous state, and bindings.
- Test identity, authorization, duplicate delivery, and task cancellation.
- Compare A2A's system boundary with MCP rather than treating them as interchangeable.

### Week 7: Agentic Threat Modeling

- Start from assets and authority, then model prompt injection, confused deputy, exfiltration, excessive agency, persistence, identity, and supply chain.
- Require exploit preconditions and blast radius, not threat-name lists.

### Week 8: Defense in Depth

- Combine policy, approval, sandbox, filesystem/network controls, secrets, identity, audit, and recovery.
- Test bypasses and stale assumptions.
- Grade residual-risk accuracy and repair evidence.

### Week 9: Evaluation Engineering

- Separate capability, regression, safety, reliability, and production monitoring suites.
- Require repeated trials, grader rationale, disagreement analysis, leakage controls, and thresholds tied to a decision.
- Include trace and end-state grading for side-effecting tasks.

### Week 10: Reliability and Observability

- Define SLOs and error budgets before instrumentation.
- Inject queue pressure, provider degradation, tool failure, and state inconsistency.
- Require timeline reconstruction, mitigation, recovery, and corrective action.

### Week 11: Deployment and Tenancy

- Compare local, container, VM, managed, and distributed boundaries only against stated needs.
- Teach secret/config ownership, migrations, rollback, backups, isolation, and data lifecycle.
- Challenge hostile multi-tenant claims with concrete evidence requirements.

### Week 12: Governance, Privacy, and Accessibility

- Map risk to control, owner, evidence, review cadence, and exception process.
- Address user notice/control, retention/deletion, protected data, incident escalation, accessibility, and human override.
- State when legal or domain-professional review is required.

### Week 13: Framework Adapters

- Hold behavioral requirements constant while changing adapter/framework.
- Identify defaults, hidden state, policy differences, trace semantics, and portability gaps.
- Require contract tests before migration claims.

### Week 14: Product Case Studies

- Use dated primary sources and observable behavior.
- Map product capabilities to stable harness contracts and unknowns.
- Do not infer private architecture or treat marketing pages as security proof.

### Week 15: Capstone Operation and Red Team

- Freeze a release candidate.
- Run the evaluation suite, performance/cost tests, threat scenarios, incident drill, rollback, and evidence audit.
- Block defense if critical findings remain unresolved or falsely downgraded.

### Week 16: Defense and Transfer

- Use a multi-role board: engineering, security, operations, product/governance.
- Ask each learner to trace a withheld failure and adapt one capability under a changed provider, protocol, policy, or tenancy condition.
- Schedule a delayed individual retest for the highest-risk competency.

## Case-Study Selection

Select cases for contrasting architecture, trust, distribution, or operating models. At least one source-visible system should permit code tracing. At least one product case should teach the boundary between public behavior and unknown internal implementation.

OpenClaw remains a useful source-visible operator/platform case. Hermes Agent can support skills/memory/provider and trust-boundary analysis. ChatGPT Work and xAI agent tooling can support product-capability and managed-system analysis. Verify every current claim before delivery.

## Capstone Review Cadence

- proposal: problem, deterministic baseline, agentic justification
- architecture gate: contracts, data, authority, failure, evidence plan
- alpha gate: core path and deterministic tests
- security/evaluation gate: attacks, corpus, graders, thresholds
- release-candidate gate: deployment, SLO, incident, rollback, privacy
- final board: live evidence, oral defense, changed task

## Instructor Readiness Gate

The instructor team must include or consult implementation, security, operations, and assessment expertise; execute all critical labs; calibrate anchor submissions; verify current standards/product sources; and rehearse the capstone incident and red-team scenarios.
