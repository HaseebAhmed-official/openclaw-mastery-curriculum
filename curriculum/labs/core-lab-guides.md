# Core Lab Guides

## How to use these guides

Each lab includes:

- objective
- recommended duration
- default environment lane
- prerequisites
- procedure
- required evidence
- common failure modes
- grading hooks

## LAB-A1: WSL2 or Linux verification

### Objective

Verify that the learner has a usable shell, package manager, filesystem, editor workflow, and browser path for the rest of the course.

### Duration

- 45 to 60 minutes

### Default lane

- low-cost student path
- standard university lab path

### Prerequisites

- machine access
- instructor-approved installation instructions

### Procedure

1. Open the terminal and confirm the active environment.
2. Print the current working directory and home directory.
3. Verify the shell can create, edit, move, and delete a test file.
4. Verify package manager access.
5. Verify browser launch path and copy/paste from terminal to browser.
6. Record environment details in a setup worksheet.

### Required evidence

- screenshot or transcript showing shell, home path, and package manager
- one short note explaining host path vs Linux path distinction

### Common failure modes

- WSL2 not actually enabled
- student running commands in PowerShell while following Linux directions
- file path confusion across Windows and Linux mounts

### Grading hooks

- pass only if the student can explain which shell they used and why
- deduct if the evidence does not distinguish Windows from WSL2 paths

## LAB-A2: Git discipline drill

### Objective

Teach safe repo movement: branch, edit, diff, commit, inspect, and recover.

### Duration

- 60 to 75 minutes

### Procedure

1. Clone or receive a practice repository.
2. Create a feature branch.
3. Make a small change to a markdown file.
4. Review `git status` and `git diff`.
5. Commit the change with a meaningful message.
6. Reset the branch back to a clean working tree without deleting history.

### Required evidence

- branch name
- short commit hash
- screenshot or transcript of `git diff`

### Common failure modes

- editing on `main`
- committing unrelated files
- not understanding staged vs unstaged state

### Grading hooks

- require clean working tree at submission
- require a short explanation of staged vs unstaged state

## LAB-A3: Node.js and JSON config drill

### Objective

Build confidence reading structured configuration and verifying runtime requirements.

### Duration

- 60 minutes

### Procedure

1. Verify Node.js version.
2. Record the current OpenClaw-supported version range from official docs.
3. Inspect a sample JSON or JSON-like config.
4. Identify required fields, optional fields, and one likely validation risk.
5. Make a valid edit and explain its effect.

### Required evidence

- terminal output showing Node version
- a before/after config snippet
- one paragraph explaining the edit

### Common failure modes

- quoting mistakes
- trailing commas in strict JSON contexts
- editing values without knowing field meaning

### Grading hooks

- no credit if the student cannot explain what changed semantically

## LAB-A4: Docker and localhost basics

### Objective

Teach container thinking well enough for sandboxing and networking labs later.

### Duration

- 75 minutes

### Procedure

1. Verify Docker availability.
2. Run a simple container.
3. Inspect running containers and ports.
4. Compare localhost inside host vs container.
5. Explain how Docker supports OpenClaw sandboxing.

### Required evidence

- one container run log
- one paragraph explaining host vs container boundary

### Common failure modes

- Docker service not running
- misunderstanding published port vs internal port

### Grading hooks

- require explanation, not only command output

## LAB-B1: OpenClaw install and onboard

### Objective

Produce a working local OpenClaw install with a successful onboarding flow.

### Duration

- 90 to 120 minutes

### Default lane

- standard university lab path

### Prerequisites

- LAB-A1 through LAB-A3
- current official install instructions

### Procedure

1. Confirm current supported install path and version guidance.
2. Install OpenClaw using the official documented method.
3. Run the onboarding flow.
4. Configure one provider or approved classroom auth path.
5. Verify the gateway launches and responds.
6. Record version, environment, provider, and any deviations from default instructions.

### Required evidence

- version output
- onboarding completion evidence
- one page install runbook

### Common failure modes

