# Screenshot Capture Standard

## Capture goal

Screenshots are evidence, not decoration. They should help a learner or reviewer verify that the right step happened in the right environment.

## Required capture rules

- capture on the canonical environment lane unless the lab explicitly targets another lane
- include the OpenClaw version or command context somewhere in the capture set when relevant
- redact secrets, tokens, email addresses, and personal identifiers
- prefer one focused capture per checkpoint instead of one cluttered full-screen image
- use consistent filenames such as `LAB-B2-step03-status-healthy.png`

## Required checkpoint types

- precondition capture: proves the student started in the correct state
- success capture: proves the step succeeded
- failure capture: shows one realistic failure or misconfiguration when the lab requires troubleshooting
- evidence capture: preserves the artifact used for grading

## Annotation rules

- add a short caption under each screenshot
- box or highlight only the relevant area
- do not crop away context that proves the command or screen belongs to the correct lab
- if the capture is from a browser UI, include the page section name or route context

## Redaction rules

- never expose provider keys, webhook tokens, pairing secrets, or auth headers
- replace sensitive values consistently using `[REDACTED]`
- if a screenshot cannot be safely redacted without becoming useless, replace it with a text evidence note

## Instructor package recommendation

For each taught lab, maintain:

- one healthy reference screenshot set
- one failure-state screenshot set
- one sample student-quality evidence set
- one strong-vs-weak comparison example for calibration

## File management rule

- use the [Reference Screenshot Manifest](reference-screenshot-manifest.md) as the filename authority
- use the [WSL Ubuntu Capture Workflow](wsl-ubuntu-capture-workflow.md) when building the canonical learner-lane screenshot set
