# Semester 2: Production Agent Systems

## Goal

Transform the minimal harness into a secure, observable, durable, interoperable, and governable agent system. Learners must prove production judgment under failures and changing requirements rather than merely adding autonomy or framework features.

## Exit Capability

The learner can choose an orchestration pattern, implement durable state transitions, integrate protocols, attack and harden authority boundaries, construct meaningful evaluations, operate against explicit objectives, compare current products/frameworks, and defend a deployed capstone.

## Weekly Sequence

| Week | Theme | Build/evidence | Assessment |
| --- | --- | --- | --- |
| 1 | Production requirements and architecture | SLOs, threat model, data classification, failure domains, cost and ownership | Architecture review |
| 2 | Orchestration patterns | Routing, parallelization, manager, handoff, evaluator-optimizer; simplest-valid choice | Pattern selection practical |
| 3 | Durable execution | Idempotency, retry policy, checkpoints, compensation, cancellation, crash recovery | Failure-injection lab |
| 4 | Memory systems | Retrieval pipeline, isolation, freshness, contamination, deletion, quality metrics | Memory adversarial evaluation |
| 5 | MCP interoperability | Capability negotiation, tools/resources/prompts, transport/auth boundaries, client/server tests | MCP adapter practical |
| 6 | A2A interoperability | AgentCard, message, task, artifact, streaming, async and auth boundaries | Cross-agent task practical |
| 7 | Agentic threat modeling | Injection, confused deputy, exfiltration, excessive agency, supply chain, persistence | Red-team plan and exploit |
| 8 | Defense in depth | Policy, approvals, sandbox, network egress, secrets, identity, audit, recovery | Midterm attack-and-repair exam |
| 9 | Evaluation engineering | Corpus design, repeated trials, graders, disagreement, leakage, capability/regression gates | Evaluation review |
| 10 | Reliability and observability | SLOs, traces, metrics, logs, queues, backpressure, capacity, latency, cost | Incident simulation |
| 11 | Deployment and tenancy | Packaging, secrets, migrations, isolation, single- versus multi-tenant claims, rollback | Deployment defense |
| 12 | Governance, privacy, and accessibility | AI risk management, secure development, data lifecycle, review roles, user controls | Control-evidence mapping |
| 13 | Framework adapters | Implement the same contract with at least two frameworks or SDKs; document semantic gaps | Portability test |
| 14 | Versioned product case studies | Audit OpenClaw, Hermes Agent, ChatGPT Work, xAI agent tooling, or approved alternatives | Evidence-backed comparison |
| 15 | Capstone operation and red team | Deploy, run trials, attack, repair, measure, and prepare rollback | Release-candidate gate |
| 16 | Final defense and changed task | Defend architecture/evidence, then adapt under a withheld constraint | Capstone board and delayed retest |

## Required Labs

- LAB-C1 orchestration pattern comparison
- LAB-C2 durable crash/retry/recovery
- LAB-C3 memory contamination and deletion
- LAB-C4 MCP integration and contract test
- LAB-C5 A2A task and artifact exchange
- LAB-C6 agentic attack-and-mitigation lab
- LAB-C7 evaluation corpus and regression gate
- LAB-C8 observability/SLO incident simulation
- LAB-C9 deployment, tenancy, and rollback review
- LAB-D1 cross-framework portability
- LAB-D2 versioned product case study

## Capstone Release Gates

The capstone must:

- solve a justified problem where agentic behavior adds value
- expose a clear provider/model boundary and deterministic test path
- use typed, least-authority tools and explicit stop conditions
- persist auditable state and recover from injected failure
- enforce policy and human approval for material effects
- produce correlated traces and inspectable end-state artifacts
- pass a repeated-trial evaluation suite with declared thresholds
- survive an authorized red-team exercise and mitigation retest
- document SLO, cost, privacy, deployment, rollback, and residual risk
- port one meaningful capability across two frameworks, protocols, or provider environments
- pass oral defense and delayed changed-task transfer

## Teaching Support

- [Semester 2 Teaching Guide](teaching-guide.md)
- [Advanced Lab Guides](../labs/advanced-lab-guides.md)
- [Specialization Lab Guides](../labs/specialization-lab-guides.md)
- [Assessment Map](../assessment-map.md)
- [Oral Defense Bank](../assessment/oral-defense-bank.md)
