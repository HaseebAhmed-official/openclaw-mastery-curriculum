# Official Reading Map

## OpenClaw core

- [OpenClaw overview](https://docs.openclaw.ai/)
- [Getting Started](https://docs.openclaw.ai/start/getting-started)
- [Onboarding Overview](https://docs.openclaw.ai/start/onboarding-overview)
- [Gateway Architecture](https://docs.openclaw.ai/concepts/architecture)
- [Control UI](https://docs.openclaw.ai/web/control-ui)
- [Configuration Reference](https://docs.openclaw.ai/gateway/configuration-reference)

## OpenClaw operations

- [Windows](https://docs.openclaw.ai/windows)
- [Docker](https://docs.openclaw.ai/install/docker)
- [Remote Access](https://docs.openclaw.ai/gateway/remote)
- [Tailscale](https://docs.openclaw.ai/gateway/tailscale)
- [Doctor](https://docs.openclaw.ai/doctor)
- [General Troubleshooting](https://docs.openclaw.ai/help/troubleshooting)
- [Status CLI](https://docs.openclaw.ai/cli/status)

## OpenClaw agent behavior

- [Memory Overview](https://docs.openclaw.ai/concepts/memory)
- [Dreaming](https://docs.openclaw.ai/concepts/memory#dreaming)
- [Sessions CLI](https://docs.openclaw.ai/cli/sessions)
- [Model Provider Quickstart](https://docs.openclaw.ai/providers/models)
- [Models CLI](https://docs.openclaw.ai/models)
- [Channels CLI](https://docs.openclaw.ai/cli/channels)
- [Nodes](https://docs.openclaw.ai/nodes)
- [Talk Mode](https://docs.openclaw.ai/nodes/talk)
- [Voice Wake](https://docs.openclaw.ai/nodes/voicewake)
- [Multi-Agent Routing](https://docs.openclaw.ai/multi-agent)
- [SOUL.md Personality Guide](https://docs.openclaw.ai/concepts/soul)

## OpenClaw security and controls

- [Security](https://docs.openclaw.ai/security)
- [Security Advisories](https://github.com/openclaw/openclaw/security/advisories)
- [Sandboxing](https://docs.openclaw.ai/sandboxing)
- [Exec Tool](https://docs.openclaw.ai/tools/exec)
- [Exec Approvals](https://docs.openclaw.ai/tools/exec-approvals)
- [Approvals CLI](https://docs.openclaw.ai/cli/approvals)
- [Security CLI](https://docs.openclaw.ai/cli/security)
- [Trusted Proxy Auth](https://docs.openclaw.ai/gateway/trusted-proxy-auth)
- [Threat Model (MITRE ATLAS)](https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS)
- [Formal Verification](https://docs.openclaw.ai/security/formal-verification/)

### Current advisory families reviewed at the 2026-08-13 baseline

The official feed published 112 advisories after the previous 2026-04-24 cutoff. Do not turn that feed into a memorization list. Use these representative cases to teach recurring boundary failures, then require learners to query the current feed for the component they are assessing:

- [GHSA-xww8-gqvh-92x9](https://github.com/openclaw/openclaw/security/advisories/GHSA-xww8-gqvh-92x9) - approval-display truncation and human decision integrity
- [GHSA-3fp5-v549-9v66](https://github.com/openclaw/openclaw/security/advisories/GHSA-3fp5-v549-9v66) - durable exec approval binding through command wrappers
- [GHSA-7vrr-rp4x-4g76](https://github.com/openclaw/openclaw/security/advisories/GHSA-7vrr-rp4x-4g76) - plugin installation, ownership, and persistence
- [GHSA-v6r2-jh58-xx6w](https://github.com/openclaw/openclaw/security/advisories/GHSA-v6r2-jh58-xx6w) - marketplace metadata and unscanned runtime payloads
- [GHSA-52xj-c9p8-78cv](https://github.com/openclaw/openclaw/security/advisories/GHSA-52xj-c9p8-78cv) - MCP loopback and owner-only tool authority
- [GHSA-mm9g-83wh-mhwj](https://github.com/openclaw/openclaw/security/advisories/GHSA-mm9g-83wh-mhwj) - isolated automation regaining denied exec tools
- [GHSA-575v-8hfq-m3mc](https://github.com/openclaw/openclaw/security/advisories/GHSA-575v-8hfq-m3mc) - sandbox bind-mount containment
- [GHSA-4pqj-3c56-5fqq](https://github.com/openclaw/openclaw/security/advisories/GHSA-4pqj-3c56-5fqq) - workspace dotenv and provider-credential ownership
- [GHSA-x863-pqjw-hmgf](https://github.com/openclaw/openclaw/security/advisories/GHSA-x863-pqjw-hmgf) - browser navigation and current-tab SSRF revalidation
- [GHSA-8f46-3xx3-8c9m](https://github.com/openclaw/openclaw/security/advisories/GHSA-8f46-3xx3-8c9m) - approval equivalence across Gateway and node environments

## OpenClaw extensibility

- [Plugins](https://docs.openclaw.ai/plugins)
- [Manage Plugins](https://docs.openclaw.ai/plugins/manage-plugins)
- [Plugin Manifest](https://docs.openclaw.ai/plugins/manifest)
- [Plugin Inventory](https://docs.openclaw.ai/plugins/plugin-inventory)
- [File Transfer Plugin](https://docs.openclaw.ai/plugins/reference/file-transfer)
- [Skills](https://docs.openclaw.ai/skills)
- [Skills CLI](https://docs.openclaw.ai/cli/skills)
- [ClawHub](https://docs.openclaw.ai/tools/clawhub)

## OpenClaw automation and detached work

- [Automation & Tasks](https://docs.openclaw.ai/automation)
- [Scheduled Tasks](https://docs.openclaw.ai/automation/cron-jobs)
- [Background Tasks](https://docs.openclaw.ai/automation/tasks)
- [Task Flow](https://docs.openclaw.ai/automation/taskflow)
- [Standing Orders](https://docs.openclaw.ai/automation/standing-orders)
- [Hooks](https://docs.openclaw.ai/automation/hooks)
- [Heartbeat](https://docs.openclaw.ai/gateway/heartbeat)
- [Sub-Agents](https://docs.openclaw.ai/tools/subagents)
- [ACP Agents](https://docs.openclaw.ai/tools/acp-agents)
- [Attach CLI](https://docs.openclaw.ai/cli/attach)

## OpenClaw maintenance and release discipline

- [Updating](https://docs.openclaw.ai/install/updating)
- [Release Channels](https://docs.openclaw.ai/install/development-channels)
- [Releases](https://github.com/openclaw/openclaw/releases)
- [OpenClaw 2026.7.1 release notes](https://docs.openclaw.ai/releases/2026.7.1)
- [OpenClaw 2026.7.1-2 correction release](https://github.com/openclaw/openclaw/releases/tag/v2026.7.1-2)
- [OpenClaw 2026.6.34 extended-stable release](https://github.com/openclaw/openclaw/releases/tag/v2026.6.34)

### Current release baseline reviewed at the 2026-08-13 baseline

- stable GitHub/npm release: `v2026.7.1-2` / `openclaw@2026.7.1-2`
- extended-stable npm release: `openclaw@2026.6.34`
- observed beta npm tag: `openclaw@2026.8.1-beta.1`, not a teaching baseline
- Documentation inconsistency to teach explicitly: Install and Getting Started recommend Node 26, while the current Security page still recommends Node 24; the supported minimums agree, but the preferred runtime must be rechecked before teaching
- High-impact teaching surfaces: four-channel release policy, current Node runtime floor, redesigned Control UI/task visibility, session-scoped `openclaw attach`, durable goals and coding-agent delegation, scheduled-work recovery, guarded workspace terminals, plugin correction releases, browser/network hardening, and advisory-driven authorization/approval/sandbox casework
- The full advisory feed was reviewed; representative cases are integrated by failure family rather than copied wholesale into the curriculum

## Prerequisite technologies

- [Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install)
- [Node.js Learn](https://nodejs.org/en/learn)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro)
- [Docker Get Started](https://docs.docker.com/get-started/)
- [Tailscale Serve](https://tailscale.com/docs/features/tailscale-serve)
- [Git documentation](https://git-scm.com/docs)
- [JSON Schema docs](https://json-schema.org/docs)
- [OWASP Prompt Injection](https://owasp.org/www-community/attacks/PromptInjection)
