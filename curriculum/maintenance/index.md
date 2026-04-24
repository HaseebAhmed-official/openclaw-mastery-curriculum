# Maintenance System

## Purpose

This curriculum is designed to stay current as OpenClaw evolves. The maintenance system exists to preserve quality, not just freshness.

## Core maintenance documents

- [Continuous Improvement System](continuous-improvement-system.md)
- [Upstream Review Playbook](upstream-review-playbook.md)
- [Change Control Checklist](change-control-checklist.md)
- [Review Log](review-log.md)
- `upstream-state.json`

## Automation layer

The repository also contains:

- a scheduled GitHub workflow that checks for new OpenClaw releases
- a script that compares the latest upstream release against the curriculum's reviewed baseline

## Maintenance rule

New upstream releases should trigger review automatically, but curriculum content should not be changed blindly. Detection can be automated. Judgment must stay explicit.
