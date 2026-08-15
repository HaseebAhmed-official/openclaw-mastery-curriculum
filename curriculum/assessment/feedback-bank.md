# Feedback Bank

Use evidence-specific language and replace brackets.

## Strong Evidence

- Your strongest evidence is `[artifact/test]` because it connects the invariant to both the injected failure and repaired end state.
- You justified the agentic boundary against a deterministic baseline rather than assuming more autonomy was better.
- The release verdict is credible because criteria were declared before trials and critical failures were not averaged away.
- Your claim boundary is accurate: you state what the test proves and what remains unverified.

## Repair Required

- The success path works, but `[failure]` has no diagnosis or recovery evidence. Reproduce it, add a regression test, and rerun under `[changed condition]`.
- The tool schema is descriptive but does not prevent `[invalid input]` from reaching execution. Add runtime validation and a negative test.
- Approval is shown, but it is not demonstrably bound to `[session/tool/arguments/freshness]`. Add an argument-substitution test.
- The evaluation grades final text while the task changes state. Add event/trace and end-state graders and revise the release decision.
- The product/framework claim lacks a dated primary source. Label it unknown or verify it before reuse.

## High Severity

- This cannot pass because a material side effect is reachable without an enforceable authority boundary.
- This cannot pass because the learner cannot trace the submitted control path or explain the tests.
- This cannot pass because critical failures were omitted, downgraded, or hidden by an average score.
- This cannot pass because the security/tenancy/readiness claim exceeds the tested boundary.
- This cannot pass because the evidence is fabricated, unverifiable, or misrepresented.

## Transfer Prompts

- Preserve the behavior after changing `[provider/tool/protocol/policy/state store]`.
- Diagnose the same symptom when the root cause moves to a different layer.
- Retest the mitigation against a paraphrased or indirect attack.
- Reassess the design under `[team use/100x workload/no network/irreversible tool/new version]`.

## Claim-Level Language

- “P0 structural evidence only; no behavior claim yet.”
- “Works in the declared fixture; clean-environment reproduction remains.”
- “Representative failures pass; longer-running/independent evidence remains.”
- “Production judgment demonstrated in simulation; real organizational adoption is not proven.”
