# Core Lab Guides

## Common Rules

- Work in an isolated learning branch or disposable copy.
- Record OS, Python, Git commit, command, exit status, and assistance used.
- Predict expected behavior before execution.
- Preserve tests, selected event/trace evidence, and final state; redact secrets and unnecessary personal data.
- Use `reference-harness/` as the baseline unless the instructor supplies an equivalent fixture.
- Never perform harmful side effects outside the authorized lab boundary.
- Complete the transfer variation without step-by-step agent guidance.

Baseline command from `reference-harness/`:

```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -v
```

Use the shell-equivalent `PYTHONPATH=src python -m unittest discover -s tests -v` on Linux/WSL.

## LAB-A1: Reproducible Python and Git Environment

### Objective

Prove that the learner can reproduce, test, change, and inspect the reference project safely.

### Prerequisites and Time

Bridge B0-B3; 60-90 minutes.

### Procedure

1. Record Python and Git versions and active working directory.
2. Run the baseline suite and capture all eight test outcomes.
3. Create a learning branch.
4. Add one harmless assertion to an existing test, make it fail intentionally, then correct it.
5. Inspect status and diff; explain every changed line.
6. Reproduce from a clean clone or fresh disposable copy without relying on an unrecorded global dependency.

### Required Evidence

- environment record and exact commands
- failing and passing test output
- scoped diff and commit identifier
- clean reproduction result
- explanation of what the test does and does not prove

### Pass Gate and Transfer

Pass when another person can reproduce the result and the learner explains the diff unaided. Transfer: repeat after changing shell, path, or Python minor version and diagnose any difference.

## LAB-A2: API, Process, and Failure Tracing

### Objective

Trace request, provider, tool, event, and state boundaries and classify a failure correctly.

### Procedure

1. Draw the call path from `Harness.run()` through provider completion and optional tool execution.
2. Run `test_valid_tool_call_is_recorded_and_returned_to_provider` and map each event/message to source code.
3. Seed one provider exception and one malformed tool response in a disposable test.
4. Predict stop reason and state before running.
5. Verify the event timeline and explain whether the defect is provider, contract, tool, policy, or state related.

### Required Evidence

- annotated control/data-flow diagram
- prediction versus observation table
- event timeline and root-cause classification
- repair or containment test

### Pass Gate and Transfer

Pass when the learner identifies the correct layer and rejects at least one plausible but wrong diagnosis. Transfer: diagnose a failure where the final text looks valid but the event/end state is wrong.

## LAB-A3: Test-Driven Defect Repair

### Objective

Repair a defect with a regression test that discriminates cause from symptom.

### Procedure

1. Instructor selects one bounded mutation: remove boolean rejection for numeric schemas, weaken approval binding, change a budget comparison, or omit a lifecycle event.
2. Learner reproduces the behavior without editing first.
3. Add the smallest failing test that captures the violated invariant.
4. Repair the implementation and run the full suite.
5. Explain why a superficial alternative fix would still fail.

### Required Evidence

- defect reproduction
- red/green test evidence
- root cause and rejected alternatives
- full regression result

### Pass Gate and Transfer

Pass when the regression fails on the mutation and passes on the repair without weakening another gate. Transfer: handle a second mutation in a different layer.

## LAB-A4: Baseline Threat Model

### Objective

Construct a concrete threat model for the reference harness and connect threats to evidence.

### Procedure

1. Identify assets, actors, entry points, trust boundaries, side effects, and sensitive records.
2. Model at least: malicious user input, compromised provider output, malformed tool arguments, stale approval, malicious tool, event leakage, and state tampering.
3. Rank likelihood and impact under declared assumptions.
4. Map preventive, detective, and recovery controls.
5. Demonstrate one safe exploit in a disposable test and propose a mitigation/retest.

### Required Evidence

- data/trust diagram
- abuse-case table with preconditions and blast radius
- exploit trace
- mitigation test and residual risks

### Pass Gate and Transfer

Pass when threats are tied to actual authority and data flow rather than generic labels. Transfer: revise for a network provider or persistent database.

## LAB-B1: Deterministic Provider Adapter

### Objective

Implement a provider contract and deterministic test double without coupling the harness to one vendor.

### Procedure

1. Trace `Provider`, `ModelTurn`, and `ScriptedProvider`.
2. Add contract tests for final response, tool call, malformed turn, refusal representation, and provider exception.
3. Implement a second deterministic provider that selects turns from input patterns or fixtures.
4. Keep vendor-specific fields outside the stable runtime contract.
5. State which live-provider behaviors the double cannot validate.

