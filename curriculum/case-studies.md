# Versioned Agent-System Case Studies

## Purpose

Use current systems to test whether learners can apply stable harness contracts to unfamiliar implementations. Case studies are dated evidence, not product endorsements, architecture truth, or claims about private internals.

Baseline review date: **2026-08-15**. Re-open every primary source before delivery.

## Case Method

For each system, build a claim table with:

- claim and exact scope
- `observed`, `documented`, `source-visible`, `inferred`, `unknown`, or `retired`
- source, version/date, and retrieval date
- stable harness contract affected
- security/operations implication
- contradiction or missing evidence
- revalidation trigger

Then answer:

1. What problem and user/organization boundary does the system target?
2. Where are model, harness, execution, state, operator, and external-system boundaries?
3. What tools/capabilities exist, and how are discovery, validation, policy, approval, and execution separated?
4. How are context, sessions, memory, artifacts, and long-running work represented?
5. What is observable, recoverable, testable, and governable?
6. What trust/tenancy assumptions limit claims?
7. Which behavior is stable architecture versus current product choice?
8. Which evidence remains unknown because the implementation is managed or private?

## Comparative Lens

| Contract | Questions |
| --- | --- |
| Agent loop | Who chooses the next action, and what bounds termination, budget, cancellation, or no progress? |
| Provider/model | Is the model/provider replaceable, routed, or hidden? What can actually be verified? |
| Context | How are instructions, local/project evidence, retrieved data, and budgets assembled? |
| Tools/execution | What capabilities exist, where do they execute, and what validates/contains them? |
| Policy/approval | Who authorizes which exact effects, and how is requester provenance preserved? |
| Sessions/state | What survives turns, processes, devices, schedules, or context resets? |
| Memory | What is retained/retrieved/deleted, with what isolation and provenance? |
| Orchestration | Which deterministic, single-agent, delegated, parallel, or evaluator patterns appear? |
| Protocols/integrations | Which interfaces are public, standardized, proprietary, or inferred? |
| Observability/evaluation | What traces, artifacts, task evidence, and evaluation claims are available? |
| Deployment/governance | What operator, tenant, admin, security, privacy, update, and support boundaries exist? |

## OpenClaw

### Why Include It

OpenClaw is a source-visible harness/platform case with extensive tools, channels, sessions, memory, automation, plugins/skills, nodes, coding-agent integration, and security advisories. It is useful for code tracing, operator authority, detached work, extension, release drift, and recurring vulnerability-family analysis.

### Primary Evidence

- [source](https://github.com/openclaw/openclaw)
- [documentation](https://docs.openclaw.ai/)
- [releases](https://github.com/openclaw/openclaw/releases)
- [security advisories](https://github.com/openclaw/openclaw/security/advisories)
- local release baseline: [upstream-state.json](maintenance/upstream-state.json)
- local review history: [review-log.md](maintenance/review-log.md)

### Required Boundaries

- Treat release, command, default, channel, plugin, and advisory facts as dated.
- Preserve the documented trusted-operator/single-gateway boundary; do not infer hostile multi-tenant isolation.
- Separate source-visible behavior from configuration-dependent or unexecuted claims.
- Use advisories as recurring failure-family evidence, not as a vulnerability-count contest.

### Suggested Exercise

Map one OpenClaw path from ingress through session/context, model, tool policy/approval, execution, events/artifacts, and response. Then select one advisory family, reproduce only in an authorized safe fixture or reason from source/advisory, map it to a stable harness control, and design a regression test.

## Hermes Agent

### Why Include It

Hermes Agent is a source-visible case for provider flexibility, tools, skills, memory/self-improvement loops, gateways/plugins, and explicit deployment/security assumptions.

### Primary Evidence

- [NousResearch Hermes Agent source](https://github.com/NousResearch/hermes-agent)
- [security policy](https://github.com/NousResearch/hermes-agent/security)

### Required Boundaries

- Verify current features and architecture from source/docs at the selected commit.
- Distinguish whole-process/environment containment from per-command terminal sandboxing.
- Treat single-user/trusted-operator assumptions as deployment constraints.
- Audit how learned skills or memory can improve behavior and create persistence/supply-chain risk.

### Suggested Exercise

Trace one tool or skill/memory lifecycle from source, compare it to the reference-harness contracts, and design tests for provenance, contamination, authority, rollback, and provider portability.

## ChatGPT Work

### Why Include It

ChatGPT Work is a managed-product case for long multi-step work, artifact production, apps/files, cloud/local work surfaces, schedules, approvals, and organizational administration. It teaches how to evaluate public behavior without inventing internal architecture.

### Primary Evidence

- [ChatGPT Work and Codex Help](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex)
- [ChatGPT Work](https://openai.com/chatgpt-work/)
- [ChatGPT for ambitious work](https://openai.com/index/chatgpt-for-your-most-ambitious-work/)

### Required Boundaries

- Product pages and observed UI support capability claims, not private implementation claims.
- Account tier, rollout, region, admin setting, and product updates can change availability.
- Separate user-visible approval/control from unknown internal policy and execution design.

### Suggested Exercise

Run or analyze one authorized multi-step task, collect visible state/artifacts/approvals, map documented and observed capabilities to stable contracts, list unknown internals, and compare the evidence available to a source-visible system.

## xAI Agent Tooling

### Why Include It

xAI's official agent tools, workflows, voice builder, skills/plugins, hooks, and marketplace materials provide a current managed/platform case for hosted tools, parallel work, multimodal agents, and extension surfaces.

### Primary Evidence

- [Grok Voice Agent Builder](https://x.ai/news/grok-voice-agent-builder)
- [Grok 4.1 Fast and Agent Tools API](https://x.ai/news/grok-4-1-fast)
- [xAI Workflows](https://x.ai/news/workflows)
- [Skills, Plugins, and Marketplaces](https://docs.x.ai/build/features/skills-plugins-marketplaces)

### Required Boundaries

- Verify current naming, availability, APIs, and account requirements before use.
- Treat official Grok Build/workflows/agent tooling as the sourced case.
- Do not teach community “Grok Bot” claims as fact without an official source.
- Separate extension packaging from runtime authority and security proof.

### Suggested Exercise

Map one official workflow or extension path to tools, policy/guardrails, MCP/integration, observability, and deployment contracts. Design a portability test against a source-visible or local harness.

## Comparative Assessment

Learners must compare at least two systems, including one source-visible case where feasible. Strong work:

- uses dated primary evidence
- distinguishes public behavior, source implementation, inference, and unknowns
- maps to stable contracts rather than feature lists
- identifies trust, security, operations, and update boundaries
- proposes executable comparison or portability tests
- revises claims when evidence conflicts

Weak work copies marketing, assumes similar names mean equivalent semantics, or awards readiness from feature count.
