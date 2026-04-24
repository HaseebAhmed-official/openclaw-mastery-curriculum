# Continuous Improvement System

## Goal

Keep the curriculum current without sacrificing rigor.

## System design

### Layer 1: automatic detection

- GitHub workflow checks the latest official OpenClaw release
- repository state tracks the last reviewed upstream release
- if upstream moves ahead, the repo opens or updates a review issue

### Layer 2: structured review

The maintainer reviews:

- release notes
- security implications
- changed defaults
- affected semester modules
- affected labs
- affected grading or submission templates

### Layer 3: controlled curriculum updates

Maintainers update only the files that actually drifted. They do not rewrite broad sections without evidence.

### Layer 4: publication discipline

After curriculum updates:

- update the review log
- update `upstream-state.json`
- push with a clear change summary

## Quality principles

- correctness beats speed
- release-aware notes beat stale certainty
- explicit trust-boundary reasoning beats generic "best practice" wording
- no blind auto-merge of upstream claims into the curriculum

## What may be automated safely

- release detection
- issue creation
- checklists
- review reminders
- tracking of last reviewed baseline

## What should not be fully automated

- final curriculum wording changes
- grading-policy changes
- trust-model interpretation
- security claims
- teaching-sequence changes

## Definition of healthy maintenance

The system is healthy when:

- the latest upstream release is either reviewed or queued for review
- release-sensitive curriculum files are date-aware
- the review log shows explicit decisions
- no one has to guess which parts need revalidation
