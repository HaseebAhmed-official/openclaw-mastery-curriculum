# Agent Harness Systems Engineering Curriculum - Project State

## Purpose

This is the canonical long-form source of truth for continuing the curriculum after context reset, compaction, or agent handoff. Read it before changing scope or claiming progress. Use `.mentor/MENTOR_STATE.md` for the compact operational checkpoint.

## Vision

Create a platform-agnostic, evidence-driven Agent Harness / Agent Systems Engineering curriculum that can be presented to universities, used by independent learners, and adapted by engineering organizations. A graduate must be able to reason about, build, test, secure, operate, and evolve systems in the class of OpenClaw, Hermes Agent, ChatGPT Work, xAI agent tooling, and future agent products.

This is not a vendor tutorial, a reading list, or a collection of generated documents. The final program must join:

- computer science and software-engineering prerequisites
- agent-loop and harness architecture from first principles
- typed tools, context, memory, sessions, policy, and execution
- durable workflows, multi-agent patterns, MCP, and A2A
- security, safety, privacy, governance, and human approval
- observability, evaluation, reliability, cost, and operations
- implementation labs with executable evidence
- calibrated assessments, oral defense, transfer, and capstones
- current product case studies without making any product the curriculum spine
- source provenance and a maintainable change-control system

The quality target is defensible university and enterprise adoption, not a literal claim of perfection. Maturity claims require observed evidence, not file count, static scores, or self-review.

## Two-Product Boundary

There are exactly two separately versioned products:

1. **Agent Harness Systems Engineering Curriculum**: this repository. It owns the academic program, labs, assessments, reference harness, case studies, sources, and course maintenance.
2. **Elite Mentor OS**: a subject-agnostic Claude Code and Codex mentor plugin in sibling repository `../elite-mentor-os`. It owns generic diagnosis, mentoring, roadmap, review, learning-state, and validation behavior.

Rules:

- The curriculum may integrate with Mentor OS, but must remain teachable without it.
- Mentor OS must not own OpenClaw or any other subject-specific content.
- Product releases, issue tracking, evidence, and roadmaps must remain separate.
- The legacy embedded Mentor OS plugin and marketplace files were removed after the standalone repository was validated and published. The curriculum links to the separate product but does not own its runtime.
- Do not create a third product or duplicate the complete curriculum across old and new trees.

## Current Repositories

Curriculum:

- local: `C:\Users\Administrator\Documents\Codex\2026-04-22-openclaw-search-deeply-on-internet-github\openclaw-mastery`
- branch: `main`
- remote: `https://github.com/HaseebAhmed-official/agent-harness-systems-engineering-curriculum.git`
- latest pushed curriculum migration milestones entering this work: `ed3c956` and `c136a86`; use Git rather than this file for the current head

Paused external product:

- local: `C:\Users\Administrator\Documents\Codex\2026-04-22-openclaw-search-deeply-on-internet-github\elite-mentor-os`
- remote: `https://github.com/HaseebAhmed-official/elite-mentor-os`
- status: separate and frozen by user decision on 2026-08-15; do not inspect, modify, validate, release, or include it in curriculum progress until explicitly resumed

User study environment:

- Windows path: `E:\Study\Openclaw mastery`
- WSL path: `/mnt/e/Study/Openclaw mastery`
- OpenClaw is already installed in the user's WSL Ubuntu environment. Do not divert curriculum work into Windows-side installation checks unless explicitly requested.

## Current Baseline

The platform-agnostic architecture and support-asset migration are pushed through `c136a86`. The current tree has 68 curriculum files; 15 reference OpenClaw only in intentional case-study, source, maintenance, comparative, or historical contexts. The embedded Mentor plugin and empty screenshot/manual layer are gone.

The reference harness now covers the minimal runtime plus bounded Semester 2 starting fixtures for memory, orchestration, protocol/telemetry ports, per-attempt events, persistence, and policy-based evaluation. These fixtures support learning; they do not replace actual protocol implementations, clean lab reproduction, or production infrastructure.

### Honest Progress Snapshot

| Scope | Evidence-based completion | Interpretation |
| --- | ---: | --- |
| Platform-agnostic curriculum artifact implementation | about 74% | Canonical/support migration and bounded advanced fixtures exist; real protocol/provider examples, deeper case ledgers, lab reproduction records, and final audit remain. |
| Hands-on reproducibility evidence | about 25% | Reference tests pass, but authored labs have not been independently reproduced and calibrated in clean learner environments. |
| Expanded curriculum institution/enterprise proof | about 30% | Alignment and delivery contracts are strong, but no real cohort, measured assessor reliability, full lab reproduction, accessibility audit, or independent adoption evidence exists. |

