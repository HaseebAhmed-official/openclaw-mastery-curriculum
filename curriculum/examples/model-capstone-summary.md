# Model Capstone Summary

## Project

Failure-Tested Durable Harness for Internal Change-Review Tasks

## Track

Platform / SRE, with Security / Assurance evidence.

## Summary

The project implements a small harness that reviews synthetic change requests, calls read-only analysis tools, and produces an artifact for human approval. The engineering goal is not broad autonomy. It is to prove explicit task state, bounded execution, safe retry, observable failure, and rollback under provider/tool/process degradation.

A deterministic rules baseline handles well-formed routine changes. A single agent handles ambiguous risk explanation only when the baseline cannot classify the request. Side effects are outside agent authority. The runtime records task/attempt events, checkpoints before delegated work, uses idempotency keys for artifact creation, and routes unknown external state to human reconciliation instead of blind retry.

The evaluation corpus contains normal, malformed, conflicting, injected, duplicate, timeout, and crash scenarios. Output, trace, and end-state graders are combined. The release candidate is blocked by any cross-task data leak, unauthorized effect, silent duplicate, or unrecoverable critical state. A red-team exercise found that retrieved request text could influence a tool query; the repair separated untrusted data, restricted query fields, and passed original plus paraphrased variants.

The system was deployed in a bounded container environment, then tested for provider degradation, worker crash, duplicate delivery, state migration failure, and rollback. It does not claim hostile multi-tenant isolation or enterprise readiness. Remaining work includes real user trials, a transactional approval store, external security review, and longer-duration capacity evidence.

## Why This Is Strong

- narrow justified problem and deterministic baseline
- stable contracts rather than framework feature dependence
- injected failures and inspectable recovery
- critical-gate evaluation rather than average-only scoring
- explicit security repair and claim limits
- clear remaining evidence instead of readiness inflation
