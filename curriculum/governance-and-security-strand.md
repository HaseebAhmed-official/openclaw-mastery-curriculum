# Governance and Security Strand

## Why this strand is mandatory

OpenClaw is valuable because it can connect models to channels, tools, nodes, and hosts. The exact same capabilities also create risk. Security is therefore not a side chapter; it is the spine of responsible OpenClaw use.

## Threaded topics across the full program

### Stage 1: trust model literacy

- personal-assistant trust model
- one trusted operator boundary per gateway
- why hostile multi-tenant assumptions are wrong here

### Stage 2: ingress and channel control

- pairing and allowlists
- DM scope and shared inbox isolation
- mention gating and group policies

### Stage 3: tool and host control

- tool policy
- sandboxing
- exec approvals
- node-host command exposure

### Stage 4: external content risk

- prompt injection
- web content, hooks, Gmail, and document ingestion
- unsafe bypass flags and why they should stay off in production

### Stage 5: deployment governance

- loopback-first design
- SSH and Tailscale patterns
- trusted proxy auth risks
- webhook ingress and token hygiene
- secret and config handling

### Stage 6: automation and detached authority

- standing orders as durable authority
- hooks as event-driven code execution
- task records and detached auditability
- sub-agents and ACP agents as coordination boundaries

### Stage 7: formal assurance and threat models

- security audit usage
- ATLAS-based threat modeling
- formal verification models and their limits

## Required learner behaviors

- start from smallest access that still works
- document every widening of trust or exposure
- justify every dangerous capability
- keep experimental and production profiles separate
- treat unofficial or third-party content as untrusted by default
- require explicit review for webhook tokens, hook code, plugin install records, and durable standing authority

## Required instructor checks

- challenge unsafe defaults in design reviews
- fail projects that treat one shared gateway as an adversarial-user boundary
- require learners to explain the limits of sandboxing
- require learners to explain the limits of formal verification claims
- require learners to address prompt injection, detached authority, and webhook ingress in any production-facing design
