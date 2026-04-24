# Track Workshop Slide Outlines

## How to use these workshops

Use these decks after the shared semesters and before final capstone defense. Each workshop is designed as a focused seminar that brings one track to its expert ceiling.

## Operator workshop

- Opening scenario: the assistant works, but daily operation is noisy and undocumented
- Focus slides: channels, diagnostics, release drift checks, runbook quality, incident triage
- Demo: daily operator health review
- Discussion: what separates a power user from a reliable operator
- Artifact bridge: operator capstone runbook and support model

## Production / DevOps workshop

- Opening scenario: persistent deployment with explicit ingress and rollback requirements
- Focus slides: environment lanes, auth placement, SSH vs Tailscale vs trusted-proxy, backups, updates
- Demo: deployment review board
- Discussion: what counts as operational evidence
- Artifact bridge: production architecture and incident-response package

## Security / Hardening workshop

- Opening scenario: a deployment looks functional but hides trust and exposure mistakes
- Focus slides: trust model, prompt injection, unsafe external content, sandboxing, advisories, audit interpretation
- Demo: security assessment walkthrough
- Discussion: what the docs do and do not claim
- Artifact bridge: full hardening assessment and defended recommendations

## Plugin Developer workshop

- Opening scenario: the plugin works locally but has weak governance and compatibility assumptions
- Focus slides: manifest design, schema validation, install/update behavior, precedence, compatibility notes
- Demo: plugin review board
- Discussion: capability ownership and config surface discipline
- Artifact bridge: plugin package and validation plan

## Contributor / Core workshop

- Opening scenario: a learner found an issue but cannot yet propose a safe repo-level change
- Focus slides: architecture tracing, changed-scope validation, docs-code consistency, scoped contributor guidance
- Demo: contribution-plan review
- Discussion: what makes a patch plan credible before code exists
- Artifact bridge: contributor proposal or design artifact

## Local Models workshop

- Opening scenario: a team wants sovereignty but underestimates hardware, quality, and safety tradeoffs
- Focus slides: hardware assumptions, fallback design, weak-model risk, latency, operational burden
- Demo: hosted vs hybrid vs local decision board
- Discussion: when local control is worth the cost
- Artifact bridge: local or hybrid architecture memo

## Cross-track capstone defense workshop

- Opening scenario: a working project meets resistance from a skeptical review panel
- Focus slides: claim, evidence, limitation, tradeoff, residual risk
- Demo: short defense followed by rebuttal
- Discussion: what weakens credibility fastest
- Artifact bridge: final demo script and oral defense note
