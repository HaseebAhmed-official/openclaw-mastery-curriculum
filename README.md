# OpenClaw Mastery

This is the master index for a university-grade, enterprise-usable OpenClaw curriculum pack. It is designed to take a learner from prerequisite foundations to production operations, security hardening, extension development, and contributor-level understanding.

## Baseline decisions

- Audience: university-first, but structured so enterprise teams can adopt the same pack
- Delivery model: two-semester core program with advanced tracks
- Learning shape: shared foundation plus role-based specialization
- Language: English
- Canonical lab baseline: WSL2/Linux + VPS + Docker
- Assessment model: project-heavy, with practical labs, design reviews, and track-specific capstones
- Security posture: governance and hardening are mandatory in the main path
- Version stance: stable-release-first, with clearly labeled preview and source-build material
- Release discipline: any provider, security, or automation lab must begin by checking current release notes and update status
- Validation stance: official sources first, validated inference second, community guidance explicitly labeled

## How to use this pack

### If you are a student

1. Start with the [Program Overview](curriculum/program-overview.md).
2. Complete the [Prerequisite Bridge](curriculum/prerequisite-bridge.md).
3. Work through [Semester 1](curriculum/semester-1/index.md) and [Semester 2](curriculum/semester-2/index.md).
4. Pick a role path from [Tracks](curriculum/tracks/index.md).
5. Complete the mapped labs, capstone, and final defense.

### If you are an instructor

1. Read the [Program Overview](curriculum/program-overview.md) and [Assessment Map](curriculum/assessment-map.md).
2. Pick an environment lane from [Environment Lanes](curriculum/labs/environment-lanes.md).
3. Use the semester maps as the default sequence.
4. Tailor the advanced tracks and capstone depth to your institution.

### If you are an enterprise team

1. Use Semester 1 as the operator onboarding baseline.
2. Use the governance, production, and security material from Semester 2.
3. Route advanced staff into the appropriate specialization track.

## Curriculum map

### Core architecture

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

### Specializations

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

### Validation and reading

- [Validation Register](curriculum/sources/validation-register.md)
- [Official Reading Map](curriculum/sources/official-reading-map.md)

## Quality rules for future expansion

- Every module should state outcomes, prerequisites, theory, labs, failure modes, and security implications.
- Every production or security claim should be traceable to a source category in the validation register.
- Preview, internal-preview, and source-build-only topics must be labeled as such.
- Automation, hooks, standing orders, sub-agents, ACP agents, and detached task auditability are first-class OpenClaw topics, not electives.
- Formal verification and threat-model artifacts must be taught with explicit maturity labels when they are draft or bounded models.
- The trust model must never be hidden: OpenClaw is a personal-assistant trust model by default, not a hostile multi-tenant platform.
