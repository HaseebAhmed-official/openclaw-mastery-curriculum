# Semester 1 Teaching Guide

## Instructor Goal

Teach learners to trace and build the minimal harness contracts themselves. Do not begin with a framework demo and then describe its abstractions as fundamentals.

## Weekly Learning Cycle

1. Retrieval from the prior week without notes.
2. Predict the behavior of a small trace or failure.
3. Teach the mental model, boundary, example, and non-example.
4. Instructor live-traces or builds one minimal slice.
5. Learners complete a guided variation.
6. Learners complete an independent changed-condition task.
7. Review code, trace, end state, security, and explanation against a rubric.
8. Assign the smallest repair and schedule a later recheck.

Use class time for construction, debugging, review, and defense. Readings and short orientation material belong before class.

## Agent-Use Contract

Agents may help locate sources, generate test ideas, critique a design, or explain an error. Learners must disclose material assistance and independently:

- trace control and data flow
- predict behavior before execution
- explain every changed contract
- reproduce and diagnose failures
- justify tests and security boundaries
- complete designated no-agent and oral tasks

If a learner cannot do those things, the artifact is not evidence of mastery.

## Week-by-Week Guide

### Week 1: Discipline Map and Boundaries

- Mental model: model reasoning is one component; the harness controls context, capabilities, state, execution, observation, and evaluation.
- Demonstration: trace one deterministic workflow and one bounded agent loop.
- Misconception to expose: “agent” means any application with an LLM call.
- Evidence: learner labels data/control/trust boundaries and defends whether autonomy is needed.

### Week 2: Reproducible Engineering

- Mental model: reproducibility is an input to every later claim.
- Demonstration: clean environment, test discovery, deterministic fixture, scoped Git diff.
- Misconception: a successful run on the author's machine proves a lab.
- Evidence: clean-clone reproduction and failure log.

### Week 3: Contracts and Test Doubles

- Mental model: depend on a provider contract; use deterministic doubles to test harness logic.
- Demonstration: scripted provider returns final, malformed, tool-call, and error turns.
- Misconception: mocking removes all useful realism or a live API is required for every test.
- Evidence: contract tests and explanation of what the double cannot prove.

### Week 4: Bounded Loop

- Mental model: every autonomous cycle requires observable progress, budgets, cancellation, and explicit termination.
- Demonstration: normal completion, max-turn, repeated-call, and provider-error paths.
- Misconception: the model will reliably decide when to stop.
- Evidence: loop invariant and stop-reason test matrix.

### Week 5: Typed Tools

- Mental model: a tool contract is for model usability, runtime validation, security review, and operations.
- Demonstration: discover, validate, reject, execute, and return a structured error.
- Misconception: type hints or tool descriptions validate runtime arguments.
- Evidence: malformed/unknown/duplicate call tests and improved error design.

### Week 6: Execution Boundary

- Mental model: tool choice and tool execution are different authority layers.
- Demonstration: working directory, environment, timeout, resource, and side-effect boundaries.
- Misconception: a prompt instruction is a sandbox.
- Evidence: execution ownership diagram and bounded failure test.

### Week 7: Context Engineering

- Mental model: context is a selected, budgeted, provenance-bearing working set, not unlimited memory.
- Demonstration: instruction/data separation and an ablation that removes one context source.
- Misconception: more context always improves output.
- Evidence: selection rationale, token budget, truncation test, and ablation result.

### Week 8: Midterm Trace and Debug

- Use unseen code with seeded failures in at least three layers.
- Require prediction before tests and root-cause explanation after repair.
- Do not grade only the final passing state.

### Week 9: Sessions and Events

- Mental model: state is reconstructed from identified records; transcript text alone is insufficient.
- Demonstration: append events and rebuild a session timeline.
- Misconception: conversation history is equivalent to durable task state.
- Evidence: schema, ordering, identity, artifact reference, and reconstruction test.

### Week 10: Checkpoint and Replay

- Mental model: checkpointing bounds lost work; replay semantics depend on determinism and side effects.
- Demonstration: crash between planned and completed side effect.
- Misconception: retrying a failed turn is always safe.
- Evidence: resume test and explicit exactly-once limitation.

### Week 11: Policy and Approval

- Mental model: approval must bind actor/session, capability, exact arguments, scope, and freshness.
- Demonstration: stale or display-mismatched approval attack.
- Misconception: a generic “allow tool” click authorizes every later argument.
- Evidence: deny-default and confused-deputy tests.

### Week 12: Memory Foundations

- Mental model: memory is governed retained state with retrieval and deletion quality, not magical recall.
- Demonstration: useful memory, stale memory, malicious memory, and deletion.
- Misconception: retrieval relevance implies truth or authorization.
- Evidence: retention/provenance policy and measured retrieval task.

### Week 13: Observability

- Mental model: traces, metrics, logs, events, and artifacts answer different questions and share correlation.
- Demonstration: reconstruct one failure without reading source first.
- Misconception: verbose logs equal observability.
- Evidence: correlated timeline with sensitive-data review.

### Week 14: Evaluation Foundations

- Mental model: an eval harness surrounds the agent harness with tasks, trials, graders, and decision thresholds.
- Demonstration: one output-only grader misses a bad side effect; end-state check catches it.
- Misconception: one successful demo or benchmark score proves correctness.
- Evidence: repeated-trial suite and failure taxonomy.

### Week 15: Integration Review

- Freeze requirements before review.
- Review interfaces, invariants, failure propagation, security, tests, and evidence.
- Require learners to delete unnecessary abstractions and document intentional limitations.

### Week 16: Practical and Transfer

- Give a changed tool, provider, policy, or state condition not rehearsed verbatim.
- Require individual execution, defense, and a delayed retest.
- Grade the reasoning path, evidence, and repair as well as output.

## Feedback and Remediation

- Return critical safety or conceptual feedback before the learner builds on it.
- Label feedback by competency and evidence level.
- Prescribe one repair task, not another long explanation.
- Retest with changed conditions.
- Escalate persistent foundation gaps back to the prerequisite bridge.

## Accessibility and Inclusion

- Provide text alternatives for diagrams and captions/transcripts for audiovisual material.
- Do not make speed of typing or spoken English accent a proxy for engineering mastery.
- Allow equivalent accessible interfaces while preserving the same technical evidence.
- Publish tool, compute, network, and cost requirements before the course.
- Supply deterministic/offline paths for core labs.

## Instructor Readiness Gate

Before delivery, the instructor must execute every required lab from a clean environment, preserve expected evidence, rehearse seeded failures, calibrate grading anchors, verify current sources, and document known platform differences.
