# Lab Authoring Standard

## Required fields for every lab

- objective
- prerequisites
- estimated duration
- environment lane
- source-backed preparation links
- step-by-step procedure
- expected outputs and evidence
- common failure modes
- rollback or recovery path
- security implications
- grading notes

## Minimum evidence rule

No lab is considered complete unless the learner submits both:

- proof that the target behavior worked
- proof that they understand at least one realistic failure mode or security implication

## Special rule for production or security labs

Labs covering remote access, webhook ingress, approvals, sandboxing, plugins, or automation must include:

- explicit trust-boundary statement
- least-privilege justification
- one misconfiguration scenario
- one remediation step
