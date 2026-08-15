# Update and Release Discipline

## Purpose

Keep the stable curriculum, reference harness, framework adapters, protocols, product cases, labs, and claims correct as their change rates differ.

## Layered Change Model

| Layer | Examples | Default handling |
| --- | --- | --- |
| Stable foundations | testing, idempotency, least privilege, experimental design | periodic evidence review |
| Harness contracts | loop, tools, state, policy, observability, eval | design review plus regression tests |
| Standards/protocols | MCP, A2A, OpenTelemetry, NIST/OWASP | pin version; compatibility/security review |
| Framework adapters | SDK APIs, defaults, persistence, tracing | verify before every lab run |
| Product cases | OpenClaw, Hermes, ChatGPT Work, xAI | date claims; review releases/docs/advisories |

## Required Release Record

Every material update records:

- component and old/new version or date
- source and retrieval date
- changed behavior, default, security boundary, or deprecation
- affected outcomes, lessons, labs, assessments, fixtures, and claims
- migration and compatibility impact
- test/evidence plan
- rollback or retirement decision
- owner and next review trigger

## Curriculum Change Gates

1. Triage: editorial, instructional, behavioral, security, protocol, or breaking.
2. Verify with primary evidence and identify contradictions.
3. Separate stable-core impact from adapter/case-study impact.
4. Update all aligned surfaces together.
5. Run links, tests, lab reproduction, and source spot checks appropriate to risk.
6. Seek independent review for security, standards, or high-stakes changes.
7. Record decision and release notes.
8. Retire stale assets rather than leaving conflicting paths.

## Cohort Reproducibility

- Freeze the reference-harness commit and lab dependency versions for graded work.
- Record framework/provider/protocol/product versions used by each cohort.
- Do not change a graded environment mid-cohort without migration support and fairness review.
- Preserve expected evidence and known deviations.
- Teach learners to identify drift rather than memorize one version.

## Security Response

Critical advisories or observed vulnerabilities can override normal cadence. Triage exposure, affected labs/deployments, compensating controls, update/rollback, learner notification, and regression coverage. Do not publish exploit detail that increases harm before coordinated handling.

## Release Channels and Previews

Stable, beta, preview, nightly, source-build, and package-only channels are case-specific. Label them and state why a non-stable surface is included. Preview material cannot silently become a required baseline.

## Teaching Rule

Assess the learner's ability to verify, migrate, test, and communicate change. Do not assess current defaults as timeless facts.
