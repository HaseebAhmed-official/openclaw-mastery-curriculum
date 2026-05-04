# Elite Mentor OS Project State

## Purpose

This repository is no longer only an OpenClaw curriculum repository. It is also the first proof case for **Elite Mentor OS**, a local-first native plugin system for Claude Code and Codex that turns any directory into a rigorous AI mentor workspace.

The goal is to create a system that can help a serious self-learner compete with students from elite universities and developers from top technology companies by combining evidence-backed pedagogy, project-based mastery, source validation, deliberate practice, portfolio evidence, and adversarial review.

## Current Directory Role

- Directory: OpenClaw mastery curriculum repository.
- Plugin product: `plugins/elite-mentor-os/`.
- Proof case: OpenClaw Mastery curriculum.
- Native targets: Claude Code and Codex.
- Distribution model: native marketplace metadata and local plugin loading; no custom command installer or package installer.
- State model: project-local `.mentor/MENTOR_STATE.md` plus optional private global learner profile outside the repo if needed later.

## Learner Profile

- Primary learner: Haseeb Ahmed, starting from beginner-friendly foundations but aiming for expert, production, enterprise, research, teaching, and portfolio-level mastery.
- Target standard: elite self-learning system strong enough to be useful to serious self-learners, universities, and companies.
- Default language: English.
- Roman Urdu: allowed only when explicitly requested as a clarification layer.
- Required skill dimensions: technical mastery, communication, critical thinking, strategic thinking, problem solving, English proficiency, research judgment, portfolio quality, and professional reasoning.

## Active Roadmap

- Current implementation track: build Elite Mentor OS as a dual-native plugin with a shared core.
- Current milestone: lean v0.1 native plugin package completed with manifests, 5 skills, 3 Claude agents, one consolidated core, one OpenClaw proof-pack, one validation file, continuity state, and local checks.
- Next milestone: run real Claude Code and Codex plugin-load tests in interactive sessions, then use the system to guide OpenClaw learning sessions.
- Mastery target: a reusable mentor system that can adapt to any directory, subject, topic, or resource set while maintaining auditable quality gates.

## Complete Dream Roadmap

| Phase | Goal | Exit evidence |
| --- | --- | --- |
| P0 Lean plugin foundation | Keep native plugin surface minimal and usable. | 17-file surface, JSON checks, no stale references, plugin-eval 91/100 baseline. |
| P1 Live plugin proof | Prove Claude and Codex can load and use the plugin. | Claude install/load test and Codex fresh-session discovery test pass. |
| P2 Learning proof | Prove the system teaches a real learner. | One OpenClaw session produces roadmap, practice, review, and state update proposal. |
| P3 Validation proof | Prove quality under adversarial review. | Fresh Codex/Claude review finds no critical blockers or all are patched. |
| P4 Institution proof | Prove university-style adoption readiness. | Outcomes, assessments, rubrics, source policy, and instructor flow pass review. |
| P5 Enterprise proof | Prove company governance readiness. | Privacy, security, prompt-injection, update drift, and auditability pass review. |
| P6 Product proof | Prove responsible distribution. | Install docs, support path, license position, versioning, and real user evidence exist. |

## Source Graph

| Source | Tier | Purpose | Status |
| --- | --- | --- | --- |
| Claude Code plugin docs | S0 | Claude native plugin manifest, skills, agents, marketplace behavior | Checked on 2026-05-04 |
| Local Codex plugin creator spec | S0 | Codex plugin manifest and marketplace layout | Checked during implementation |
| Existing OpenClaw curriculum files | S0/S2 by claim | First proof case and curriculum mapping | Present in repo |
| How People Learn II | S1 | Learning science foundation | Used as pedagogy anchor |
| IES practice guides | S1 | Study organization and learning guidance | Used as pedagogy anchor |
| Retrieval, spacing, active learning, deliberate practice, ICAP, cognitive apprenticeship literature | S1 | Durable learning design | Used as pedagogy anchor |

## Portfolio Evidence

| Artifact | Mastery level | Evidence quality | Review status |
| --- | --- | --- | --- |
| OpenClaw curriculum repository | L4-L6 curriculum and production-readiness design | Strong but still needs cohort testing and screenshot population | Reviewed by Codex and Claude in `Validations/` |
| Elite Mentor OS plugin package | L5-L7 learning-system design and native plugin architecture | Lean v0.1 implemented; 17-file surface; plugin-eval improved from 46/100 to 91/100 before final tiny cleanup | Needs plugin-load testing and adversarial review |
| Validation prompt pack | L5 adversarial review readiness | Strong | Needs rerun after plugin completion |

## Session Log

| Date | Work completed | Evidence | Next repair/action |
| --- | --- | --- | --- |
| 2026-05-04 | Hardened Elite Mentor OS into a lean native Claude/Codex plugin surface. | 17 plugin/state files; 5 skills; 3 Claude agents; consolidated `MENTOR_OS.md`, `OPENCLAW_PROOF_PACK.md`, and `VALIDATION.md`; JSON checks and `git diff --check` passed; plugin-eval reached 91/100 before final tiny cleanup. | Run interactive Claude/Codex plugin-load tests and external adversarial review. |

## Quality Gates

- Every workflow must read `.mentor/MENTOR_STATE.md` first when present.
- Every write to `.mentor`, curriculum files, repo files, or portfolio artifacts must be explicit and auditable.
- Every roadmap must include prerequisites, practice, retrieval checks, assessments, and portfolio evidence.
- Every source-sensitive claim must be labeled by source tier.
- Every high-stakes learning request must stay learning-only unless qualified professional context is provided.
- Every future release-sensitive curriculum update must record source checks and residual uncertainty.
- Do not claim 99% confidence until P1-P6 exit evidence exists.

## Open Questions

- Need real plugin-load tests inside Claude Code and Codex after the package is complete.
- Need external validation after the plugin layer is added.
- Need decide later whether to publish a separate product repository after the OpenClaw proof case stabilizes.
- Need design a future update/drift automation plan separately after current implementation is complete.

## Next Actions

1. Run Claude Code local marketplace install test.
2. Run Codex plugin discovery test in a fresh session.
3. Use `plugins/elite-mentor-os/validation/VALIDATION.md` for external review and behavior testing.
4. Start the first OpenClaw learning session with `elite-mentor-os:openclaw-master`.
