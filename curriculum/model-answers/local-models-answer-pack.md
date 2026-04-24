# Local Models Answer Pack

## Target standard

This track should produce a sober local or hybrid-model architecture, not a sovereignty slogan.

## Model capstone answer shape

1. State the business or institutional reason for local or hybrid operation.
2. Document hardware, latency, throughput, and quality assumptions.
3. Explain fallback strategy and what happens when the local path is too weak or too slow.
4. Address safety: model strength on tool-enabled tasks, containment expectations, and degraded-mode behavior.
5. Compare the chosen design against a hosted or hybrid alternative honestly.

## Strong evidence bundle

- hardware and capacity assumptions
- latency/quality tradeoff table
- fallback decision rule
- safety note on weak-model risk
- recommendation with explicit limits

## Strong-answer signals

- acknowledges that local control increases operational burden
- differentiates privacy, sovereignty, cost, and performance motivations
- includes a fail-safe or downgrade path
- does not oversell weak local models for tool-enabled authority

## Weak-answer signals

- local chosen because it feels more independent, with no operational math
- no fallback path
- no safety reasoning for weak or inconsistent models
- no comparison to hosted or hybrid alternatives

## Oral defense prompts

- When is local the wrong answer even if you have the hardware?
- What workload would you keep on a hosted model and why?
- What is your safety plan when the local model quality drops below the needed threshold?
