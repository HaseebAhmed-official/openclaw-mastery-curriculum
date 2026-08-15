# Competency Framework

## Purpose

Define observable capabilities for curriculum alignment, learner progression, assessment, hiring adaptation, and program review. Topic exposure is not competency.

## Competency Domains

### C1: Foundations and Problem Analysis

- trace programs, processes, network calls, data flow, concurrency, and failure propagation
- decompose ambiguous requirements and identify when deterministic software is sufficient
- use tests, measurement, and debugging to distinguish causes from symptoms

### C2: Agent and Harness Architecture

- distinguish models, tools, workflows, agents, harnesses, execution environments, and operators
- define authority, state, data, control, stop, and failure boundaries
- compare single-agent, manager, handoff, routing, parallel, and evaluator patterns

### C3: Harness Implementation

- implement provider interfaces and deterministic test doubles
- implement bounded loops, typed tools, validation, structured errors, and budgets
- assemble context with provenance, relevance, freshness, and truncation behavior

### C4: State, Memory, and Durability

- design sessions, event records, checkpoints, replay, and versioned state
- implement retries, idempotency, compensation, cancellation, and recovery
- evaluate memory retention, retrieval, deletion, contamination, and privacy

### C5: Tools, Protocols, and Interoperability

- design discoverable, typed, least-authority tools with useful errors
- implement or integrate MCP and A2A contracts
- port capabilities across frameworks without changing behavioral requirements silently

### C6: Security, Safety, and Privacy

- threat-model prompt injection, tool misuse, confused deputy, exfiltration, persistence, supply chain, identity, and isolation
- design layered policy, approval, sandbox, network, secret, and audit controls
- state assurance limits and residual risk without security theater

### C7: Evaluation and Observability

- define task, trial, transcript, outcome, grader, dataset, and threshold
- combine code, model, human, trace, and end-state graders appropriately
- measure capability, regression, reliability, variance, latency, cost, and human override

### C8: Production and Operations

- define SLOs, capacity, deployment, tenancy, rollback, and incident response
- diagnose failures using correlated traces, metrics, logs, events, and artifacts
- manage releases, migrations, compatibility, dependencies, and operational ownership

### C9: Governance and Responsible Engineering

- map risks, controls, evidence, owners, retention, privacy, accessibility, and review obligations
- communicate limitations to users and decision-makers
- distinguish internal readiness, regulatory obligations, certification, accreditation, and marketing claims

### C10: Research, Communication, and Transfer

- retrieve current primary evidence and label uncertainty
- explain and defend design tradeoffs to multiple audiences
- learn an unfamiliar framework or product, compare it to stable contracts, and transfer a solution to changed constraints

## Evidence Levels

| Level | Name | Observable evidence |
| --- | --- | --- |
| L0 | Orientation | Defines scope and vocabulary; distinguishes facts from assumptions. |
| L1 | Recall and trace | Retrieves core concepts and traces a supplied example. |
| L2 | Guided construction | Completes a representative task with bounded hints and explains each step. |
| L3 | Independent implementation | Builds and tests a standard component without procedural guidance. |
| L4 | Transfer and debugging | Solves a changed task, diagnoses failures, and repairs the correct layer. |
| L5 | System design | Chooses and defends architecture under conflicting constraints. |
| L6 | Production judgment | Handles reliability, security, cost, privacy, operations, and governance evidence. |
| L7 | Expert contribution | Audits, teaches, extends, or produces validated original work that survives external review. |

Mastery at L4 or above requires delayed, unaided, changed-task evidence. Agent-generated artifacts, immediate repetition, recognition, and self-confidence cannot establish the level alone.

## Core Graduation Profile

Every graduate must achieve:

- C1-C4 at L4 or higher
- C5-C8 at L4 or higher
- C9-C10 at L4 or higher
- at least two domains at L5
- capstone-specific security, evaluation, and operations evidence at L5

L6 requires real or high-fidelity production constraints and incident evidence. L7 is post-program expert evidence, not an automatic course award.

## Role Profiles

| Profile | Required depth |
| --- | --- |
| Product/Operator | C2, C6-C10 at L4; can configure, bound, evaluate, and govern existing systems. |
| Harness Engineer | C1-C8 at L5; implements core contracts and ports across adapters. |
| Platform/SRE | C4, C7-C9 at L5-L6; owns durability, observability, deployment, and incidents. |
| Security/Assurance | C2, C5-C9 at L5-L6; attacks controls, verifies mitigations, and states assurance limits. |
| Tools/Protocols | C3-C7 at L5; builds typed tools, MCP/A2A adapters, and compatibility tests. |
| Core/Framework | C1-C8 at L5-L6; contributes runtime, orchestration, and evaluation infrastructure. |
| Local-Model Infrastructure | C1, C3, C7-C9 at L5; owns model serving, routing, performance, privacy, and capacity. |

## Evidence Bundle

For every claimed domain/level, preserve:

- artifact or commit reference
- task and constraints
- assistance received
- tests and observed results
- trace or end-state evidence where relevant
- failure analysis and repair
- source/version baseline
- rubric decision and assessor
- delayed transfer result

## Anti-Outsourcing Standard

Agents may help research, critique, generate tests, or accelerate implementation. The learner must still independently trace control flow, explain data and authority boundaries, reproduce failures, justify tests, verify claims, debug changed conditions, and defend final decisions. If these cannot be demonstrated, the artifact does not prove the learner's competency.
