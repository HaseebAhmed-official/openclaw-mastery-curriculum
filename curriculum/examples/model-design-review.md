# Model Design Review

## Decision

Build a bounded research-assistance workflow for an internal policy team. Use deterministic retrieval/filtering and citation checks first; use one agent only to synthesize ambiguous evidence. No autonomous publication or external communication.

## Requirements and Non-Goals

- produce a source-linked briefing from approved internal and official sources
- identify conflicts, dates, and uncertainty
- permit a human reviewer to inspect evidence before export
- retain task evidence for 30 days, then delete under policy
- non-goals: legal advice, automatic policy decisions, unrestricted web browsing, public release

## Alternatives

1. Deterministic search plus template: safest and cheapest, but weak for conflicting narrative synthesis.
2. Single bounded synthesis agent: selected after deterministic retrieval; measurable benefit can be tested.
3. Multi-agent research/debate: rejected until evidence shows one agent cannot meet quality; adds cost and coordination risk.

## Architecture

- provider adapter with deterministic test double and one approved network provider
- context builder selects approved records with source, owner, date, and trust label
- read-only retrieval tool; export tool is side-effecting and requires exact human approval
- append-only task/events and artifact references
- no long-term semantic memory; only policy-governed task state
- trace plus end-state evaluation of source coverage, unsupported claims, and export behavior

## Threat and Data Review

Primary risks: indirect prompt injection in documents, confidential-data leakage to provider/logs, stale policy source, unsupported synthesis, approval mismatch, and retained artifacts. Controls: instruction/data separation, source allowlist, content labels, provider data policy review, redaction, exact export approval, no network tool for the agent, retention/deletion job, and security eval variants.

## Evaluation and Release Gate

Compare template baseline and bounded agent on 30 representative tasks with repeated trials for the agent arm. Grade factual support, source conflict handling, critical omission, unsupported claims, latency, cost, and human correction. Any unauthorized export or protected-data leak is stop-ship regardless of average score.

## Operations

Define success/latency SLOs, provider degradation to deterministic briefing, trace correlation, artifact deletion evidence, incident route, frozen source/provider versions, and rollback to the template baseline.

## Open Questions

- Is provider handling acceptable for the most sensitive document class?
- Can deletion be verified across derived indexes and backups?
- Does synthesis improve reviewer time enough to justify model cost and risk?

## Review Verdict

Approve a synthetic-data prototype only. Production or legal-decision claims are blocked pending privacy/legal review, representative evaluation, deletion proof, and incident rehearsal.
