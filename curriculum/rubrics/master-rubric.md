# Master Rubric

## Scale

| Score | Meaning |
| ---: | --- |
| 0 | Missing, fabricated, unsafe, or cannot be explained. |
| 1 | Fragmentary; works only under copied/guided conditions; major errors remain. |
| 2 | Baseline task works; evidence or boundary reasoning is incomplete. |
| 3 | Independent, correct, tested, and defensible under representative failures. |
| 4 | Transfers under changed constraints, handles tradeoffs, and improves evidence or design. |

Scores describe the submitted evidence, not a learner's identity or potential.

## Dimensions

### R1: Problem Framing and Architecture

Assesses requirements, deterministic baseline, agentic justification, stable contracts, alternatives, data/control/authority boundaries, and simplicity.

### R2: Implementation Correctness

Assesses typed contracts, bounded loop, tools, context, state, memory, protocols/adapters, code quality, and correct end state.

### R3: Testing and Debugging

Assesses reproducibility, test quality, seeded failures, root-cause diagnosis, regression coverage, and changed-condition repair.

### R4: Security, Safety, and Privacy

Assesses threat model, least authority, policy/approval, isolation, identity, secrets, data lifecycle, attack evidence, mitigation, recovery, and residual risk.

### R5: Evaluation Validity

Assesses task corpus, repeated trials, grader suitability, trace/end-state inspection, variance, leakage, thresholds, failure taxonomy, and claim limits.

### R6: Reliability and Operations

Assesses durability, retries/idempotency, cancellation, observability, SLOs, capacity, latency/cost, deployment, incident response, migration, backup, and rollback.

### R7: Communication and Governance

Assesses source provenance, fact/inference separation, diagrams, decision records, accessibility, ethics, stakeholder communication, ownership, and change control.

### R8: Independence and Transfer

Assesses assistance disclosure, unaided tracing, oral defense, delayed retention, portability, and performance under changed constraints.

## Default Weighting

| Dimension | Semester 1 | Semester 2/capstone |
| --- | ---: | ---: |
| R1 | 15% | 12.5% |
| R2 | 25% | 17.5% |
| R3 | 20% | 12.5% |
| R4 | 15% | 15% |
| R5 | 10% | 15% |
| R6 | 5% | 12.5% |
| R7 | 5% | 7.5% |
| R8 | 5% | 7.5% |

Local programs may adjust weights, but not critical gates.

## Pass Rules

- Overall weighted score: at least 2.5/4.
- R2, R3, R4, R5, and R8: at least 2 for Semester 1 and at least 3 for capstone release.
- No unresolved critical gate failure.
- Delayed transfer must pass independently; it cannot be replaced by points elsewhere.

## Critical Gate Failures

- fabricated, unverifiable, or misrepresented evidence
- learner cannot trace or explain material submitted behavior
- hidden high-impact side effect or unsafe execution
- critical authorization, isolation, secret, or exfiltration defect presented as acceptable without explicit authorized risk decision
- no meaningful tests or tests weakened to hide failure
- evaluation leakage or post-result threshold manipulation
- final output conflicts with trace/end state and conflict is ignored
- unrecoverable production claim without rollback/recovery evidence
- current product/security claim based only on unsourced or stale material

## Distinction

Distinction requires at least 3.5/4 overall, no dimension below 3, changed-task transfer at 4, and an externally useful contribution such as a reproducible evaluation, verified security repair, protocol adapter, core change, or teaching artifact that survives independent review.
