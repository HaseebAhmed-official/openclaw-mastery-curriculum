# Production / DevOps Track

## Goal

Produce engineers who can design and operate OpenClaw as a persistent service with explicit trust boundaries, secure ingress, diagnostics, and change management.

## Best fit for

- DevOps engineers
- platform engineers
- SRE-minded operators

## Additional emphasis

- WSL2/Linux and VPS operations
- SSH tunnels, Tailscale Serve, and reverse-proxy patterns
- security audit and hardening loops
- Docker usage for sandboxing and packaging choices
- webhook ingress, task auditability, update channels, rollback, and recovery
- `openclaw update --dry-run`, `--json`, update status, npm hotfix awareness, `doctor`, restart, and health verification
- externalized official plugin repair and runtime-load verification after updates
- operational runbooks and environment lanes

## Extra labs

- VPS deployment lab
- trusted proxy risk review
- update and rollback governance exercise
- package-vs-GitHub release drift exercise
- webhook and detached-task audit exercise
- operational rollback exercise

## Capstone

Design and implement a persistent OpenClaw deployment with documented ingress, authentication, hardening, webhook and detached-work controls, backup, update strategy, plugin repair/runtime verification, package-channel policy, and incident-response decisions.
