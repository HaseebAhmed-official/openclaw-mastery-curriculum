# Master Rubric

## Scoring dimensions

### 1. Technical correctness

- 4: correct, reproducible, and clearly validated
- 3: mostly correct with minor gaps
- 2: partially correct but unstable or weakly validated
- 1: major functional misunderstandings

### 2. Operational maturity

- 4: explicit runbooks, diagnostics, rollback thinking, and environment awareness
- 3: workable operations with some missing depth
- 2: fragile operations and weak recovery planning
- 1: no meaningful operational thinking

### 3. Security and trust reasoning

- 4: explicit trust model, controlled exposure, principled risk tradeoffs
- 3: mostly sound but incomplete security reasoning
- 2: superficial or confused hardening choices
- 1: unsafe assumptions or ignored trust boundaries

### 4. Documentation and explanation

- 4: concise, accurate, and teachable
- 3: understandable with small gaps
- 2: unclear or incomplete
- 1: weak communication and poor evidence

### 5. Capstone defense

- 4: responds clearly to challenge questions and justifies choices
- 3: answers most challenges competently
- 2: unclear reasoning under pressure
- 1: unable to defend design choices

## Automatic downgrade triggers

- claims hostile multi-tenant isolation where official docs do not
- exposes the gateway without adequate auth or trust explanation
- uses dangerous bypass flags without explicit containment
- produces a tool-enabled deployment design without addressing prompt injection or unsafe external content
- omits discussion of tool risk for tool-enabled agents
- designs a production memory strategy without considering `DREAMS.md` and dreaming configuration
- ignores webhook ingress, detached authority, or auditability in a production-facing design that uses automation or hooks
- cannot explain why a chosen model/provider is acceptable for the use case
