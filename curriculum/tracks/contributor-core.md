# Core / Framework Track

## Role

Implement, audit, and maintain harness runtime, orchestration, context, state, policy, observability, or evaluation internals.

## Outcomes

- trace unfamiliar source across multiple runtime layers
- define stable core contracts and isolate provider/framework adapters
- implement bounded concurrency, state transitions, cancellation, and failure propagation
- design regression, performance, compatibility, and migration tests
- evaluate complexity and remove abstractions that do not improve evidence
- contribute within upstream conventions and communicate maintenance impact

## Required Evidence

- LAB-B2 through LAB-B7, LAB-C1, LAB-C2, LAB-D1, LAB-D5
- source-level control/data-flow trace
- tested runtime subsystem or scoped upstream change
- performance and failure evidence
- compatibility and maintenance analysis
- delayed unfamiliar-code change

## Advanced Topics

Runtime architecture, schedulers, event sourcing, workflow engines, concurrency, protocol internals, compilers/DSLs, model routing, observability pipelines, and benchmark infrastructure.

## Capstone Emphasis

Prefer a small high-leverage subsystem over an unreviewable framework rewrite. Code volume without traced invariants, tests, and maintenance evidence does not pass.
