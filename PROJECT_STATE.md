# OpenClaw Mastery Curriculum Project State

## Purpose of this file

This is the standalone source of truth for resuming the OpenClaw Mastery Curriculum project after chat history is cleared, compacted, or unavailable.

If a new Codex, Claude, or other LLM session starts from this file, it should understand the goal, repository state, quality bar, implementation history, current files, and next steps without needing the original conversation.

## Current date captured

- Captured on: 2026-05-02
- Timezone context: Asia/Karachi
- Primary repo branch: `main`
- Committed baseline before this state-file update: `366d3e0` - `Add WSL screenshot capture curriculum assets`
- To get the latest commit after future edits, run `git log -1 --oneline`

## Primary vision

Build a world-class, all-in-one OpenClaw mastery curriculum that starts from absolute beginner level and progresses to expert, production, enterprise, security, extension, contributor, and teaching mastery.

The goal is not a simple course, roadmap, tutorial, or reading list. The target is a complete, standalone curriculum system that can be used by:

- millions of self-learners
- universities
- instructors
- enterprise onboarding teams
- AI operations teams
- DevOps and platform teams
- security and governance teams
- plugin developers
- open-source contributors

The curriculum must be strong enough that a serious instructor or institution can teach from it without reconstructing the structure from scratch.

## Product standard

The curriculum should aim for:

- standalone ready-to-teach quality
- university-grade structure
- enterprise-aware operations
- production readiness
- security realism
- hands-on labs
- theory and concept depth
- capstone and assessment rigor
- instructor usability
- future maintainability under OpenClaw release changes
- evidence-backed validation
- adversarial review readiness

The desired final quality is "world-class", meaning:

- no vague claims without evidence
- no shallow tutorial-only coverage
- no security theater
- no unsupported hostile multi-tenant claims
- no frozen assumptions about moving OpenClaw defaults
- no curriculum content that cannot be traced to official sources, verified inference, or clearly labeled secondary material

## Repository locations

Primary local repo:

- `/mnt/c/Users/Administrator/Documents/Codex/2026-04-22-openclaw-search-deeply-on-internet-github/openclaw-mastery`

User-facing Windows study copy:

- `E:\Study\Openclaw mastery`
- WSL path: `/mnt/e/Study/Openclaw mastery`

GitHub repo:

- `https://github.com/HaseebAhmed-official/openclaw-mastery-curriculum`

Old GitHub remote retained locally:

- `https://github.com/mhaseebahmed/openclaw-mastery.git`

## Current Git state

At the time this file was written:

- branch: `main`
- latest pushed commit before this state-file update: `366d3e0`
- latest actual commit should be checked with `git log -1 --oneline`
- local repo was clean before this state-file update
- current remote `origin`: `https://github.com/HaseebAhmed-official/openclaw-mastery-curriculum.git`
- repo visibility: public
- license: MIT

Recent important commits:

- `366d3e0` - Add WSL screenshot capture curriculum assets
- `f791682` - Add classroom delivery and calibration assets
- `a3e120e` - Deepen Semester 2 security teaching guidance
- `5ed2e55` - Integrate current OpenClaw advisory guidance
- `814fee7` - Add model artifacts and maintenance automation
- `d331fae` - Add submission templates and grading assets
- `3526f4a` - Add ready-to-teach curriculum delivery assets
- `bd8071e` - Polish repository for public release

## Current implementation status

Estimated status:

- Standalone ready-to-teach curriculum: approximately 85-90%
- True world-class, institution-proof polished product: approximately 70-75%

The core architecture is implemented. The remaining work is mainly validation, depth expansion, real-world calibration, and final polish.

## Implemented major components

### Core curriculum

- `README.md`
- `curriculum/program-overview.md`
- `curriculum/prerequisite-bridge.md`
- `curriculum/competency-framework.md`
- `curriculum/assessment-map.md`
- `curriculum/governance-and-security-strand.md`
- `curriculum/automation-and-detached-work.md`
- `curriculum/update-and-release-discipline.md`
- `curriculum/instructor-handbook.md`
- `curriculum/course-syllabus-template.md`

