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

## Logging rule

Every future upstream review should append:

- date
- upstream release reviewed
- change category
- curriculum files touched
- whether a follow-up validation pass is required
