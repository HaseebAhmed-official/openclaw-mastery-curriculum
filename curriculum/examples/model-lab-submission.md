# Model Lab Submission

## Context

This is a model-quality response for a Semester 1 operational lab, based on the structure expected from [Lab Submission Template](../templates/lab-submission-template.md).

## Submission metadata

- Student name: Example Student
- Student ID: 2026-OC-014
- Course / section: OpenClaw Mastery / Section A
- Lab ID: LAB-B2
- Submission date: 2026-04-24
- Environment lane: standard university lab path
- OpenClaw version: v2026.4.23
- Release channel: stable

## Lab objective

This lab was meant to prove that I can diagnose OpenClaw systematically instead of guessing. The required outcome was to use the documented diagnostic ladder, compare healthy and broken states, and explain which layer was responsible for the failure.

## Environment summary

- Host OS: Windows 11 with WSL2 Ubuntu
- Shell used: bash inside WSL2
- Docker available: yes
- Provider used: Anthropic classroom key
- Channel used: none for this lab

## Steps completed

1. Verified that the gateway and Control UI were reachable locally.
2. Ran the required commands: `openclaw status`, `openclaw doctor`, `openclaw gateway probe`, `openclaw gateway status`, `openclaw channels status --probe`, and `openclaw logs --follow`.
3. Captured a healthy baseline.
4. Re-ran the ladder after the instructor-provided provider failure scenario.
5. Compared the differences and isolated the issue to the provider/auth layer rather than the gateway or UI layer.

## Evidence

- command outputs or screenshots:
  - baseline status transcript
  - doctor output showing environment health
  - provider-failure transcript
- config snippet or policy artifact:
  - not applicable for this lab
- log or diagnostic evidence:
  - `openclaw logs --follow` showed repeated auth failure while gateway remained healthy
- supporting file:
  - `lab-b2-diagnostics-notes.md`

## Failure encountered

- failure description: provider authentication failed after a deliberately invalid credential was introduced
- where it occurred: provider layer during prompt execution
- how I diagnosed it: `gateway status` stayed healthy, `doctor` showed no host/runtime fault, and logs showed auth-specific failure
- how I resolved it: restored the approved credential and reran the diagnostic ladder to verify healthy state

## Security and trust reflection

1. The main authority in this lab was local gateway access plus provider access.
2. The lab was safe enough because it stayed local, used classroom-approved credentials, and did not expose the gateway remotely.
3. In production, the same workflow would be unsafe if logs exposed secrets, if the gateway were publicly reachable, or if diagnostics were run against an unreviewed plugin/hook environment.

## Release-aware note

- release notes checked: OpenClaw latest release page
- date checked: 2026-04-24
- one current assumption that might drift later: the exact diagnostic wording and provider defaults can change between releases, so the ladder must be revalidated before reuse next term

## Final conclusion

The lab succeeded fully. The key lesson was that healthy gateway status does not imply healthy provider execution, and the logs were necessary to isolate that difference.

## Why this is a strong example

- It proves the work happened.
- It includes one real failure and diagnosis path.
- It treats security as part of operations.
- It records release-aware assumptions instead of assuming the commands are timeless.
