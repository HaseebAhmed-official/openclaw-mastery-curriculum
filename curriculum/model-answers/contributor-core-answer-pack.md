# Contributor / Core Answer Pack

## Target standard

This track should produce contribution artifacts that respect repo scope, validation gates, and architecture surfaces.

## Model capstone answer shape

1. Name the problem and show how it maps to the current codebase or docs.
2. Bound the change: affected subsystem, neighboring risks, validation commands, and documentation impact.
3. Show repo-literacy evidence: architecture trace, scoped `AGENTS.md`, changed-scope validation, docs consistency.
4. Present a credible proposal, design doc, issue investigation, or patch plan.
5. State what is still uncertain and what would be validated next.

## Strong evidence bundle

- architecture trace note
- changed-scope validation plan
- docs-to-code consistency check
- proposed artifact with explicit boundaries
- risk note describing what is not being changed

## Strong-answer signals

- narrow scope is justified
- validation gates are chosen intentionally
- contributor guidance is treated as operational input
- uncertain areas are named instead of hidden

## Weak-answer signals

- repo exploration mistaken for contribution readiness
- patch plan with no validation commands
- subsystem boundaries ignored
- no evidence that docs and implementation were compared

## Oral defense prompts

- Why is `pnpm check:changed` or `pnpm test:changed` the right first gate here?
- Which files or systems would you explicitly avoid touching in the first iteration?
- What would make this proposal too broad for a first contribution?