### Semester structure

- `curriculum/semester-1/index.md`
- `curriculum/semester-1/teaching-guide.md`
- `curriculum/semester-2/index.md`
- `curriculum/semester-2/teaching-guide.md`

Semester 1 focuses on:

- environment readiness
- Git and repo hygiene
- Node.js, JSON, TypeScript literacy
- Docker and networking basics
- LLM agent fundamentals
- OpenClaw architecture and trust model
- installation and onboarding
- Control UI, diagnostics, status, doctor
- sessions, workspace, memory
- providers and release-aware defaults
- tools, sandboxing, approvals
- channels and pairing
- nodes and multimodal surfaces
- remote access
- troubleshooting and secure baseline
- practical exam and mini-project

Semester 2 focuses on:

- production framing
- multi-agent routing and identity files
- configuration architecture
- security audit, advisories, webhook ingress, and hardening
- exec approvals and host authority
- remote access and trusted proxy patterns
- shared inboxes and DM scope
- plugins, bundles, ClawHub, supply chain
- skills and six-layer precedence
- automation, hooks, heartbeat, standing orders
- sub-agents, ACP agents, task auditability
- memory strategy and Dreaming
- threat modeling and formal verification limits
- contributor and ecosystem literacy
- track capstone sprint
- final defense

### Tracks

- `curriculum/tracks/index.md`
- `curriculum/tracks/operator.md`
- `curriculum/tracks/production-devops.md`
- `curriculum/tracks/security-hardening.md`
- `curriculum/tracks/plugin-developer.md`
- `curriculum/tracks/contributor-core.md`
- `curriculum/tracks/local-models.md`

Tracks are:

- Operator / Power User
- Production / DevOps
- Security / Hardening
- Plugin Developer
- Contributor / Core Developer
- Local Models Specialization

### Labs and manuals

- `curriculum/labs/index.md`
- `curriculum/labs/lab-authoring-standard.md`
- `curriculum/labs/lab-catalog.md`
- `curriculum/labs/core-lab-guides.md`
- `curriculum/labs/advanced-lab-guides.md`
- `curriculum/labs/specialization-lab-guides.md`
- `curriculum/labs/environment-lanes.md`

Classroom manuals:

- `curriculum/lab-manuals/index.md`
- `curriculum/lab-manuals/core-classroom-manuals.md`
- `curriculum/lab-manuals/advanced-classroom-manuals.md`
- `curriculum/lab-manuals/specialization-classroom-manuals.md`
- `curriculum/lab-manuals/screenshot-capture-standard.md`
- `curriculum/lab-manuals/reference-screenshot-manifest.md`
- `curriculum/lab-manuals/wsl-ubuntu-capture-workflow.md`
- `curriculum/lab-manuals/assets/README.md`

Screenshot asset directories:

- `curriculum/lab-manuals/assets/core/`
- `curriculum/lab-manuals/assets/advanced/`
- `curriculum/lab-manuals/assets/specialization/`

Important note:

- The screenshot system is now structured, but real screenshots are not yet populated.
- The user clarified that their real OpenClaw learning environment is WSL Ubuntu with OpenClaw installed.
- Do not spend future effort trying to install or run OpenClaw from the Windows-side Codex shell unless the user explicitly asks.

### Assessment assets

- `curriculum/assessment/index.md`
- `curriculum/assessment/question-bank.md`
- `curriculum/assessment/practical-exams.md`
- `curriculum/assessment/oral-defense-bank.md`
- `curriculum/assessment/assessor-calibration-guide.md`
- `curriculum/assessment/grading-packet-templates.md`
- `curriculum/assessment/answer-key-guidance.md`
- `curriculum/assessment/feedback-bank.md`
- `curriculum/assessment/track-evaluation-sheets.md`

### Rubrics

- `curriculum/rubrics/index.md`
- `curriculum/rubrics/master-rubric.md`
- `curriculum/rubrics/track-rubrics.md`

### Submission templates

