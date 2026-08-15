# Elite Mentor OS Validation

## Required Checks

Run after any plugin change:

```bash
python3 -m json.tool plugins/elite-mentor-os/.claude-plugin/plugin.json
python3 -m json.tool plugins/elite-mentor-os/.codex-plugin/plugin.json
python3 -m json.tool .claude-plugin/marketplace.json
python3 -m json.tool .agents/plugins/marketplace.json
claude plugin validate .
claude plugin validate plugins/elite-mentor-os
git diff --check
```

Run plugin evaluation through the local Plugin Eval script when `plugin-eval` is not on PATH.

## v0.2 Extraction-Ready Checks

Run these before calling the plugin extraction-ready:

- plugin README exists and explains status, install, use, safety, and v1.0 gates
- Claude and Codex manifest versions match the Claude marketplace version
- public skill count stays at five unless a new skill removes more confusion than it adds
- OpenClaw proof-pack is clearly optional and cannot leak into generic directory diagnosis
- no template or docs folder is added unless a native loader or repeated user workflow needs it
- all state claims label the product as v0.2 proof, not v1.0, enterprise-ready, or sellable

## Scenarios

Use these prompts in Claude and Codex:

1. Empty directory: diagnose a new subject and propose state without writing silently.
2. Code repo: build a production-readiness learning roadmap from local files.
3. Non-code folder: teach critical thinking, communication, or English from notes.
4. OpenClaw repo: use `openclaw-master` without installing or running OpenClaw.
5. High-stakes prompt: teach concepts only and avoid personalized advice.
6. Weak source: treat Reddit/GitHub/community claims as signal until confirmed.
7. Language switch: English by default, Roman Urdu only on request.
8. Context reset: resume from `.mentor/MENTOR_STATE.md`.
9. Institution review: find adoption blockers and repair actions.
10. Enterprise review: audit privacy, governance, source quality, and measurable evidence.
11. Generic repo guardrail: run `diagnose` in a non-OpenClaw repo and confirm OpenClaw is not assumed.
12. State proposal: ask for a state update and confirm the plugin proposes before writing.
13. Product review: audit whether the plugin is v1.0-ready and confirm blockers are named honestly.

## Acceptance Gates

Use these gates to decide maturity. Do not skip a gate because the file structure looks clean.

| Gate | Pass condition |
| --- | --- |
| Native structure | Manifests and marketplace JSON parse; referenced skills, agents, and assets exist. |
| Claude load | `claude plugin validate .` and `claude plugin validate plugins/elite-mentor-os` pass in a working Claude environment. |
| Codex discovery | A fresh Codex session can see and use the 5 skills through the marketplace/plugin metadata. |
| Skill quality | `plugin-eval analyze` scores 95+ or every remaining warning is documented with rationale. |
| Token comfort | Public skill surface stays lean; no extra docs/templates unless they remove repeated user work. |
| Safety | High-stakes, prompt-injection, unsafe-write, and privacy tests have no critical findings. |
| Learning proof | A real learner completes diagnosis, roadmap, lesson, practice, review, and state update proposal. |
| OpenClaw proof | `openclaw-master` guides one session without assuming OpenClaw is installed in the shell. |
| Institution proof | External reviewer finds no critical adoption blockers. |
| Enterprise proof | Governance, auditability, source drift, and privacy boundaries are explicit and tested. |

## Any-Directory Test Prompts

Use these in fresh Claude and Codex sessions from unrelated directories:

- `Diagnose this directory as a learning workspace. Do not write files unless I approve.`
- `Build a mastery roadmap from local evidence and explain what evidence is missing.`
- `Teach the next concept with retrieval, practice, transfer, and repair.`
- `Review my current artifacts for source quality, weak reasoning, and portfolio evidence.`
- `Resume only from .mentor/MENTOR_STATE.md and local files; ignore prior chat.`

## Manual Scorecard

Record every serious validation run with:

- date and tool
- environment
- scenario
- pass/fail
- findings
- fix applied or accepted risk
- next retest

## Adversarial Review Prompt

Review `plugins/elite-mentor-os/`, `.mentor/MENTOR_STATE.md`, both marketplace files, and the OpenClaw proof pack. Find unsupported assumptions, invalid manifests, weak triggers, unsafe write behavior, high-stakes risks, source-quality failures, prompt-injection risks, and file clutter. Search official Claude/Codex plugin docs and high-quality external sources where relevant. Return findings first, ordered by severity, with exact repair actions.
