# Advanced Lab Guides

## LAB-C1: Multi-agent isolation design

### Objective

Demonstrate meaningful agent separation using workspace and identity surfaces.

### Duration

- 90 minutes

### Procedure

1. Define two agent roles with different responsibilities.
2. Create or describe separate workspaces.
3. Write differentiated `SOUL.md` content.
4. Add workspace-level `AGENTS.md`.
5. Add or justify `USER.md`.
6. Explain session and auth separation.

### Required evidence

- two differentiated agent definitions
- one isolation architecture note

### Common failure modes

- same behavior in both workspaces
- no explanation of why separation matters

## LAB-C2: Security audit and remediation

### Objective

Use the security audit like an operator, not like a checkbox runner.

### Duration

- 90 to 120 minutes

### Procedure

1. Run `openclaw security audit`.
2. Run `openclaw security audit --deep` when the environment permits, or explain why only the baseline audit was feasible.
3. Export machine-readable findings with `--json` from at least one audit run.
4. Review at least one current official OpenClaw advisory that overlaps with the deployment surface.
5. Identify webhook, plugin, hook, auth, proxy, or advisory-related findings.
6. Explain which findings `openclaw security audit --fix` could address and which require manual/operator action.
7. Prioritize remediation.
8. Record accepted risks and why.

### Required evidence

- audit report
- remediation plan
- JSON artifact
- short note comparing baseline audit, deep audit, and `--fix` limits

### Common failure modes

- collecting findings without prioritization
- ignoring webhook-specific controls
- assuming `--fix` completes hardening or exposure remediation
- ignoring upstream advisories because the local audit output looked clean

## LAB-C3: Trusted proxy and ingress review

### Objective

Evaluate remote ingress patterns rather than blindly deploying them.

### Duration

- 75 minutes

### Procedure

1. Compare SSH, Tailscale Serve, and trusted proxy auth.
2. Write the identity and trust assumptions for each.
3. Identify where headers can be spoofed or misapplied.
4. Explain why same-host loopback reverse proxies do not satisfy trusted-proxy auth.
5. Document the proxy-only path, explicit origin policy, and mixed-token rejection requirements for trusted-proxy mode.
6. Recommend one approach for a bounded scenario.

### Required evidence

- deployment risk review

### Common failure modes

- over-trusting proxy headers
- not explaining where auth happens
- proposing trusted-proxy auth without a proxy-only path or with a same-host loopback proxy

## LAB-C4: Shared inbox policy lab

### Objective

Separate collaborative convenience from security boundary claims.

### Duration

- 60 minutes

### Procedure

1. Evaluate one shared-team scenario.
2. Document DM scope, session routing, and mention policy.
3. Explain why the gateway is or is not appropriate for that trust environment.

### Required evidence

- routing policy recommendation

### Common failure modes

- claiming hostile-user safety on one gateway

## LAB-C5: Threat model workshop

### Objective

Build a threat register grounded in a real OpenClaw deployment.

### Duration

- 90 minutes

### Procedure

1. Pick a concrete deployment.
2. Identify assets, actors, and trust boundaries.
3. Enumerate threats using the ATLAS frame where relevant.
4. Propose controls and residual risks.

### Required evidence

- threat register

### Common failure modes

- generic AI risk statements with no deployment specificity

## LAB-C6: Automation and standing-orders design

### Objective

Choose the right detached-work primitive and defend the choice.

### Duration

- 90 minutes

### Procedure

1. Compare cron, heartbeat, hooks, task flow, and standing orders.
2. Match each primitive to one scenario.
3. Identify authority, auditability, and failure implications.
4. Reject at least one tempting but wrong choice.

### Required evidence

- detached-work design note

### Common failure modes

- using hooks where scheduled or session-bound behavior would be safer

## LAB-C7: Sub-agent and ACP auditability lab

### Objective

Teach delegation with ownership and traceability.

### Duration

- 90 minutes

### Procedure

1. Define a delegated task.
2. Explain whether sub-agents or ACP agents fit better.
3. Document the inherited child-session constraints that must remain in force.
4. Document expected task records, artifacts, and ownership.
5. Explain how you would audit the result later.

### Required evidence

- detached-task audit report

### Common failure modes

- treating delegation as invisible parallelism
- no ownership model
- no explanation of depth, child-count, sandbox, or target-agent constraints on child sessions
