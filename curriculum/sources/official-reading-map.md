# Official Reading Map

## Use Policy

This map separates durable foundations from fast-moving implementations. Record retrieval date, version or commit where available, relevant claim, and residual uncertainty in substantial work.

- **S0:** official standard, specification, documentation, source, release, or advisory
- **S1:** peer-reviewed research, academic text, or government guidance
- **S2:** maintainer engineering explanation or reputable technical analysis
- **S3:** issue, forum, Reddit, community report, or practitioner anecdote; discovery signal only
- **S4:** unsourced summary or model output; lead only

Current behavior, APIs, releases, advisories, and product capabilities require current S0 evidence. Durable theory may use S1. Do not cite this map as proof; open and inspect the source.

## Program and Software-Engineering Alignment

- [ABET 2026-2027 Computing Criteria](https://www.abet.org/accreditation/accreditation-criteria/criteria-for-accrediting-computing-programs-2026-2027/) - student outcomes, curriculum, assessment, and continuous improvement; alignment only, not accreditation
- [ACM/IEEE-CS CS2023](https://csed.acm.org/final-report/) - computing knowledge areas and curricular guidance
- [SWEBOK v4](https://www.computer.org/education/bodies-of-knowledge/software-engineering) - software-engineering knowledge and professional practice
- [NIST Secure Software Development Framework, SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final) - secure lifecycle practices

## Agent-System Architecture

- [OpenAI: A Practical Guide to Building AI Agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/) - model/tools/instructions, loop, single versus multi-agent choice, manager and handoff patterns, guardrails, evaluation
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) - current SDK contracts, agents, tools, handoffs, guardrails, sessions, tracing
- [Anthropic: Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) - workflows versus agents, routing, parallelization, orchestrator-workers, evaluator-optimizer, simplest-system principle
- [Anthropic: Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) - context selection and management
- [Anthropic: Writing Tools for Agents](https://www.anthropic.com/engineering/writing-tools-for-agents) - tool interfaces and agent usability
- [Anthropic: Effective Harnesses for Long-Running Agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) - structured handoff and multi-context continuity
- [Anthropic: Harness Design for Long-Running Apps](https://www.anthropic.com/engineering/harness-design-long-running-apps) - planner/generator/evaluator roles, structured artifacts, simplification and ablation
- [Anthropic: Managed Agents](https://www.anthropic.com/engineering/managed-agents) - separation of model reasoning, execution capabilities, and session management

## Foundational Agent Research

- [ReAct](https://arxiv.org/abs/2210.03629) - interleaving reasoning and action; historical research, not a production architecture mandate
- [Toolformer](https://arxiv.org/abs/2302.04761) - learned tool-use research
- [Reflexion](https://arxiv.org/abs/2303.11366) - feedback/reflection research and limitations
- [MemGPT](https://arxiv.org/abs/2310.08560) - memory hierarchy research

Read papers for method, assumptions, evaluation, and limitations. Do not convert research prototypes into universal production recommendations.

## Learning, Assessment, and Transfer

- [How People Learn II](https://www.nationalacademies.org/publications/24783) - consensus synthesis on learning, prior knowledge, context/culture, motivation, self-regulation, and instructional environments
- [IES: Organizing Instruction and Study to Improve Student Learning](https://ies.ed.gov/ncee/wwc/PracticeGuide/1) - evidence-graded guidance for spacing, interleaving worked examples and problems, representations, quizzing/retrieval, and metacognitive judgment
- [Roediger and Karpicke: Test-Enhanced Learning](https://www.psychologicalscience.org/journals/psychological-science/j.1467-9280.2006.01693.x/) - delayed-retention evidence for retrieval practice in the studied prose-learning tasks
- [Cepeda et al.: Distributed Practice Meta-Analysis](https://digitalcommons.usf.edu/psy_facpub/1771/) - spacing evidence and interaction between study interval and desired retention interval
- [Freeman et al.: Active Learning in STEM](https://doi.org/10.1073/pnas.1319030111) - meta-analysis of undergraduate STEM courses; relevant evidence, not proof that every activity labeled active is effective
- [Chi and Wylie: ICAP](https://icap.education.asu.edu/research) - framework and evidence for distinguishing passive, active, constructive, and interactive engagement
- [Barnett and Ceci: Taxonomy for Far Transfer](https://doi.org/10.1037/0033-2909.128.4.612) - transfer dimensions and why changed-task evidence must state what changed rather than use an unqualified near/far label
- [Macnamara et al.: Deliberate Practice Meta-Analysis](https://www.psychologicalscience.org/journals/psychological-science/0956797614535810/) - deliberate practice matters but does not explain all performance variance and varies materially by domain
- [AERA/APA/NCME Standards for Educational and Psychological Testing](https://ncme.org/resources/books/testing-standards/) - validity, reliability/error, fairness, test design, administration, scoring, and use; current revision activity must be monitored

These sources justify design hypotheses, not effectiveness claims for this program. The curriculum still requires local pilot data, transfer evidence, assessor agreement, accessibility review, and adverse-impact analysis.

## Framework and Adapter Studies

- [Google Agent Development Kit](https://adk.dev/agents/) and [source](https://github.com/google/adk-python) - agents, workflows, tools, sessions, artifacts, evaluation, deployment
- [Google ADK Plugins](https://adk.dev/plugins/) - cross-cutting policies and lifecycle behavior
- [Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/) - agents, workflows, persistence, hosting, and migration context
- [Microsoft Agent Resources](https://microsoft.github.io/agent-resources/develop-agents/) - development and harness examples
- [LangGraph Overview](https://docs.langchain.com/oss/python/langgraph/overview) - graph runtime and durable execution
- [LangGraph Persistence](https://docs.langchain.com/oss/python/langgraph/persistence) - checkpoints and state
- [LangGraph Human-in-the-Loop](https://docs.langchain.com/oss/python/langchain/human-in-the-loop) - interrupts and approval patterns
- [PydanticAI Durable Execution](https://ai.pydantic.dev/durable_execution/overview/) - integration with durable workflow systems

Framework documentation is an adapter study. Learners must compare semantics against the curriculum's stable contracts and verify current versions.

## Protocols and Observability

- [Model Context Protocol Architecture, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/architecture) - host/client/server architecture, stateless requests, per-request capabilities, and `server/discover`
- [MCP Base Protocol, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic) - JSON-RPC messages, statelessness, version metadata, schema rules, authorization boundary, and trace-context propagation
- [MCP Python SDK v2.0.0](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.0.0) - exact SDK used by the bounded reference proof; its in-process client/server path is a contract fixture, not network deployment evidence
- [MCP TypeScript SDK Protocol Eras](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/protocol-versions.md) - implementation-facing differences between initialization-era revisions and the modern `2026-07-28` revision; pin SDK behavior as well as specification text
- [MCP 2026 Roadmap](https://blog.modelcontextprotocol.io/posts/2026-07-28/) - historical planning evidence; distinguish proposals from behavior now present in the normative specification
- [Agent2Agent Protocol Specification, latest released version 1.0.0](https://a2a-protocol.org/latest/specification/) - AgentCard, message, task, artifact, parts, streaming, asynchronous work, bindings, versioning, and authentication
- [A2A Python SDK v1.1.2](https://github.com/a2aproject/a2a-python/releases/tag/v1.1.2) - exact SDK used by the bounded JSON-RPC/ASGI proof; SDK release and protocol release are separate pins
- [A2A Project](https://a2a-protocol.org/) - current ecosystem and specification entry point
- [OpenTelemetry Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/) - shared trace, metric, and log semantics
- [OpenTelemetry GenAI Semantic Conventions](https://github.com/open-telemetry/semantic-conventions-genai) - dedicated current source for GenAI, agent, MCP, and provider conventions after migration from the core repository
- [Pinned OpenTelemetry GenAI source snapshot](https://github.com/open-telemetry/semantic-conventions-genai/tree/a685613a207a580163353b8e48a7ad88967e7b42) - development-status source used by the reference span proof; source pinning does not convert development conventions into a stable standard
- [OpenTelemetry Concepts: Semantic Conventions](https://opentelemetry.io/docs/concepts/semantic-conventions/) - stability and versioning guidance

Pin protocol and semantic-convention versions in labs. Compatibility claims require contract tests, not only manifest discovery.

## Security, Safety, Privacy, and Governance

- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) - Govern, Map, Measure, and Manage functions
- [NIST Generative AI Profile, AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) - generative-AI risk actions and considerations
- [OWASP Agentic AI Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) - agentic threat categories and mitigations
- [OWASP AI Agent Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html) - practical architecture and control guidance
- [Anthropic: Claude Code Sandboxing](https://www.anthropic.com/engineering/claude-code-sandboxing) - filesystem/network isolation approach and boundaries

High-stakes, privacy, regulatory, and security claims need jurisdiction- and context-specific primary evidence. Framework guardrails, prompts, and approvals are controls, not proof of safety.

## Evaluation and Benchmarking

- [Anthropic: Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) - task, trial, grader, transcript, outcome, eval harness, capability versus regression suites
- [AgentBench](https://arxiv.org/abs/2308.03688) - multi-environment agent benchmark and limitations
- [tau-bench](https://arxiv.org/abs/2406.12045) - tool-agent-user interaction benchmark
- [OSWorld](https://arxiv.org/abs/2404.07972) - computer-use environment and evaluation
- [METR Task Completion Time Horizons](https://metr.org/time-horizons/) - capability measurement over task duration; inspect current methodology and caveats

Benchmarks are evidence about a defined setup, not universal production readiness. Course evaluations require local realistic tasks, repeated trials, trace inspection, and end-state verification.

## Product Case Studies

### OpenClaw

- [OpenClaw source](https://github.com/openclaw/openclaw)
- [OpenClaw documentation](https://docs.openclaw.ai/)
- [OpenClaw releases](https://github.com/openclaw/openclaw/releases)
- [OpenClaw security advisories](https://github.com/openclaw/openclaw/security/advisories)

The machine-readable baseline remains in `../maintenance/upstream-state.json`; human review history remains in `../maintenance/review-log.md`.

### Hermes Agent

- [NousResearch Hermes Agent source](https://github.com/NousResearch/hermes-agent)
- [Hermes Agent security policy](https://github.com/NousResearch/hermes-agent/security)

Use as a source-visible case in skills, memory, tools, provider adapters, gateways, plugins, and single-tenant trust assumptions.

### ChatGPT Work

- [ChatGPT Work and Codex Help](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex)
- [ChatGPT Work](https://openai.com/chatgpt-work/)
- [ChatGPT for ambitious work](https://openai.com/index/chatgpt-for-your-most-ambitious-work/)

Use only official observed/documented capabilities as a product case. Do not infer internal architecture from product behavior.

### xAI Agent Tooling

- [Grok Voice Agent Builder](https://x.ai/news/grok-voice-agent-builder)
- [Grok 4.1 Fast and Agent Tools API](https://x.ai/news/grok-4-1-fast)
- [xAI Workflows](https://x.ai/news/workflows)
- [xAI Skills, Plugins, and Marketplaces](https://docs.x.ai/build/features/skills-plugins-marketplaces)

Use official Grok Build, Agent Tools, workflow, skill, and plugin materials. Treat community claims about a separate “Grok Bot” as unverified unless an official source is found.

## Retrieval Baseline

This map was restructured on 2026-08-15 and its executable protocol pins were checked again on 2026-08-16. The bounded proof uses MCP Python SDK `2.0.0`, A2A Python SDK `1.1.2` against protocol `1.0`, and OpenTelemetry SDK `1.44.0` against a commit-pinned development GenAI schema. Fast-moving sources must be re-opened before teaching or assessment; stable URLs do not guarantee stable content.
