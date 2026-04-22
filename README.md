# OpenClaw Mastery Curriculum

[![License](https://img.shields.io/github/license/HaseebAhmed-official/openclaw-mastery-curriculum)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/HaseebAhmed-official/openclaw-mastery-curriculum)](https://github.com/HaseebAhmed-official/openclaw-mastery-curriculum/commits/main)
[![Repo Size](https://img.shields.io/github/repo-size/HaseebAhmed-official/openclaw-mastery-curriculum)](https://github.com/HaseebAhmed-official/openclaw-mastery-curriculum)

This repository is a university-grade, enterprise-usable **OpenClaw mastery curriculum** designed to take a learner from prerequisite foundations to production operations, security hardening, extension development, and contributor-level understanding.

It is not just a reading list. It is a structured curriculum system with:

- a prerequisite bridge for beginners
- a two-semester core program
- advanced role-based tracks
- hands-on lab architecture
- capstones and rubrics
- source-backed validation artifacts

## Vision

The goal is to build one of the strongest publicly available learning systems for OpenClaw:

- technically accurate
- security-realistic
- production-aware
- pedagogically structured
- reusable by universities, instructors, and enterprise teams

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

### Core program

- [Program Overview](curriculum/program-overview.md)
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
- [Lab Authoring Standard](curriculum/labs/lab-authoring-standard.md)
- [Lab Catalog](curriculum/labs/lab-catalog.md)
- [Environment Lanes](curriculum/labs/environment-lanes.md)
- [Capstones Index](curriculum/capstones/index.md)
- [Capstone Specs](curriculum/capstones/capstone-specs.md)
- [Rubrics Index](curriculum/rubrics/index.md)
- [Master Rubric](curriculum/rubrics/master-rubric.md)

### Validation and evidence

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
- specialization tracks
- lab catalog and environment lanes
- capstone framework
- master rubric
- official-source reading map
- independent validation reviews

The next major phase is deeper execution quality:

- full runnable lab guides
- instructor notes and teaching packets
- track-specific scoring rubrics
- challenge banks and certification-grade assessments

## Quality Rules

- Every module should state outcomes, prerequisites, theory, labs, failure modes, and security implications.
- Every production or security claim should be traceable to a source category in the validation register.
- Preview, internal-preview, and source-build-only topics must be labeled explicitly.
- Automation, hooks, standing orders, sub-agents, ACP agents, and detached task auditability are first-class OpenClaw topics.
- Formal verification and threat-model artifacts must be taught with explicit maturity labels when they are draft or bounded models.
- The OpenClaw trust model must never be misrepresented as a hostile multi-tenant boundary.

## License

This repository is released under the [MIT License](LICENSE).
