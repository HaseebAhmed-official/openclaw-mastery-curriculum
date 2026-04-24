# Operator Answer Pack

## Target standard

This track should produce a reliable operator, not just a successful installer.

## Model capstone answer shape

1. State the deployment scope: one trusted operator boundary, intended channels, and usage pattern.
2. Describe the operating baseline: install path, provider/model choice, release baseline, and environment lane.
3. Document daily operations: health checks, logs, status flow, session and memory hygiene, safe channel rules.
4. Document failure handling: what breaks first, how to diagnose it, when to escalate.
5. State security posture: channel policy, sandbox or tool-policy assumptions, remote-access choice, unsafe features left off.

## Strong evidence bundle

- release-aware baseline note
- daily or weekly operator runbook
- diagnostic ladder with one healthy and one failure case
- channel policy note
- support escalation rule set

## Strong-answer signals

- uses operational language instead of vague enthusiasm
- explains why the chosen channel policy is narrow enough
- shows a clean troubleshooting ladder before proposing reinstall or reset
- records what defaults are current instead of assuming they are timeless

## Weak-answer signals

- "it works" used as the main proof of quality
- channel enabled with no written policy
- remote access justified only by convenience
- no runbook or no distinction between quick fix and root cause

## Oral defense prompts

- What is the first signal you would inspect if replies stop reaching the user?
- What changes in your runbook if the release baseline moves?
- Why is this design an operator workflow and not yet a production service?
