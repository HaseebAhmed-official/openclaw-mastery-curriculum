# Answer-Key Guidance

## Purpose

Build defensible grading anchors without forcing one architecture, freezing current product facts, or publishing hidden-transfer answers.

## Key Structure

For each item record:

- competency and evidence level
- essential concepts/invariants
- acceptable alternatives and required assumptions
- evidence expected: code, trace, end state, source, measurement, or oral explanation
- critical misconceptions or unsafe responses
- likely partial-credit boundaries
- follow-up or changed-condition probe
- source/version date for time-sensitive facts

## Strong-Answer Pattern

A strong answer usually:

1. defines the exact problem and boundary
2. selects the simplest valid design
3. traces control, data, state, and authority
4. states invariant, failure, and recovery behavior
5. provides inspectable evidence
6. addresses security/privacy and operations
7. distinguishes fact, inference, decision, and unknown
8. rejects claims stronger than evidence
9. adapts when one condition changes

## Core Anchor Expectations

- **Architecture:** separates model, harness, tools/execution, state, operator, and external systems; justifies autonomy.
- **Tools/policy:** runtime-validates arguments and binds authority to exact behavior; descriptions/prompts are not controls.
- **Durability:** separates internal task state from external end state; does not claim exactly-once without proof.
- **Memory/context:** tracks provenance, trust, freshness, isolation, budget, retention, and deletion.
- **Protocols:** distinguishes interoperability/discovery from authorization and semantic compatibility.
- **Security:** traces attack preconditions and authority, layers prevention/detection/recovery, and states residual risk.
- **Evaluation:** defines tasks/trials/graders, repeats nondeterministic trials, and checks trace/end state where actions matter.
- **Operations:** defines SLO, degradation, incident, migration, backup, rollback, owner, and evidence.
- **Product cases:** dates claims and labels observed/documented/source-visible/inferred/unknown.

## Critical No-Credit Conditions

Fabricated evidence, inability to explain submitted work, unsafe out-of-scope execution, hidden critical authority, evaluation leakage, or readiness/security claims that contradict known evidence trigger the Master Rubric gate regardless of wording.

## Key Maintenance

Revalidate current sources before use, rotate task details, preserve old keys only with the assessment version they graded, and repair keys when assessor disagreement reveals ambiguity.
