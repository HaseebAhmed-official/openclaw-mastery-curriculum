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
4. Review current official advisories for the deployment components, classify at least two by failure family, and record exact affected and patched versions before drawing conclusions.
5. Identify webhook, plugin, hook, auth, proxy, file-transfer, or advisory-related findings.
6. Explain which findings `openclaw security audit --fix` could address and which require manual/operator action.
7. Cross-check whether open issue signals suggest extra caution without treating issues as authoritative documentation.
8. Prioritize remediation.
9. Record accepted risks and why.

### Required evidence

- audit report
- remediation plan
- JSON artifact
- short note comparing baseline audit, deep audit, and `--fix` limits
- source note distinguishing official docs/release notes from non-authoritative issue signals
- advisory matrix with component, failure family, affected version, patched version, control, and residual risk

### Common failure modes

- collecting findings without prioritization
- ignoring webhook-specific controls
- ignoring plugin, file-transfer, or hook authority
- assuming `--fix` completes hardening or exposure remediation
- ignoring upstream advisories because the local audit output looked clean

## LAB-C2A: Config fail-closed and doctor repair drill

### Objective

Teach learners that invalid configuration is an operational safety event, not a formatting inconvenience.

### Duration

- 60 minutes

### Procedure

1. Inspect the current configuration reference and release notes for config-load behavior.
2. Review a safe instructor-provided invalid config sample.
3. Explain why fail-closed behavior is safer than auto-restoring invalid config during startup or hot reload.
4. Run or conceptually trace the `doctor --fix` repair path in a controlled environment.
5. Record which repairs are safe migrations and which require operator judgment.

### Required evidence

- config repair note
- before/after explanation
- one decision table separating automatic repair from manual review

### Common failure modes

- assuming every config error should auto-repair
- treating `doctor --fix` as permission to ignore review
- failing to preserve operator-owned secrets or plugin config boundaries

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

1. Compare cron, heartbeat, hooks, task flow, standing orders, `/steer`, and `/side`.
2. Match each primitive to one scenario.
3. Identify authority, auditability, failure, retry, and delivery implications.
4. Prove an isolated job cannot regain a tool denied by its effective policy, using a safe simulation or documented trace.
5. Explain how completed heartbeat work is distinguished from notification delivery and duplicate retry.
6. Explain why `/steer` changes the active run while cron/tasks create durable work records.
7. Reject at least one tempting but wrong choice.

### Required evidence

- detached-work design note
- steering-vs-task distinction
- policy-inheritance and idempotent-delivery evidence

### Common failure modes

- using hooks where scheduled or session-bound behavior would be safer
- using `/steer` when the work needs a durable task record

## LAB-C7: Sub-agent and ACP auditability lab

### Objective

Teach delegation with ownership and traceability.

### Duration

- 90 minutes

### Procedure

1. Define a delegated task.
2. Explain whether sub-agents, ACP agents, or `openclaw attach` fit better.
3. For an attach case, document target-session selection, grant TTL, credential transport, strict MCP configuration, and revocation behavior.
4. Document the inherited child-session constraints that must remain in force.
5. Document expected task records, artifacts, requester provenance, and ownership.
6. Explain how you would audit the result later.

### Required evidence

- detached-task audit report

### Common failure modes

- treating delegation as invisible parallelism
- no ownership model
- no explanation of depth, child-count, sandbox, or target-agent constraints on child sessions
- treating temporary attach access as ambient or process-wide authority
