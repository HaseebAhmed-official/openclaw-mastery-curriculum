# Semester 1 Teaching Guide

## How to use this guide

Each week below includes:

- teaching goal
- instructor prep
- live-session structure
- in-class activity
- homework or lab
- watchouts

Use this guide with the core lab guides and the official reading map.

## Week 1: Environment baseline

- Goal: make every student operational in WSL2/Linux, shell, editor, and package tooling
- Prep: verify the institution-approved install path for WSL2 or Linux
- Live session: explain why the environment matters for OpenClaw and where Windows-native paths usually fail learners
- Activity: students verify shell, home directory, editor, Node path, and browser access
- Homework: complete LAB-A1
- Watchouts: students mixing Windows paths with Linux paths; students without virtualization enabled

## Week 2: Git and repo hygiene

- Goal: give learners enough Git discipline to survive repo-based work without damaging state
- Prep: have a demo repo or branch workflow ready
- Live session: status, add, commit, branch, diff, and safe recovery
- Activity: students create a branch, make a change, review the diff, and revert safely
- Homework: complete LAB-A2
- Watchouts: students committing generated files blindly or working on `main`

## Week 3: Node.js, JSON, TypeScript literacy

- Goal: make learners capable of reading runtime expectations and editing config intentionally
- Prep: verify the currently supported OpenClaw Node version and update class notes if needed
- Live session: explain Node runtime checks, npm/pnpm roles, JSON config shape, and light TypeScript reading
- Activity: inspect a sample structured config and identify required fields vs optional fields
- Homework: complete LAB-A3
- Watchouts: students treating JSON like prose; students not understanding schema-driven validation

## Week 4: Docker and networking basics

- Goal: build the minimum container and network literacy required for sandboxing and remote access
- Prep: have one container example and one local port-mapping example ready
- Live session: images, containers, localhost, bridges, ports, and why Docker matters to OpenClaw sandboxing
- Activity: students run a simple container and explain which port is exposed where
- Homework: complete LAB-A4
- Watchouts: students confusing `localhost` inside WSL2, Windows, and containers

## Week 5: LLM agent fundamentals

- Goal: give a non-magical explanation of model providers, tool use, and prompt injection
- Prep: prepare one benign tool flow and one malicious external-content scenario
- Live session: provider vs model vs tool, why stronger models matter, why prompt injection remains real
- Activity: analyze one unsafe workflow and identify the trust failure
- Homework: short reflection plus tool-risk analysis worksheet
- Watchouts: students assuming better models eliminate security concerns

## Week 6: OpenClaw overview and trust model

- Goal: establish the mental model of gateway, control plane, channels, nodes, and operator boundary
- Prep: use the architecture docs and security docs together
- Live session: what OpenClaw is, what it is not, and why the trusted-operator boundary matters
- Activity: students draw the gateway architecture and label where trust widens
- Homework: architecture concept check
- Watchouts: students describing OpenClaw as multi-tenant secure by default

## Week 7: Installation and onboarding

- Goal: complete a first working OpenClaw install
- Prep: verify the latest supported install path and onboarding flow
- Live session: installation sequence, onboarding wizard, auth bootstrap, and daemon concepts
- Activity: instructor live install plus student install start
- Homework: complete LAB-B1
- Watchouts: provider auth confusion, Windows shell vs WSL shell drift

## Week 8: Control UI, doctor, status, health

- Goal: make diagnosis normal instead of reactive guesswork
- Prep: pre-stage at least one broken setup for a demo
- Live session: Control UI basics, `status`, `doctor`, `gateway probe`, `gateway status`, and live logs
- Activity: students compare a healthy and broken status sequence
- Homework: complete LAB-B2
- Watchouts: students skipping logs and jumping to reinstall

## Week 9: Sessions, workspace, and memory

- Goal: teach the workspace state model clearly enough that students stop imagining hidden memory
- Prep: prepare one example workspace with `MEMORY.md` and daily notes
- Live session: sessions, workspace, memory files, and what actually persists
- Activity: students inspect workspace artifacts and explain what would survive a new session
- Homework: complete LAB-B3
- Watchouts: students assuming the model "just remembers" outside persisted state

## Week 10: Models, providers, and release-aware defaults

- Goal: teach students how to configure providers without freezing assumptions in time
- Prep: check current release notes for model default changes
- Live session: provider auth, default selections, fallback strategy, rate-limit awareness, and release drift
- Activity: compare a current release note with older assumptions and document the delta
- Homework: complete LAB-B4
- Watchouts: students memorizing a specific default model as a timeless truth

## Week 11: Tools, sandboxing, and approvals

- Goal: make host authority and sandbox boundaries concrete
- Prep: prepare one sandboxed example and one host-exec policy example
- Live session: built-in tools, sandbox purpose, exec approvals, allowlists, and danger of bypass flags
- Activity: students classify actions into safe, risky, and prohibited
- Homework: complete LAB-B5
- Watchouts: students overstating what sandboxing guarantees

## Week 12: Channels and pairing

- Goal: connect at least one communication surface safely
- Prep: decide whether the cohort will use Telegram, WhatsApp, or webchat-only fallbacks
- Live session: pairing, DM scope, group mention controls, and channel-specific policy
- Activity: policy design for one one-to-one channel and one group scenario
- Homework: complete LAB-B6
- Watchouts: students enabling channels without a written policy

## Week 13: Nodes and multimodal surfaces

- Goal: teach nodes as capability surfaces, not novelty features
- Prep: verify what is stable, preview, or source-build-only at the current validation date
- Live session: node role, pairing, talk mode, voice wake, and dependency risks like TTS services
- Activity: architecture walkthrough and dependency-risk discussion
- Homework: node concept note
- Watchouts: students mistaking preview or source-build-only node features for universal baseline

## Week 14: Remote access patterns

- Goal: teach remote access by safest defaults first
- Prep: prepare examples of loopback-only, SSH tunnel, Tailscale Serve, and a rejected unsafe public exposure
- Live session: compare remote access patterns and their security tradeoffs
- Activity: students choose a remote access pattern for three scenarios
- Homework: complete LAB-B7
- Watchouts: students jumping directly to public exposure or reverse proxy without understanding trust

## Week 15: Troubleshooting and hardening baseline

- Goal: consolidate the first semester into disciplined ops
- Prep: stage multiple failure cases across provider, channel, and local runtime
- Live session: full diagnostic ladder and secure baseline review
- Activity: rotating troubleshooting stations
- Homework: complete secure baseline review artifact
- Watchouts: students focusing on symptoms and not tracing from ingress to provider to host state

## Week 16: Practical exam and mini-project

- Goal: prove independent safe operation
- Prep: assign project prompts and final practical conditions in advance
- Live session: practical build, short demonstration, and defense
- Activity: supervised build and review
- Homework: final package submission
- Watchouts: students prioritizing flashy channels over documented safety and operational maturity
