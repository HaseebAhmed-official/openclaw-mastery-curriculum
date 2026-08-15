# Durable, Automated, and Detached Work

## Why It Is Core

Work that continues after the initiating turn, process, operator attention, or context window changes authority, state, failure, and accountability. Product names differ; the engineering contracts remain.

## Mechanism Families

### Deterministic Schedules and Triggers

Cron-like schedules, event hooks, webhooks, queues, and monitors initiate known work. Teach trigger identity, deduplication, missed/late execution, concurrency, pause/disable, and audit.

### Background and Asynchronous Tasks

A task outlives the request that created it. Teach task identity, state transitions, progress, artifacts, cancellation, timeout, retry, and result retrieval.

### Durable Workflows

Workflow engines persist steps and coordinate retries, timers, signals, compensation, and recovery. Teach delivery semantics and external-side-effect limits rather than assuming durability from a library name.

### Standing or Recurring Intent

Long-lived instructions or policies may generate future work. Teach owner, scope, expiry, change review, input trust, escalation, and revocation.

### Delegated and Multi-Agent Work

Subagents, remote agents, coding agents, and worker pools receive tasks and capabilities. Teach requester provenance, least delegation, inherited versus independent policy, artifact validation, and result trust.

### Human Checkpoints

Interrupts and approvals transfer control to a human. Teach exact action binding, freshness, context display, role separation, timeout, revocation, and safe resume.

## Canonical Task State

A durable task should identify:

- task, attempt, parent/requester, and session
- state and valid transitions
- capability and policy snapshot or version
- input and artifact references
- schedule/trigger and deduplication key
- checkpoint and progress
- timeout, retry, cancellation, and recovery
- approval records
- trace correlation
- final outcome and owner

## Failure Matrix

Learners test:

- trigger delivered twice or not delivered
- worker crashes before and after side effect
- provider/tool timeout or partial result
- stale policy or approval after delay
- cancellation races with completion
- child receives too much or too little authority
- context/state schema changes during work
- result arrives after requester/session closes
- malicious artifact or delegated response
- observability or notification failure

## Security and Governance

- Time separation does not expand authority automatically.
- Retries do not make irreversible effects safe.
- Child/delegated work must have explicit capability boundaries.
- Long-lived intent requires owner, expiry, review, and revocation.
- Every material action needs an attributable task/attempt and outcome.
- Recovery must account for both system state and external end state.

## Mastery Evidence

Learners choose the simplest valid mechanism, model the task state machine, inject duplicate/crash/cancellation failures, demonstrate recovery, and defend authority and audit evidence. Product-specific automation surfaces are assessed only as dated implementations of these contracts.
