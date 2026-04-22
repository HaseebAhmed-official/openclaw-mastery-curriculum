# Validation Register

## Validation categories

- `official-docs`: official OpenClaw documentation
- `official-repo`: official GitHub repository content, release notes, manifests, or code-adjacent docs
- `official-ecosystem`: official docs for prerequisite technologies such as Node.js, Docker, Microsoft WSL, Tailscale, Git, JSON Schema, and OWASP
- `validated-inference`: conclusions drawn from multiple primary sources
- `community-derived`: useful but non-authoritative material

## Curriculum claims and source status

| Domain | Claim | Status | Primary sources |
| --- | --- | --- | --- |
| Install baseline | OpenClaw recommends Node 24 and supports Node 22.14+ | official-docs | Getting Started |
| Windows baseline | WSL2 is the recommended Windows path for the full experience | official-docs | Windows, Getting Started |
| Architecture | The gateway is the long-lived owner of messaging surfaces and control-plane APIs | official-docs | Gateway Architecture |
| Trust model | OpenClaw is designed around one trusted operator boundary per gateway | official-docs | Security |
| Security posture | OpenClaw should not be taught as hostile multi-tenant isolation on one shared gateway | official-docs | Security |
| Memory model | Memory is persisted in markdown files in the agent workspace; there is no hidden memory state | official-docs | Memory Overview |
| Dreaming | `DREAMS.md` and dreaming are real, optional background memory-promotion surfaces and should be taught as such | official-docs | Memory Overview |
| Sandboxing | Docker-based sandboxing reduces blast radius but is not a perfect security boundary | official-docs | Sandboxing |
| Remote access | Loopback plus SSH or Tailscale Serve is the safer default remote-access pattern | official-docs | Remote Access, Tailscale |
| Channels | Telegram is one of the fastest beginner channel paths; WhatsApp is production-ready via WhatsApp Web plugin | official-docs | OpenClaw overview, WhatsApp |
| Skills | Skills load from six documented layers with explicit precedence rules and workspace-level override power | official-docs | Skills |
| Plugins | Plugins extend channels, providers, tools, and skills, and native plugins require `openclaw.plugin.json` | official-docs | Plugins, Plugin Manifest |
| Multi-agent workspaces | Per-agent workspaces include `SOUL.md`, `AGENTS.md`, and optional `USER.md` alongside isolated state and sessions | official-docs | Multi-Agent Routing |
| Approvals | Host exec must be governed by tool policy plus approvals/allowlists when enabled | official-docs | Exec Tool, Exec Approvals, Approvals CLI |
| Diagnostics | `doctor`, `status`, `gateway probe`, and `security audit` form the operational debugging backbone | official-docs | Doctor, Troubleshooting, Security CLI |
| Automation | Cron, tasks, task flow, hooks, standing orders, heartbeat, sub-agents, and ACP agents are core OpenClaw execution surfaces | official-docs | Automation & Tasks, Sub-Agents, ACP Agents |
| Updates | Teaching materials should account for update channels, dry runs, pinning, and rollback when behavior can drift across releases | official-docs | Updating, Release Channels |
| Formal assurance | OpenClaw has formal security models, but they are bounded models rather than proof of total implementation security | official-docs | Formal Verification |
| Security curriculum requirement | Governance and hardening must be first-class teaching material | validated-inference | Security, Exec Approvals, Sandboxing, Threat Model |

## Freshness target

- baseline date: April 22, 2026
- teaching baseline: stable-release behavior
- preview or source-build material: must be labeled in module notes and capstone expectations

## Usage rule

Any future file added to this pack should reference one of the categories above when making a platform claim.
