# Instructor Feedback Examples

## Distinction

Your strongest evidence is the failure/recovery chain: prediction, injected duplicate, event reconstruction, reconciliation, repair, and variant retest. The architecture remains intentionally small, and your claims match the tested boundary. For L6 evidence, repeat under a longer-running workload and independent operations review.

## Pass With Repair

The core path works, but the evaluation cannot support your release claim. You graded final text only even though the task changes external state. Add end-state and event graders, predeclare a critical-failure rule, run repeated trials, and explain disagreements before resubmission.

## Fail: Authenticity/Tracing

The artifact is polished, but you could not trace the approval decision or explain why the changed-argument test should fail. This does not establish independent implementation mastery. Rebuild the smallest policy path, annotate its events, then complete a new argument-substitution task without procedural help.

## Fail: Security Boundary

The design relies on a prompt telling the model not to read sensitive files while the execution tool still has access. That is not containment. Restrict capability before execution, add a safe exploit and variant, then demonstrate prevention, detection, and recovery evidence.

## Fail: Readiness Inflation

“Enterprise-ready” is unsupported. You have a local success path but no SLO, capacity, tenancy, privacy, incident, migration, rollback, independent review, or user evidence. Revise the claim to the observed maturity and create a gate plan for the missing evidence.
