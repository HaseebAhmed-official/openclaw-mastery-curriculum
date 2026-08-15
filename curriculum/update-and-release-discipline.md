# Update and Release Discipline

## Why this matters

OpenClaw moves quickly. Defaults, security checks, model selections, plugin behavior, and deployment guidance can shift across releases. A world-class curriculum must therefore teach not only platform features, but also how to check whether those features changed.

## Required release discipline

Before any week involving providers, security controls, plugins, channels, automation, or deployment, instructors and learners should:

1. check the current installed version
2. read the latest release notes relevant to that module
3. review current official security advisories that overlap with that module's surface
4. verify the current update channel
5. note any behavior changes that affect labs or grading

## Operational topics learners must know

### Updating

- `openclaw update`
- `openclaw update --dry-run`
- `openclaw update --json`
- `openclaw update status --json`
- channel switching
- version pinning and one-off tag targeting
- rollback awareness
- npm hotfix awareness when the GitHub release and npm package differ
- post-update `doctor`, restart, and health verification

### Release channels

- `stable`: npm `latest`; normal baseline for teaching and most users
- `extended-stable`: trailing supported-month package channel; exact verified package, foreground-only updates, read-only update hints, and no fallback to another channel
- `beta`: candidate channel that can fall back to stable when its dist-tag is missing or older
- `dev`: moving `main`; experimentation only and not a production baseline

Package-install decisions must use npm dist-tags as the source of truth. A release review must record stable, extended-stable when relevant, and any preview tag used by a lab without treating beta as the default.

### Current baseline example

The August 13, 2026 review found three distinct operational baselines: stable `v2026.7.1-2` / `openclaw@2026.7.1-2`, extended-stable `openclaw@2026.6.34`, and beta `openclaw@2026.8.1-beta.1`. Teach learners to record the selected channel, package source, exact version, and plugin convergence behavior rather than calling whichever tag is numerically newest the production baseline.

### Plugin and package updates

Current OpenClaw releases treat plugin installation and plugin updates as first-class maintenance surfaces. Learners must review:

- plugin source choice: ClawHub, npm, git, or local path
- runtime proof with `openclaw plugins inspect <plugin-id> --runtime --json`
- dependency status from `openclaw plugins list --json`
- official plugin externalization and repair behavior across OpenClaw updates
- the difference between installed plugin inventory and a running Gateway that has actually loaded the plugin

### Connected coding-agent updates

Current releases add `openclaw attach`, which launches Claude Code with a temporary grant bound to one Gateway session. Teach the grant lifetime, credential handling, session selection, revocation behavior, strict MCP configuration, and the difference between scoped attachment and process-wide credentials. Codex delegation and native subagent results should be audited through task records rather than treated as invisible parallelism.

### Security cadence

- treat new official advisories as teaching inputs, not just maintainer notes
- group large advisory waves by failure family: requester authorization, approval equivalence, plugin persistence, sandbox and SSRF containment, credential ownership, channel identity, and detached authority
- revalidate security, deployment, automation, plugin, browser, and contributor modules when advisories touch their scope
- document whether a lab or rubric assumes behavior before or after a specific security fix
- require exact-version evidence; a clean current audit does not prove that an older package was unaffected

### Cohort consistency

- freeze teaching cohorts to a known version or channel when needed
- document any module that depends on a rapidly moving surface
- avoid grading students against unstated defaults

## Teaching rule

Any curriculum statement about defaults, model choices, or current behavior must either:

- cite the official docs and validation date, or
- cite the official advisories if security behavior changed recently, or
- tell the learner to check the current release notes before proceeding

## Best insertion points in the program

- Semester 1 Week 10: providers and model defaults
- Semester 2 Week 1: production framing
- Semester 2 Week 8: plugins, externalized packages, and supply-chain review
- Production / DevOps track
- Contributor / Core track