Percentages are planning estimates, not quality claims. The gate ledger below is authoritative.

## Preserved Strengths

- two-semester instructional structure
- prerequisite bridge and competency framework
- labs, rubrics, practical exams, oral defenses, calibration, and feedback assets
- production, security, operations, extension, and contributor tracks
- release-aware maintenance and source-validation mechanisms
- OpenClaw security/advisory baseline through the August 2026 review
- historical Codex and Claude validation reports

These assets should be migrated and improved, not discarded merely to make the repository look new.

## Material Gaps

### Curriculum Architecture

- The platform-agnostic spine, stable/adapters/case layers, build progression, portability, and alignment matrix are implemented.
- Remaining risk is consistency in less-central historical/maintenance artifacts and absence of independent curriculum architecture review after migration.

### Technical Depth

- The executable reference harness proves deterministic provider behavior, bounded loop, typed tools, exact approval, context budgeting, per-attempt event identity, session/event persistence, bounded memory/orchestration, checked adapter ports, event export, and policy-based repeated-trial evaluation. It still lacks real process isolation, full JSON Schema, distributed durability, actual MCP/A2A implementations, OpenTelemetry export, and production provider adapters.
- MCP and A2A are taught as independent interoperability contracts, but their labs still lack pinned executable reference implementations and reproduction evidence.
- Durable workflow engines, checkpoint/replay semantics, idempotency, cancellation, and recovery need first-class treatment.
- Evaluation fixtures now implement repeated trials, per-task thresholds, critical gates, and retained runs, but the curriculum still lacks a maintained representative corpus, validated graders, uncertainty analysis, leakage checks, cost, and latency evidence.
- Threat modeling needs platform-independent agentic attack labs and measurable mitigations.

### Delivery Evidence

- Many labs are authored guidance rather than executed, frozen proof bundles.
- No real cohort timing or completion data exists.
- No inter-rater reliability evidence exists for assessors.
- No delayed, unaided, changed-task transfer study exists.
- Accessibility, localization, and learning-analytics evidence are incomplete.
- Presentation outlines are not a substitute for complete lecture delivery materials.

### Validation

- Historical reviews predate the expanded vision.
- Independent reviewers have not evaluated the migrated curriculum.
- Product claims have not passed legal/licensing, privacy, accessibility, or enterprise adoption review.
- No pilot institution or enterprise has supplied adoption evidence.

## Target Curriculum Architecture

Teach four layers explicitly:

1. **Stable foundations**: programming, operating systems, networking, distributed systems, databases, software engineering, security, statistics, LLM fundamentals, and human factors.
2. **Harness contracts**: agent loop, model/provider adapter, context assembly, typed tools, policy/approval, execution environments, sessions/event log, memory, orchestration, observability, evaluation, and release governance.
3. **Standards and adapters**: MCP, A2A, OpenTelemetry, durable execution engines, and selected framework adapters such as OpenAI Agents SDK, Google ADK, Microsoft Agent Framework, LangGraph, and PydanticAI.
4. **Versioned case studies**: OpenClaw, Hermes Agent, ChatGPT Work, xAI agent tooling, and future systems. Product facts must be dated and sourced.

Canonical implementation language: Python for the reference harness, with TypeScript literacy and at least one cross-language adapter exercise. Prefer standard-library-first foundations before framework convenience.

## Proposed Program Spine

### Prerequisite Bridge

- command line, Git, Python, TypeScript/JSON literacy
- testing, debugging, APIs, HTTP, authentication, databases
- processes, containers, networking, concurrency, queues
- probability/statistics, experimental design, basic ML/LLM concepts
- threat modeling, least privilege, secrets, and secure development

### Semester 1: Harness Foundations

- define agents, workflows, harnesses, and trust boundaries
- build a deterministic model-adapter test double
- implement a bounded agent loop and stop conditions
- implement schemas, typed tool registry, validation, errors, and idempotency
- build context assembly and budget management
- implement session state, event log, checkpoints, and replay
- add policy, approval, sandbox boundaries, and audit records
- add structured traces, metrics, logs, and a basic eval harness
- complete a minimal-harness practical and oral defense

### Semester 2: Production Agent Systems

