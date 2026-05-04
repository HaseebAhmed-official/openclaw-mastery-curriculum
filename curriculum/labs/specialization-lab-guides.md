# Specialization Lab Guides

## LAB-D1: Plugin manifest inspection

### Objective

Teach extension review with manifest, schema, and install/update behavior in view.

### Duration

- 75 minutes

### Procedure

1. Inspect a native plugin manifest.
2. Identify capabilities, config surface, and schema expectations.
3. Compare ClawHub, npm, git, and local-path install sources for the plugin.
4. Inspect or describe `openclaw plugins list --json` dependency status.
5. Inspect or describe `openclaw plugins inspect <plugin-id> --runtime --json` as proof of runtime loading.
6. Review the official file-transfer plugin as a capability and policy example.
7. Record install/update and compatibility assumptions.
8. Flag one supply-chain or operational concern.

### Required evidence

- manifest review
- runtime inspection note
- dependency status note
- file-transfer policy note

### Common failure modes

- assuming installed inventory means the running Gateway loaded the plugin
- skipping source provenance because the plugin appears official or familiar
- ignoring per-node file-transfer path policy and byte limits

## LAB-D2: Skills precedence and install flow

### Objective

Make six-layer skill precedence operationally clear.

### Duration

- 60 to 75 minutes

### Procedure

1. Map all six layers.
2. Create one name-collision scenario.
3. Predict which skill wins and explain why.
4. Record how to debug a precedence issue.

### Required evidence

- skill precedence map

## LAB-D3: Headless node design

### Objective

Teach distributed execution with explicit host authority and approval concerns.

### Duration

- 75 minutes

### Procedure

1. Define a headless node use case.
2. Document the command surface.
3. Explain approval boundaries.
4. Record why the node should or should not exist for that scenario.

### Required evidence

- distributed execution design

## LAB-D4: Local-model tradeoff lab

### Objective

Compare hosted vs local or hybrid models without ideology.

### Duration

- 90 minutes

### Procedure

1. Pick one workload.
2. Compare hosted and local options.
3. Evaluate quality, cost, latency, safety, and hardware assumptions.
4. Recommend one design and justify the fallback strategy.

### Required evidence

- comparative design memo

## LAB-D5: Contributor toolchain orientation

### Objective

Make contributor workflow concrete on day one.

### Duration

- 60 minutes

### Procedure

1. Read the current contributor guidance.
2. Run the changed-scope validation commands conceptually or in practice where appropriate.
3. Identify at least one scoped `AGENTS.md`.
4. Explain how a safe contribution differs from an unscoped edit.

### Required evidence

- contributor workflow checklist
