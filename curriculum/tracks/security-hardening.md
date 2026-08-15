# Security / Hardening Track

## Goal

Produce practitioners who can evaluate OpenClaw setups against the official trust model, identify risky assumptions, and recommend controls that fit the platform's actual security posture.

## Best fit for

- security students
- platform security engineers
- AI governance teams

## Additional emphasis

- trust boundaries and personal-assistant model limits
- prompt injection and unsafe external content
- tool risk, sandboxing, approval-display integrity, wrapper revalidation, and Gateway/node environment equivalence
- webhook ingress, hook code, plugin runtime-payload provenance, owner-only install/persistence, and file-transfer/node file authority
- current release/advisory review with exact affected/patched versions, recurring failure-family classification, official-source priority, and issue signals labeled separately
- threat modeling and formal verification boundaries
- channel exposure and shared inbox risk

## Extra labs

- threat model workshop
- prompt-injection scenario review
- security audit and remediation lab
- webhook and hook-risk review
- plugin and file-transfer policy review
- detached-work policy-inheritance and scoped `openclaw attach` review

## Capstone

Produce a full security assessment of an OpenClaw deployment, including threat model, control recommendations, and a defended hardening baseline.
