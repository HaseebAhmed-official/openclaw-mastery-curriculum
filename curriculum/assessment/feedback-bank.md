# Feedback Bank

## Purpose

This bank helps instructors give fast, specific feedback without collapsing into generic praise or generic criticism.

## Positive feedback options

- Your artifact was strongest where you explicitly documented trust boundaries instead of assuming them.
- The diagnostic sequence was well structured and showed operational maturity.
- You handled release drift correctly by recording current defaults and version assumptions.
- Your design rejected a tempting but unsafe shortcut, which is the right judgment signal for this course.
- The capstone defense was convincing because you named residual risk rather than pretending the system was risk-free.

## Corrective feedback options

- The artifact works, but it does not yet explain why the authority it creates is safe enough.
- Your reasoning is too abstract; tie it to actual OpenClaw surfaces like sessions, approvals, hooks, or ingress.
- You documented the success path, but not the failure path or recovery path.
- The submission relies on current behavior without recording version or release assumptions.
- Your security claims are broader than the official OpenClaw trust model supports.

## High-severity feedback options

- This submission cannot pass because it treats OpenClaw as a hostile multi-tenant boundary.
- This submission cannot pass because it exposes a dangerous capability without adequate justification or containment.
- This submission cannot pass because prompt injection or unsafe external content is not addressed where it clearly matters.
- This submission cannot pass because the design uses automation or detached authority without explaining auditability or policy.

## Revision prompts

- Add one section that explains exactly who is trusted and who is not.
- Add one failure mode and show how you would diagnose it.
- Add a release-aware note and record what defaults you relied on.
- Add a supply-chain review section if your work depends on plugins, hooks, or external code.
- Rewrite the conclusion so it states whether the design should be approved, approved with conditions, or rejected.
