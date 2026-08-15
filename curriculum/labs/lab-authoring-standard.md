# Lab Authoring Standard

## Required Contract

Every lab includes:

- ID, title, competency/outcome, and evidence level
- objective and predeclared acceptance/failure criteria
- prerequisites and diagnostic/repair route
- duration range and environment lane(s)
- source/version baseline and drift trigger
- safety, authorization, data, and cleanup boundary
- learner task/procedure with prediction before execution
- normal, negative, failure-injection, and transfer conditions
- required code/test/trace/end-state/measurement evidence
- common failures and diagnosis guidance
- recovery or rollback
- rubric hooks and critical gates
- assistance rules and disclosure
- accessibility/equivalent path
- verification status and owner

## Evidence Rule

At minimum, learners prove target behavior, one realistic failure, root-cause reasoning, repair/recovery, security/privacy implication, and changed-condition transfer. Side-effecting tasks require end-state evidence.

## Procedure Versus Task

Use step-by-step procedure only while teaching a new foundation. Fade support and assess with task contracts plus acceptance criteria. A copied procedure is not independent capability.

## Security/Production Additions

Labs with side effects, external content, protocols, automation, delegation, remote access, plugins/dependencies, durable state, or multi-user scope also require explicit trust/authority diagrams, least-authority rationale, safe exploit/misconfiguration, detection, recovery, and residual-risk decision.

## Verification Status

- `authored`: contract exists
- `dry-reviewed`: clarity/safety independently reviewed
- `executed`: author ran it in declared lane
- `reproduced`: second person completed cleanly
- `calibrated`: learner timing/failures and grading anchors evidenced

Record date, commit/versions, lane, executor/reviewer, result, deviations, and evidence reference. Do not call an authored lab ready to teach.
