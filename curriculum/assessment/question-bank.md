# Question Bank

## Usage

Each prompt should be scored for correctness, boundaries, evidence, counterexample/failure reasoning, and communication. Convert selected prompts into diagrams, code traces, incident evidence, or oral probes; do not grade only prose.

## Foundations and Architecture

1. Distinguish a model, tool, workflow, agent, harness, execution environment, and agent system using one concrete example.
2. Given a business task, decide whether deterministic code, a workflow, a single agent, or multiple agents is the simplest valid design. State disconfirming evidence.
3. Draw control, data, authority, and trust boundaries for a tool-using agent.
4. Explain why framework classes are not automatically stable architecture contracts.
5. Separate model failure from context, tool, policy, execution, state, and evaluator failure in a supplied trace.
6. Define an invariant for a bounded agent loop and show how it can be violated.
7. Explain why probabilistic behavior changes test strategy but does not remove the need for deterministic tests.
8. Identify which parts of a harness should remain deterministic and why.
9. Compare manager, handoff, routing, parallel, and evaluator-optimizer patterns under one constrained task.
10. Give a case where adding another agent reduces reliability or quality.

## Provider, Loop, and Tools

11. Design a provider protocol that can support a deterministic test double and two network providers.
12. Explain what a provider test double proves and what it cannot prove.
13. Define explicit stop reasons for normal completion, budget exhaustion, cancellation, policy denial, provider failure, and no progress.
14. Design a no-progress detector and describe false positives and false negatives.
15. Explain why a wall-clock timeout, turn budget, tool budget, and cost budget are different controls.
16. Review a tool schema for ambiguity, excessive authority, weak errors, and runtime-validation gaps.
17. Explain why compile-time types do not validate model-generated runtime arguments.
18. Design a structured tool error that enables repair without leaking sensitive internals.
19. Distinguish idempotent, retry-safe, compensatable, and irreversible operations.
20. Show how a harmless-looking wrapper can change the effective authority of a tool.

## Context, State, and Memory

21. Define a context-assembly policy using relevance, provenance, trust, freshness, and budget.
22. Explain why more context can reduce performance or safety.
23. Design an ablation that tests whether a retrieved record actually helps.
24. Separate instructions from untrusted data in a supplied context bundle.
25. Distinguish conversation history, session state, task state, event log, checkpoint, artifact, and memory.
26. Reconstruct a session from an event sequence and identify the first invalid transition.
27. Explain replay limits when model calls and external side effects are nondeterministic.
28. Choose retry, compensation, resume, rollback, or human repair for five supplied failure states.
29. Design memory retention, provenance, isolation, and deletion rules for a team system.
30. Explain how stale or malicious memory can create a confused-deputy path.

## Policy, Approval, and Execution

31. Define the minimum fields an approval must bind to prevent argument substitution.
32. Explain the difference between tool policy, human approval, sandboxing, and host authorization.
33. Analyze a stale approval reused in another session and propose a failing test.
34. Design deny-by-default behavior for an unknown capability.
35. Explain why a prompt instruction is not an execution sandbox.
36. Identify filesystem, network, process, secret, working-directory, and resource controls for a code-execution tool.
37. State what evidence would be required before claiming hostile multi-tenant isolation.
38. Explain how operator identity and requester provenance affect authorization.

## Protocols and Interoperability

39. Explain MCP host, client, and server responsibilities and where local policy must remain authoritative.
40. Distinguish capability discovery from authorization and trust.
41. Design MCP contract tests for version, capability, error, timeout, and malicious returned content.
42. Explain A2A AgentCard, message, task, artifact, part, and task-state concepts.
43. Compare MCP and A2A boundaries for a concrete system; identify where they can coexist.
44. Design duplicate, cancellation, and identity-failure tests for delegated A2A work.
45. Explain why protocol compliance does not prove semantic compatibility.
46. Define a cross-framework adapter test that detects silent behavioral drift.

## Security, Safety, and Privacy

47. Build an attack path from prompt injection to a high-impact tool; identify every required precondition.
48. Distinguish prompt injection, confused deputy, excessive agency, exfiltration, persistence, and supply-chain compromise.
49. Map preventive, detective, and recovery controls to one agentic threat.
50. Explain why approvals and sandboxes are complementary rather than interchangeable.
51. Analyze an approval display that omits normalized or wrapped arguments.
52. Threat-model an MCP server or plugin added from an untrusted source.
53. Explain how logs, traces, prompts, memory, and artifacts can leak sensitive data.
54. Design secret handling and redaction tests without making debugging impossible.
55. Define containment and safe cleanup for an authorized prompt-injection lab.
56. Explain why a formal model or security audit is bounded evidence rather than proof of total security.

## Evaluation and Observability

57. Distinguish task, trial, transcript, outcome, grader, dataset, eval harness, and agent harness.
58. Explain why a single successful trial is weak evidence for nondeterministic behavior.
59. Choose code, model, human, trace, and end-state graders for a side-effecting task.
60. Give a case where final output passes but trace or end state must fail the trial.
61. Separate capability, regression, security, reliability, and production-monitoring suites.
62. Analyze grader disagreement and decide whether to repair the grader, task, or system.
63. Identify test leakage, corpus contamination, selection bias, and threshold tuning after results.
64. Define success, variance, retry, tool failure, human override, latency, and cost measures for a release decision.
65. Explain how OpenTelemetry semantic conventions help and why version pinning still matters.
66. Reconstruct a failure timeline from partial traces, metrics, logs, and events; identify missing evidence.

## Production, Governance, and Change

67. Define SLOs and an error-budget response for an agent system.
68. Design degradation behavior for provider, tool, memory, and queue failure.
69. Explain backup, migration, rollback, and compatibility responsibilities for durable agent state.
70. Compare local, container, VM, managed, and distributed deployment boundaries for stated requirements.
71. Map NIST AI RMF functions to one agent-system release decision without claiming certification.
72. Map NIST SSDF practices to the lifecycle of tools, prompts/policies, dependencies, and deployment artifacts.
73. Define data classification, retention, deletion, user control, and incident escalation for a learner-selected case.
74. Explain how accessibility requirements change interfaces or evidence collection without lowering competency standards.
75. Create a release-sensitive claim record with source, version/date, confidence, contradiction, and revalidation trigger.
76. Decide when a current product claim must be observed, documented, inferred, unknown, or retired.

## Product and Framework Cases

77. Map OpenClaw or Hermes Agent to the stable harness contracts using current source/docs and identify unknowns.
78. Analyze a managed product such as ChatGPT Work without inferring private implementation architecture.
79. Compare two frameworks on the same behavioral contract, not their feature lists.
80. Identify one product default that should remain outside the stable core and define its update trigger.
81. Explain how a single-tenant trust assumption changes deployment and governance claims.
82. Propose a migration from one framework/product adapter to another while preserving tests and evidence.

## Transfer Scenarios

83. A tool succeeded but the acknowledgment event was lost. Design safe recovery for idempotent and irreversible operations.
84. A retrieved memory contains a valid instruction from the wrong user. Diagnose the failure and controls.
85. A benchmark improves while real-user task success declines. Build an investigation plan.
86. A provider changes structured-output behavior. Identify which contract, tests, labs, and release evidence must change.
87. An MCP server adds a powerful new capability after update. Define discovery, approval, policy, and regression behavior.
88. A multi-agent design is slower, more expensive, and no more accurate than a workflow. Defend the redesign decision.
89. A security reviewer finds a critical bypass one day before release. Define stop-ship, repair, retest, and communication.
90. A learner's capstone is polished but they cannot trace a hidden failure. Decide the mastery outcome and repair path.
