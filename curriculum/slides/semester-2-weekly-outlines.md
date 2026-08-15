# Semester 2 Weekly Deck Outlines

Every deck begins with requirements/risk and ends with an injected failure, evidence decision, or defense.

## Week 1: Production Requirements

- question: what must be true before “production-ready” has meaning?
- visuals: workload/SLO/data/threat/failure/owner canvas
- activity: reject an underspecified readiness claim
- exit: release and rollback criteria

## Week 2: Orchestration Patterns

- question: what value justifies coordination complexity?
- visuals: routing/parallel/manager/handoff/evaluator tradeoff map
- activity: compare two patterns against deterministic baseline
- exit: evidence that would simplify the design

## Week 3: Durable Execution

- question: what happens between side effect and acknowledgment?
- visuals: transition and crash-point diagrams
- activity: duplicate/partial/cancel recovery
- exit: delivery semantics and exactly-once limit

## Week 4: Memory Systems

- question: how do we measure both memory benefit and harm?
- visuals: provenance/isolation/retention/deletion pipeline
- activity: contamination and deletion test
- exit: one privacy or stale-memory gate

## Week 5: MCP

- question: what does protocol discovery authorize? Nothing by itself.
- visuals: host/client/server and capability negotiation
- activity: version/error/malicious-content contract test
- exit: local policy boundary

## Week 6: A2A

- question: how does delegated work retain identity and lifecycle?
- visuals: AgentCard/message/task/artifact/state flow
- activity: duplicate/cancel/auth failure
- exit: A2A versus MCP boundary

## Week 7: Agentic Threats

- question: what authority path makes the attack real?
- visuals: injection-to-impact attack tree
- activity: precondition/blast-radius analysis
- exit: one non-prompt control

## Week 8: Defense in Depth

- question: which layer prevents, detects, and recovers?
- visuals: policy/approval/isolation/identity/audit/recovery stack
- activity: attack-and-repair variant
- exit: residual-risk decision

## Week 9: Evaluation Engineering

- question: what decision will this evaluation support?
- visuals: capability/regression/security/reliability suite matrix
- activity: grader disagreement and leakage analysis
- exit: predeclared threshold

## Week 10: Reliability and Observability

- question: how will we detect user harm before dashboard comfort?
- visuals: SLO/error-budget and correlated incident timeline
- activity: provider/tool/queue degradation
- exit: corrective action and regression test

## Week 11: Deployment and Tenancy

- question: what evidence supports the isolation claim?
- visuals: local/container/VM/managed boundaries and state ownership
- activity: migration/rollback and cross-session test
- exit: exact tenancy claim

## Week 12: Governance, Privacy, Accessibility

- question: who owns the risk and what proves the control?
- visuals: Govern-Map-Measure-Manage evidence loop
- activity: control/owner/evidence/exception mapping
- exit: one professional-review boundary

## Week 13: Framework Adapters

- question: which semantics change when the framework changes?
- visuals: stable core and adapter comparison
- activity: run common contract tests through two adapters
- exit: portability gap

## Week 14: Product Case Studies

- question: what is observed, documented, source-visible, inferred, or unknown?
- visuals: comparative contract matrix
- activity: source-visible versus managed-product evidence
- exit: dated claim and revalidation trigger

## Week 15: Capstone Red Team

- question: why should this release be stopped?
- visuals: release-gate evidence board
- activity: inject attack/failure, repair, rerun
- exit: release verdict and unresolved risk

## Week 16: Defense and Transfer

- question: can the engineer adapt without the rehearsed path?
- visuals: board roles and transfer conditions
- activity: individual trace and withheld change
- exit: mastery evidence and next repair
