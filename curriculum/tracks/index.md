# Specialization Tracks

## Purpose

Specializations deepen a role after the common harness core. They do not permit learners to skip implementation, security, evaluation, operations, communication, or transfer gates.

## Tracks

| Track | Deep competencies | Required specialization evidence |
| --- | --- | --- |
| Product / Operator | requirements, bounded configuration, workflow choice, human control, adoption, user evidence | evaluated workflow plus governance and operating guide |
| Platform / SRE | durability, deployment, observability, SLOs, capacity, incidents, recovery | failure-tested deployment and incident evidence |
| Security / Assurance | threat modeling, policy, isolation, identity, red team, privacy, assurance limits | exploit/mitigation portfolio and control-evidence map |
| Tools / Protocols | typed tools, MCP, A2A, schemas, compatibility, supply chain | tested extension or protocol adapter |
| Core / Framework | runtimes, orchestration, context/state engines, performance, contribution | traced and tested core change or independent runtime subsystem |
| Local-Model Infrastructure | serving, hardware, routing, quality, latency, cost, privacy, operations | measured serving/routing design with failure tests |

## Selection Gate

Before selecting a track, the learner must pass Semester 1 core competencies at L4 and state:

- target role and decisions they expect to own
- current evidence and gaps
- available environment, time, compute, budget, and privacy constraints
- selected track deliverable and transfer task

## Track Completion Gate

Every track requires:

- one implemented or operated artifact
- one failure-injection or adversarial exercise
- one measurement/evaluation report
- one security/privacy review
- one source/version baseline
- one peer or assessor review
- one oral defense
- one delayed changed-condition task

## Product Case Studies

OpenClaw, Hermes Agent, ChatGPT Work, xAI agent tooling, and other current systems may be selected as track contexts. The assessed capability remains portable. Product-specific commands, defaults, and advisories must be dated and cannot replace explanation of the underlying harness contract.

## Existing Track Files

The legacy track files are migration inputs and will be rewritten in place:

- [Operator](operator.md) -> Product / Operator
- [Production / DevOps](production-devops.md) -> Platform / SRE
- [Security / Hardening](security-hardening.md) -> Security / Assurance
- [Plugin Developer](plugin-developer.md) -> Tools / Protocols
- [Contributor / Core](contributor-core.md) -> Core / Framework
- [Local Models](local-models.md) -> Local-Model Infrastructure

Until each file is migrated and revalidated, this index is authoritative where wording conflicts.
