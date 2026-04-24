# Advanced Classroom Lab Manuals

Use these manuals with the phase C lab guides. These labs require stronger review discipline and clearer evidence standards than the Semester 1 baseline.

## LAB-C1: Multi-agent isolation design

- Classroom target: learners produce meaningful workspace and identity separation, not only different names
- Instructor setup: prepare two agents with distinct `SOUL.md`, `AGENTS.md`, and `USER.md` choices
- Student flow: define roles, separate workspaces, explain session and auth boundaries, justify identity files
- Visual checkpoints: two workspace trees, identity-file excerpts, isolation note
- Evidence pack: architecture note and differentiated workspace definitions
- Recovery focus: same workspace with cosmetic changes only

## LAB-C2: Security audit and remediation

- Classroom target: learners treat the audit as a risk-review workflow
- Instructor setup: capture one baseline audit, one `--deep` example, and one advisory-to-lab mapping example
- Student flow: run baseline audit, run `--deep` when feasible, export JSON, review overlapping advisories, classify `--fix` vs manual actions
- Visual checkpoints: baseline audit summary, deep audit finding, JSON artifact, advisory reference, remediation priority table
- Evidence pack: audit report, remediation plan, JSON artifact, short note on `--deep` and `--fix` limits
- Recovery focus: no prioritization, no advisory review, treating `--fix` as completed hardening

## LAB-C3: Trusted proxy and ingress review

- Classroom target: learners reject unsafe proxy designs for the right reasons
- Instructor setup: prepare SSH, Tailscale Serve, and trusted-proxy examples, including a same-host loopback failure case
- Student flow: compare identity paths, header trust, proxy-only path requirements, origin policy, mixed-token rejection
- Visual checkpoints: ingress comparison table, rejected loopback trusted-proxy design, accepted bounded design
- Evidence pack: deployment risk review
- Recovery focus: proxy headers trusted without path control, same-host loopback proxy proposed as valid trusted-proxy auth

## LAB-C4: Shared inbox policy lab

- Classroom target: learners distinguish cooperative routing from adversarial-isolation claims
- Instructor setup: provide one trusted-team scenario and one mixed-trust scenario
- Student flow: define `dmScope`, mention policy, routing boundaries, and remaining shared-agent risk
- Visual checkpoints: routing policy table, trust-boundary note
- Evidence pack: routing policy recommendation
- Recovery focus: calling shared gateway routing a hostile-user boundary

## LAB-C5: Threat model workshop

- Classroom target: learners build a deployment-specific threat register
- Instructor setup: supply one concrete deployment with assets, actors, and ingress surfaces
- Student flow: define assets, actors, boundaries, threats, controls, and residual risks
- Visual checkpoints: trust-boundary diagram, threat register excerpt, control-to-threat mapping
- Evidence pack: threat register
- Recovery focus: generic AI-risk prose with no deployment context

## LAB-C6: Automation and standing-orders design

- Classroom target: learners choose detached-work primitives with governance reasoning
- Instructor setup: prepare scenarios for cron, heartbeat, hooks, task flow, and standing orders
- Student flow: map each scenario to one primitive, explain authority, auditability, and safer alternatives
- Visual checkpoints: primitive-selection matrix, rejected wrong-choice example, authority note
- Evidence pack: detached-work design note
- Recovery focus: hooks chosen because they are powerful, no auditability argument

## LAB-C7: Sub-agent and ACP auditability lab

- Classroom target: learners explain delegation with ownership and inherited constraints
- Instructor setup: provide one delegated workflow and one ACP-style workflow
- Student flow: choose sub-agent or ACP, document child-session limits, ownership, task records, and later audit path
- Visual checkpoints: delegation diagram, inherited-constraint table, task-record expectations
- Evidence pack: detached-task audit report
- Recovery focus: invisible parallelism, no child-session constraint reasoning, no ownership model
