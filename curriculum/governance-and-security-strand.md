# Governance and Security Strand

## Purpose

Thread security, safety, privacy, accessibility, ethics, and accountable change through every module. These are system properties and operating practices, not a late compliance lecture.

## Stage 1: Scope, Assets, and Trust

Learners identify users, operators, developers, providers, tools, data, identities, execution environments, external systems, and adversaries. They label control, data, authority, and trust boundaries before implementation.

Evidence: architecture/data-flow diagram, assumptions, misuse cases, and explicit single-user/team/multi-tenant boundary.

## Stage 2: Input, Context, and Memory

Teach instruction/data separation, source provenance, prompt injection, retrieval contamination, memory isolation, freshness, retention, deletion, and sensitive-context minimization.

Evidence: malicious-context test, memory isolation/deletion test, and data lifecycle.

## Stage 3: Capabilities and Authority

Teach least-authority tools, typed validation, requester provenance, policy, exact approval, capability discovery versus authorization, high-impact classification, and safe denial.

Evidence: authority graph, argument-substitution test, deny-default test, and approval audit record.

## Stage 4: Execution and Supply Chain

Teach process/filesystem/network isolation, secrets, dependency provenance, plugin/server trust, resource limits, egress, working-directory ownership, updates, and rollback.

Evidence: execution-boundary test, dependency/source review, secret-redaction test, and recovery plan.

## Stage 5: State, Durability, and Detached Work

Teach sessions, task identity, events, retries, idempotency, cancellation, compensation, schedules, triggers, delegated work, inherited authority, and human review after context or time separation.

Evidence: crash/retry scenarios, duplicate prevention, cancellation test, and accountable task timeline.

## Stage 6: Detection, Evaluation, and Response

Teach correlated observability, security evals, abuse corpora, trace/end-state graders, alert ownership, containment, incident response, evidence preservation, recovery, and post-incident improvement.

Evidence: exploit/mitigation variants, detection record, incident drill, and regression gate.

## Stage 7: Organizational Governance

Teach risk ownership, NIST AI RMF/SSDF mapping, exceptions, change approval, user notice/control, privacy, accessibility, vendor review, assurance limits, and when qualified legal/domain/security review is required.

Evidence: control-evidence-owner map, review cadence, exception record, user-facing limitation, and release decision.

## Required Threat Families

- direct and indirect prompt injection
- confused-deputy and requester-provenance failure
- excessive agency and approval mismatch
- secret/data exfiltration and sensitive observability
- malicious/stale memory and persistence
- tool/plugin/protocol/dependency supply chain
- identity, session, and tenant-boundary failure
- retry/duplicate/partial-side-effect failure
- model/provider manipulation or degradation
- evaluation leakage, grader gaming, and false readiness claims

## Required Learner Behaviors

- test only within authorization and containment
- never use real secrets or protected data in exercises
- stop and report unexpected impact
- label evidence and uncertainty
- distinguish prevention, detection, response, and recovery
- state residual risk and decision owner
- reject claims stronger than the observed boundary

## Program Gate

No learner passes the core or capstone with an unresolved critical security/privacy failure, hidden authority, unsafe experiment, fabricated evidence, or inability to explain the trust boundary. Points elsewhere cannot compensate.
