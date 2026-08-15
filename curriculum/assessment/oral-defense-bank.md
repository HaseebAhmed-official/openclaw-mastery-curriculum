# Oral Defense Bank

## Use

Select prompts after inspecting the learner's actual artifact. Ask follow-ups that change one assumption. Require diagrams, code/event traces, test rationale, and explicit uncertainty; do not accept rehearsed definitions alone.

## Authenticity and Tracing

1. Trace this run from user input to final event and identify every authority decision.
2. Which line or component would you inspect first for this observed failure, and why?
3. Show one test you wrote. What incorrect implementation could still pass it?
4. Which artifact was primarily agent-generated, and how did you verify it?
5. Reproduce one failure without consulting your report.
6. Remove one abstraction. What breaks and what improves?

## Architecture Judgment

7. Why is this agentic rather than deterministic? What evidence would make you replace it with a workflow?
8. What belongs in the stable core versus provider/framework adapter?
9. Why did you select this orchestration pattern? Defend its cost and failure complexity.
10. Identify the system's most important invariant and show its enforcement evidence.
11. Where can the model influence control, data, and authority? Where can it not?
12. What hidden assumption would most likely invalidate your design?

## State and Durability

13. Crash the system at this state. What is lost, duplicated, or recoverable?
14. Which operations are idempotent, retry-safe, compensatable, or irreversible?
15. What does replay mean in your system, and where is it nondeterministic?
16. How do you detect and repair corrupted or incompatible state?
17. Show evidence that cancellation cannot silently leave a dangerous effect.

## Security and Privacy

18. Give the shortest credible path from untrusted content to material impact.
19. Why does your approval bind the action actually executed?
20. Which sandbox/network/identity assumption is weakest?
21. Show one exploit variant your mitigation still does not stop.
22. What sensitive data can enter prompts, logs, traces, memory, and artifacts? How is deletion verified?
23. What evidence supports your tenancy claim?
24. Which risk did you accept, who owns it, and when must it be reviewed?

## Evaluation and Operations

25. Why are these tasks representative of the intended workload?
26. Show a trial where output and trace/end-state graders disagree. Which verdict is valid?
27. Why is the number of trials adequate for this decision?
28. What failure is your evaluation most likely to miss?
29. Which metric would alert first during this incident, and which evidence confirms root cause?
30. Demonstrate rollback or explain why it is unsafe.
31. What happens when the provider, tool, memory store, or queue is unavailable?
32. How did latency, cost, and human override affect the release decision?

## Protocol and Portability

33. Where does MCP/A2A protocol trust end and local policy begin?
34. Which version assumption is pinned, and what breaks if it changes?
35. Show the same behavior through two adapters. What semantics do not port cleanly?
36. Why is capability discovery not authorization?
37. Replace this framework tomorrow. Which tests protect the migration?

## Product Case Studies

38. Which claims are observed, documented, inferred, unknown, or outdated?
39. What can source-visible OpenClaw or Hermes evidence prove that a managed-product page cannot?
40. What can a managed product demonstrate without revealing internal architecture?
41. Identify one product default that must never become a stable curriculum principle.
42. How would a new release or advisory change your analysis and assessments?

## Communication, Ethics, and Governance

43. Explain the same critical limitation to an engineer, executive, and affected user.
44. Which NIST/OWASP/secure-development control applies, and what artifact proves implementation?
45. What would you refuse to claim in marketing or an institutional review?
46. How did accessibility or learner/user context change your design?
47. Where is qualified legal, medical, financial, safety, or security review required?

## Changed-Condition Prompts

48. The tool is now irreversible. Redesign approval and recovery.
49. The provider no longer guarantees structured output. Preserve the contract.
50. The system becomes team-shared. Reassess identity, state, memory, and audit.
51. Network access is removed. Preserve the core learning or product goal.
52. Task volume grows 100x. Reassess queueing, budgets, storage, and SLOs.
53. A new protocol version changes task lifecycle. Define migration and compatibility evidence.
54. A critical security advisory lands after release. Define triage, communication, rollback, and retest.

## Scoring Signal

Strong defenses trace actual evidence, identify limits, revise claims under challenge, and reason through changed conditions. Weak defenses repeat terminology, appeal to framework defaults, or cannot connect an artifact to observed behavior.
