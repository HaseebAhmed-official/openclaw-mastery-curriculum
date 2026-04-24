# Semester 2 Weekly Slide Outlines

## Week 1: Production framing

- Opening: why "works on my machine" is not a production design
- Core slides: operators, environments, trust boundaries, ownership questions
- Demo: baseline setup vs production design review
- Whiteboard: production gap categories
- Failure slide: production equals VPS only
- Lab bridge: readiness memo
- Exit ticket: what changes first when moving from personal baseline to persistent service

## Week 2: Multi-agent routing and workspace identity files

- Opening: multiple agents only matter if isolation is real
- Core slides: workspaces, session stores, `SOUL.md`, `AGENTS.md`, `USER.md`
- Demo: compare two agent workspaces with different scope
- Whiteboard: privacy isolation vs authorization isolation
- Failure slide: shared workspace sold as isolation
- Lab bridge: LAB-C1
- Exit ticket: which files define agent behavior and which define session context

## Week 3: Configuration architecture

- Opening: configuration drift is an architectural risk, not only a syntax risk
- Core slides: config ownership, plugin-owned surfaces, schema reasoning, environment boundaries
- Demo: trace one config key from file to behavior
- Whiteboard: global config vs workspace `.env` vs plugin-specific settings
- Failure slide: steering sensitive endpoints from the wrong ownership boundary
- Lab bridge: schema, config, and dotenv-boundary drill
- Exit ticket: where should security-sensitive connector endpoints be governed and why

## Week 4: Security audit, advisories, webhook ingress, and hardening

- Opening: an audit is a decision aid, not a security certificate
- Core slides: `security audit`, `--deep`, `--fix`, advisory review, webhook hygiene
- Demo: compare baseline and deep findings and classify what `--fix` can and cannot change
- Whiteboard: operator action vs tool-supported remediation
- Failure slide: `--fix` equals complete hardening
- Lab bridge: LAB-C2
- Exit ticket: what must still be reviewed manually after `security audit --fix`

## Week 5: Exec approvals and host authority

- Opening: convenience arguments are not sufficient to justify host authority
- Core slides: exec policy, approvals, allowlists, node-host controls, exact request context
- Demo: compare deny, ask, and allowlist policies
- Whiteboard: strongest safe default for each use case
- Failure slide: approval prompts mistaken for hostile-user isolation
- Lab bridge: approval policy lab
- Exit ticket: when does an allowlist reduce risk and when does it create false confidence

## Week 6: Remote access and proxy patterns

- Opening: reverse proxy success can still hide a bad trust design
- Core slides: SSH, Tailscale Serve, trusted-proxy auth, loopback fail-closed behavior, origin policy
- Demo: accepted vs rejected trusted-proxy setups
- Whiteboard: proxy-only path and header trust model
- Failure slide: same-host loopback proxy as trusted-proxy auth
- Lab bridge: LAB-C3
- Exit ticket: what must be true before trusted-proxy auth is acceptable

## Week 7: Shared inboxes and DM scope

- Opening: collaborative convenience is not a hostile-user boundary
- Core slides: `dmScope`, shared inbox behavior, mention gating, session isolation
- Demo: one trusted-team case and one rejected mixed-trust case
- Whiteboard: routing policy review
- Failure slide: one gateway claimed safe for mutually untrusted users
- Lab bridge: LAB-C4
- Exit ticket: what risk remains even when sessions are per-user but the agent tools are shared

## Week 8: Plugins, bundles, ClawHub, and supply-chain controls

- Opening: extension surfaces expand both capability and attack surface
- Core slides: manifests, bundles, install/update behavior, provenance, compatibility assumptions
- Demo: inspect one plugin install path and one risk path
- Whiteboard: ecosystem maturity vs core-platform maturity
- Failure slide: "plugin works" equals "plugin is trustworthy"
- Lab bridge: manifest and plugin-install risk lab
- Exit ticket: what questions must be answered before a plugin is allowed in a serious deployment

## Week 9: Skills, ClawHub, and six-layer precedence

- Opening: precedence confusion creates silent behavior drift
- Core slides: six skill layers, collision tracing, install flow, workspace override power
- Demo: same skill name across multiple layers
- Whiteboard: precedence debugging sequence
- Failure slide: flattening all agent-level skills into one layer
- Lab bridge: skill collision lab
- Exit ticket: why is workspace precedence powerful and risky

## Week 10: Automation, hooks, heartbeat, and standing orders

- Opening: detached work changes the authority model
- Core slides: cron, heartbeat, hooks, task flow, standing orders, durable authority
- Demo: choose the right primitive for multiple scenarios
- Whiteboard: auditability vs convenience
- Failure slide: hooks selected because they are powerful, not because they are appropriate
- Lab bridge: LAB-C6
- Exit ticket: which primitive creates the narrowest acceptable authority for a repeated task

## Week 11: Sub-agents, ACP agents, headless nodes, and task auditability

- Opening: delegated work is only safe when ownership and inherited constraints stay visible
- Core slides: sub-agents, ACP agents, task records, child-session constraints, audit trails
- Demo: inspect a delegated workflow with inherited limits
- Whiteboard: parent-to-child security envelope
- Failure slide: invisible parallelism with no control surface
- Lab bridge: LAB-C7
- Exit ticket: what must never be lost when a child session is created

## Week 12: Memory strategy, Dreaming, and advanced knowledge layers

- Opening: memory architecture is a production decision, not just a personalization feature
- Core slides: `MEMORY.md`, search/indexing, memory wiki, `DREAMS.md`, dreaming thresholds
- Demo: compare memory strategies across deployment profiles
- Whiteboard: what should be durable, searchable, or ignored
- Failure slide: production design with no dreaming or promotion reasoning
- Lab bridge: memory strategy lab
- Exit ticket: when should knowledge remain in search instead of promoted memory

## Week 13: Threat modeling, draft artifacts, and formal verification limits

- Opening: assurance artifacts help only when their limits are stated clearly
- Core slides: ATLAS threat modeling, residual risk, draft vs stable artifacts, bounded formal models
- Demo: one deployment threat register
- Whiteboard: evidence claim ladder from docs to proof limits
- Failure slide: formal verification as blanket security proof
- Lab bridge: threat model workshop
- Exit ticket: what claim is legitimate after reading a bounded formal model

## Week 14: Contributor and ecosystem literacy

- Opening: contributor credibility comes from scope discipline, not repo familiarity alone
- Core slides: architecture tracing, `pnpm check:changed`, `pnpm test:changed`, scoped `AGENTS.md`, docs validation
- Demo: trace one change through contributor validation gates
- Whiteboard: changed-scope review workflow
- Failure slide: contribution plans without scope or validation reasoning
- Lab bridge: contributor proposal
- Exit ticket: what should happen before a learner proposes a multi-subsystem change

## Week 15: Track capstone sprint

- Opening: sprint time should strengthen evidence, not inflate scope
- Core slides: milestone gates, evidence review, defense preparation, late-risk control
- Demo: capstone review checklist
- Whiteboard: evidence gaps that block final defense
- Failure slide: feature churn in the last week
- Lab bridge: capstone build
- Exit ticket: what artifact should be strengthened first if the solution works but the reasoning is weak

## Week 16: Final defense

- Opening: defense is about judgment under challenge
- Core slides: demo flow, oral defense structure, rubric dimensions, panel questioning
- Demo: strong vs weak defense patterns
- Whiteboard: outcome, evidence, risk, limitation
- Failure slide: polished demo with weak governance reasoning
- Lab bridge: final capstone and viva
- Exit ticket: what makes a capstone defense credible to a skeptical reviewer
