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
| Install baseline | OpenClaw requires Node 22.22.3+, 24.15+, or 25.9+; Install/Getting Started recommend Node 26 while the current Security page still says Node 24, so the recommendation is documented drift rather than a settled claim | official-docs | Install, Getting Started, Security |
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
| Security maintenance | Current official OpenClaw advisories should be treated as first-class teaching inputs for security and production modules | official-repo | Security Advisories |
| Automation | Cron, tasks, task flow, hooks, standing orders, heartbeat, sub-agents, and ACP agents are core OpenClaw execution surfaces | official-docs | Automation & Tasks, Sub-Agents, ACP Agents |
| Updates | Teaching materials should account for update channels, dry runs, pinning, and rollback when behavior can drift across releases | official-docs | Updating, Release Channels |
| Updates | `openclaw update` should be taught with dry-run, JSON/status inspection, channel semantics, `doctor`, restart, health verification, rollback, and correction-release awareness | official-docs/official-repo | Updating, Release `v2026.7.1-2` |
| Release channels | Stable, package-only extended-stable, beta, and dev have different fallback, update, and production semantics; npm dist-tags are authoritative for package installs | official-docs | Release Channels, Updating |
| Connected coding agents | `openclaw attach` grants Claude Code temporary, session-scoped Gateway access and revokes normal-launch grants on exit | official-docs/official-repo | Attach CLI, Release `v2026.7.1` |
| Durable work | Sessions, goals, tasks, coding-agent delegation, and heartbeat/cron recovery are release-sensitive operational surfaces that require audit evidence | official-docs/official-repo | Release `v2026.7.1`, Tasks, Automation |
| Workspace terminals | Guarded workspace terminals are authenticated administrative capability surfaces, can be disabled by policy, and must not be taught as ordinary chat UI | official-docs/official-repo | Release `v2026.7.1`, Control UI |
| Advisory case method | Current advisories should be grouped into recurring failure families such as authorization provenance, approval equivalence, plugin persistence, sandbox/SSRF containment, credential ownership, and detached-authority inheritance | official-repo/validated-inference | Security Advisories reviewed through 2026-06-30 |
| Plugin lifecycle | Plugin install, update, uninstall, runtime inspect, dependency status, ClawHub/npm source choice, and official externalized plugin repair are required mastery topics | official-docs/official-repo | Manage Plugins, Release `v2026.5.3` |
| File transfer | The official file-transfer plugin introduces node file fetch/list/write capabilities with policy and size boundaries that belong in plugin/security teaching | official-docs/official-repo | File Transfer Plugin, Release `v2026.5.3` |
| Channel streaming | Streaming progress drafts and channel-specific delivery behavior can affect learner expectations and evidence collection | official-docs/official-repo | Release `v2026.5.3`, channel docs |
| Command steering | `/steer` and `/side` are current command surfaces for queue-independent steering and side questions, so advanced operator training should label them as current release behavior | official-repo | Release `v2026.5.3` |
| Config safety | Invalid config now fails closed in current release notes; `doctor --fix` owns safe repair/migration workflows | official-repo | Release `v2026.5.3` |
| Formal assurance | OpenClaw has formal security models, but they are bounded models rather than proof of total implementation security | official-docs | Formal Verification |
| Security curriculum requirement | Governance and hardening must be first-class teaching material | validated-inference | Security, Exec Approvals, Sandboxing, Threat Model |

## Freshness target

- baseline date: August 13, 2026
- reviewed stable baseline: OpenClaw `v2026.7.1-2` / `openclaw@2026.7.1-2`
- reviewed extended-stable baseline: `openclaw@2026.6.34`
- observed beta tag: `openclaw@2026.8.1-beta.1`, not a teaching baseline
- reviewed advisory publication cutoff: June 30, 2026
- teaching baseline: stable-release behavior
- preview or source-build material: must be labeled in module notes and capstone expectations

## Usage rule

Any future file added to this pack should reference one of the categories above when making a platform claim.
