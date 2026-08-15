# Elite Mentor OS

Elite Mentor OS is a local-first, subject-agnostic mentor plugin for Claude Code and Codex. It turns the current directory into a learning workspace by diagnosing local evidence, building roadmaps, teaching concepts, assigning deliberate practice, reviewing artifacts, validating sources, and preserving continuity through `.mentor/MENTOR_STATE.md`.

Status: **v0.2 extraction-ready proof**. It is usable for testing in real directories, but it is not yet v1.0, institution-ready, enterprise-ready, or sellable without the validation gates below.

## Product Boundary

- Elite Mentor OS is the generic mentor system.
- OpenClaw Mastery is only the first proof-pack and must not drive generic mentoring unless local evidence shows the user is in this curriculum.
- The plugin must adapt to code repos, study folders, curriculum repos, empty directories, and resource bundles without assuming one subject.
- It must propose writes before changing `.mentor/`, curriculum files, portfolio artifacts, or repo files.

## Native Surfaces

- Claude plugin manifest: `.claude-plugin/plugin.json`
- Codex plugin manifest: `.codex-plugin/plugin.json`
- Shared core policy: `core/MENTOR_OS.md`
- Public skills: `diagnose`, `mentor`, `roadmap`, `review`, `openclaw-master`
- Claude agents: `mentor-professor`, `research-auditor`, `assessment-board`
- OpenClaw proof-pack: `proof-packs/openclaw/OPENCLAW_PROOF_PACK.md`
- Validation pack: `validation/VALIDATION.md`

## Install From This Repo

Claude Code:

```text
/plugin marketplace add HaseebAhmed-official/openclaw-mastery-curriculum
/plugin install elite-mentor-os@elite-mentor-os-marketplace
/elite-mentor-os:diagnose
```

Claude Code CLI sparse checkout:

```bash
claude plugin marketplace add HaseebAhmed-official/openclaw-mastery-curriculum --sparse .claude-plugin plugins/elite-mentor-os
```

Codex CLI:

```bash
codex plugin marketplace add HaseebAhmed-official/openclaw-mastery-curriculum --sparse .agents/plugins --sparse plugins/elite-mentor-os
```

Then open a fresh session in any directory and invoke one of the plugin skills.

## Test In Any Directory

Use these starter prompts:

- `Diagnose this directory as a learning workspace. Do not write files unless I approve.`
- `Build a mastery roadmap from the local files and my current beginner level.`
- `Teach the next concept with retrieval, practice, transfer, and a repair drill.`
- `Review my progress, source quality, and next evidence artifact.`

Pass criteria:

- It identifies the directory role instead of forcing OpenClaw.
- It reads existing `.mentor/MENTOR_STATE.md` when present.
- It proposes the smallest useful state update when state is missing.
- It separates facts, assumptions, weak sources, and current-source requirements.
- It refuses silent writes and high-stakes personalized advice.

## v1.0 Gates

Do not call this product complete until:

- Claude Code install/load tests pass from the remote marketplace.
- Codex discovery and skill invocation pass in a fresh session.
- At least three non-OpenClaw directories pass diagnosis, roadmap, mentor, and review scenarios.
- One OpenClaw learner session produces roadmap, practice, review, and state-update evidence.
- External adversarial Codex and Claude reviews find no critical blockers.
- Security, prompt-injection, high-stakes, privacy, and unsafe-write tests have no critical findings.
- Plugin evaluation reaches 95+ or every remaining warning has a documented accepted-risk rationale.
- `PROJECT_STATE.md`, `.mentor/MENTOR_STATE.md`, and this README match the actual product state.
