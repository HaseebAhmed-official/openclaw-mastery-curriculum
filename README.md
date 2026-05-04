# OpenClaw Mastery Curriculum

[![License](https://img.shields.io/github/license/HaseebAhmed-official/openclaw-mastery-curriculum)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/HaseebAhmed-official/openclaw-mastery-curriculum)](https://github.com/HaseebAhmed-official/openclaw-mastery-curriculum/commits/main)
[![Repo Size](https://img.shields.io/github/repo-size/HaseebAhmed-official/openclaw-mastery-curriculum)](https://github.com/HaseebAhmed-official/openclaw-mastery-curriculum)

This repository is a university-grade, enterprise-usable **OpenClaw mastery curriculum** designed to take a learner from prerequisite foundations to production operations, security hardening, extension development, and contributor-level understanding.

It also contains the first proof implementation of **Elite Mentor OS**, a local-first native plugin system for Claude Code and Codex that turns any directory into a rigorous AI mentor workspace.

It is not just a reading list. It is a structured curriculum system with:

- a prerequisite bridge for beginners
- a two-semester core program
- advanced role-based tracks
- hands-on lab architecture
- capstones and rubrics
- source-backed validation artifacts

For project continuity after chat resets or context clearing, start from [Project State](PROJECT_STATE.md) and [Mentor State](.mentor/MENTOR_STATE.md).

## Vision

The goal is to build one of the strongest publicly available learning systems for OpenClaw:

- technically accurate
- security-realistic
- production-aware
- pedagogically structured
- reusable by universities, instructors, and enterprise teams

The broader Elite Mentor OS goal is to make this curriculum teachable through native AI mentor workflows that can diagnose a directory, build a roadmap, teach lessons, assign deliberate practice, review evidence, validate sources, and preserve continuity through `.mentor/MENTOR_STATE.md`.

## Elite Mentor OS Native Plugin

Elite Mentor OS is implemented under `plugins/elite-mentor-os/`. Its runtime contract is [Mentor OS Core](plugins/elite-mentor-os/core/MENTOR_OS.md). It is designed as:

- a shared mentor core for Claude Code and Codex
- a Claude native plugin with `.claude-plugin/plugin.json`, skills, and agents
- a Codex native plugin with `.codex-plugin/plugin.json` and skills
- a local-first state system using `.mentor/MENTOR_STATE.md`
- an OpenClaw proof-pack that maps this curriculum into mentor-guided sessions
- a guided-action system that proposes writes before changing state, curriculum, or portfolio files

Native marketplace files:

- Claude Code marketplace: [.claude-plugin/marketplace.json](.claude-plugin/marketplace.json)
- Codex marketplace: [.agents/plugins/marketplace.json](.agents/plugins/marketplace.json)

Remote plugin use after this repo is pushed:

Claude Code:

```text
/plugin marketplace add HaseebAhmed-official/openclaw-mastery-curriculum
/plugin install elite-mentor-os@elite-mentor-os-marketplace
/elite-mentor-os:diagnose
```

Claude Code CLI, sparse checkout variant:

```bash
claude plugin marketplace add HaseebAhmed-official/openclaw-mastery-curriculum --sparse .claude-plugin plugins/elite-mentor-os
```

Codex CLI:

```bash
codex plugin marketplace add HaseebAhmed-official/openclaw-mastery-curriculum --sparse .agents/plugins --sparse plugins/elite-mentor-os
```

Then open `/plugins`, install `elite-mentor-os` from `Elite Mentor OS Marketplace`, start a new thread, and invoke the plugin or one of its bundled skills with `@`.

Plugin references:

- [Mentor OS Core](plugins/elite-mentor-os/core/MENTOR_OS.md)
- [OpenClaw Proof-Pack](plugins/elite-mentor-os/proof-packs/openclaw/OPENCLAW_PROOF_PACK.md)
- [Validation](plugins/elite-mentor-os/validation/VALIDATION.md)

## Program Baseline

- Audience: university-first, but structured so enterprise teams can adopt it directly
- Delivery model: two-semester core program plus advanced tracks
- Learning shape: shared foundation plus role-based specialization
- Language: English
- Canonical lab baseline: WSL2/Linux + VPS + Docker
- Assessment model: project-heavy with labs, design reviews, and track-specific capstones
- Security posture: governance and hardening are mandatory in the main path
- Version stance: stable-release-first, with clearly labeled preview and source-build material
- Release discipline: provider, security, automation, and deployment labs must begin with current release-note checks
- Validation stance: official sources first, validated inference second, community guidance explicitly labeled

## Repository Structure

### Elite Mentor OS

- [Mentor OS Core](plugins/elite-mentor-os/core/MENTOR_OS.md)
- [OpenClaw Proof-Pack](plugins/elite-mentor-os/proof-packs/openclaw/OPENCLAW_PROOF_PACK.md)
- [Validation](plugins/elite-mentor-os/validation/VALIDATION.md)
- [Mentor State](.mentor/MENTOR_STATE.md)

### Core program

- [Program Overview](curriculum/program-overview.md)
- [Instructor Handbook](curriculum/instructor-handbook.md)
- [Course Syllabus Template](curriculum/course-syllabus-template.md)
- [Prerequisite Bridge](curriculum/prerequisite-bridge.md)
- [Competency Framework](curriculum/competency-framework.md)
- [Assessment Map](curriculum/assessment-map.md)
- [Governance and Security Strand](curriculum/governance-and-security-strand.md)
- [Automation and Detached Work](curriculum/automation-and-detached-work.md)
- [Update and Release Discipline](curriculum/update-and-release-discipline.md)

### Semester sequence

- [Semester 1: Foundations and Safe Operation](curriculum/semester-1/index.md)
- [Semester 2: Production, Security, and Expert Paths](curriculum/semester-2/index.md)

### Specialization tracks

- [Tracks Index](curriculum/tracks/index.md)
- [Operator Track](curriculum/tracks/operator.md)
- [Production / DevOps Track](curriculum/tracks/production-devops.md)
- [Security / Hardening Track](curriculum/tracks/security-hardening.md)
- [Plugin Developer Track](curriculum/tracks/plugin-developer.md)
- [Contributor / Core Developer Track](curriculum/tracks/contributor-core.md)
- [Local Models Specialization](curriculum/tracks/local-models.md)

### Hands-on delivery

- [Labs Index](curriculum/labs/index.md)
- [Classroom Lab Manuals](curriculum/lab-manuals/index.md)
- [Lab Authoring Standard](curriculum/labs/lab-authoring-standard.md)
- [Lab Catalog](curriculum/labs/lab-catalog.md)
- [Core Lab Guides](curriculum/labs/core-lab-guides.md)
- [Advanced Lab Guides](curriculum/labs/advanced-lab-guides.md)
- [Specialization Lab Guides](curriculum/labs/specialization-lab-guides.md)
- [Environment Lanes](curriculum/labs/environment-lanes.md)
- [Capstones Index](curriculum/capstones/index.md)
- [Capstone Specs](curriculum/capstones/capstone-specs.md)
- [Rubrics Index](curriculum/rubrics/index.md)
- [Master Rubric](curriculum/rubrics/master-rubric.md)
- [Track Rubrics](curriculum/rubrics/track-rubrics.md)

### Classroom delivery assets

- [Slide Deck Outlines](curriculum/slides/index.md)
- [Semester 1 Weekly Slide Outlines](curriculum/slides/semester-1-weekly-outlines.md)
- [Semester 2 Weekly Slide Outlines](curriculum/slides/semester-2-weekly-outlines.md)
- [Track Workshop Slide Outlines](curriculum/slides/track-workshop-outlines.md)
- [Screenshot Capture Standard](curriculum/lab-manuals/screenshot-capture-standard.md)
- [Reference Screenshot Manifest](curriculum/lab-manuals/reference-screenshot-manifest.md)
- [WSL Ubuntu Capture Workflow](curriculum/lab-manuals/wsl-ubuntu-capture-workflow.md)
- [Core Classroom Lab Manuals](curriculum/lab-manuals/core-classroom-manuals.md)
- [Advanced Classroom Lab Manuals](curriculum/lab-manuals/advanced-classroom-manuals.md)
- [Specialization Classroom Lab Manuals](curriculum/lab-manuals/specialization-classroom-manuals.md)

### Assessment assets

- [Assessment Index](curriculum/assessment/index.md)
- [Question Bank](curriculum/assessment/question-bank.md)
- [Practical Exams](curriculum/assessment/practical-exams.md)
- [Oral Defense Bank](curriculum/assessment/oral-defense-bank.md)
- [Assessor Calibration Guide](curriculum/assessment/assessor-calibration-guide.md)
- [Grading Packet Templates](curriculum/assessment/grading-packet-templates.md)
- [Answer Key Guidance](curriculum/assessment/answer-key-guidance.md)
- [Feedback Bank](curriculum/assessment/feedback-bank.md)
- [Track Evaluation Sheets](curriculum/assessment/track-evaluation-sheets.md)

### Submission assets

- [Submission Templates](curriculum/templates/index.md)
- [Lab Submission Template](curriculum/templates/lab-submission-template.md)
- [Runbook Template](curriculum/templates/runbook-template.md)
- [Design Review Template](curriculum/templates/design-review-template.md)
- [Threat Model Template](curriculum/templates/threat-model-template.md)
- [Capstone Submission Template](curriculum/templates/capstone-submission-template.md)
- [Release-Aware Note Template](curriculum/templates/release-aware-note-template.md)

### Model artifacts

- [Model Artifacts Index](curriculum/examples/index.md)
- [Model Lab Submission](curriculum/examples/model-lab-submission.md)
- [Model Design Review](curriculum/examples/model-design-review.md)
- [Model Capstone Summary](curriculum/examples/model-capstone-summary.md)
- [Instructor Model Feedback](curriculum/examples/instructor-model-feedback.md)
- [Weak Submission Red Flags](curriculum/examples/weak-submission-red-flags.md)

### Instructor calibration packs

- [Model Answer Packs](curriculum/model-answers/index.md)
- [Operator Answer Pack](curriculum/model-answers/operator-answer-pack.md)
- [Production / DevOps Answer Pack](curriculum/model-answers/production-devops-answer-pack.md)
- [Security / Hardening Answer Pack](curriculum/model-answers/security-hardening-answer-pack.md)
- [Plugin Developer Answer Pack](curriculum/model-answers/plugin-developer-answer-pack.md)
- [Contributor / Core Answer Pack](curriculum/model-answers/contributor-core-answer-pack.md)
- [Local Models Answer Pack](curriculum/model-answers/local-models-answer-pack.md)

### Maintenance system

- [Maintenance Index](curriculum/maintenance/index.md)
- [Continuous Improvement System](curriculum/maintenance/continuous-improvement-system.md)
- [Upstream Review Playbook](curriculum/maintenance/upstream-review-playbook.md)
- [Change Control Checklist](curriculum/maintenance/change-control-checklist.md)
- [Review Log](curriculum/maintenance/review-log.md)
- Automated release drift workflow: `.github/workflows/openclaw-upstream-drift-check.yml`

### Validation and evidence

- [Mentor State](.mentor/MENTOR_STATE.md)
- [Project State](PROJECT_STATE.md)
- [Master Validation Prompt](Validations/master-validation-prompt.md)
- [Validation Register](curriculum/sources/validation-register.md)
- [Official Reading Map](curriculum/sources/official-reading-map.md)
- [External Validation Reviews](Validations/)

## How to Use It

### Students

1. Start with the [Program Overview](curriculum/program-overview.md).
2. Finish the [Prerequisite Bridge](curriculum/prerequisite-bridge.md).
3. Work through [Semester 1](curriculum/semester-1/index.md) and [Semester 2](curriculum/semester-2/index.md).
4. Choose a role path from [Tracks](curriculum/tracks/index.md).
5. Complete the mapped labs, capstone, and final defense.

### AI-mentor learning

1. Start with [Mentor State](.mentor/MENTOR_STATE.md).
2. Use `elite-mentor-os:diagnose` to locate your current level.
3. Use `elite-mentor-os:openclaw-master` for the next OpenClaw session.
4. Use `elite-mentor-os:mentor` for lessons and deliberate practice.
5. Use `elite-mentor-os:review` to prove mastery through artifacts.
6. Approve `.mentor` updates only after the proposed state change is accurate.

### Instructors

1. Read the [Program Overview](curriculum/program-overview.md) and [Assessment Map](curriculum/assessment-map.md).
2. Choose an environment lane from [Environment Lanes](curriculum/labs/environment-lanes.md).
3. Use the semester maps as the default teaching sequence.
4. Tailor tracks, capstones, and validation depth to your institution.

### Enterprise teams

1. Use Semester 1 as the baseline operator onboarding path.
2. Use Semester 2 for governance, production, security, and detached-work surfaces.
3. Route staff into the relevant specialization tracks based on operational ownership.

## Current Status

This repository is in active build-out. The backbone now exists, including:

- the curriculum architecture
- weekly semester maps
- full semester teaching guides
- instructor delivery handbook
- detailed core, advanced, and specialization lab guides
- classroom lab manuals and screenshot capture standards
- specialization tracks
- capstone framework
- master and track-specific rubrics
- assessment bank, grading, and practical exam assets
- reusable submission templates for students
- model artifacts for students and instructors
- weekly slide-deck outlines and track workshop deck outlines
- track-specific model answer packs for instructor calibration
- maintenance docs and automated upstream drift detection
- official-source reading map
- independent validation reviews
- native Elite Mentor OS plugin package for Claude Code and Codex
- project-local mentor state and OpenClaw proof-pack mapping

The next major phase is iteration and refinement:

- test plugin loading in Claude Code and Codex
- run adversarial validation against the new plugin layer
- populate the classroom manuals with locally captured reference screenshots
- add cohort-tested timing adjustments and pacing evidence
- build optional presentation-ready slide files from the current outlines
- continue updating against OpenClaw release drift

## Quality Rules

- Every module should state outcomes, prerequisites, theory, labs, failure modes, and security implications.
- Every production or security claim should be traceable to a source category in the validation register.
- Preview, internal-preview, and source-build-only topics must be labeled explicitly.
- Automation, hooks, standing orders, sub-agents, ACP agents, and detached task auditability are first-class OpenClaw topics.
- Formal verification and threat-model artifacts must be taught with explicit maturity labels when they are draft or bounded models.
- The OpenClaw trust model must never be misrepresented as a hostile multi-tenant boundary.

## License

This repository is released under the [MIT License](LICENSE).
