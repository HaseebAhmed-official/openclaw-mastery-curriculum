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
- pinned release: [`v2026.8.13`](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.8.13)
- pinned [security policy](https://github.com/NousResearch/hermes-agent/blob/v2026.8.13/SECURITY.md)
- pinned feature docs: [tools](https://github.com/NousResearch/hermes-agent/blob/v2026.8.13/website/docs/user-guide/features/tools.md), [skills](https://github.com/NousResearch/hermes-agent/blob/v2026.8.13/website/docs/user-guide/features/skills.md), and [plugins](https://github.com/NousResearch/hermes-agent/blob/v2026.8.13/website/docs/user-guide/features/plugins.md)

### Claim Ledger

Reviewed **2026-08-15** against release `v2026.8.13`. `Source-visible` means the claim is present in pinned repository material; it does not mean this curriculum independently reproduced it.

| Claim | Status | Evidence | Stable contract | Boundary and revalidation trigger |
| --- | --- | --- | --- | --- |
| Hermes declares a single-tenant personal-agent posture rather than hostile multi-tenant isolation. | `source-visible` | pinned `SECURITY.md` | deployment/governance | Treat operator and co-user trust as part of the security boundary; recheck when the security model changes. |
| The default terminal backend executes on the host; documented alternatives include container, remote, and cloud backends. | `source-visible` | pinned tools docs and `SECURITY.md` | tools/execution | A terminal backend does not automatically isolate file tools, plugins, hooks, skills, or every subprocess; recheck backend semantics per release. |
| The built-in tool registry covers terminal/files, browser/search, memory/session search, delegation, scheduled tasks, and MCP integrations, with toolsets configurable by platform. | `source-visible` | pinned tools docs | tools/execution, orchestration, protocols | Presence is not proof of least privilege, reliability, or equivalent behavior across backends. |
| Skills use progressive disclosure and share `~/.hermes/skills/` as the stated source of truth; the agent can modify or delete them. | `source-visible` | pinned skills docs | context, memory, extension | Agent-writable expertise creates provenance, persistence, rollback, and supply-chain questions; recheck write-approval and update rules. |
| Plugins can register tools, hooks, commands, skills, context/memory/model providers, and MCP calls; project-local plugins are disabled by default. | `source-visible` | pinned plugins docs | extension, policy, integrations | Enabled plugins run in the agent process and therefore require operator trust; recheck discovery and trust defaults. |
| Effective containment of every execution and extension path under a chosen backend is not established by these documents. | `unknown` | pinned `SECURITY.md` | execution, security | Require path-by-path tests for shell, file, code execution, MCP, skills, plugins, hooks, credentials, and delegated work. |

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

### Claim Ledger

Reviewed **2026-08-15**. These are public product-contract claims, not observations of a specific account or evidence about OpenAI's private implementation.

| Claim | Status | Evidence | Stable contract | Boundary and revalidation trigger |
| --- | --- | --- | --- | --- |
| Work is presented as an agent for longer multi-step work and finished documents, spreadsheets, presentations, reports, and Sites. | `documented` | Help Center and product page, retrieved 2026-08-15 | agent loop, artifacts | Availability and supported artifact types can change; recheck before delivery. |
| Work can use project context and, where permitted in the desktop app, local folders, files, and desktop apps. | `documented` | Help Center, retrieved 2026-08-15 | context, tools/execution | Permission, plan, workspace, OS, and rollout boundaries apply; do not infer unrestricted host access. |
| Cloud Work chats synchronize across supported surfaces, while local chats and local files stay on the computer unless explicitly moved or shared. | `documented` | Help Center, retrieved 2026-08-15 | sessions/state, deployment | This is a user-visible data-location boundary, not a complete retention, backup, or privacy architecture. |
| Scheduled Tasks can run once, on a schedule or trigger, or monitor for changes; users can review progress, steer work, and approve important actions. | `documented` | Help Center and launch page, retrieved 2026-08-15 | durable work, policy/approval | Exact trigger, retry, approval, and failure semantics are not established by these pages. |
| Workspace owners and admins can control Work access and related browser/network settings through roles; starting defaults do not themselves grant model access. | `documented` | Help Center, retrieved 2026-08-15 | governance | Controls differ by eligible plan and workspace; revalidate role and product documentation. |
| Internal planning loops, policy enforcement, tool isolation, checkpoint format, model routing, and durability guarantees are not public in the cited material. | `unknown` | absence from cited public contract | loop, policy, execution, state | Do not fill these gaps from UI similarity or marketing; require a public specification or authorized observation. |

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
- [Grok Build](https://x.ai/news/grok-build-cli)
- [xAI Workflows](https://x.ai/news/workflows)
- [Skills, Plugins, and Marketplaces](https://docs.x.ai/build/features/skills-plugins-marketplaces)

### Claim Ledger

Reviewed **2026-08-15**. Dated news posts and documentation describe public behavior; none of these claims establishes xAI's private runtime architecture or independent reliability.

| Claim | Status | Evidence | Stable contract | Boundary and revalidation trigger |
| --- | --- | --- | --- | --- |
| The Agent Tools API exposes hosted web/X search, uploaded-file retrieval, code execution, and remote MCP tools. | `documented` | Agent Tools announcement, retrieved 2026-08-15 | tools/execution, protocols | Hosted execution reduces operator-managed components but does not by itself establish tenant isolation, policy, or reliability. Recheck API docs and model support. |
| Grok Build plan mode exposes a plan for review and approval, then presents changes as diffs. | `documented` | Grok Build announcement, 2026-05-25 | policy/approval, artifacts | This is a visible interaction contract, not proof that every effect is covered by the same approval boundary. |
| Grok Build documents parallel subagents and workflows with phased fan-out, verification, saved progress, pause/resume, budgets, and reusable workflow files. | `documented` | Workflows announcement, 2026-07-23 | orchestration, durable work | Limits and semantics are release-sensitive; independently test failure, cancellation, duplication, and resume behavior before operational claims. |
| Skills are reusable folders discovered from project, user, plugin, and configured paths; plugins can add skills, agents, hooks, MCP, and LSP servers. | `documented` | build docs, updated 2026-08-11 | context, extension, integrations | Discovery compatibility is not a security proof; audit precedence, trust, install, update, and execution authority. |
| Voice Agent Builder documents telephony, retrieval, tools, guardrails, MCP, observability, human transfer, and recorded/transcribed tool-use review. | `documented` | Voice Agent Builder announcement, 2026-07-01 | tools, policy, observability, deployment | Product claims require authorized scenario testing; recording, consent, retention, and regional obligations need separate review. |
| Runtime isolation, tenancy internals, checkpoint representation, hook containment, and end-to-end approval coverage are not established by the cited public pages. | `unknown` | absence from cited public contract | execution, state, governance | Keep unknown until source, specification, contractual evidence, or authorized tests support a narrower claim. |

### Required Boundaries

- Verify current naming, availability, APIs, and account requirements before use.
- Treat official Grok Build/workflows/agent tooling as the sourced case.
- Do not teach Grok Bot or community claims as fact without a current official source and a bounded evidence record.
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
