# Specialization Classroom Lab Manuals

Use these manuals with the phase D labs and the role-specific tracks.

## LAB-D1: Plugin manifest inspection

- Classroom target: learners evaluate a plugin as an operational surface, not just a feature bundle
- Instructor setup: prepare one manifest that is strong and one that is weak
- Student flow: inspect manifest fields, bundle assumptions, config surfaces, install/update behavior
- Visual checkpoints: manifest excerpt, risk classification table, compatibility note
- Evidence pack: manifest review
- Recovery focus: plugin accepted because it "installs fine"

## LAB-D2: Skills precedence and install flow

- Classroom target: learners can debug skill collisions across all six layers
- Instructor setup: build one intentional name-collision example
- Student flow: map the six precedence layers, predict winner, verify the result, explain risk of workspace overrides
- Visual checkpoints: precedence diagram, collision example, resolution note
- Evidence pack: skill precedence map
- Recovery focus: flattening the precedence model into one generic "skills layer"

## LAB-D3: Headless node design

- Classroom target: learners reason about remote execution surfaces with approvals and exposure controls
- Instructor setup: define a bounded node-host scenario
- Student flow: document command surface, approval expectations, remote authority, and audit path
- Visual checkpoints: node surface diagram, policy note, rejected dangerous command exposure
- Evidence pack: distributed execution design
- Recovery focus: remote execution enabled with vague approvals or no trust explanation

## LAB-D4: Local-model tradeoff lab

- Classroom target: learners justify local or hybrid architecture with hardware and safety reasoning
- Instructor setup: prepare one hosted, one hybrid, and one local-only profile
- Student flow: compare cost, quality, latency, fallback behavior, and weak-model risk
- Visual checkpoints: tradeoff matrix, fallback decision tree, safety justification note
- Evidence pack: comparative design memo
- Recovery focus: local choice justified only by sovereignty slogans

## LAB-D5: Contributor toolchain orientation

- Classroom target: learners can propose contributor-safe work with scope awareness
- Instructor setup: provide one change idea and its affected subsystems
- Student flow: inspect changed-scope validation, `pnpm check:changed`, `pnpm test:changed`, scoped `AGENTS.md`, docs consistency
- Visual checkpoints: repo-scope map, validation command plan, change proposal note
- Evidence pack: contributor workflow checklist
- Recovery focus: patch proposal with no validation gate or scope map
