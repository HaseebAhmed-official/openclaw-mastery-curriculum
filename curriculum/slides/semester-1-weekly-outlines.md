# Semester 1 Weekly Deck Outlines

Use 8-14 concise slides plus live construction/activity. Begin with retrieval/prediction and end with an evidence-based exit check.

## Week 1: Discipline and Boundaries

- question: when is an agent the wrong engineering choice?
- visuals: workflow versus agent loop; model/harness/operator trust map
- demonstration: trace one deterministic and one model-directed path
- activity: classify four tasks and defend the simplest design
- exit: label control, data, authority, and unknowns

## Week 2: Reproducible Engineering

- question: what does a successful run actually prove?
- visuals: environment/commit/test evidence chain
- demonstration: failing then passing clean-clone test
- activity: explain a scoped diff
- exit: list one hidden dependency and reproduction test

## Week 3: Contracts and Test Doubles

- question: how can harness logic be tested without a live model?
- visuals: provider protocol and scripted-turn sequence
- demonstration: final/tool/error turns
- activity: write one contract test and one limitation
- exit: core versus adapter boundary

## Week 4: Bounded Loop

- question: who guarantees termination?
- visuals: loop state machine and stop-reason matrix
- demonstration: no-progress and budget stop
- activity: find an unbounded path
- exit: defend one invariant

## Week 5: Typed Tools

- question: what makes a tool usable and safe enough to expose?
- visuals: discover-validate-authorize-execute-observe path
- demonstration: malformed call and structured repair error
- activity: redesign an ambiguous API
- exit: compile-time versus runtime validation

## Week 6: Execution Boundary

- question: where does chosen capability become real authority?
- visuals: model, policy, executor, host/resource boundary
- demonstration: environment/working-directory mismatch
- activity: define controls for a code tool
- exit: prompt instruction versus sandbox

## Week 7: Context Engineering

- question: why can more context make performance worse?
- visuals: source/provenance/freshness/budget pipeline
- demonstration: instruction-data separation and ablation
- activity: choose truncation order
- exit: one test for stale or malicious context

## Week 8: Trace and Debug Midterm

- question: which layer actually failed?
- visuals: failure taxonomy and evidence hierarchy
- demonstration: misleading final output with bad event/end state
- activity: unseen trace diagnosis
- exit: rejected diagnosis and evidence

## Week 9: Sessions and Events

- question: why is a transcript not durable task state?
- visuals: session/task/attempt/event/artifact identities
- demonstration: timeline reconstruction
- activity: identify invalid transition
- exit: minimum event fields

## Week 10: Checkpoint and Replay

- question: when is retry unsafe?
- visuals: crash points around external side effect
- demonstration: checkpoint/resume and duplicate risk
- activity: choose retry/compensate/reconcile
- exit: replay claim boundary

## Week 11: Policy and Approval

- question: what exact action did the human approve?
- visuals: requester-capability-arguments-session-freshness binding
- demonstration: argument substitution
- activity: design deny-default matrix
- exit: stale approval attack

## Week 12: Memory

- question: when does retained context become contamination?
- visuals: write-policy/index/retrieve/use/delete lifecycle
- demonstration: useful versus malicious memory
- activity: define retention/deletion proof
- exit: relevance versus truth/authority

## Week 13: Observability

- question: which evidence answers which operational question?
- visuals: correlated trace/metric/log/event/artifact map
- demonstration: reconstruct one failure
- activity: redact without losing diagnosis
- exit: identify missing signal

## Week 14: Evaluation

- question: can the answer be correct while the run fails?
- visuals: task-trial-grader-outcome; agent harness inside eval harness
- demonstration: output grader versus end-state grader
- activity: predeclare a regression threshold
- exit: why repeated trials matter

## Week 15: Integration Review

- question: which abstractions and claims are unnecessary?
- visuals: full minimal-harness contract map
- demonstration: architecture review findings
- activity: delete or simplify one layer
- exit: top unresolved risk/test

## Week 16: Practical and Transfer

- question: can capability survive changed conditions?
- visuals: evidence bundle and mastery ladder
- demonstration: none; protect assessment authenticity
- activity: individual changed task and oral trace
- exit: evidence-based level and repair
