# Assessor Calibration Guide

## Purpose

This guide keeps grading standards stable across instructors, TAs, reviewers, and cohorts.

## Calibration goals

- reduce grading drift
- separate polished presentation from real competence
- enforce the trust model consistently
- keep pass/fail judgments aligned to the curriculum's risk posture

## Before grading

Every assessor should:

1. read the [Master Rubric](../rubrics/master-rubric.md)
2. read the [Track Rubrics](../rubrics/track-rubrics.md)
3. read the relevant lab guide or capstone spec
4. review the current release-aware assumptions if the artifact depends on fast-moving features

## Evidence hierarchy

Grade in this order:

1. demonstrated behavior or artifact evidence
2. written reasoning
3. oral defense quality
4. polish or presentation quality

Do not reverse this order.

## Calibration exercise

Before a major grading cycle:

1. choose 3 sample submissions
2. have all graders score them independently
3. compare scores and reasoning
4. identify where graders disagreed
5. align on pass/fail gates and distinction criteria

## Non-negotiable fail gates

Do not pass a major artifact if it:

- treats OpenClaw as a hostile multi-tenant boundary
- exposes the gateway without explaining why the exposure is safe enough
- ignores prompt injection in a tool-enabled or external-content workflow
- ignores detached authority in an automation-heavy design
- cannot explain why its chosen model or provider is acceptable

## Score interpretation

### Score 4

- evidence is complete
- reasoning is explicit
- risks are named and bounded
- the student rejects unsafe shortcuts proactively

### Score 3

- work is mostly correct
- some depth is missing
- operational or security reasoning is present but not exhaustive

### Score 2

- work is fragile or only partially reasoned
- evidence is incomplete
- the student relies on assumptions they cannot defend

### Score 1

- core misunderstanding
- unsafe claims
- weak or missing evidence

## Oral defense calibration

Reward:

- concise, direct answers
- explicit tradeoffs
- correct limitation statements

Do not reward:

- confidence without evidence
- vague references to "best practice"
- unsupported claims about security, memory, or isolation

## Feedback expectations

Every graded artifact should receive:

- one statement of what was strong
- one statement of what was missing
- one concrete next improvement

## Regrade policy suggestion

Allow regrade or resubmission when:

- the student can correct evidence gaps
- the issue is incomplete reasoning rather than dishonesty
- the resubmission does not erase the original trace of what changed