- `curriculum/templates/index.md`
- `curriculum/templates/lab-submission-template.md`
- `curriculum/templates/runbook-template.md`
- `curriculum/templates/design-review-template.md`
- `curriculum/templates/threat-model-template.md`
- `curriculum/templates/capstone-submission-template.md`
- `curriculum/templates/release-aware-note-template.md`

### Model artifacts and model answer packs

Student/instructor examples:

- `curriculum/examples/index.md`
- `curriculum/examples/model-lab-submission.md`
- `curriculum/examples/model-design-review.md`
- `curriculum/examples/model-capstone-summary.md`
- `curriculum/examples/instructor-model-feedback.md`
- `curriculum/examples/weak-submission-red-flags.md`

Track-specific instructor calibration packs:

- `curriculum/model-answers/index.md`
- `curriculum/model-answers/operator-answer-pack.md`
- `curriculum/model-answers/production-devops-answer-pack.md`
- `curriculum/model-answers/security-hardening-answer-pack.md`
- `curriculum/model-answers/plugin-developer-answer-pack.md`
- `curriculum/model-answers/contributor-core-answer-pack.md`
- `curriculum/model-answers/local-models-answer-pack.md`

### Slide outlines

- `curriculum/slides/index.md`
- `curriculum/slides/semester-1-weekly-outlines.md`
- `curriculum/slides/semester-2-weekly-outlines.md`
- `curriculum/slides/track-workshop-outlines.md`

### Sources, validation, and maintenance

- `curriculum/sources/official-reading-map.md`
- `curriculum/sources/validation-register.md`
- `Validations/README.md`
- `Validations/codex-review/openclaw-curriculum-pack-validation-review-2026-04-22.md`
- `Validations/Claude-code-review/openclaw-mastery-curriculum-full-validation-review-2026-04-22.md`

Maintenance:

- `curriculum/maintenance/index.md`
- `curriculum/maintenance/continuous-improvement-system.md`
- `curriculum/maintenance/upstream-review-playbook.md`
- `curriculum/maintenance/change-control-checklist.md`
- `curriculum/maintenance/review-log.md`
- `curriculum/maintenance/upstream-state.json`
- `scripts/check_openclaw_release_drift.py`
- `.github/workflows/openclaw-upstream-drift-check.yml`

## Validation history

Two external-style reviews were added previously:

- Codex review in `Validations/codex-review/`
- Claude review in `Validations/Claude-code-review/`

Those reviews found important gaps, many of which were later addressed:

- automation and detached work
- tasks, task flow, standing orders, hooks, heartbeat
- sub-agents and ACP agents
- Dreaming and `DREAMS.md`
- `SOUL.md`, `USER.md`, workspace `AGENTS.md`
- six-layer skill precedence
- webhook security
- detached-task auditability
- update and release discipline
- contributor workflow details
- formal verification maturity labeling
- advisory-aware security teaching

The reviews should remain preserved as historical validation artifacts, but future reviewers must independently verify them.

## Current source baseline and advisory state

As of the latest maintenance work:

- OpenClaw tracked repo: `openclaw/openclaw`
- Last reviewed OpenClaw release in state file: `v2026.4.23`
- Last reviewed date in state file: `2026-04-24`
- Latest curriculum advisory integration included official advisories published around `2026-04-23`

Important advisory examples integrated into teaching:

- `GHSA-93rg-2xm5-2p9v` - Gateway Control UI bootstrap config required Gateway auth
- `GHSA-55cf-xx38-4p9p` - Workspace dotenv files cannot override connector endpoint hosts
- `GHSA-x3h8-jrgh-p8jx` - Exec allowlist analysis rejects shell expansion in unquoted heredocs
- `GHSA-r6xh-pqhr-v4xh` - MCP loopback owner context is derived from server-issued bearer tokens
- `GHSA-q3jj-46pq-826r` - ACP child sessions inherit subagent security envelope constraints
- `GHSA-wppj-c6mr-83jj` - OpenShell FS bridge writes stay pinned to the sandbox mount root

Future validation must re-check current releases, docs, and advisories because the project moves quickly.

