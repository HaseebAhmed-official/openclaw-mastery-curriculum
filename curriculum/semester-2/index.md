# Semester 2

## Goal

Move learners from competent baseline operation to production-grade reasoning, security maturity, extensibility, and specialization.

By the end of Semester 2, a learner should be able to design and defend an OpenClaw deployment architecture, harden it within the documented trust model, reason about advanced integrations, and complete a role-specific capstone.

## Weekly sequence

| Week | Theme | Core outcomes | Hands-on focus | Assessment |
| --- | --- | --- | --- | --- |
| 1 | Production framing | Translate baseline setups into production design questions | Production gap analysis | Readiness memo |
| 2 | Multi-agent routing and workspace identity files | Explain agent isolation, session stores, `SOUL.md`, `AGENTS.md`, `USER.md`, and workspace boundaries | Multi-agent design lab with differentiated agent files | Isolation review |
| 3 | Configuration architecture | Navigate config schema, plugin-owned config, and control-plane settings | Schema and config drill | Config review |
| 4 | Security audit, advisories, webhook ingress, and hardening | Use `openclaw security audit`, interpret findings, review current official advisories, review webhook risks, and prioritize fixes | Audit lab with JSON export and remediation plan | Hardening worksheet |
| 5 | Exec approvals and host authority | Explain host execution, approvals, allowlists, and node-host controls | Approval policy lab | Policy defense |
| 6 | Remote access and proxy patterns | Compare SSH, Tailscale Serve, and trusted proxy auth | Proxy and remote lab | Deployment review |
| 7 | Shared inboxes and DM scope | Reason about cooperative vs adversarial usage and session isolation | Shared-inbox design lab | Routing critique |
| 8 | Plugins, bundles, ClawHub, and supply-chain controls | Understand plugin system, manifests, bundles, install/update behavior, schemas, and capability ownership | Manifest and plugin-install risk lab | Midterm practical 2 |
| 9 | Skills, ClawHub, and six-layer precedence | Understand all six skill-precedence layers, install flows, and workspace vs shared skills | Skill installation and collision lab | Skill policy check |
| 10 | Automation, hooks, heartbeat, and standing orders | Choose the right detached-work primitive and reason about durable authority | Automation and standing-orders lab | Automation design review |
| 11 | Sub-agents, ACP agents, headless nodes, and task auditability | Explain delegated and detached execution surfaces and inspect their task records | Distributed execution and task-audit lab | Distributed execution review |
| 12 | Memory strategy, Dreaming, and advanced knowledge layers | Compare default memory, memory wiki, search/indexing choices, `DREAMS.md`, and dreaming thresholds | Memory strategy and dreaming lab | Memory architecture note |
| 13 | Threat modeling, draft artifacts, and formal verification limits | Use ATLAS threat modeling, label draft maturity correctly, and understand bounded formal-model limits | Threat model workshop | Threat report |
| 14 | Contributor and ecosystem literacy | Understand repo contribution, pnpm-based toolchain, scoped `AGENTS.md`, docs validation, and community interfaces | Contribution plan lab | Contribution proposal |
| 15 | Track capstone sprint | Build the selected track artifact | Capstone build | Milestone review |
| 16 | Final defense | Defend technical and security choices | Capstone demo and viva | Final capstone |

## Required Semester 2 deliverables

- one production architecture document
- one security audit and hardening report
- one detached-work or webhook risk review
- one policy review for approvals, channels, or remote access
- one extension, design artifact, or contributor proposal
- one track-specific capstone and defense

## Core readings

- multi-agent routing
- configuration reference
- security guide and audit docs
- current official security advisories
- sandboxing and exec approvals
- remote access, Tailscale, and trusted proxy auth
- automation, tasks, cron, hooks, standing orders, heartbeat, sub-agents, and ACP agents
- plugins and plugin manifest
- skills and skills CLI
- formal verification and threat model docs, labeled for maturity
- updating and release channels

See the [Official Reading Map](../sources/official-reading-map.md) for the exact links.

## Teaching support

- [Semester 2 Teaching Guide](teaching-guide.md)
- [Advanced Lab Guides](../labs/advanced-lab-guides.md)
- [Specialization Lab Guides](../labs/specialization-lab-guides.md)
- [Question Bank](../assessment/question-bank.md)
- [Oral Defense Bank](../assessment/oral-defense-bank.md)