### Evidence and Pass Gate

Preserve the adapter, contract tests, request capture, and limitation note. Pass when either deterministic provider can drive the same runtime tests. Transfer: design, but do not necessarily call, a current network-provider adapter from official API docs.

## LAB-B2: Bounded Agent Loop

### Objective

Prove that all loop paths terminate or explicitly transfer control.

### Procedure

1. Enumerate every `StopReason` and its trigger.
2. Add tests for cancellation, provider error, tool budget, turn budget, and no progress.
3. Create a script that alternates two useless calls and decide whether fingerprint-only detection is sufficient.
4. Add one justified progress signal or document why the current policy intentionally remains simple.
5. Confirm `run.finished` is emitted on every path.

### Evidence and Pass Gate

Pass with a state-machine diagram, branch-complete test matrix, and no unbounded path. Transfer: add a wall-clock or cost budget without hiding nondeterminism in tests.

## LAB-B3: Typed Tool Registry

### Objective

Design model-usable and runtime-verifiable tool contracts.

### Procedure

1. Add a read-only tool and a side-effecting tool with schemas and structured outputs.
2. Test missing, extra, wrong-type, unknown, handler-error, and duplicate-registration cases.
3. Improve one error so a model can repair its call without exposing sensitive internals.
4. Identify limits of the teaching schema validator and define the boundary to a full JSON Schema implementation.
5. Review descriptions for ambiguity and overlapping tools.

### Evidence and Pass Gate

Pass when invalid input cannot reach the handler, side-effect metadata is accurate, and errors support repair. Transfer: redesign a poorly shaped real API as a bounded tool.

## LAB-B4: Context Assembly and Budget

### Objective

Implement explicit context selection, provenance, and budget behavior.

### Procedure

1. Replace direct `session.messages` forwarding with a `ContextBuilder` contract.
2. Separate trusted system instructions from user/tool/retrieved data.
3. Attach source identity, freshness, and trust label to selected context records.
4. Enforce a deterministic test budget and declare truncation order.
5. Run ablations: remove instructions, stale memory, recent tool result, and irrelevant long text.

### Evidence and Pass Gate

Pass with selection tests, provenance evidence, truncation tests, and an ablation report. Transfer: adapt selection for a long-running session with one malicious retrieved record.

## LAB-B5: Session, Event Log, Checkpoint, and Replay

### Objective

Make task state inspectable and recoverable without claiming impossible replay guarantees.

### Procedure

1. Define session and attempt identity.
2. Version event/checkpoint schemas and record artifact references instead of embedding large payloads.
3. Simulate crash before tool start, during handler failure, and after tool completion but before next model turn.
4. Reconstruct the timeline and choose retry, compensate, resume, or human review.
5. Test a schema migration and a corrupted checkpoint.

### Evidence and Pass Gate

Pass when recovery decisions prevent silent duplicate side effects and every state transition is auditable. Transfer: replace in-memory state with a transactional store interface and test process restart.

## LAB-B6: Policy, Approval, and Execution Boundary

### Objective

Bind authority to exact behavior and separate model choice from execution permission.

### Procedure

1. Test tool allowlist and exact session/tool/argument approval behavior.
2. Attempt argument substitution, stale-session reuse, approval-display mismatch, and unknown tool.
3. Define side-effect risk classes and expiry/one-time-use requirements.
4. Design an execution interface with working directory, environment, timeout, resource, filesystem, and network controls.
5. State which controls the local teaching runtime does not implement.

### Evidence and Pass Gate

Pass when unauthorized side effects fail closed and approval evidence identifies the exact requested action. Transfer: add one-time approval consumption or a two-person approval class.

## LAB-B7: Observability and Evaluation Baseline

### Objective

Connect runtime evidence to a repeatable decision about behavior.

### Procedure

1. Define trace/span or equivalent correlation across run, model turn, policy, and tool events.
2. Redact or hash sensitive fields while preserving diagnostic value.
3. Create at least five tasks covering success, repairable malformed call, denial, no progress, and provider failure.
4. Run at least three trials per nondeterministic task or justify a deterministic fixture.
5. Combine output, event/trace, and end-state graders.
6. Define a regression threshold before inspecting final results.

### Evidence and Pass Gate

Pass with corpus, trial records, grader rationale, failure taxonomy, and threshold decision. Transfer: add latency/cost fields and explain measurement error.
