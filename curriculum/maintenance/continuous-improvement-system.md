# Continuous Improvement System

## Objectives

- keep claims current and correctly scoped
- preserve outcome/module/lab/assessment alignment
- improve learner transfer, not only satisfaction or pass rates
- detect security, accessibility, reproducibility, and grading failures
- retire stale or duplicate material instead of accumulating clutter

## Change Streams

### Stable Foundations

Review research, CS/software-engineering alignment, pedagogy, and core contracts annually or when material evidence emerges.

### Standards and Security

Review MCP, A2A, OpenTelemetry, NIST, OWASP, and critical security evidence each term and on material revision/advisory.

### Frameworks and Providers

Verify current versions, APIs, defaults, persistence, policy, tracing, and evaluation before every affected lab run.

### Product Cases

Review docs, releases, advisories, availability, and claim tables before delivery. OpenClaw has an automated release signal; other cases currently require manual primary-source review.

### Delivery Evidence

After every cohort or pilot, review prerequisites, lab reproduction/time, failure patterns, assessment performance, assessor agreement, remediation, delayed transfer, accessibility, support load, and learner/instructor feedback.

## Workflow

1. Detect: source change, test failure, learner evidence, review finding, or adoption need.
2. Triage: editorial, source, technical, security, pedagogical, assessment, accessibility, or breaking.
3. Scope: affected outcomes, modules, labs, code/fixtures, assessment, case claims, and state.
4. Verify: primary evidence, reproduction, contradiction, and residual uncertainty.
5. Decide: keep, repair, pin, migrate, disable, split, or retire.
6. Implement the smallest coherent aligned change.
7. Validate with risk-appropriate static, executable, security, teaching, and review gates.
8. Record decision, evidence, owner, and next trigger.
9. Release with migration/rollback and known limitations.
10. Measure whether the change improved the intended outcome.

## Safe Automation

- link and JSON/schema checks
- reference-harness tests and coverage reports
- release/advisory detection
- pinned-version inventory and drift alerts
- outcome/lab/assessment ID consistency
- stale-date and unresolved-marker reports
- review reminders and evidence dashboards

## Human Decision Required

- interpreting conflicting sources
- changing stable architecture or outcomes
- security/privacy/tenancy claims
- grading standards and critical gates
- high-stakes or legal/regulatory meaning
- learner data use
- institution/enterprise/readiness claims

## Health Measures

- critical lab reproduction rate
- broken/stale claim count and review latency
- reference test and security regression pass rate
- outcome-to-assessment coverage
- assessor agreement and moderation changes
- first-pass, remediation, and delayed-transfer success
- accessibility/support incidents
- critical external-review findings and repair time
- duplicate/retired file count

## Claim Boundary

An automated green status proves only the checks it executed. Curriculum effectiveness and institution/enterprise readiness require independent and real-user evidence.
