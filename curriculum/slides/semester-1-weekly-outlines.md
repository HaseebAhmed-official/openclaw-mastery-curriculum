# Semester 1 Weekly Slide Outlines

## Week 1: Environment baseline

- Opening: why environment drift ruins OpenClaw learning faster than model confusion
- Core slides: canonical WSL2/Linux path, shell/editor/package baseline, path differences across Windows and Linux
- Demo: verify shell, home path, editor, browser, and package manager
- Visual board: "good baseline" vs "fragile baseline"
- Failure slide: virtualization disabled, mixed paths, wrong shell
- Lab bridge: LAB-A1
- Exit ticket: name the minimum environment checks before installing OpenClaw

## Week 2: Git and repo hygiene

- Opening: why unsafe Git behavior damages labs and team grading
- Core slides: working tree, branch, diff, commit, safe recovery
- Demo: create a branch, change one file, inspect diff, revert safely
- Whiteboard: why `main` is not a student sandbox
- Failure slide: blind commits, deleted state, generated noise
- Lab bridge: LAB-A2
- Exit ticket: what evidence proves a clean Git workflow

## Week 3: Node.js, JSON, TypeScript literacy

- Opening: runtime literacy vs random copy-paste
- Core slides: supported Node version, package tooling, JSON structure, light TypeScript reading
- Demo: inspect config shape and identify required vs optional fields
- Whiteboard: schema-backed config thinking
- Failure slide: invalid JSON, prose-style config edits, version mismatch
- Lab bridge: LAB-A3
- Exit ticket: what makes a config change intentional instead of accidental

## Week 4: Docker and networking basics

- Opening: why OpenClaw sandboxing and remote access depend on network literacy
- Core slides: images, containers, localhost, ports, bridge networking, host vs container perspective
- Demo: run one simple container and explain exposed ports
- Visual board: localhost from Windows, WSL2, and container viewpoints
- Failure slide: port confusion, wrong bind assumption, container isolation myths
- Lab bridge: LAB-A4
- Exit ticket: explain the difference between publishing a port and securing a service

## Week 5: LLM agent fundamentals

- Opening: what changes when a model can use tools instead of just chat
- Core slides: provider vs model vs tool, prompt injection basics, model strength, workflow trust
- Demo: compare a benign tool flow with a risky external-content flow
- Whiteboard: "access control before intelligence"
- Failure slide: better model equals safe model, prompt injection equals solved problem
- Lab bridge: tool-risk worksheet
- Exit ticket: what makes a tool-enabled agent dangerous in a new way

## Week 6: OpenClaw overview and trust model

- Opening: OpenClaw as assistant infrastructure, not just another chat UI
- Core slides: gateway, Control UI, channels, nodes, tools, sessions, memory
- Demo: architecture map walkthrough
- Whiteboard: one trusted operator boundary per gateway
- Failure slide: hostile multi-tenant claims, session key as auth myth
- Lab bridge: architecture mapping lab
- Exit ticket: where does trust widen in a normal OpenClaw deployment

## Week 7: Installation and onboarding

- Opening: the first reliable install matters more than feature breadth
- Core slides: install path, onboarding flow, auth bootstrap, daemon concepts
- Demo: first-run installation sequence
- Visual board: where installs fail on Windows vs WSL2
- Failure slide: wrong shell, provider auth mismatch, daemon confusion
- Lab bridge: LAB-B1
- Exit ticket: what must be captured to prove a valid first install

## Week 8: Control UI, doctor, status, health

- Opening: diagnostics should be normal behavior, not panic behavior
- Core slides: Control UI surfaces, `status`, `doctor`, `gateway probe`, `gateway status`, logs
- Demo: healthy path and broken path side by side
- Whiteboard: diagnostic ladder from UI to host state
- Failure slide: reinstall-first mindset, skipping logs, unstructured guessing
- Lab bridge: LAB-B2
- Exit ticket: which signal would you check before reinstalling

## Week 9: Sessions, workspace, and memory

- Opening: OpenClaw memory is a file-backed design surface, not hidden magic
- Core slides: sessions, workspace, `MEMORY.md`, daily notes, persistence boundaries
- Demo: inspect workspace artifacts after a turn
- Whiteboard: what survives a new session and why
- Failure slide: "the model just remembers," no persisted-state reasoning
- Lab bridge: LAB-B3
- Exit ticket: what is the difference between session history and durable memory

## Week 10: Models, providers, and release-aware defaults

- Opening: provider setup without release discipline is fragile
- Core slides: auth profiles, model selection, fallback ordering, release-note drift, rate limits
- Demo: compare assumed defaults with current release notes
- Whiteboard: stable assumption vs time-sensitive assumption
- Failure slide: timeless default-model claims
- Lab bridge: LAB-B4
- Exit ticket: what must be documented before trusting a current model default

## Week 11: Tools, sandboxing, and approvals

- Opening: tool power is where OpenClaw becomes operationally serious
- Core slides: tool groups, sandbox vs tool policy vs elevated, exec approvals, allowlists
- Demo: classify actions by authority level
- Whiteboard: sandbox as containment, not perfect isolation
- Failure slide: sandbox solves everything, approvals equal hostile-user boundary
- Lab bridge: LAB-B5
- Exit ticket: when is host execution acceptable, and what must be documented

## Week 12: Channels and pairing

- Opening: a connected channel is a trust decision, not a vanity milestone
- Core slides: pairing, DM scope, mention rules, group policies, safe first channel
- Demo: one one-to-one policy and one group policy
- Whiteboard: safe channel onboarding checklist
- Failure slide: no written policy, over-open groups, vague sender rules
- Lab bridge: LAB-B6
- Exit ticket: what written policy must exist before enabling a channel

## Week 13: Nodes and multimodal surfaces

- Opening: nodes extend capability and risk at the same time
- Core slides: node role, pairing, command surface, talk mode, voice wake, dependency risk
- Demo: node architecture walkthrough
- Whiteboard: stable vs preview vs source-build-only node surfaces
- Failure slide: treating preview capabilities as baseline
- Lab bridge: node concept note
- Exit ticket: why are nodes a governance surface and not just a convenience feature

## Week 14: Remote access patterns

- Opening: remote access should start from safest defaults, not fastest exposure
- Core slides: loopback, SSH tunnel, Tailscale Serve, rejected unsafe exposure patterns
- Demo: compare the trust path of three remote methods
- Whiteboard: ingress path and auth placement
- Failure slide: public bind first, reverse proxy without trust reasoning
- Lab bridge: LAB-B7
- Exit ticket: which remote path best preserves a bounded trust model for a personal deployment

## Week 15: Troubleshooting and hardening baseline

- Opening: good operators narrow causes instead of chasing symptoms
- Core slides: full diagnostic ladder, hardening baseline, safe recovery
- Demo: trace a fault from ingress to provider to host state
- Whiteboard: evidence-based remediation order
- Failure slide: symptom chasing, unsafe shortcuts, skipped security review
- Lab bridge: secure baseline review
- Exit ticket: what turns a troubleshooting note into an operational artifact

## Week 16: Practical exam and mini-project

- Opening: the exam validates judgment, not memorized commands
- Core slides: project expectations, evidence bundle, defense structure, fail conditions
- Demo: example evidence package
- Whiteboard: what distinguishes competent from fragile operation
- Failure slide: flashy output with weak safety or documentation
- Lab bridge: final package submission
- Exit ticket: what three artifacts prove safe baseline competence
