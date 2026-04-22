# Track Rubrics

## How to use these rubrics

Use the [Master Rubric](master-rubric.md) for common scoring dimensions, then apply the track-specific anchors below.

## Operator Track Rubric

### Required artifacts

- workflow deployment note
- channel policy
- troubleshooting runbook
- secure baseline note

### Distinction indicators

- explicit DM/group policy
- clean diagnostic ladder
- realistic operator recovery procedure

### Fail indicators

- undocumented unsafe channel exposure
- no troubleshooting evidence
- no prompt injection awareness for external content

## Production / DevOps Track Rubric

### Required artifacts

- deployment architecture
- ingress and auth note
- update and rollback note
- webhook or detached-work control note
- operational runbook

### Distinction indicators

- clear trust boundary diagram
- explicit release-aware change control
- auditable detached-work policy

### Fail indicators

- public exposure without defense
- no rollback path
- no explanation of auth and identity flow

## Security / Hardening Track Rubric

### Required artifacts

- threat model
- audit review
- prioritized remediation plan
- residual-risk statement

### Distinction indicators

- distinguishes must-fix from accepted risk clearly
- connects controls to concrete attack surfaces
- correctly limits claims about sandboxing and formal verification

### Fail indicators

- treats OpenClaw as hostile multi-tenant safe
- ignores webhook, hook, plugin, or external-content risk
- uses generic AI safety language without deployment specificity

## Plugin Developer Track Rubric

### Required artifacts

- manifest or design artifact
- schema note
- install/update behavior note
- compatibility note
- validation/test plan

### Distinction indicators

- strong configuration ergonomics
- explicit compatibility and failure handling
- awareness of supply-chain and ecosystem maturity

### Fail indicators

- no install/update path reasoning
- no precedence reasoning for skills or config ownership
- no validation story

## Contributor / Core Track Rubric

### Required artifacts

- contribution proposal
- architecture impact note
- validation plan
- docs plan

### Distinction indicators

- correct use of scoped contributor boundaries
- right-sized change scope
- clear affected-surface reasoning

### Fail indicators

- ignores contributor toolchain
- proposes sweeping changes without scope control
- no validation gate awareness

## Local Models Track Rubric

### Required artifacts

- local or hybrid model architecture
- hardware assumptions
- quality and safety tradeoff note
- fallback and cost note

### Distinction indicators

- rejects local models where they are not justified
- ties workload quality to model strength honestly
- documents fallback logic clearly

### Fail indicators

- ideology instead of tradeoff analysis
- no fallback plan
- no explanation of why the chosen model is safe enough for tool-enabled work
