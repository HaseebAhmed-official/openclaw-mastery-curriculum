# Program Overview

## Mission

Build learners who can understand, operate, secure, extend, and evaluate OpenClaw at an expert level, while staying grounded in how the platform actually works today.

This curriculum is not just "how to use a bot." It is a structured path through:

- systems and operator foundations
- OpenClaw architecture and trust model
- hands-on deployment and troubleshooting
- durable automation, detached work, and authority boundaries
- production operations and governance
- extension and plugin development
- contributor-level understanding of the platform

## Design principles

### 1. Stable-first, reality-based

Required teaching material should track stable OpenClaw behavior. Preview and source-build topics are included, but they must be labeled clearly so institutions do not mistake them for universal baseline requirements.

Release-sensitive modules must also teach learners how to check current release notes, update channels, and current defaults before they trust old screenshots or old lab answers.

### 2. Security is part of the core, not an elective

OpenClaw is powerful because it can touch real tools, real channels, and real hosts. That means threat modeling, approvals, hardening, and deployment boundaries are core literacy.

### 3. Theory and practice move together

Every important concept should be paired with a hands-on exercise, an operational review, or a debugging scenario.

This is especially important for detached execution features like cron, tasks, hooks, standing orders, sub-agents, and ACP agents because they change authority, auditability, and failure modes.

### 4. Reusable by different institutions

The curriculum is modular so a university, bootcamp, or enterprise team can adapt it without rewriting the whole program.

### 5. Source-backed instruction

Official docs and repo materials are the primary source of truth. Inferences and community knowledge are allowed, but they must be marked separately.

## Audience model

### Primary audience

- university students
- instructors building an AI systems, agent engineering, or platform operations course

### Secondary audience

- power users and operators
- platform / DevOps engineers
- AI safety and security engineers
- plugin authors
- contributors to the OpenClaw ecosystem

## Entry assumptions

This program is designed so a learner can start near zero, but not below basic computer use.

The curriculum therefore includes a bridge in:

- terminal and filesystem literacy
- Linux and WSL2 basics
- Git and GitHub workflow
- Node.js and package management
- TypeScript and JSON config literacy
- Docker and container basics
- networking, SSH, port forwarding, and tailnet concepts
- LLM and tool-use fundamentals
- security fundamentals for agentic systems

## Delivery architecture

### Semester 1: foundations and safe operation

Learners build the baseline needed to understand how OpenClaw works, how to install and operate it, and how to reason about tools, sessions, memory, channels, and nodes without drifting into unsafe habits.

### Semester 2: production, security, and expert paths

Learners move from competent operation to production readiness, governance, extensibility, distributed execution, and contributor-level reasoning.

## Canonical technical baseline

- Windows learners should prefer WSL2 for the full experience because OpenClaw's own docs recommend it as the more stable path.
- The canonical deployment progression is local WSL2/Linux -> loopback-only gateway -> remote access over SSH/Tailscale -> VPS deployment -> advanced reverse-proxy or multi-agent setups.
- Docker is taught as both an optional gateway packaging method and as the mechanism behind sandboxing.

## Learning outcomes

By the end of the full program, learners should be able to:

- explain the OpenClaw gateway architecture, control-plane model, and node model
- install, onboard, validate, and troubleshoot OpenClaw on supported environments
- choose and configure model providers, fallbacks, and operational defaults
- check release notes, update channels, and default changes before running provider or security-sensitive labs
- reason about sessions, memory, workspace state, and multi-agent isolation
- explain detached work surfaces including cron, tasks, hooks, standing orders, heartbeat, sub-agents, and ACP agents
- apply tool policy, sandboxing, and exec approvals safely
- deploy remote or persistent gateway setups with appropriate security boundaries
- reason about webhook ingress, delivery modes, audit records, and release/rollback policy
- evaluate risk in channels, hooks, remote control, and shared inbox designs
- build and validate plugins, skills, or contributor-level changes
- defend a production-ready OpenClaw design using explicit trust, security, and operational arguments

## Required supporting artifacts

This program depends on the following companion documents:

- [Instructor Handbook](instructor-handbook.md)
- [Prerequisite Bridge](prerequisite-bridge.md)
- [Competency Framework](competency-framework.md)
- [Assessment Map](assessment-map.md)
- [Assessment Assets](assessment/index.md)
- [Governance and Security Strand](governance-and-security-strand.md)
- [Automation and Detached Work](automation-and-detached-work.md)
- [Update and Release Discipline](update-and-release-discipline.md)
- [Semester 1](semester-1/index.md)
- [Semester 2](semester-2/index.md)

## What this curriculum will not pretend

- It will not treat OpenClaw as a multi-tenant hostile isolation system when the official docs explicitly do not.
- It will not flatten preview and source-build topics into fake baseline requirements.
- It will not separate "security" from "usage" as if agent systems remain safe that way.
- It will not teach fast-moving defaults as timeless facts without anchoring them to a validation date and release channel.
