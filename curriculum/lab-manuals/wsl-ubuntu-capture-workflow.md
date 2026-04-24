# WSL Ubuntu Capture Workflow

## Purpose

This workflow standardizes screenshot capture for the exact learner lane this curriculum expects most often: WSL Ubuntu plus a local browser.

## Use this workflow when

- the learner or instructor is running OpenClaw from WSL Ubuntu
- the course needs updated screenshots after an OpenClaw release change
- a teaching team wants one clean reference screenshot set for future cohorts

## Capture baseline

- distro: Ubuntu on WSL2
- shell: bash
- terminal width: at least 110 columns
- terminal theme: high-contrast light or dark, but consistent across the set
- browser width for Control UI captures: desktop width first, then optional narrow/mobile comparison if needed
- OpenClaw version: record before starting the capture session

## Pre-capture checklist

1. confirm `openclaw --version`
2. confirm the current release baseline used by the curriculum
3. clean or isolate any personal data in the workspace
4. prepare one healthy path and one failure path for labs that require both
5. verify the screenshot filenames from the [Reference Screenshot Manifest](reference-screenshot-manifest.md)

## Terminal capture rules

- keep the prompt visible where it proves the environment is Ubuntu
- prefer one command or one narrow workflow per capture
- wrap or widen the terminal so key lines remain readable
- redact tokens, secrets, phone numbers, and personal identifiers
- if output is too long, capture the key section and preserve the full output in the written artifact

## Browser capture rules

- keep the browser route or section visible when it proves context
- do not capture private browsing data, cookies, or unrelated tabs
- for Control UI captures, prefer one screenshot per operational panel rather than one cluttered page
- record whether the page reflects a healthy state, onboarding state, or failure state

## Capture session structure

1. version capture
2. healthy baseline captures
3. failure-state captures
4. artifact-evidence captures
5. final redaction review

## Recommended first capture set

If you are building the screenshot library from scratch, start with:

- LAB-B1
- LAB-B2
- LAB-B4
- LAB-B5
- LAB-C2
- LAB-C3

These give the best teaching value first because they cover install, diagnostics, providers, authority, audit, and ingress.

## File placement

Place files exactly where the manifest expects them:

- `curriculum/lab-manuals/assets/core/`
- `curriculum/lab-manuals/assets/advanced/`
- `curriculum/lab-manuals/assets/specialization/`

## Post-capture update rule

After a capture session:

1. update the relevant classroom manual if the screenshot revealed a workflow change
2. note the OpenClaw version and validation date used
3. update the maintenance log if the change came from upstream drift
