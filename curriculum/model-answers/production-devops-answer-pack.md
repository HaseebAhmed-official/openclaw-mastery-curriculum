# Production / DevOps Answer Pack

## Target standard

This track should produce a bounded, defensible service design with explicit ingress, auth, update, and rollback reasoning.

## Model capstone answer shape

1. Define trust boundary, operator set, intended ingress path, and environment ownership.
2. Present the chosen architecture: local, VPS, Docker, SSH, Tailscale Serve, or trusted-proxy pattern.
3. Explain authentication and exposure controls: gateway auth mode, firewalling, origin policy, proxy-only path if relevant.
4. Show operational controls: backup, update process, rollback path, logs, audit artifacts, maintenance cadence.
5. Address detached authority: webhooks, automation, hooks, task auditability, and incident-response expectations.

## Strong evidence bundle

- architecture diagram
- ingress decision record
- security audit artifact with manual follow-up actions
- update and rollback runbook
- incident-response outline

## Strong-answer signals

- explicitly rejects public exposure when not justified
- distinguishes what `security audit --fix` can do from what operators must still review
- documents why a proxy pattern is accepted or rejected
- shows rollback thinking before the first production update

## Weak-answer signals

- reverse proxy chosen with no proxy-only path or origin reasoning
- no backup or rollback story
- no account of detached work or webhook risk
- production claims based only on persistence, not governance

## Oral defense prompts

- Why is SSH or Tailscale Serve better than public exposure here?
- What remains manual after a clean audit run?
- What would force you to split this deployment into separate trust boundaries?
