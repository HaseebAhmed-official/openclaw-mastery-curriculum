# Assessment Map

## Assessment Philosophy

Assessment must determine whether a learner can reason, implement, verify, debug, secure, operate, and transfer capability. It must not reward document volume, framework memorization, or agent-produced polish without understanding.

Use multiple measures because no single quiz, benchmark, capstone, or oral defense can establish all program outcomes.

## Assessment System

### Diagnostic Assessment

- prerequisite retrieval and changed-condition tasks
- code and architecture tracing
- source-quality and uncertainty check
- no grade contribution; routes repair work

### Formative Assessment

- retrieval prompts
- prediction before execution
- worked-example completion and fading
- code reviews and design critiques
- failure-injection drills
- repair tasks with rapid feedback

### Practical Assessment

- reproducible implementation tasks
- tests, traces, logs, state, and end-result evidence
- hidden or changed conditions
- tool and assistance disclosure
- explicit failure modes and rollback

### Design and Security Review

- architecture decision records
- threat models and abuse cases
- operational and governance evidence
- reviewer challenge and oral defense

### Evaluation Assessment

- task corpus design
- repeated trials and variance
- grader selection and disagreement analysis
- trace plus end-state inspection
- regression threshold and cost/latency tradeoffs

### Transfer Assessment

- delayed and unaided
- altered tool, provider, protocol, failure, or policy condition
- requires explanation of what transferred and what changed

### Capstone and Defense

- integrated working harness
- attack-and-repair exercise
- evaluation report
- production operations evidence
- framework/product portability exercise
- independent oral defense and changed-task retest

## Program Outcome Alignment

| Outcome | Primary direct evidence | Supporting evidence |
| --- | --- | --- |
| PLO-1 | prerequisite practicals; debugging exam | concept checks; design notes |
| PLO-2 | architecture decision exercise; oral defense | pattern comparison; case critique |
| PLO-3 | minimal-harness implementation practical | code review; trace explanation |
| PLO-4 | checkpoint/replay and failure-recovery lab | state design review; incident exercise |
| PLO-5 | MCP/A2A adapter and portability test | protocol quiz; framework comparison |
| PLO-6 | threat lab, exploit evidence, mitigation retest | threat model; security viva |
| PLO-7 | evaluation corpus and repeated-trial report | grader critique; regression review |
| PLO-8 | production simulation and incident recovery | SLO/cost review; deployment defense |
| PLO-9 | design review, team assessment, ethics/governance defense | written communication rubric |
| PLO-10 | unfamiliar-system audit and delayed transfer | source audit; comparative case study |

## Curriculum Alignment Matrix

| Outcome | Primary teaching locations | Required labs | High-stakes evidence |
| --- | --- | --- | --- |
| PLO-1 | Bridge B0-B11; Semester 1 weeks 1-3, 8 | LAB-A1 through LAB-A4 | prerequisite exit; midterm trace/debug |
| PLO-2 | Semester 1 weeks 1, 15; Semester 2 weeks 1-2 | LAB-A4, LAB-C1 | architecture review; capstone agentic justification |
| PLO-3 | Semester 1 weeks 3-7, 11-12, 15 | LAB-B1 through LAB-B6 | minimal-harness final practical |
| PLO-4 | Semester 1 weeks 9-10; Semester 2 weeks 3-4 | LAB-B5, LAB-C2 through LAB-C3 | crash/recovery practical; capstone failure injection |
| PLO-5 | Semester 2 weeks 5-6, 13 | LAB-C4 through LAB-C5; LAB-D1 through LAB-D3 | protocol adapter and portability test |
| PLO-6 | Semester 1 weeks 6, 11-12; Semester 2 weeks 7-8, 11-12 | LAB-A4, LAB-B6, LAB-C3 through LAB-C6, LAB-C9 | attack-and-repair exam; security board |
| PLO-7 | Semester 1 weeks 13-14; Semester 2 weeks 9-10 | LAB-B7, LAB-C7 through LAB-C8 | evaluation corpus/report; release gate |
| PLO-8 | Semester 2 weeks 1, 3, 10-12, 15 | LAB-C2, LAB-C7 through LAB-C9 | incident/rollback evidence; capstone operations board |
| PLO-9 | threaded through design reviews, labs, teams, source and risk decisions | all labs' evidence/defense sections | written/oral defense; governance review |
| PLO-10 | Semester 2 weeks 13-14, 16; case studies and tracks | LAB-D1 through LAB-D5 | unfamiliar-system audit; delayed portability task |

An institution should map local course/credit outcomes to this matrix and record any omitted evidence. A topic mention without direct assessment does not count as outcome coverage.

## Semester 1 Assessment

| Component | Weight | Minimum gate |
| --- | ---: | --- |
| Retrieval and concept checks | 10% | 70% aggregate |
| Foundation and component labs | 30% | Every critical lab passes |
| Midterm trace/debug practical | 15% | 70%; no critical tracing failure |
| Design and security reviews | 15% | No unresolved critical finding |
| Minimal-harness final practical | 20% | All required contracts work under changed input |
| Oral defense and delayed transfer | 10% | Independent explanation and transfer pass |

## Semester 2 Assessment

| Component | Weight | Minimum gate |
| --- | ---: | --- |
| Advanced labs and failure injections | 25% | Every critical lab passes |
| Evaluation and security practical | 15% | No invalid evaluation or unresolved critical risk |
| Architecture/operations reviews | 15% | Defensible tradeoffs and recovery evidence |
| Specialization evidence | 10% | Track rubric passes |
| Capstone system and evidence bundle | 25% | All capstone release gates pass |
| Oral defense and delayed portability task | 10% | Independent defense and transfer pass |

Weights can be adapted locally, but critical safety, implementation, evaluation, and transfer gates cannot be averaged away by other marks.

## Required Artifact Contract

Every substantial submission identifies:

- task, requirements, constraints, and acceptance criteria
- source and version baseline
- design and alternatives considered
- implementation and tests
- trace, event, and end-state evidence
- security/privacy implications
- failure injection and repair
- latency/cost/reliability evidence where relevant
- agent/tool assistance received
- unresolved risks and next test

## Automatic Failure Conditions

- fabricated or unverifiable evidence
- hidden agent authorship presented as unaided learner work
- inability to trace or explain the submitted system
- destructive or high-impact execution outside the authorized lab boundary
- credentials or protected data in submissions
- benchmark leakage or changing success criteria after seeing results
- security claims that omit known trust boundaries or residual risk
- single-trial claims for nondeterministic behavior where repeated evidence is required
- missing rollback or recovery in a production-readiness claim

## Assessor Calibration

Before grading high-stakes work, assessors independently score common anchor submissions, compare severity and outcome decisions, resolve rubric ambiguity, and record agreement. Institution-ready claims require measured inter-rater evidence, not only a calibration guide.

Use the [Assessment Assets](assessment/index.md), [Master Rubric](rubrics/master-rubric.md), and [Competency Framework](competency-framework.md).