## Key design decisions

- The curriculum is university-first but enterprise-usable.
- The program is English-only.
- The main shape is a two-semester core plus specialization tracks.
- The canonical learning lane is WSL Ubuntu / Linux plus browser-based Control UI.
- Stable OpenClaw behavior is the baseline.
- Preview, internal-preview, source-build, beta, or dev behavior must be labeled.
- Local models are an advanced specialization, not the core baseline.
- Security and governance are mandatory across the main path.
- Detached authority is first-class: cron, tasks, task flow, hooks, standing orders, heartbeat, sub-agents, ACP agents.
- The trust model must not be misrepresented as hostile multi-tenant isolation.
- Release and advisory drift must be explicitly handled.
- Real screenshots should be captured from the user's WSL Ubuntu lane, not invented or forced from the Windows-side Codex shell.

## Current known gaps

The curriculum is strong, but not final-perfect. Remaining likely gaps:

- real captured screenshots are not yet committed
- slide outlines are not full slide decks
- no rendered docs site or GitHub Pages layer yet
- labs are strong manuals but not all are fully command-by-command runnable scripts
- certification tiers are implied but could be formalized more
- external validation after the newest commits is still needed
- current OpenClaw release state must be rechecked because this state file is dated 2026-05-02 and upstream may have changed
- more top-quality community/blog/Reddit evidence can be reviewed and categorized, but official sources must stay primary

## Current best next step

Run a fresh external validation round using the master validation prompt:

- `Validations/master-validation-prompt.md`

Recommended reviewers:

- new Codex session
- Claude session
- optionally another strong model

The reviewers should:

- inspect the local repo and GitHub repo
- browse current official OpenClaw docs, GitHub, releases, advisories
- search high-quality external sources including serious blogs, community threads, Reddit, issue discussions, and expert posts
- label source quality clearly
- validate the whole curriculum from technical, pedagogical, security, enterprise, production, and maintenance perspectives
- produce a ranked remediation plan

After receiving new reviews:

1. Save the review outputs under `Validations/`.
2. Compare overlap across reviewers.
3. Create a prioritized remediation backlog.
4. Patch the curriculum.
5. Update this `PROJECT_STATE.md`.
6. Commit and push.
7. Sync the Windows study copy at `E:\Study\Openclaw mastery`.

## Future session startup instructions

If a future session starts after chat clear:

1. Open this file first.
2. Run `git status --short` in the repo.
3. Read `README.md`.
4. Read `Validations/master-validation-prompt.md`.
5. Check `curriculum/maintenance/upstream-state.json`.
6. If the user asks for validation, use the prompt and source rules from `Validations/master-validation-prompt.md`.
7. If the user asks for implementation, inspect relevant files before editing.
8. After any meaningful update, update this file, commit, push, and sync to `E:\Study\Openclaw mastery` if possible.

## Strict working rules for future agents

- Do not delete or rewrite the curriculum wholesale.
- Do not treat old chat history as more authoritative than this file plus the repo.
- Do not run OpenClaw installation experiments unless explicitly asked.
- Do not invent screenshots.
- Do not add unsupported claims just to make the curriculum look complete.
- Do not over-trust secondary sources.
- Do not ignore official advisories.
- Do not represent OpenClaw as a hostile multi-tenant security boundary.
- Do not mark the curriculum world-class without fresh validation.
- Always preserve source-quality labels: official, verified inference, secondary, weak, uncertain, incorrect.

## Definition of done for final world-class target

The curriculum can be considered near final when:

- fresh Codex and Claude reviews both find no critical blockers
- all high-severity findings are patched or explicitly accepted with rationale
- official OpenClaw release/docs/advisory baseline is current
- every major module has teachable objectives, readings, labs, failure modes, assessments, and security implications
- every track has a defensible capstone, rubric, and model answer pack
- classroom lab manuals have either real screenshots or a clearly documented capture path
- maintenance automation and manual review workflow are working
- the README and instructor handbook can onboard a new instructor without chat context
- this `PROJECT_STATE.md` is current
