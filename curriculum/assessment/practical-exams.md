# Practical Exams

## Administration Standard

- Use a fresh disposable environment and unique seeded variants.
- Freeze permitted references, agents, tools, network access, and time before the exam.
- Capture commands, commits, tests, event/trace evidence, and end state.
- Include an individual oral check and a later transfer task.
- Do not expose hidden fixtures in public practice material.
- Stop unsafe or out-of-bound execution immediately.

## Semester 1 Practical: Repair and Extend a Minimal Harness

### Goal and Duration

Assess PLO-1 through PLO-4, PLO-6, PLO-7, PLO-9, and PLO-10 over 4-6 hours plus 20-minute defense.

### Candidate Packet

Provide a variant of the reference harness containing:

- one provider-contract defect
- one loop termination or budget defect
- one schema/tool error defect
- one approval or policy defect
- one incomplete event/evaluation condition
- one changed feature request, such as cancellation, context builder, one-time approval, or persistent-store interface

### Required Work

1. Run the baseline and record observed state.
2. Trace the supplied architecture and rank defects by impact.
3. Add failing regression tests before repairs.
4. Repair defects without coupling core logic to a vendor.
5. Implement the changed feature with tests and events.
6. Run the complete suite and inspect final state.
7. Produce a concise design/failure note and disclose assistance.

### Required Evidence

- prediction and diagnostic log
- scoped diff and tests
- stop/tool/policy/event evidence
- final regression result
- limitations and residual risk
- oral trace of one withheld path

### Critical Failures

- unbounded loop or silent failure path
- invalid tool input reaches a side-effect handler
- approval is not bound to the tested action
- tests are weakened to make implementation pass
- learner cannot explain the repaired control path
- fabricated or copied evidence

### Transfer

Within 3-14 days, require one new provider, tool, policy, or state condition without procedural help.

## Semester 2 Midterm: Attack, Evaluate, and Recover

### Goal and Duration

Assess PLO-4 through PLO-8 over 4-6 hours plus 20-minute defense.

### Candidate Packet

Provide a deployed or locally networked harness with:

- one durable duplicate/partial-side-effect failure
- one prompt-injection or confused-deputy path
- one observability gap
- one misleading output-only grader
- one current MCP or A2A integration boundary

### Required Work

1. Declare authorization and containment.
2. Reproduce the durability failure and reconstruct the event timeline.
3. Execute the bounded exploit and capture blast radius.
4. Repair controls and recovery behavior.
5. Replace or complement the weak grader with trace/end-state evidence.
6. Rerun repeated trials and issue a release verdict against predeclared thresholds.

### Critical Failures

- attack crosses the authorized boundary
- duplicate or irreversible effect is hidden
- mitigation blocks only the exact prompt string without addressing authority
- release verdict ignores critical failures
- product/protocol claim lacks current evidence

## Semester 2 Final: Production Capstone Board

### Goal and Duration

Assess integrated PLO-1 through PLO-10. Run a 30-45 minute board per team plus individual changed tasks.

### Pre-Board Release Packet

- requirements and deterministic baseline
- architecture, data, trust, and failure diagrams
- source/version ledger
- working system and reproducible tests
- evaluation corpus and repeated-trial report
- threat model, exploit, mitigation, and retest
- SLO, latency/cost, deployment, incident, and rollback evidence
- privacy, accessibility, governance, and residual-risk record
- portability comparison
- contribution and assistance record

### Live Board

1. Select a random task from the corpus and observe execution.
2. Inject one withheld provider/tool/state/policy failure.
3. Ask the team to diagnose from evidence before editing.
4. Challenge one security and one evaluation claim.
5. Require rollback or recovery demonstration.
6. Assign each learner an individual control-flow trace.

### Final Transfer

After the board, give a new provider, framework, protocol version, tenancy rule, or tool authority constraint. The learner adapts one capability while preserving behavioral tests and explains semantic gaps.

### Distinction Standard

Distinction requires not more features but stronger evidence: simple justified architecture, effective failure recovery, valid evaluation, accurate assurance limits, clean portability boundaries, and independent judgment under challenge.
