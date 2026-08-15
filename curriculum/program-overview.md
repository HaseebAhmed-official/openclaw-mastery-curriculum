# Program Overview

## Mission

Develop engineers who can build and govern agent harnesses from first principles, not merely operate one current product. The program treats models as fallible components inside larger software systems and makes human judgment, evidence, and explicit trust boundaries central.

## Definitions

- **Model:** a probabilistic component that produces or scores outputs from context.
- **Tool:** a typed capability that reads, computes, changes state, or communicates with an external system.
- **Workflow:** a mostly predetermined control path around models and tools.
- **Agent:** a model-directed process that chooses actions within bounded authority and stop conditions.
- **Harness:** the software and operational control plane that assembles context, exposes tools, enforces policy, persists state, executes actions, observes behavior, and evaluates outcomes.
- **Agent system:** one or more agents plus their harness, execution environments, data, protocols, operators, and governance.

These are working engineering definitions. Learners must compare alternate definitions and state which boundary they use in design work.

## Audience

- undergraduate or graduate computing students
- independent learners seeking first-principles capability
- software, AI, platform, security, and reliability engineers
- instructors building agent-systems courses
- organizations creating internal capability programs

## Entry Profile

Learners may start near zero, but they must pass the prerequisite bridge before core implementation. Prior framework use does not waive programming, debugging, networking, testing, security, or statistical reasoning evidence.

## Design Principles

### Stable contracts before products

Teach concepts that survive vendor churn. Frameworks and products are adapters or case studies, not foundational truth.

### Build before abstraction

Learners first implement a small deterministic harness with a model test double. Frameworks are introduced only after learners can trace the equivalent control flow and failure modes.

### Evidence before confidence

Claims require tests, traces, end-state inspection, source provenance, oral defense, and changed-task transfer. Self-reported confidence and generated artifacts are supporting evidence only.

### Security and governance by construction

Authority, isolation, data flow, approvals, auditability, privacy, and recovery are designed with the loop, not added after deployment.

### Simplicity before autonomy

Use deterministic code or workflows when they satisfy the requirement. Add model-directed autonomy only where its value exceeds its uncertainty, cost, and attack surface.

### Current claims are versioned

Standards, frameworks, product behavior, releases, and advisories are dated. Stable theory and time-sensitive implementation facts are stored and assessed separately.

## Program Learning Outcomes

Graduates will be able to:

| ID | Outcome |
| --- | --- |
| PLO-1 | Apply programming, systems, networking, data, testing, security, and statistical foundations to agent-system problems. |
| PLO-2 | Analyze requirements and choose appropriately among deterministic code, workflows, single agents, and multi-agent systems. |
| PLO-3 | Design and implement a bounded harness with provider abstraction, typed tools, context management, policy, execution, sessions, memory, and explicit stop conditions. |
| PLO-4 | Design stateful and durable behavior using event records, checkpoints, replay, retries, idempotency, compensation, cancellation, and recovery. |
| PLO-5 | Integrate and evaluate interoperability through MCP, A2A, observability conventions, and framework adapters. |
| PLO-6 | Threat-model and mitigate prompt injection, excessive agency, confused-deputy behavior, exfiltration, supply-chain, persistence, and isolation failures. |
| PLO-7 | Construct evaluation corpora and run repeated trials using appropriate code, model, human, trace, and end-state graders. |
| PLO-8 | Operate agent systems against reliability, latency, cost, capacity, privacy, incident-response, and change-control objectives. |
| PLO-9 | Communicate architecture, evidence, uncertainty, ethics, and tradeoffs to technical and non-technical audiences and work effectively in review teams. |
| PLO-10 | Independently learn, compare, port, audit, and extend unfamiliar agent products or frameworks from primary evidence. |

## Delivery Architecture

### Prerequisite Bridge

Diagnostic and repair modules establish the minimum foundations. Learners test out only with evidence.

### Semester 1: Harness Foundations

Learners build a minimal harness from a model test double through tools, context, state, policy, observability, and evaluation. The semester ends with a changed-requirement practical and oral defense.

### Semester 2: Production Agent Systems

Learners add orchestration, memory, durable execution, protocols, security, reliability, deployment, governance, and comparative framework/product analysis. The semester ends with a defended production capstone.

### Specialization

Tracks deepen platform/SRE, security/assurance, tools/protocols, core/framework, product/operator, or local-model infrastructure capability without replacing the common core.

## Canonical Build Progression

1. Deterministic model test double and contract tests.
2. Single-turn provider interface.
3. Bounded agent loop with explicit termination.
4. Typed tool registry with validation and structured errors.
5. Context assembly with provenance and token/cost budgets.
6. Session state, event log, checkpoints, and replay.
7. Policy, approval, execution isolation, and audit records.
8. Memory with retention, retrieval, deletion, and quality tests.
9. Traces, metrics, logs, and correlation.
10. Eval harness with tasks, repeated trials, graders, and regression gates.
11. Durable and multi-agent orchestration.
12. MCP/A2A adapters and cross-framework comparison.
13. Production deployment, operations, governance, and incident response.

## Required Graduate Evidence

- a tested reference-harness implementation
- a trace and end-state evidence bundle for representative tasks
- an evaluation corpus with repeated-trial results and documented variance
- a threat model plus exploit-and-mitigation demonstrations
- an incident exercise and recovery report
- an interoperability adapter or protocol exercise
- a comparative case-study analysis based on current primary sources
- a capstone deployed in a bounded environment
- an oral defense and delayed, unaided transfer task

## Claim Boundaries

The curriculum does not claim that:

- autonomous agents are preferable to deterministic software by default
- a framework supplies production safety, durability, or evaluation automatically
- sandboxing or approvals eliminate all risk
- benchmark success proves real-world reliability
- one successful trial proves a probabilistic system is correct
- one operator-oriented harness is safe hostile multi-tenant infrastructure
- institution-ready or enterprise-ready status can be established without external and real-user evidence

## Alignment

Program design is informed by ABET computing outcomes, ACM/IEEE-CS CS2023, SWEBOK v4, NIST AI RMF, NIST SSDF, OWASP agentic security guidance, and primary agent-system specifications and documentation. This is alignment evidence, not accreditation or endorsement.

See the [Competency Framework](competency-framework.md), [Assessment Map](assessment-map.md), and [Official Reading Map](sources/official-reading-map.md).
