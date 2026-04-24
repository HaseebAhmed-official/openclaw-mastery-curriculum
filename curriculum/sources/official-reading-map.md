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

### Current advisory exemplars reviewed at the 2026-04-24 baseline

- [GHSA-93rg-2xm5-2p9v](https://github.com/openclaw/openclaw/security/advisories/GHSA-93rg-2xm5-2p9v) - Gateway Control UI bootstrap config required Gateway auth
- [GHSA-55cf-xx38-4p9p](https://github.com/openclaw/openclaw/security/advisories/GHSA-55cf-xx38-4p9p) - Workspace dotenv files cannot override connector endpoint hosts
- [GHSA-x3h8-jrgh-p8jx](https://github.com/openclaw/openclaw/security/advisories/GHSA-x3h8-jrgh-p8jx) - Exec allowlist analysis rejects shell expansion in unquoted heredocs
- [GHSA-r6xh-pqhr-v4xh](https://github.com/openclaw/openclaw/security/advisories/GHSA-r6xh-pqhr-v4xh) - MCP loopback owner context is derived from server-issued bearer tokens
- [GHSA-q3jj-46pq-826r](https://github.com/openclaw/openclaw/security/advisories/GHSA-q3jj-46pq-826r) - ACP child sessions inherit subagent security envelope constraints
- [GHSA-wppj-c6mr-83jj](https://github.com/openclaw/openclaw/security/advisories/GHSA-wppj-c6mr-83jj) - OpenShell FS bridge writes stay pinned to the sandbox mount root

## OpenClaw extensibility

- [Plugins](https://docs.openclaw.ai/plugins)
- [Plugin Manifest](https://docs.openclaw.ai/plugins/manifest)
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

## OpenClaw maintenance and release discipline

- [Updating](https://docs.openclaw.ai/install/updating)
- [Release Channels](https://docs.openclaw.ai/install/development-channels)
- [Releases](https://github.com/openclaw/openclaw/releases)

## Prerequisite technologies

- [Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install)
- [Node.js Learn](https://nodejs.org/en/learn)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro)
- [Docker Get Started](https://docs.docker.com/get-started/)
- [Tailscale Serve](https://tailscale.com/docs/features/tailscale-serve)
- [Git documentation](https://git-scm.com/docs)
- [JSON Schema docs](https://json-schema.org/docs)
- [OWASP Prompt Injection](https://owasp.org/www-community/attacks/PromptInjection)
