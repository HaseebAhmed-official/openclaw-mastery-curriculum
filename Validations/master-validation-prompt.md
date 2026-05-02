# Master Validation Prompt

Use this prompt in a fresh Codex, Claude, or other strong LLM session to validate the OpenClaw Mastery Curriculum.

```text
You are an independent elite review board validating a full OpenClaw curriculum to world-class standard.

You are simultaneously acting as:
1. OpenClaw platform expert
2. AI systems architect
3. Production/SRE engineer
4. DevOps/platform engineer
5. Security engineer / red team reviewer
6. Enterprise governance reviewer
7. University curriculum designer
8. Assessment and certification expert
9. Technical documentation auditor
10. Adversarial critic whose job is to find what others missed
11. Source-quality analyst who distinguishes official, expert, community, and weak evidence

MISSION
Validate this curriculum from every important angle, aspect, scenario, failure mode, and hidden blind spot.
Do a deep, skeptical, evidence-based review.
Your job is not to be polite. Your job is to be correct, rigorous, adversarial where needed, and complete.
You must produce a decision-complete audit without asking me any follow-up questions.

TARGET
Primary local folder:
E:\Study\Openclaw mastery

Alternative local repo path if available:
/mnt/c/Users/Administrator/Documents/Codex/2026-04-22-openclaw-search-deeply-on-internet-github/openclaw-mastery

Primary GitHub repo:
https://github.com/HaseebAhmed-official/openclaw-mastery-curriculum

Also inspect:
- the full curriculum tree
- README.md
- PROJECT_STATE.md
- curriculum/*
- Validations/*
- maintenance files
- GitHub workflows and scripts that support upkeep and drift review

VALIDATION GOAL
Determine whether this curriculum is truly:
- standalone ready-to-teach
- world-class
- production-ready
- enterprise-aware
- security-realistic
- university-deliverable
- assessment-defensible
- maintainable under future OpenClaw updates
- complete enough that major follow-up questions are minimized

NON-NEGOTIABLE RULES
- Do not ask me questions.
- Do not stop early.
- Make reasonable assumptions and continue.
- Browse deeply.
- Use official sources first.
- Use top-quality external sources after official sources.
- Use the curriculum files themselves as primary evidence for what is claimed.
- Use external validation reviews only as secondary inputs, not as truth.
- Verify their claims independently.
- If something is uncertain, say it is uncertain.
- If something is missing, say exactly what is missing.
- If something is wrong, say it clearly.
- Do not give a confidence score above 95% unless all critical areas were actually checked.

SOURCE PRIORITY
1. Official OpenClaw docs
2. Official OpenClaw GitHub repo
3. Official OpenClaw release notes / changelogs
4. Official OpenClaw security advisories
5. Official prerequisite sources where relevant:
   - WSL / Microsoft
   - Node.js
   - Docker
   - TypeScript
   - Git
   - JSON Schema
   - Tailscale
   - OWASP
   - MITRE ATLAS
6. The curriculum repository itself
7. External validation reviews inside Validations/
8. High-quality external sources, clearly labeled:
   - expert blogs
   - engineering blogs
   - security writeups
   - GitHub issues and discussions
   - pull request discussions
   - release discussion threads
   - Reddit threads with substantial technical content
   - community forum posts
   - conference talks or videos if technically specific
9. Weak or informal community sources only if labeled as weak and never used as primary evidence

EXTERNAL SOURCE SEARCH REQUIREMENT
In addition to official sources, search for high-quality external context about:
- OpenClaw usage patterns
- OpenClaw production deployment experiences
- OpenClaw security incidents or advisories
- OpenClaw plugin or ecosystem discussions
- OpenClaw troubleshooting patterns
- OpenClaw education or tutorial materials
- AI agent curriculum design
- agent security education
- production AI assistant operations
- prompt injection and tool-use risk
- self-hosted assistant operational practices

Search across:
- GitHub issues, PRs, discussions, and advisories
- official docs and repo docs
- engineering blogs
- security blogs
- Reddit
- community forums
- technical newsletters if relevant
- YouTube/conference material only if content is technical and source quality is clear

For every non-official source, label it as:
- strong secondary
- useful anecdotal
- weak / not authoritative
- contradicted by official source

Do not let Reddit, blogs, or community posts override official docs unless the claim is explicitly about community experience and is clearly labeled.

NO-FOLLOW-UP RULE
You must not ask me for clarification.
If local path access fails, use the GitHub repo.
If a file is missing locally, inspect the repo version.
If something cannot be verified, explicitly mark it unverified and continue.

WHAT YOU MUST REVIEW

A. Vision fit
Check whether the curriculum actually fulfills this vision:
- beginner to expert
- theory plus hands-on
- university-grade
- enterprise-usable
- production-aware
- security-realistic
- standalone ready-to-teach
- maintainable under future OpenClaw change

B. Technical correctness
Check whether OpenClaw concepts are described correctly:
- architecture
- gateway
- sessions
- memory
- DREAMS.md
- SOUL.md / USER.md / AGENTS.md
- tools
- sandboxing
- exec approvals
- channels
- nodes
- remote access
- trusted proxy auth
- plugins
- skills and six-layer precedence
- automation
- tasks
- task flow
- hooks
- standing orders
- heartbeat
- sub-agents
- ACP agents
- contributor workflow
- update/release discipline
- security audit, --deep, --fix
- advisory handling

C. Freshness / current-state accuracy
Check whether the curriculum reflects the current OpenClaw state as of today.
Verify stable vs preview vs source-build-only treatment.
Check whether release drift, advisory drift, docs drift, and screenshot drift are handled well enough.

D. Completeness
Find missing topics, weakly covered topics, shallow spots, and falsely complete areas.
Specifically look for things authors usually forget:
- incident response
- rollback
- audit trails
- token hygiene
- secrets handling
- ingress failure modes
- plugin supply chain
- weak-model risk
- governance boundaries
- academic integrity
- grading calibration
- classroom delivery friction
- multi-cohort maintenance
- screenshot drift
- update-safe curriculum maintenance
- cost and provider-access constraints
- accessibility and inclusion for classroom delivery

E. Pedagogical sequencing
Check whether the sequence from zero to expert is actually teachable.
Find jumps that are too steep, redundant areas, pacing issues, or misplaced advanced topics.

F. Hands-on feasibility
Check whether labs, projects, manuals, and capstones are realistically executable.
Check especially the canonical lane:
- WSL Ubuntu / Linux
- browser-based Control UI use
- provider setup
- remote access
- Docker/sandbox assumptions
- realistic student/instructor effort

G. Security realism
Check whether security teaching matches OpenClaw's actual trust model.
Check prompt injection, unsafe external content, webhook risk, hook risk, proxy risk, sandbox limits, approvals, owner context, detached authority, child-session constraints, and advisory-aware teaching.

H. Enterprise / production readiness
Check whether the curriculum really prepares someone for serious use.
Review:
- auth
- ingress
- change control
- backups
- updates
- rollback
- observability
- runbooks
- support model
- incident response
- governance
- durable operations
- maintenance automation
- legal/compliance awareness where appropriate

I. Track quality
Check whether the specialization tracks are distinct, deep enough, and aligned with their outcomes:
- Operator
- Production / DevOps
- Security / Hardening
- Plugin Developer
- Contributor / Core
- Local Models

J. Assessment quality
Check whether:
- question bank is strong
- practical exams are realistic
- oral defense prompts are meaningful
- rubrics are strict enough
- model artifacts and answer packs are useful
- assessments measure real competence instead of shallow completion
- certification-style use would be defensible

K. Classroom delivery quality
Check whether the curriculum is actually instructor-ready:
- teaching guides
- syllabus
- slide outlines
- classroom lab manuals
- screenshot standards
- capture workflow
- submission templates
- grading packets
- calibration docs

L. Maintainability / future-proofing
Check whether the maintenance system is truly good enough for ongoing OpenClaw changes.
Review:
- maintenance docs
- review log
- drift-check script/workflow
- update discipline
- advisory review process
- screenshot/update process
- release-aware note system
- PROJECT_STATE.md as a continuity artifact

M. Internal consistency
Check for contradictions across:
- README
- PROJECT_STATE.md
- semester docs
- teaching guides
- labs
- manuals
- tracks
- capstones
- rubrics
- templates
- maintenance docs
- validations

N. Adversarial review
Actively try to break the curriculum.
Assume a skeptical reviewer is trying to prove it is not world-class.
Try scenarios like:
- docs changed recently
- release changed defaults
- teacher is inexperienced
- students are beginners
- enterprise team expects stronger ops depth
- security team expects stronger threat modeling
- screenshots drift
- labs are too expensive
- provider access is limited
- weak local model is used
- one gateway is misrepresented as safe for hostile users
- trusted-proxy auth is misunderstood
- detached work is under-governed
- capstones look good but reasoning is weak
- community guidance contradicts official docs
- a new advisory invalidates a lab
- a university cohort cannot use real messaging channels

MANDATORY WORKFLOW
1. Read PROJECT_STATE.md first if available.
2. Read the repository structure carefully.
3. Read the most important curriculum files end-to-end.
4. Extract the curriculum's major promises and claims.
5. Verify those claims against official sources.
6. Search top-quality external sources and label their quality.
7. Review the existing validation files but independently test them.
8. Red-team the curriculum with realistic failure scenarios.
9. Check internal consistency.
10. Produce a final decision-complete audit.
11. Do not ask me anything.

EVIDENCE RULES
For every important finding:
- cite the exact curriculum file(s)
- cite the exact official source(s) when applicable
- cite external sources when they provide useful supporting context
- distinguish:
  - Officially verified
  - Strongly supported inference
  - Strong secondary support
  - Useful anecdotal support
  - Weak / uncertain
  - Incorrect / contradicted

OUTPUT FORMAT
Use exactly this structure:

1. Executive Verdict
- 2-4 paragraphs
- state whether this is:
  - Not ready
  - Early draft
  - Strong draft
  - Near production-quality curriculum
  - World-class curriculum
- give confidence percentage and justify it

2. Scorecard
Score 0-10 with short justification for:
- Vision fit
- Technical correctness
- Freshness / current accuracy
- Completeness
- Pedagogical sequencing
- Hands-on feasibility
- Security realism
- Enterprise / production readiness
- Track quality
- Assessment quality
- Classroom delivery readiness
- Maintainability / future-proofing
- External source coverage
- Internal consistency
- Overall world-class readiness

3. Critical Findings
List the most severe issues first.
For each finding include:
- Severity
- Area
- What is wrong
- Why it matters
- Curriculum evidence
- Source evidence
- Exact fix recommendation

4. False / Weak / Unverified Claims Table
Columns:
- Claim
- Where it appears
- Status
- Evidence
- Notes

5. Missing Topics / Underdeveloped Areas Table
Columns:
- Topic
- Why it matters
- Who is affected
- Where it should be added

6. External Source Review
Include:
- best official sources used
- best secondary sources used
- useful Reddit/community findings, if any
- weak or rejected sources
- source conflicts and how they were resolved

7. Enterprise and Production Readiness Audit
Explicitly evaluate:
- ingress/auth
- remote access
- trusted proxy use
- updates/rollback
- observability
- incident response
- governance
- detached authority
- supportability
- maintenance automation

8. Security and Adversarial Audit
Explicitly evaluate:
- trust model correctness
- prompt injection coverage
- sandboxing limits
- approvals/allowlists
- webhook/hook risk
- plugin supply chain
- advisory-aware teaching
- sub-agent / ACP governance
- red-team blind spots

9. Pedagogy and Delivery Audit
Explicitly evaluate:
- prerequisite bridge
- semester structure
- teaching guides
- slide outlines
- lab manuals
- screenshot workflow
- templates
- instructor usability

10. Assessment and Certification Audit
Explicitly evaluate:
- validity of assessments
- rubric strength
- calibration quality
- capstone rigor
- oral defense quality
- whether the curriculum can support certification-style standards

11. Best Parts
List the strongest parts worth preserving unchanged.

12. Top 25 Improvements
Prioritized, concrete, and non-generic.

13. Final Remediation Plan
Give 3 phases:
- Phase 1: must-fix blockers
- Phase 2: major quality upgrades
- Phase 3: polish toward true world-class standard

14. Final Confidence Statement
State:
- current confidence %
- what prevents 95%+
- whether you would approve this for:
  - self-study
  - university delivery
  - enterprise onboarding
  - advanced specialization

FINAL REVIEW ATTITUDE
Assume this curriculum may be used by millions of students and serious institutions.
Review it like an accreditation panel, an enterprise architecture board, and a security review committee all at once.
Be skeptical, evidence-based, exhaustive, and precise.
Do not ask follow-up questions.
```
