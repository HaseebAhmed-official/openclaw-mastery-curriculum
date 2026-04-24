# Security / Hardening Answer Pack

## Target standard

This track should produce a security assessment grounded in OpenClaw's actual trust model, not generic AI-security language.

## Model capstone answer shape

1. Define the supported trust model and reject unsupported hostile multi-tenant claims.
2. Map assets, actors, ingress, channels, tools, and detached authority surfaces.
3. Present the hardening baseline: auth, exposure, sandboxing, exec policy, channel restrictions, plugin controls.
4. Use the security audit, current advisories, and threat-model docs together.
5. State residual risks and compensating controls honestly.

## Strong evidence bundle

- deployment-specific threat register
- security audit findings with prioritization
- advisory review note tied to the assessed surfaces
- hardening recommendations ordered by risk and effort
- defended statement of residual risk

## Strong-answer signals

- uses the official trust model precisely
- separates auth problems, exposure problems, tool-risk problems, and prompt-injection problems
- treats advisories as current teaching inputs
- avoids claiming sandboxing or formal verification proves total safety

## Weak-answer signals

- generic security buzzwords with no deployment mapping
- prompt injection described as the only risk
- current advisories ignored
- "secure because internal" reasoning with no control explanation

## Oral defense prompts

- Which current advisory most closely matches this deployment surface?
- Why is one shared gateway not the right answer for mutually untrusted users?
- What risk remains even after strong sandboxing and approvals?
