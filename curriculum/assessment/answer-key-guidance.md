# Answer Key Guidance

## Purpose

This file is not a rigid script of exact answers. It tells instructors what a strong answer should contain so grading stays rigorous without forcing one wording.

## High-priority concept answers

### What problem does OpenClaw solve that a normal hosted chatbot does not?

A strong answer should mention:

- self-hosted gateway or control plane
- channels, tools, nodes, and durable workspace state
- operator control over deployment and integrations

Weak answer signs:

- says "it is just a chatbot with more features"
- ignores tools, routing, or host control

### Why is OpenClaw a trusted-operator system rather than a hostile multi-tenant boundary?

A strong answer should mention:

- one trusted operator boundary per gateway
- official docs do not position it as adversarial-user isolation
- design and grading implications for shared inboxes and team use

Weak answer signs:

- claims it is safe for mutually untrusted users by default

### Why is "the model remembers it" an unsafe explanation in OpenClaw?

A strong answer should mention:

- persisted memory is in workspace files
- visible artifacts like `MEMORY.md`, daily notes, and related files matter
- students should distinguish persisted state from assumed hidden state

### Why should release notes matter in provider or security labs?

A strong answer should mention:

- default models and security behavior can drift across releases
- labs can become inconsistent across cohorts without version awareness
- teaching should anchor to current stable behavior plus release-note checks

## Scenario grading guidance

### Public exposure for convenience

A strong response should:

- reject convenience as sufficient justification
- prefer loopback plus SSH or Tailscale Serve unless there is a defended reason otherwise
- mention trust boundary and ingress risk

### Shared gateway for untrusted users

A strong response should:

- reject the design as framed
- explain why OpenClaw is not a hostile multi-tenant boundary
- suggest separation, stronger isolation, or different architecture

### Sandbox means host risk is solved

A strong response should:

- say sandboxing materially helps but is not a perfect security boundary
- explain residual risk and why approvals and policy still matter

### Memory strategy without `DREAMS.md`

A strong response should:

- challenge the omission
- explain that dreaming is part of the documented memory system
- ask how promotion, thresholds, or memory strategy were considered

## Scoring reminder

Do not award full marks to answers that are:

- confident but vague
- security-flavored but not OpenClaw-specific
- operationally unrealistic
- correct in spirit but missing the trust model
