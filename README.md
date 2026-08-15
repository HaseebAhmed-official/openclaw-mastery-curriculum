# Agent Harness Systems Engineering Curriculum

An evidence-driven, platform-agnostic curriculum for learning how to design, build, test, secure, operate, and evolve production agent systems.

The program teaches the engineering discipline behind systems such as OpenClaw, Hermes Agent, ChatGPT Work, xAI agent tooling, and future agent products. It does not make any vendor, framework, or current product the curriculum spine.

**Status:** architecture migration in progress. The former OpenClaw-focused curriculum provides substantial labs, assessment, security, and maintenance infrastructure, but the expanded program is not yet institution-ready or enterprise-proven. See [Project State](PROJECT_STATE.md) for evidence and remaining gates.

## Graduate Capability

A successful graduate can:

- explain the difference between deterministic workflows, agents, harnesses, models, tools, and execution environments
- implement a bounded agent loop rather than only configuring a framework
- design provider adapters, typed tools, context assembly, policy, sessions, memory, and event logs
- implement checkpointing, recovery, human approval, and durable execution
- integrate MCP, A2A, and observability standards without confusing protocol support with system correctness
- threat-model prompt injection, tool abuse, confused-deputy failures, exfiltration, persistence, and supply-chain risk
- build evaluation corpora, run repeated trials, inspect traces and end state, and enforce regression gates
- operate systems with explicit SLOs, incident response, cost, latency, privacy, and governance boundaries
- compare products and frameworks using evidence rather than marketing claims
- defend design decisions orally and transfer skills to a changed task without agent step-by-step help

## Program Structure

The curriculum uses four layers:

1. **Foundations:** programming, systems, networking, data, software engineering, security, statistics, LLMs, and human factors.
2. **Harness contracts:** agent loop, providers, context, typed tools, policy, execution, sessions, memory, orchestration, observability, evaluation, and governance.
3. **Standards and adapters:** MCP, A2A, OpenTelemetry, durable execution, and selected framework adapters.
4. **Versioned case studies:** OpenClaw, Hermes Agent, ChatGPT Work, xAI agent tooling, and future systems.

[Semester 1](curriculum/semester-1/index.md) builds a minimal harness from first principles. [Semester 2](curriculum/semester-2/index.md) hardens it into a production agent system and tests interoperability, security, reliability, and governance.

## Start Here

### Learners

1. Read the [Program Overview](curriculum/program-overview.md).
2. Pass the [Prerequisite Bridge](curriculum/prerequisite-bridge.md), using repair modules only where needed.
3. Track evidence against the [Competency Framework](curriculum/competency-framework.md).
4. Complete Semester 1 in order; do not skip the minimal-harness practical.
5. Complete Semester 2 and one specialization track.
6. Defend a capstone that builds, attacks, evaluates, operates, and ports a working harness.

### Instructors

1. Map local course requirements to the [program outcomes](curriculum/program-overview.md#program-learning-outcomes).
2. Use the [Assessment Map](curriculum/assessment-map.md) for constructive alignment.
3. Select reproducible labs from the [Lab Catalog](curriculum/labs/lab-catalog.md).
4. Calibrate graders with the [Assessment Assets](curriculum/assessment/index.md) and [Rubrics](curriculum/rubrics/index.md).
5. Record delivery evidence and improvement decisions through the [Maintenance System](curriculum/maintenance/index.md).

### Engineering Organizations

Use the same core outcomes, then emphasize the Platform/SRE, Security/Assurance, or Tools/Protocols track. Replace academic grades with verified capability gates, incident simulations, architecture review, and production-readiness evidence.

## Canonical Documents

- [Program Overview](curriculum/program-overview.md)
- [Prerequisite Bridge](curriculum/prerequisite-bridge.md)
- [Competency Framework](curriculum/competency-framework.md)
- [Assessment Map](curriculum/assessment-map.md)
- [Semester 1](curriculum/semester-1/index.md)
- [Semester 2](curriculum/semester-2/index.md)
- [Lab Catalog](curriculum/labs/lab-catalog.md)
- [Executable Reference Harness](reference-harness/README.md)
- [Tracks](curriculum/tracks/index.md)
- [Versioned Case Studies](curriculum/case-studies.md)
- [Official Reading Map](curriculum/sources/official-reading-map.md)
- [Validation Register](curriculum/sources/validation-register.md)
- [Project State](PROJECT_STATE.md)

## Evidence Standard

Every major milestone must join theory, implementation, testing, failure analysis, security implications, and inspectable evidence. A polished artifact or same-session explanation is not mastery. Higher-level claims require delayed, unaided, changed-task transfer plus oral defense.

Current product, framework, release, API, security, and standards claims require dated primary sources. Community sources are useful for discovering risks but are not authoritative until verified.

## Product Boundary

Elite Mentor OS is a separate optional mentoring product at [HaseebAhmed-official/elite-mentor-os](https://github.com/HaseebAhmed-official/elite-mentor-os). This curriculum must remain teachable without it. No Mentor OS runtime or product development belongs in this repository after separation is complete.

## License

MIT. See [LICENSE](LICENSE).