- stale install instructions
- provider auth pasted into the wrong environment
- students skipping version checks

### Grading hooks

- require explicit version/date notation
- require one troubleshooting note even if install succeeded

## LAB-B2: Control UI and diagnostics ladder

### Objective

Normalize disciplined troubleshooting using the documented command ladder.

### Duration

- 90 minutes

### Procedure

1. Open the Control UI and identify the main operational panels.
2. Run `openclaw status`.
3. Run `openclaw doctor`.
4. Run `openclaw gateway probe`.
5. Run `openclaw gateway status`.
6. Run `openclaw channels status --probe`.
7. Run `openclaw logs --follow`.
8. Compare the output against one instructor-provided broken scenario.

### Required evidence

- full diagnostic ladder transcript
- a fault-isolation note that narrows one issue to one layer

### Common failure modes

- students stopping after the first error
- students not reading logs long enough to identify sequence

### Grading hooks

- highest marks require a clear isolation path, not just raw output

## LAB-B3: Session and memory inspection

### Objective

Teach what really persists between sessions.

### Duration

- 60 to 75 minutes

### Procedure

1. Start from an existing OpenClaw workspace.
2. Locate `MEMORY.md` and any daily note files.
3. Trigger or inspect a small conversational change.
4. Compare what is visible in workspace files with what students think the agent "remembers."
5. Write a short note distinguishing persisted state from non-persisted state.

### Required evidence

- memory/session observation sheet
- one screenshot or snippet of workspace memory files

### Common failure modes

- assuming internal model state is visible nowhere
- confusing session transcript with long-term memory

### Grading hooks

- require explicit use of the phrase "persisted to disk" or equivalent

## LAB-B4: Provider and model selection

### Objective

Teach learners to choose a provider baseline with current release awareness.

### Duration

- 90 minutes

### Procedure

1. Read the latest release notes relevant to provider defaults.
2. Identify the current default or recommended model path.
3. Configure the provider.
4. Explain why the selected model is acceptable for the use case.
5. Record one fallback or alternative.
6. Note one cost or rate-limit consideration.

### Required evidence

- provider setup review
- release-aware note with date and release reference

### Common failure modes

- using outdated defaults from old screenshots
- selecting weak models for tool-heavy tasks without justification

### Grading hooks

- no full credit without release-aware documentation

## LAB-B5: Sandbox and exec policy

### Objective

Make tool authority tangible and governable.

### Duration

- 75 to 90 minutes

### Procedure

1. Identify which tools are sandboxed and which can reach the host.
2. Review exec approval modes.
3. Propose a policy for a student-safe environment.
4. Document one dangerous misconfiguration and one mitigation.

### Required evidence

- safety policy note
- one scenario table with safe, unsafe, and conditional actions

### Common failure modes

- overstating Docker as total security
- assuming approvals can be skipped in teaching environments

### Grading hooks

- require explicit least-privilege language

## LAB-B6: Channel onboarding

### Objective

Connect a communication surface without widening trust accidentally.

### Duration

- 90 minutes

### Procedure

1. Select the approved channel or webchat fallback.
2. Pair or configure the channel.
3. Document DM scope or mention policy.
4. Test one allowed interaction and one blocked or disallowed interaction.

### Required evidence

- working interaction proof
- written channel policy

### Common failure modes

- unclear group mention rules
- exposing a channel before writing the policy

### Grading hooks

- require both technical completion and policy clarity

## LAB-B7: Remote access baseline

### Objective

Teach safest-default remote access.

### Duration

- 90 to 120 minutes

### Procedure

1. Start from a loopback-only local gateway.
2. Implement the approved remote access method such as SSH tunnel or Tailscale Serve.
3. Confirm the access path works remotely.
4. Record the trust assumptions.
5. Reject one unsafe alternative in writing.

### Required evidence

- remote access runbook
- trust-boundary statement

### Common failure modes

- direct public exposure
- incomplete explanation of identity flow

### Grading hooks

- require an explicit "why not public exposure" answer
