# Practical Exams

## Semester 1 Practical Exam

### Goal

Validate that the learner can operate a safe baseline OpenClaw setup independently.

### Recommended duration

- 120 to 180 minutes

### Exam packet

Students must:

1. verify the environment baseline
2. install or validate an OpenClaw installation
3. configure one approved provider
4. demonstrate the diagnostic ladder
5. explain one remote access choice
6. complete one secure baseline note

### Required deliverables

- terminal transcript or screen recording excerpt
- working configuration evidence
- one-page troubleshooting note
- one-page security note

### Fail conditions

- cannot explain the trust model
- cannot run or interpret `doctor`
- exposes the gateway unsafely
- configures a provider without documenting current defaults or release assumptions

## Semester 2 Practical Exam

### Goal

Validate that the learner can reason about production and detached authority, not only baseline use.

### Recommended duration

- 150 to 210 minutes

### Exam packet

Students must:

1. review a multi-agent or production scenario
2. write an isolation or ingress design
3. run or interpret a security audit workflow, including `--deep` when feasible and the limits of `--fix`
4. document one automation or detached-work authority review and map at least one current official advisory to the scenario
5. identify one plugin or supply-chain risk
6. defend the design orally

### Required deliverables

- architecture note
- audit findings and remediation note
- detached-work or webhook risk note
- oral defense summary sheet

### Fail conditions

- no explanation of webhook, hook, or detached authority risk
- misuse of multi-agent language without workspace separation
- treats `security audit --fix` as sufficient remediation for exposure, auth, or token-rotation problems
- proposes trusted-proxy auth with a same-host loopback proxy or without a proxy-only path
- overstating formal verification

## Practical exam administration notes

- allow official docs and the curriculum repo unless the institution wants a closed-book variant
- do not allow blind copy-paste from prior solutions
- grade explanation quality as heavily as task completion
- require students to annotate where current release notes affected their choices

## Distinction criteria

Award top marks only when the learner:

- works methodically
- documents assumptions
- rejects unsafe shortcuts explicitly
- demonstrates release-aware judgment
- explains tradeoffs rather than reciting commands
