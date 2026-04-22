# Question Bank

## Usage

This bank is designed for quizzes, written exams, recitations, and oral warm-up questions. Instructors should rotate and adapt questions rather than reuse the same set every term.

## Foundations and concepts

1. What problem does OpenClaw solve that a normal hosted chatbot does not?
2. What is the role of the gateway in OpenClaw architecture?
3. Why is OpenClaw described as a trusted-operator system rather than a hostile multi-tenant boundary?
4. What is the difference between a session and workspace memory?
5. Why is "the model remembers it" an unsafe explanation in OpenClaw?
6. Why is WSL2 usually the recommended Windows path?
7. What does Docker contribute to OpenClaw sandboxing?
8. Why is loopback-only safer than public exposure?
9. What is the difference between a tool and a channel?
10. Why should release notes matter in provider or security labs?

## Operations and diagnostics

11. When should `openclaw doctor` be used?
12. What does `gateway probe` tell you that a static config read does not?
13. Why should logs be part of the diagnostic ladder?
14. What is one likely cause of a provider setup that worked last week but fails now?
15. Why is a reinstall often the wrong first troubleshooting action?
16. What is the minimum evidence needed to defend a remote access choice?
17. What is the difference between a healthy channel configuration and a safe channel configuration?
18. Why must provider choice include quality and rate-limit reasoning?
19. What is one reason to prefer SSH or Tailscale Serve over a public reverse proxy?
20. What must a secure baseline review include besides "it works"?

## Security and governance

21. What is prompt injection in the context of tool-enabled agents?
22. Why is sandboxing valuable even if it is not a perfect security boundary?
23. What risk does a dangerous bypass flag create in a teaching lab?
24. Why do webhook tokens and path restrictions matter?
25. What is the difference between approvals and allowlists?
26. Why is plugin installation a supply-chain question, not only a feature question?
27. Why should standing orders be reviewed like policy?
28. What is the risk of using hooks without explicit review?
29. Why is it incorrect to market one shared gateway as safe against adversarial users?
30. What is the difference between a bounded formal model and a proof of total implementation security?

## Extensibility and contributor depth

31. What does `openclaw.plugin.json` communicate?
32. Why is JSON Schema literacy important for plugin work?
33. Name the six skill-precedence layers in order.
34. Why do workspace-level skills deserve special caution?
35. What problem do `SOUL.md` and `USER.md` solve in multi-agent setups?
36. Why do scoped `AGENTS.md` files matter to contributors?
37. Why is `pnpm check:changed` more useful than running every check blindly?
38. What is the operational difference between a skill and a plugin?
39. What is ClawHub from a governance perspective?
40. Why is contributor readiness not the same as being able to read the repo once?

## Automation and detached work

41. When should cron be preferred over heartbeat?
42. When should heartbeat be preferred over cron?
43. What makes hooks higher risk than many interactive actions?
44. Why do sub-agents require an ownership model?
45. What problem do background task records solve?
46. How do ACP agents change the trust surface?
47. Why should detached work be auditable?
48. What makes standing orders powerful and risky at the same time?
49. What must be documented before enabling automation in a production environment?
50. Why is the wrong automation primitive a governance problem, not only a technical mistake?

## Scenario prompts

51. A student exposes the gateway publicly because SSH tunneling "takes too long." What do you say and why?
52. A team wants one OpenClaw gateway for users who do not trust each other. Evaluate the design.
53. A student says the sandbox means host risk is solved. How do you respond?
54. A plugin looks useful but has unclear install/update provenance. What review steps are required?
55. A release changed the default provider model and the cohort's lab answers diverge. How should the instructor respond?
56. A student designs a memory strategy but never mentions `DREAMS.md`. What question should you ask first?
57. A shared inbox design works functionally but has vague mention rules. What risk remains?
58. A hook executes on external events and writes to the workspace. What must be reviewed?
59. A sub-agent workflow returns a result but no one can explain who owned which step. What is wrong?
60. A contribution proposal modifies multiple subsystems but ignores scoped contributor guidance. What should happen next?
