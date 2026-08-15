# Specialization Lab Guides

## LAB-D1: Cross-Framework Portability

Implement one stable capability through two current frameworks or SDKs. Keep acceptance tests, task corpus, policy, and evidence constant. Record current versions, default differences, hidden state, tool/error semantics, tracing gaps, and migration cost.

Pass when behavior tests run against both adapters and the learner can identify which differences belong in the adapter rather than the core. Transfer by adding a third provider or framework design without rewriting the domain contract.

## LAB-D2: Versioned Product Case Study

Select OpenClaw, Hermes Agent, ChatGPT Work, xAI agent tooling, or an approved current system. Build a dated claim table from primary evidence and map observed/documented capabilities to:

- loop and orchestration
- providers/models
- context and memory
- tools and execution
- policy/approval and trust boundary
- sessions/durability
- protocols/integrations
- observability/evaluation
- deployment/governance

Label every item `observed`, `documented`, `inferred`, `unknown`, or `not applicable`. Pass when no private implementation is inferred from product marketing and at least one changed-version risk is identified.

## LAB-D3: Tool or Protocol Extension

Build one tool, plugin, MCP server/client, or A2A adapter. Require clear naming, typed schemas, least authority, structured errors, timeout/cancellation, idempotency semantics, tests, threat model, dependency provenance, release/version policy, and usage evidence.

Pass when an unfamiliar client can discover and use it, malformed/untrusted inputs fail safely, and a reviewer can reproduce tests from clean instructions.

## LAB-D4: Local-Model Serving and Routing

Given declared hardware, budget, privacy, workload, context, concurrency, and quality requirements, compare at least two feasible serving/model configurations. Measure task success, variance, throughput, time to first token, completion latency, memory/accelerator use, failure behavior, and cost proxy.

Pass when the recommendation follows measured constraints, includes fallback/degradation behavior, and avoids universal “best model” claims. Transfer under one changed hardware, privacy, or workload constraint.

## LAB-D5: Core Runtime Contribution

Choose an unfamiliar source-visible harness or framework. Trace one request across at least three core layers, reproduce an issue or limitation, add a regression test, and implement or propose a scoped change using the project's contribution rules.

Evidence includes source locations, control/data flow, test result, compatibility impact, security/operations impact, maintainer feedback if available, and unresolved tradeoffs. A proposal may pass when upstream contribution is impractical, but only if the reasoning and executable reproduction are strong.
