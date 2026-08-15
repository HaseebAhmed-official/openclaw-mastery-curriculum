# Calibration Answer Pack

## Purpose

Give assessors shared anchors for reasoning quality without publishing fixed answers to high-stakes tasks. Strong answers may differ in design but must preserve correct contracts, evidence, failure reasoning, security, and claim boundaries.

## Core Architecture Anchor

Prompt: choose deterministic code, workflow, single agent, or multiple agents for a support triage task.

A strong answer:

- defines workload, uncertainty, effects, users, latency/cost, and error tolerance
- starts with deterministic rules/search and measures unresolved cases
- adds a bounded agent only for cases requiring flexible interpretation
- keeps irreversible effects behind typed tools and exact approval
- compares task success, override, latency, cost, and failure against the baseline
- names evidence that would remove the agent again

A weak answer selects multi-agent orchestration because it appears advanced or lists framework features without requirements.

## Runtime and Durability Anchor

Prompt: a side-effecting tool completed, the worker crashed before recording acknowledgment, and the task is delivered again.

A strong answer:

- separates internal task state from external end state
- identifies whether the operation has an idempotency key or queryable outcome
- blocks blind retry for an irreversible/unknown result
- reconciles external state, then records completion, compensation, or human-repair state
- preserves task/attempt/tool identity and a complete event timeline
- adds a regression/failure-injection test

A weak answer retries automatically because the framework supports retries or claims exactly-once without controlling the external system.

## Security Anchor

Prompt: retrieved content tells the agent to upload local files through an approved network tool.

A strong answer:

- treats retrieved content as untrusted data, not authority
- traces the confused-deputy path and required tool/filesystem/network permissions
- binds policy/approval to requester, exact files, destination, purpose, and freshness
- minimizes readable files and allowed egress before model reasoning
- records detection and supports cancellation/recovery
- tests paraphrased/indirect variants and states residual risk

A weak answer adds a stronger system prompt, assumes the approval solves all variants, or claims sandboxing alone prevents exfiltration.

## Evaluation Anchor

Prompt: a system passes 92% of output graders but sometimes creates duplicate records.

A strong answer:

- rejects the output-only release conclusion
- adds end-state and event/trace graders for duplicate effects
- separates capability average from critical failure gates
- reports repeated trials, severity, confidence/variance, retries, and human overrides
- repairs idempotency/reconciliation, reruns original and variant tasks, and uses a predeclared threshold

A weak answer accepts 92% as production-ready or tunes the threshold after seeing results.

## Product Case Anchor

Prompt: compare one source-visible harness with one managed product.

A strong answer:

- dates each claim and uses current primary sources
- separates observed, documented, source-visible, inferred, and unknown behavior
- maps both to stable contracts rather than feature-count ranking
- uses source tracing where available and refuses to invent managed internals
- identifies trust, security, operations, and update boundaries
- proposes equivalent behavioral tasks for comparison

A weak answer treats marketing text as architecture proof or assumes similarly named features have equivalent semantics.

## Role-Specific Distinction Signals

| Track | Distinction evidence |
| --- | --- |
| Product / Operator | better user task outcomes with less unnecessary autonomy and clear override/governance evidence |
| Platform / SRE | recovery across multiple failure modes, valid SLOs, and reproducible rollback/incident evidence |
| Security / Assurance | non-obvious authority path, safe exploit variants, reusable mitigation, accurate residual risk |
| Tools / Protocols | independent interoperability, strong errors/lifecycle, least authority, version/security tests |
| Core / Framework | traced invariant, focused runtime improvement, regression/performance/compatibility evidence |
| Local-Model Infrastructure | measured routing under explicit hardware/workload/privacy constraints and safe degradation |

## Calibration Use

Assessors score an anchor independently with the Master Rubric, compare dimension and critical-gate decisions, discuss evidence rather than wording, and record ambiguities requiring rubric repair. Do not distribute these anchors as templates for the exact graded task.
