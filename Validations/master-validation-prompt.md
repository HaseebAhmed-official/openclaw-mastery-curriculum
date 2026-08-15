# Master Validation Prompt

Give the following prompt to a fresh capable agent with local repository, terminal, Git, and web access.

```text
You are an independent adversarial review board evaluating the complete Agent Harness Systems Engineering Curriculum in this repository.

Do not ask follow-up questions. Inspect evidence, make conservative assumptions, continue when one source/tool fails, and return a decision-complete audit. Do not edit files unless the operator separately asks you to implement repairs.

MISSION

Determine whether this curriculum can defensibly teach a prerequisite-ready learner to design, implement, test, secure, evaluate, operate, compare, and evolve agent harness systems from first principles. Systems such as OpenClaw, Hermes Agent, ChatGPT Work, xAI agent tooling, and frameworks are case studies/adapters, not the curriculum spine.

Review as all of these roles:

1. university computing curriculum/accreditation-alignment reviewer
2. learning-science and assessment-validity specialist
3. agent-harness/runtime architect
4. distributed-systems and durability engineer
5. production/SRE and observability engineer
6. application/platform security and red-team reviewer
7. privacy, governance, accessibility, and responsible-engineering reviewer
8. MCP/A2A/protocol and tool-interface engineer
9. framework/product evidence auditor
10. open-source maintainer and technical documentation reviewer
11. skeptical enterprise adoption board
12. adversarial student/instructor trying to expose unteachable or gameable material

TARGET

Read PROJECT_STATE.md and .mentor/MENTOR_STATE.md first. Then inspect the complete repository, Git status/log, curriculum, reference-harness code/tests, maintenance, workflows/scripts, templates, examples, and historical validations.

The canonical GitHub repository is HaseebAhmed-official/agent-harness-systems-engineering-curriculum. Treat old OpenClaw-only reviews and filenames as historical inputs only.

NON-NEGOTIABLE REVIEW RULES

- Findings first, ordered by severity and supported by exact file/line evidence.
- Verify current claims with current sources; do not trust repository summaries blindly.
- Separate static structure, executable behavior, lab reproduction, learner outcomes, institutional readiness, and enterprise evidence.
- Never infer readiness from file count, writing polish, test count, self-score, or one LLM review.
- Distinguish fact, source-supported inference, reviewer judgment, anecdote, and unknown.
- Downgrade any claim stronger than evidence.
- Check links and run safe repository tests/checks.
- Do not install or execute OpenClaw; it is only a case study unless an authorized fixture is explicitly provided.
- Do not run harmful security tests or access real secrets/data.
- Do not give more than 95% confidence unless every critical surface was inspected and execution evidence supports it.

SOURCE POLICY

Use current primary sources first:

- official specifications, standards, documentation, source repositories, releases, and advisories
- peer-reviewed research and government/academic guidance for durable theory
- maintainer engineering posts for implementation rationale

Required source families to inspect where relevant:

- ABET 2026-2027 Computing Criteria
- ACM/IEEE-CS CS2023
- SWEBOK v4
- NIST AI RMF and Generative AI Profile
- NIST SSDF
- OWASP Agentic AI threats and AI Agent Security Cheat Sheet
- MCP specification/roadmap
- A2A specification
- OpenTelemetry semantic conventions
- official OpenAI Agents guidance/SDK
- official Anthropic agent, context, tools, harness, sandbox, and eval guidance
- Google ADK, Microsoft Agent Framework, LangGraph, and PydanticAI official docs/source
- ReAct, Toolformer, Reflexion, MemGPT, AgentBench, tau-bench, OSWorld, METR, and relevant learning-science research
- current official OpenClaw, Hermes Agent, ChatGPT Work, and xAI evidence for case-study claims

Search high-quality secondary sources, engineering/security blogs, GitHub issues/PRs/discussions, conference material, community forums, and substantive Reddit reports for missing failure modes and adoption experience. Label each as strong secondary, useful anecdotal, weak/unverified, or contradicted. Community evidence may reveal a risk; it cannot override primary behavior/specification evidence without a clear conflict analysis.

MANDATORY EXECUTABLE CHECKS

Run or independently reproduce the safest applicable checks:

1. git status -sb and recent log
2. git diff --check when changes exist
3. local Markdown-link validation
4. JSON validation for curriculum/maintenance/upstream-state.json
5. Python reference-harness compile/import checks
6. PYTHONPATH=reference-harness/src python -m unittest discover -s reference-harness/tests -v (adapt syntax to shell)
7. inspect test adequacy, not only pass/fail
8. inspect OpenClaw drift script/workflow statically and run safe help/fixture paths where feasible
9. check duplicate/stale/conflicting files and obsolete product coupling
10. map stated lab verification states to actual evidence

If a check cannot run, record the exact blocker and residual risk. Do not convert inability to test into a pass.

AUDIT SURFACES

A. Product boundary and vision
- exactly one curriculum product in this repo
- Elite Mentor OS is separate and optional
- stable contracts precede frameworks/products
- OpenClaw is a maintained case study, not hidden spine
- claims match current maturity

B. Curriculum architecture and alignment
- prerequisites through two semesters and tracks
- PLO-to-competency-to-week-to-lab-to-assessment traceability
- constructive alignment and workload feasibility
- stable, standards/adapter, and case-study layers
- no major missing discipline area or unnecessary duplication

C. Technical architecture
- workflow versus agent choice
- provider/model abstraction and deterministic test path
- bounded loop, stop/cancel/budgets/no progress
- typed tools, validation, errors, idempotency, execution boundary
- context selection/provenance/budget
- sessions/events/checkpoints/replay
- memory lifecycle and contamination
- policy, exact approval, identity/requester provenance
- orchestration and multi-agent failure propagation
- durable execution/retry/compensation/recovery
- MCP and A2A interoperability
- observability and evaluation harness
- deployment, tenancy, release, and rollback

D. Reference harness
- code correctness and API design
- tests and missing negative/property/concurrency/security cases
- educational clarity versus accidental production claims
- alignment to Semester 1 labs
- explicit limitations
- suitability as a base for Semester 2 extensions

E. Security, safety, privacy
- direct/indirect prompt injection
- confused deputy and excessive agency
- exact approval/display/execution equivalence
- sandbox/filesystem/network/process/secret boundaries
- memory/persistence and supply chain
- protocol/plugin/server trust
- identity/session/tenant isolation
- duplicate/partial side effects and recovery
- sensitive prompts/logs/traces/artifacts
- authorized red-team containment and cleanup
- residual-risk and stop-ship rules

F. Evaluation and assessment validity
- task/trial/grader/outcome definitions
- repeated trials, variance, leakage, representativeness
- code/model/human/trace/end-state graders
- capability versus regression/security/reliability suites
- practical authenticity, oral defense, assistance disclosure
- delayed unaided changed-task transfer
- critical gates and non-compensable failures
- assessor calibration and measurable agreement
- certification/readiness claim boundaries

G. Pedagogy and learner experience
- extreme-beginner repair without lowering core standard
- retrieval, spacing, worked-example fading, active construction, deliberate practice, feedback/repair, metacognition, transfer
- cognitive-load and pacing risks
- communication, critical thinking, strategic thinking, problem solving, and English integration
- agent use without cognitive outsourcing
- accessibility, low-cost/offline lane, inclusion, and support
- workload and infrastructure realism

H. Instructor and institutional adoption
- handbook, syllabus, teaching guides, decks, labs, examples, templates, rubrics
- clean-environment lab execution and calibration evidence
- instructor expertise and staffing assumptions
- credits/contact/self-study hours
- academic integrity, appeals, accommodations, data governance
- continuous improvement and learner-outcome evidence
- ABET/CS2023/SWEBOK alignment accuracy without false accreditation

I. Enterprise and production adoption
- workload/SLO/capacity/cost/latency
- identities, secrets, data classification, retention/deletion
- deployment, migrations, backups, rollback, incidents
- tenancy and organizational trust
- vendor/protocol/framework lifecycle
- support, ownership, exceptions, audit evidence
- NIST/OWASP/SSDF mapping
- no enterprise-ready claim without observed organizational proof

J. Sources, currency, and cases
- source tiers and claim register
- dated protocol/framework/product facts
- official versus inferred behavior
- case-study balance and selection rationale
- OpenClaw release/advisory maintenance
- Hermes/ChatGPT Work/xAI claim quality
- Grok Bot/community claims rejected unless officially verified
- revalidation triggers and contradiction handling

K. Maintenance and repository quality
- state continuity after reset
- change-control completeness
- automation/human judgment boundary
- no broken links, stale filenames, duplicated docs, dead placeholders, hidden product ownership, or unsupported percentages
- clean release/version/name/license/support boundaries

ADVERSARIAL SCENARIOS

Try to break the program under at least these conditions:

- learner has no paid provider, accelerator, or strong hardware
- learner copies agent-generated work but cannot trace it
- instructor knows AI products but not distributed systems/security
- provider API or structured output changes mid-term
- MCP/A2A version changes or remote capability becomes malicious
- side effect completes but acknowledgment is lost
- task is delivered twice or cancellation races with completion
- memory contains stale, malicious, or cross-user data
- output is correct but end state is unsafe
- benchmark improves but real task outcomes decline
- evaluator/threshold is gamed
- shared/team system is misrepresented as hostile multi-tenant
- critical advisory appears before delivery or release
- network/provider access is unavailable
- accessibility or privacy constraint blocks the default interface
- capstone looks polished but lacks recovery, transfer, or independent evidence
- university requires credit-hour/workload and assessment-moderation evidence
- enterprise requires support, incident, data, governance, and adoption proof

MATURITY DECISIONS

Issue separate verdicts for:

- curriculum architecture completeness
- artifact/content implementation
- reference implementation
- ready for supervised self-study
- ready for instructor-led pilot
- ready for standalone university delivery
- institution-ready adoption claim
- enterprise capability-program claim
- world-class/public benchmark claim

Use `not ready`, `early`, `strong draft`, `pilot-ready`, `release candidate`, or `evidence-proven`. Never collapse these into one optimistic percentage.

OUTPUT FORMAT

1. Executive Verdict
- 3-6 concise paragraphs
- repository commit/date reviewed
- separate maturity verdicts and confidence

2. Gate Scorecard
For G0-G10 from PROJECT_STATE.md: pass/partial/fail/not tested, evidence, blocker, exact retest.

3. Critical Findings
Findings first, ordered P0-P3. For each: title, severity, file/line evidence, external source evidence, failure scenario, exact repair, retest criteria.

4. Claim Audit
Table: claim, location, verdict, evidence tier, corrected boundary, revalidation trigger.

5. Alignment Matrix Audit
Missing or weak PLO/competency/week/lab/assessment links and workload/pacing issues.

6. Reference Harness Audit
Correctness, test gaps, security/production boundaries, educational fit, and exact code repairs.

7. Security/Privacy/Adversarial Audit
Threat coverage, exploitability, controls, evidence, residual risk, and unsafe teaching risks.

8. Evaluation/Assessment Audit
Validity, authenticity, transfer, calibration, critical gates, and certification/readiness limits.

9. Pedagogy/Accessibility/Instructor Audit
Teaching quality, beginner support, cognitive outsourcing, infrastructure equity, accessibility, staffing, and delivery evidence.

10. Enterprise/Operations/Governance Audit
SLOs, durability, deployment, tenancy, incidents, data, governance, support, and claim limits.

11. Source and Case-Study Audit
Best primary/secondary/community sources, conflicts, rejected weak sources, stale facts, and missing cases/evidence.

12. Repository/Clutter/Maintenance Audit
Files to keep, consolidate, retire, or add only when essential; continuity and automation findings.

13. Top Strengths
Only strengths supported by exact evidence.

14. Prioritized Remediation
- Phase 0 stop-ship
- Phase 1 curriculum/reference blockers
- Phase 2 pilot/readiness evidence
- Phase 3 institution/enterprise proof
For every item: owner type, files, evidence, test, dependency.

15. Final Approval Table
Self-study, supervised pilot, university delivery, institution adoption, enterprise program, and world-class claim: approve/conditional/reject with rationale.

16. Residual Uncertainty
What was not inspected/tested and why; what would change confidence.

Do not praise effort, repeat repository marketing, or ask questions. Be precise, skeptical, source-backed, and useful enough that an implementation agent can repair findings without another clarification round.
```
