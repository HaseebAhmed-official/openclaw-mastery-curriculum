# Design Review Template

## Design title

## Problem statement

What problem is this design solving, and for whom?

## Proposed solution

Give a short, high-level explanation of the proposed architecture or workflow.

## Context and assumptions

- intended users:
- trust model:
- environment:
- version / release assumptions:
- constraints:

## Architecture summary

- gateway location:
- access method:
- provider / model strategy:
- channels or nodes used:
- plugins or skills involved:
- automation or detached work involved:

## Trust boundary analysis

### Who is trusted?

### Who is not trusted?

### Where does authority widen?

### What authority is durable?

## Operational design

- install or deployment method:
- health checks:
- logging and diagnostics:
- rollback expectations:
- update strategy:

## Security review

- prompt injection exposure:
- sandboxing / exec policy:
- webhook or hook exposure:
- plugin or supply-chain concerns:
- remote ingress concerns:

## Alternatives considered

### Alternative 1

- why considered:
- why rejected:

### Alternative 2

- why considered:
- why rejected:

## Failure modes

List the top 3 realistic failures and how the design responds.

1. 
2. 
3. 

## Evidence and references

- official docs used:
- release notes used:
- repo or validation artifacts used:

## Final recommendation

State whether you recommend approval, approval with conditions, or rejection.
