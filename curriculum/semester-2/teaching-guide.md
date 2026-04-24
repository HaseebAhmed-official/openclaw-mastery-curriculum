# Semester 2 Teaching Guide

## How to use this guide

This guide assumes learners have passed the Semester 1 baseline. The emphasis now shifts from "can operate" to "can design, secure, extend, and defend."

## Week 1: Production framing

- Goal: reframe baseline operation as a production design problem
- Prep: prepare three deployment scenarios: solo operator, small trusted team, and enterprise bounded service
- Live session: environment choice, auth placement, secrets handling, and operational ownership
- Activity: students produce a gap analysis from Semester 1 baseline to production
- Homework: readiness memo
- Watchouts: students assuming "production" only means "move it to a VPS"

## Week 2: Multi-agent routing and workspace identity files

- Goal: teach isolation by workspace, session store, and identity files
- Prep: prepare examples of `SOUL.md`, workspace `AGENTS.md`, and `USER.md`
- Live session: why agents need separated workspaces and what each identity file does
- Activity: students define two agents with different behavior and context
- Homework: complete LAB-C1
- Watchouts: students talking about multi-agent routing without changing the workspace identity surfaces

## Week 3: Configuration architecture

- Goal: make students comfortable navigating real config complexity
- Prep: prepare examples of core config, plugin-owned config, and schema-backed validation
- Live session: schema reading, ownership boundaries, and where settings should live
- Activity: trace a config key from reading map to operational outcome
- Homework: configuration review note
- Watchouts: students scattering settings without understanding ownership

## Week 4: Security audit, webhook ingress, and hardening

- Goal: make the audit workflow real and actionable
- Prep: run `openclaw security audit` on a controlled setup, prepare a webhook-focused example, and review the latest official OpenClaw security advisories
- Live session: audit categories, JSON export, remediation prioritization, advisory-driven case analysis, and webhook token/path hygiene
- Activity: students triage findings into must-fix, should-fix, and accepted-risk
- Homework: complete LAB-C2
- Watchouts: students treating the audit as a checklist rather than a risk review

## Week 5: Exec approvals and host authority

- Goal: teach authority boundaries inside the tool plane
- Prep: prepare examples of deny, allowlist, and full approvals
- Live session: host execution, policy modes, node-host controls, and why convenience is not a sufficient justification
- Activity: students write a policy for a constrained operator use case
- Homework: approval policy defense
- Watchouts: students confusing interactive convenience with safe governance

## Week 6: Remote access and proxy patterns

- Goal: move from "it works remotely" to "it is remotely exposed with intent"
- Prep: compare SSH, Tailscale Serve, and trusted proxy auth with explicit trust assumptions
- Live session: ingress, headers, identity forwarding, and failure modes
- Activity: students review and reject one unsafe proxy design
- Homework: deployment review
- Watchouts: students over-trusting reverse proxies and under-documenting identity assumptions

## Week 7: Shared inboxes and DM scope

- Goal: reason clearly about cooperative usage vs adversarial assumptions
- Prep: prepare scenarios involving one operator, a trusted team, and mixed-trust participants
- Live session: session isolation, shared inbox behavior, DM scope, and mention gating
- Activity: students design a routing policy for a real team scenario
- Homework: shared-inbox critique
- Watchouts: students claiming one gateway safely separates hostile users

## Week 8: Plugins, bundles, ClawHub, and supply-chain controls

- Goal: teach the extension surface as an operational and security surface
- Prep: prepare at least one plugin manifest and one install/update scenario
- Live session: manifest structure, bundle concept, ClawHub distribution, install records, and supply-chain caution
- Activity: students classify plugin risks and identify compatibility assumptions
- Homework: plugin-install risk review
- Watchouts: students assuming ecosystem maturity is the same as core-platform maturity

## Week 9: Skills, ClawHub, and six-layer precedence

- Goal: make precedence bugs teachable instead of mysterious
- Prep: prepare a name-collision example across multiple skill layers
- Live session: six-layer precedence, workspace override power, and debugging strategy
- Activity: collision tracing exercise
- Homework: complete LAB-D2
- Watchouts: students flattening all agent-level skills into one conceptual layer

## Week 10: Automation, hooks, heartbeat, and standing orders

- Goal: teach detached work as a change in authority and auditability
- Prep: prepare examples where cron, heartbeat, hooks, and standing orders are each the right choice
- Live session: detached execution, event-driven execution, durable authority, and task visibility
- Activity: students choose primitives for multiple operational scenarios
- Homework: complete LAB-C6
- Watchouts: students selecting hooks because they are "powerful" rather than because they are appropriate

## Week 11: Sub-agents, ACP agents, headless nodes, and task auditability

- Goal: teach delegation and detached execution with control and traceability
- Prep: prepare one delegated-workflow example and one ACP-style integration example
- Live session: ownership, audit trail, task records, and distributed execution
- Activity: students inspect a delegated workflow and identify what must be logged or reviewed
- Homework: complete LAB-C7
- Watchouts: students treating sub-agents as magic parallelism without governance

## Week 12: Memory strategy, Dreaming, and advanced knowledge layers

- Goal: teach memory as a design surface, not just a background feature
- Prep: review `MEMORY.md`, daily notes, and `DREAMS.md` concepts from official docs
- Live session: memory persistence, promotion, dreaming thresholds, and when search or memory wiki layers matter
- Activity: students compare three memory strategies for three deployment profiles
- Homework: memory architecture note
- Watchouts: students ignoring dreaming while claiming production memory design competence

## Week 13: Threat modeling, draft artifacts, and formal verification limits

- Goal: teach students to use assurance artifacts without overstating them
- Prep: review ATLAS threat model docs and formal verification docs with current maturity labels
- Live session: threat modeling, draft vs stable artifacts, and bounded formal models
- Activity: threat workshop using one concrete deployment
- Homework: threat report
- Watchouts: students treating formal verification language as blanket proof of total system security

## Week 14: Contributor and ecosystem literacy

- Goal: make contributor-level work real instead of aspirational
- Prep: inspect the current OpenClaw contributor workflow and repo guidance
- Live session: pnpm workflow, changed-scope checks, scoped `AGENTS.md`, docs validation, and contribution planning
- Activity: students sketch a contributor-safe change plan
- Homework: contributor proposal
- Watchouts: students designing contributions without understanding affected scope and validation gates

## Week 15: Track capstone sprint

- Goal: create enough supervised build time for quality capstones
- Prep: require milestone review before students enter the sprint
- Live session: build support, risk review, and one-on-one architecture checks
- Activity: capstone implementation
- Homework: finalize deliverables and demo package
- Watchouts: students adding features late instead of strengthening evidence and defense notes

## Week 16: Final defense

- Goal: validate judgment, not only working output
- Prep: use the oral defense bank and track rubrics
- Live session: demos, critique, and oral defense
- Activity: capstone review panels
- Homework: post-course reflection and repository handoff
- Watchouts: instructors letting polished demos outweigh poor security reasoning
