# Semester 1: Harness Foundations

## Goal

Move a prerequisite-ready learner from tracing small systems to independently implementing, testing, and defending a minimal agent harness. Frameworks and network model APIs are optional until the deterministic reference path works.

## Exit Capability

The learner can build a bounded single-agent harness with a provider contract, typed tools, context assembly, session/event state, policy and approval, isolated execution boundary, observability, and a basic evaluation harness. They can diagnose whether a failure belongs to the model, context, tool, policy, execution, state, or evaluator layer.

## Weekly Sequence

| Week | Theme | Build/evidence | Assessment |
| --- | --- | --- | --- |
| 1 | Discipline map and system boundaries | Map model, workflow, agent, harness, operator, data, control, and trust boundaries | Diagnostic trace and vocabulary defense |
| 2 | Reproducible engineering environment | Python project, tests, fixtures, lint/type checks, Git evidence | Environment and change-control gate |
| 3 | Contracts and deterministic test doubles | Provider protocol, scripted model, response types, error taxonomy | Contract-test practical |
| 4 | Agent loop and termination | Bounded loop, budgets, stop reasons, cancellation, no-progress detection | Loop invariant and failure test |
| 5 | Typed tool registry | Schemas, discovery, validation, structured errors, idempotency metadata | Malformed-call and duplicate-call drill |
| 6 | Tool execution boundary | Timeouts, resource limits, working directory, environment ownership, audit event | Execution-boundary review |
| 7 | Context engineering | Instruction/data separation, provenance, relevance, freshness, token budget, truncation | Context-ablation lab |
| 8 | Midterm trace and debug | Diagnose seeded failures across loop, context, tool, and provider layers | Individual practical and viva |
| 9 | Sessions and event records | Session identity, append-only events, artifact references, schema versions | State reconstruction task |
| 10 | Checkpoints and replay | Snapshot, resume, deterministic replay boundary, migration failure | Crash-and-resume lab |
| 11 | Policy and human approval | Capability policy, risk classification, approval binding, deny-by-default behavior | Confused-deputy scenario |
| 12 | Memory foundations | Working/episodic/semantic distinctions, retention, retrieval, deletion, provenance | Memory-quality and deletion test |
| 13 | Observability | Correlated traces, metrics, logs, events, artifacts, redaction | Failure timeline reconstruction |
| 14 | Evaluation foundations | Task/trial/grader/dataset, repeated trials, trace and end-state checks | Build a small regression suite |
| 15 | Minimal harness integration | Integrate components, document contracts, test failure matrix | Architecture and code review |
| 16 | Final practical and transfer | Implement a changed tool/provider/policy requirement without procedural help | Demonstration, oral defense, delayed retest |

## Required Labs

- LAB-A1 reproducible Python/Git environment
- LAB-A2 API, process, and failure tracing
- LAB-A3 testing and defect repair
- LAB-A4 threat-model baseline
- LAB-B1 deterministic provider adapter
- LAB-B2 bounded loop and stop conditions
- LAB-B3 typed tool registry
- LAB-B4 context assembly and budget
- LAB-B5 session/event log and replay
- LAB-B6 policy, approval, and execution boundary
- LAB-B7 observability and evaluation baseline

## Required Deliverables

- tested minimal harness repository
- architecture and trust-boundary diagram
- contract and failure taxonomy
- trace and event evidence bundle
- context-ablation report
- policy/approval test matrix
- evaluation corpus with repeated trials
- design review response
- oral defense and delayed transfer result

## Canonical Constraints

- Use a deterministic model test double before a paid or network model.
- Keep framework-specific code outside core contracts.
- Every external side effect must pass tool validation and policy.
- Every loop termination must produce a machine-readable reason.
- Events must identify session, attempt, actor/capability, and outcome.
- Tests must include denial, malformed input, timeout, duplicate action, and partial failure.

## Teaching Support

- [Semester 1 Teaching Guide](teaching-guide.md)
- [Lab Catalog](../labs/lab-catalog.md)
- [Core Lab Guides](../labs/core-lab-guides.md)
- [Assessment Map](../assessment-map.md)
- [Question Bank](../assessment/question-bank.md)
