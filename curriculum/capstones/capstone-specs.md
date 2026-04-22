# Capstone Specs

## Operator capstone

- artifact: deploy a practical assistant workflow
- required elements: onboarding path, safe channel policy, memory/session strategy, operator runbook, troubleshooting section
- defense question: why is this safe enough for its audience?

## Production / DevOps capstone

- artifact: persistent deployment architecture
- required elements: host choice, remote access pattern, auth mode, hardening controls, webhook and detached-work policy, rollback plan, update-channel strategy, change-management note
- defense question: why is this deployment operationally durable and appropriately exposed?

## Security / Hardening capstone

- artifact: full security review
- required elements: trust model statement, threat model, audit findings, risky assumptions, webhook and automation risk review, compensating controls, residual risk statement
- defense question: what risks remain even after your controls?

## Plugin Developer capstone

- artifact: extension package or plugin design
- required elements: manifest, schema, config shape, user story, validation plan, deployment notes, install/update behavior, compatibility assumptions
- defense question: how does your design avoid becoming an operational footgun?

## Contributor / Core capstone

- artifact: repo-level contribution proposal or implementation artifact
- required elements: architecture understanding, impacted surfaces, tests/docs plan, compatibility note, validation method
- defense question: what part of the system did you intentionally avoid changing, and why?

## Local Models capstone

- artifact: local or hybrid model architecture
- required elements: hardware assumptions, model/provider choice, fallback plan, quality/safety tradeoff analysis, operating cost note, release-aware default-check strategy
- defense question: when should this design be rejected in favor of hosted models?
