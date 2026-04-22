# Lab Catalog

## Phase A: bridge labs

### LAB-A1: WSL2 or Linux verification

- focus: environment readiness
- output: verified shell, package manager, filesystem, and editor workflow

### LAB-A2: Git discipline drill

- focus: branching, diffing, commit hygiene
- output: clean branch workflow and review notes

### LAB-A3: Node.js and JSON config drill

- focus: runtime verification and config literacy
- output: valid config edits and schema reasoning

### LAB-A4: Docker and localhost basics

- focus: containers, ports, and isolation
- output: working container demo and explanation of host vs container network

## Phase B: OpenClaw core labs

### LAB-B1: OpenClaw install and onboard

- focus: install, provider auth, daemon setup
- output: working OpenClaw installation

### LAB-B2: Control UI and diagnostics ladder

- focus: dashboard, `status`, `doctor`, `gateway probe`
- required commands: `openclaw status`, `openclaw doctor`, `openclaw gateway probe`, `openclaw gateway status`, `openclaw channels status --probe`, `openclaw logs --follow`
- output: diagnostic report with a fault-isolation ladder
- evidence: one healthy run and one intentionally broken scenario

### LAB-B3: Session and memory inspection

- focus: workspace, `MEMORY.md`, daily notes, session behavior
- output: memory/session observation sheet

### LAB-B4: Provider and model selection

- focus: auth, model defaults, fallback awareness, release-note drift, and cost/rate-limit awareness
- output: configured model baseline, rationale, and release-aware note documenting the current default assumptions

### LAB-B5: Sandbox and exec policy

- focus: sandboxing, exec settings, approval behavior
- output: safety policy note with one misconfiguration and one mitigation

### LAB-B6: Channel onboarding

- focus: Telegram or WhatsApp setup with safe access policy
- output: working channel and documented policy

### LAB-B7: Remote access baseline

- focus: SSH tunnel or Tailscale Serve path
- output: remote access runbook

## Phase C: production and governance labs

### LAB-C1: Multi-agent isolation design

- focus: workspaces, sessions, auth profiles, isolation, `SOUL.md`, `AGENTS.md`, and `USER.md`
- output: isolation architecture note plus two differentiated agent workspace definitions

### LAB-C2: Security audit and remediation

- focus: `openclaw security audit`, webhook findings, plugin and hook install records, and JSON export
- output: audit findings, remediation plan, and machine-readable audit artifact using `--json`

### LAB-C3: Trusted proxy and ingress review

- focus: reverse proxy assumptions and failure modes
- output: deployment risk review

### LAB-C4: Shared inbox policy lab

- focus: dmScope and shared control risk
- output: routing policy recommendation

### LAB-C5: Threat model workshop

- focus: ATLAS-style threat analysis
- output: threat register

### LAB-C6: Automation and standing-orders design

- focus: cron, heartbeat, task flow, standing orders, and hooks
- output: detached-work design note choosing the correct primitive for multiple scenarios

### LAB-C7: Sub-agent and ACP auditability lab

- focus: sub-agents, ACP agents, background task records, and delegated-work ownership
- output: detached-task audit report

## Phase D: specialization labs

### LAB-D1: Plugin manifest inspection

- focus: `openclaw.plugin.json`, plugin bundles, schema-driven validation, and install/update behavior
- output: manifest review

### LAB-D2: Skills precedence and install flow

- focus: all six skill-precedence layers: extra dirs, bundled, managed/local, personal-agent, project-agent, and workspace
- output: skill precedence map with a name-collision resolution exercise

### LAB-D3: Headless node design

- focus: node-host command surface and approvals
- output: distributed execution design

### LAB-D4: Local-model tradeoff lab

- focus: cost, quality, latency, and fallback strategy
- output: comparative design memo

### LAB-D5: Contributor toolchain orientation

- focus: `pnpm check:changed`, `pnpm test:changed`, scoped `AGENTS.md`, and contributor-safe workflow
- output: contributor workflow checklist

## Suggested minimum lab set by program type

### Semester-only university run

- LAB-A1 to LAB-A4
- LAB-B1 to LAB-B7
- LAB-C1 to LAB-C3

### Full expert program

- all labs

### Enterprise onboarding adaptation

- LAB-B1, B2, B4, B5, B7
- LAB-C1, C2, C3, C4