- planning, routing, parallelization, manager/handoff patterns
- memory architecture and retrieval quality
- durable execution, retries, compensation, cancellation, recovery
- MCP and A2A interoperability
- prompt injection, confused deputy, supply chain, data exfiltration, and tool abuse
- reliability, SLOs, capacity, cost, latency, and incident response
- evaluation corpora, repeated trials, graders, regression gates, red teaming
- deployment, tenancy, governance, privacy, accessibility, and change control
- comparative product/framework case studies
- capstone: build, defend, attack, evaluate, operate, and port a working harness

## Source Standard

Primary anchors already researched for the migration:

- OpenAI practical agent guide and Agents SDK documentation
- Anthropic effective agents, context engineering, tool design, long-running harness, sandboxing, and agent-evaluation guidance
- Google Agent Development Kit documentation and source
- Microsoft Agent Framework documentation
- LangGraph persistence and human-in-the-loop documentation
- PydanticAI durable-execution documentation
- MCP and A2A specifications
- OpenTelemetry semantic conventions
- NIST AI RMF and Generative AI Profile
- NIST Secure Software Development Framework
- OWASP Agentic AI threats and Agent Security Cheat Sheet
- ABET 2026-2027 computing accreditation criteria
- ACM/IEEE-CS CS2023 and SWEBOK v4
- ReAct, Toolformer, Reflexion, MemGPT, AgentBench, tau-bench, OSWorld, and METR time-horizon research

Official standards, specifications, source repositories, current docs, releases, and advisories are authoritative for current behavior. Peer-reviewed research supports durable theory. Maintainer engineering posts support rationale. Blogs, issues, forums, Reddit, and product commentary are discovery signals that require verification.

## Completion Gates

The project is complete only when every applicable gate has evidence:

| Gate | Required evidence | Current state |
| --- | --- | --- |
| G0 Scope and boundary | Stable outcomes, product separation, claim limits | Implemented; independent audit pending |
| G1 Source integrity | Claim-source map, versions/dates, independent spot checks | Partial |
| G2 Curriculum alignment | Outcome-to-module-to-lab-to-assessment traceability | Implemented; audit/calibration pending |
| G3 Reference implementation | Runnable harness, tests, fixtures, documented failure modes | Partial; bounded fixtures pass, production adapters absent |
| G4 Hands-on reproducibility | Labs executed in clean environments with expected evidence | Early; reference suite only |
| G5 Assessment validity | Authentic tasks, oral defense, transfer, anti-outsourcing controls | Strong authored system; empirical validity pending |
| G6 Security and governance | Threat labs, controls, privacy, change management, audits | Strong authored system; execution/audit pending |
| G7 Teaching readiness | Instructor notes, pacing, accessibility, calibration | Partial |
| G8 Learner evidence | Pilot data and delayed changed-task transfer | Missing |
| G9 External validation | Independent academic, practitioner, security reviews repaired | Missing for new scope |
| G10 Release readiness | Clean repo, licensing, versioning, release notes, support boundary | In progress; repository/license exist, release package does not |

No completion percentage overrides a failed gate.

## Implementation Sequence

1. Run internal adversarial validation across alignment, source integrity, code, security, accessibility, delivery, and claim boundaries; repair findings.
2. Execute every critical lab in clean environments and record reproduction status.
3. Complete dated claim ledgers/exercises for non-OpenClaw cases and reverify current protocol/framework sources.
4. Add actual pinned protocol/provider/telemetry examples only where they materially improve labs.
5. Run independent adversarial academic, enterprise, security, and practitioner reviews; repair findings.
6. Pilot with real learners and assessors before institution-ready or enterprise-ready claims.

## Immediate Next Actions

1. Keep `../elite-mentor-os` frozen until the user explicitly resumes that product.
2. Finish the internal adversarial validation and write one consolidated current evidence report.
3. Align detailed lab verification status with actual execution evidence; do not mark authored labs reproduced.
4. Complete dated non-OpenClaw case claim ledgers and exercises.
5. Reproduce critical labs cleanly, then seek independent review and pilot evidence.

## State-Preservation Protocol

At every meaningful milestone:

1. Read `PROJECT_STATE.md`, `.mentor/MENTOR_STATE.md`, `git status -sb`, and the latest commit.
2. Verify current sources for release-sensitive claims.
3. Change the smallest coherent scope and run matching checks.
4. Update both state files with decisions, evidence, blockers, and next action.
5. Commit and push separate product or milestone scopes only after validation.

Do not store chat transcripts, credentials, secrets, or speculative claims in state. Do not mark completion from document count. Do not ask the user to repeat decisions already recorded here.
