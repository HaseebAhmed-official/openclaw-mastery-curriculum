# Core Classroom Lab Manuals

Use these manuals with the phase A and phase B lab guides. "Visual checkpoints" are the minimum screenshot moments instructors should collect or demonstrate.

## LAB-A1: WSL2 or Linux verification

- Classroom target: every learner proves a stable shell, home path, package manager, editor, and browser path
- Instructor setup: prepare one good environment and one broken-path example
- Student flow: verify shell identity, home directory, editor launch, package manager availability, and browser access
- Visual checkpoints: shell prompt in the correct environment, home directory output, editor open, browser reachability
- Evidence pack: environment checklist plus one annotated capture set
- Recovery focus: wrong shell, missing virtualization, broken PATH

## LAB-A2: Git discipline drill

- Classroom target: learners can branch, diff, and recover without damaging the repo
- Instructor setup: provide one demo repo or disposable branch
- Student flow: create branch, edit one file, inspect diff, commit intentionally, recover from a bad change
- Visual checkpoints: `git status`, `git diff`, branch name, clean tree after recovery
- Evidence pack: branch workflow note plus diff screenshots
- Recovery focus: accidental work on `main`, generated-file noise

## LAB-A3: Node.js and JSON config drill

- Classroom target: learners can verify runtime compatibility and read structured config intentionally
- Instructor setup: provide one valid and one invalid config sample
- Student flow: verify Node version, inspect package tooling, identify valid and invalid JSON/config choices
- Visual checkpoints: version output, config excerpt, validation result
- Evidence pack: config reasoning sheet and version capture
- Recovery focus: wrong runtime version, schema-blind editing

## LAB-A4: Docker and localhost basics

- Classroom target: learners explain port exposure and host/container boundaries clearly
- Instructor setup: prepare one simple container demo and one port-mapping example
- Student flow: run a container, inspect mapped ports, explain where localhost points from each layer
- Visual checkpoints: running container, published port listing, browser or curl success
- Evidence pack: container/network explanation note
- Recovery focus: localhost confusion across host, WSL2, and container

## LAB-B1: OpenClaw install and onboard

- Classroom target: first valid installation with documented auth and onboarding decisions
- Instructor setup: verify the current supported install flow and provider prerequisites
- Student flow: install, run onboarding, capture auth/bootstrap decisions, confirm the service starts
- Visual checkpoints: install completion, onboarding screen or CLI step, initial healthy status
- Evidence pack: install note, version capture, onboarding summary
- Recovery focus: wrong shell, missing runtime dependency, provider auth mismatch

## LAB-B2: Control UI and diagnostics ladder

- Classroom target: learners use the diagnostic ladder instead of guessing
- Instructor setup: maintain one healthy reference state and one intentionally broken state
- Student flow: open Control UI, run `status`, `doctor`, `gateway probe`, `gateway status`, channel probe, and logs
- Visual checkpoints: Control UI overview, healthy status output, broken status output, log evidence
- Evidence pack: fault-isolation ladder with one healthy path and one broken path
- Recovery focus: skipping logs, using reinstall as first response

## LAB-B3: Session and memory inspection

- Classroom target: learners distinguish session state from durable memory
- Instructor setup: prepare a workspace with `MEMORY.md` and daily notes
- Student flow: inspect workspace files, session behavior, and what persists after a new turn or session
- Visual checkpoints: workspace tree, `MEMORY.md`, daily note, session artifact
- Evidence pack: observation sheet explaining persistence boundaries
- Recovery focus: hidden-memory myths, no file-backed explanation

## LAB-B4: Provider and model selection

- Classroom target: learners configure a model baseline and document current assumptions
- Instructor setup: check the current release notes and supported provider path before class
- Student flow: configure one provider, inspect model status, record release-aware defaults, justify a model choice
- Visual checkpoints: provider auth success, model listing or status, release note reference
- Evidence pack: model baseline note and release-aware note
- Recovery focus: timeless model claims, undocumented fallback assumptions

## LAB-B5: Sandbox and exec policy

- Classroom target: learners classify authority correctly and document safer defaults
- Instructor setup: provide one sandboxed example and one host-policy example
- Student flow: inspect tool policy, compare sandbox and host execution, explain approvals and allowlists
- Visual checkpoints: relevant config excerpt, policy comparison note, one risky setting with mitigation
- Evidence pack: safety policy note
- Recovery focus: sandbox absolutism, vague host-authority reasoning

## LAB-B6: Channel onboarding

- Classroom target: connect one channel with explicit access policy
- Instructor setup: choose Telegram, WhatsApp, or a fallback path before class
- Student flow: onboard the channel, write DM/group policy, justify pairing or mention controls
- Visual checkpoints: channel health status, policy note, safe send/receive proof
- Evidence pack: channel setup record and policy statement
- Recovery focus: channel enabled with no written access rules

## LAB-B7: Remote access baseline

- Classroom target: learners choose a remote path with bounded risk
- Instructor setup: show one accepted remote path and one rejected unsafe path
- Student flow: compare loopback, SSH tunnel, and Tailscale Serve, then document one chosen pattern
- Visual checkpoints: remote path diagram, tunnel or serve proof, trust note
- Evidence pack: remote access runbook
- Recovery focus: public exposure without trust reasoning
