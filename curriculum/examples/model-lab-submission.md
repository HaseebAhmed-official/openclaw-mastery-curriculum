# Model Lab Submission

## Metadata

- lab: LAB-B6 Policy, Approval, and Execution Boundary
- reference commit: `[example commit]`
- environment: Python 3.12 on WSL Ubuntu
- assistance: agent suggested attack cases; learner implemented, predicted, ran, traced, and defended all tests

## Objective and Acceptance

Prove that a side-effecting tool cannot execute unless policy allows the tool and an approval binds the same session, tool name, and canonical arguments. Required attacks: missing approval, changed arguments, wrong session, unknown tool, and allowed exact action.

## Prediction

The existing reference harness should deny a side effect without approval and allow an exact approval. It should also reject changed arguments because the fingerprint changes. It does not consume approval after use, so replay within the same session remains a known gap.

## Work and Evidence

1. Ran the baseline 8 tests: all passed.
2. Added tests for wrong session and changed destination arguments; both were denied with `policy.decided.allowed=false`.
3. Added an exact matching approval; the handler ran once and emitted `tool.started` then `tool.completed`.
4. Reused the same approval in the same session; the action ran again, confirming the documented one-time-use limitation.
5. Added a proposed `consume_on_use` design but did not merge it because concurrency semantics require a transactional store.

Evidence references:

- test names and commit: `[references]`
- denied event excerpt: `[redacted excerpt]`
- allowed end-state assertion: `[reference]`

## Failure Analysis

The first changed-argument test unexpectedly passed because the test constructed approval after mutating the arguments. The defect was in the fixture, not policy. I froze the approved arguments first, reran the test, and verified denial. A regression assertion now compares both fingerprints explicitly.

## Security and Boundary

Approval is only one layer. The teaching runtime does not isolate the handler process, restrict filesystem/network access, authenticate a human approver, enforce expiry, or make approval consumption atomic. Therefore the result proves exact argument binding in this process, not production authorization or containment.

## Result and Transfer

Core acceptance passed. Remaining gap: one-time approval under concurrent workers. Transfer task: design a transactional consume-on-use record and show the failure state if execution completes but approval consumption acknowledgment is lost.

## Why This Is Strong

It includes predictions, negative and positive paths, a real fixture error, event/end-state evidence, exact claim boundaries, assistance disclosure, and a next changed-condition task.
