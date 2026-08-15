# Upstream Review Log

## 2026-04-24

- Reviewed upstream baseline through OpenClaw release `v2026.4.23`
- Reviewed selected official OpenClaw advisories published on `2026-04-23` that map directly to current curriculum security surfaces
- Change category: advisory-aware security and maintenance clarification with no release drift
- Confirmed the curriculum repo baseline after adding delivery assets, templates, grading assets, and maintenance automation
- Added advisory-aware reading, security, and maintenance references to the curriculum
- Confirmed no additional release-driven curriculum changes were required beyond the existing `v2026.4.23` baseline
- Curriculum files touched: `curriculum/sources/official-reading-map.md`, `curriculum/sources/validation-register.md`, `curriculum/governance-and-security-strand.md`, `curriculum/semester-2/index.md`, `curriculum/semester-2/teaching-guide.md`, `curriculum/labs/advanced-lab-guides.md`, `curriculum/update-and-release-discipline.md`, `curriculum/templates/release-aware-note-template.md`, `curriculum/maintenance/upstream-review-playbook.md`, `curriculum/maintenance/change-control-checklist.md`, `curriculum/maintenance/upstream-state.json`
- Follow-up validation: targeted revalidation of Semester 2 security teaching and audit labs before the next formal curriculum review
- Established the automated drift-check system for future upstream review

### 2026-04-24 targeted follow-up

- Upstream release/advisory baseline unchanged from the same-day review
- Change category: targeted Semester 2 security-teaching revalidation
- Curriculum files touched: `curriculum/governance-and-security-strand.md`, `curriculum/semester-2/index.md`, `curriculum/semester-2/teaching-guide.md`, `curriculum/labs/advanced-lab-guides.md`, `curriculum/assessment/question-bank.md`, `curriculum/assessment/practical-exams.md`, `curriculum/rubrics/master-rubric.md`
- Outcome: clarified `security audit --deep` vs `--fix`, trusted-proxy failure modes, workspace dotenv ownership boundaries, and ACP child-session constraint inheritance
- Follow-up validation: include these items in the next external curriculum audit

## 2026-05-04

- Reviewed upstream baseline through OpenClaw GitHub release `v2026.5.3`
- Reviewed npm package baseline `openclaw@2026.5.3-1`, published after `v2026.5.3` as a core npm hotfix
- Reviewed official release highlights touching plugin install/update hardening, externalized official plugin behavior, file-transfer tooling, channel streaming progress drafts, `/steer`, `/side`, update/doctor behavior, invalid-config fail-closed behavior, provider/proxy handling, memory/search reliability, and Codex harness/persona forwarding
- Reviewed selected open GitHub issues as non-authoritative risk signals, including current plugin, Discord, WSL/browser, security-audit, and performance reports
- Change category: release-drift curriculum repair
- Curriculum files touched: `PROJECT_STATE.md`, `.mentor/MENTOR_STATE.md`, `curriculum/maintenance/upstream-state.json`, `curriculum/maintenance/review-log.md`, `curriculum/sources/official-reading-map.md`, `curriculum/sources/validation-register.md`, `curriculum/update-and-release-discipline.md`, `curriculum/semester-1/index.md`, `curriculum/semester-2/index.md`, `curriculum/labs/lab-catalog.md`, `curriculum/labs/core-lab-guides.md`, `curriculum/labs/advanced-lab-guides.md`, `curriculum/labs/specialization-lab-guides.md`, `curriculum/tracks/plugin-developer.md`, `curriculum/tracks/production-devops.md`, `curriculum/tracks/security-hardening.md`
- Outcome: curriculum baseline updated from `v2026.4.23` to `v2026.5.3` / `2026.5.3-1`; latest plugin/update/file-transfer/release-discipline changes mapped into teaching surfaces
- Follow-up validation: run fresh external Codex/Claude adversarial review after this patch and convert at least the highest-value labs into fully command-by-command manuals

## 2026-08-13

- Reviewed current stable GitHub/npm baseline `v2026.7.1-2` / `openclaw@2026.7.1-2`
- Reviewed package-only extended-stable baseline `openclaw@2026.6.34` and observed beta tag `openclaw@2026.8.1-beta.1` without promoting beta into the teaching baseline
- Reviewed current official install, update-channel, `openclaw attach`, release-note, security-policy, and advisory surfaces
- Reviewed all 112 official advisories published after the prior 2026-04-24 advisory cutoff; integrated representative cases by recurring failure family instead of copying the full feed into teaching material
- Change category: major release, documentation, runtime, coding-agent, update-channel, and advisory drift repair
- Curriculum files touched: `PROJECT_STATE.md`, `.mentor/MENTOR_STATE.md`, `curriculum/maintenance/upstream-state.json`, `curriculum/maintenance/review-log.md`, `curriculum/sources/official-reading-map.md`, `curriculum/sources/validation-register.md`, `curriculum/update-and-release-discipline.md`, `curriculum/governance-and-security-strand.md`, `curriculum/automation-and-detached-work.md`, `curriculum/semester-1/index.md`, `curriculum/semester-2/index.md`, `curriculum/labs/advanced-lab-guides.md`, `curriculum/tracks/security-hardening.md`, `curriculum/templates/release-aware-note-template.md`
- Outcome: refreshed the supported Node floor and flagged conflicting Node 24/26 recommendation text across official docs; taught stable, extended-stable, beta, and dev semantics; added scoped `openclaw attach` and durable coding-agent evidence; strengthened approval, plugin persistence, sandbox/SSRF, credential ownership, channel identity, and detached-authority casework
- Follow-up validation: map the advisory-family cases into assessment questions and model answers, run command-level labs on an installed stable OpenClaw environment, and obtain fresh external adversarial review

## Logging rule

Every future upstream review should append:

- date
- upstream release reviewed
- change category
- curriculum files touched
- whether a follow-up validation pass is required
