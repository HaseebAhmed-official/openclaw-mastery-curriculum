# Internal Migration Audit - 2026-08-15

## Decision Record

- Candidate audited: commit `eb8d423`
- Scope: platform-agnostic Agent Harness Systems Engineering curriculum, reference harness, source controls, and OpenClaw maintenance automation
- Excluded product: Elite Mentor OS, which is separately versioned and frozen by user decision
- Reviewer: repository-authoring Codex session; this is internal evidence, not independent validation
- Review date: 2026-08-15, Asia/Karachi

## Verdict

| Claim level | Verdict | Reason |
| --- | --- | --- |
| Strong self-study draft | `conditional` | The program spine, labs, assessments, sources, and bounded executable fixtures are coherent; advanced labs still need clean reproduction and some require external systems. |
| Supervised pilot | `conditional` | Run critical labs in clean learner environments first, freeze expected evidence, and brief assessors on current fixture limits. |
| Standalone ready-to-teach program | `reject` | Complete lecture delivery, accessibility review, timing evidence, and independently reproduced labs do not yet exist. |
| Institution-ready curriculum | `reject` | There is no real cohort, assessor-reliability result, delayed transfer study, independent academic review, or adoption evidence. |
| Enterprise-ready program | `reject` | There is no organizational security/privacy/legal review, production workload evidence, support model, or enterprise pilot. |
| World-class or optimum claim | `reject` | Internal artifacts and tests cannot establish comparative excellence or learning effectiveness. |

## Executed Checks

| Check | Observed result | Boundary |
| --- | --- | --- |
| Reference harness | 20 of 20 `unittest` cases passed | Standard-library teaching fixtures only; not a production runtime. |
| OpenClaw drift script | 4 of 4 `unittest` cases passed | Tests request construction and issue-body behavior, not GitHub Actions execution. |
| Python compilation | 15 files compiled from source | Syntax/import-independent compilation is not type, lint, or security analysis. |
| JSON parsing | 1 repository JSON file parsed | Schema semantics were reviewed manually; no separate JSON Schema exists. |
| Curriculum structure | 25 unique labs each have one guide; 90 sequential questions; 54 sequential oral prompts; both semesters contain weeks 1-16 | Structural completeness is not pedagogical validity. |
| Outcome traceability | PLO-1 through PLO-10 each map to direct evidence, teaching locations, required labs, and high-stakes assessment | Mapping is internally coherent but has not been empirically validated with learners or assessors. |
| Local Markdown links | Targets validated across 75 Markdown files | Anchor fragments and external semantics were not certified by this check. |
| Duplicate-content check | No exact duplicate curriculum files | Near-duplicate prose still requires editorial judgment. |
| Source crawl | 128 unique HTTPS URLs checked | Ten legitimate sources rejected or timed out in the generic crawler but were independently resolved through current browser/search or Crossref; two deliberate invalid fixtures and two code-span parser artifacts were excluded. |
| Secret checks | No high-confidence secret signature or likely hard-coded credential assignment found | This is a pattern scan, not full history or specialized secret scanning. |
| Git whitespace | `git diff --check` passed before candidate commit | Does not replace formatters or linters. |
| Optional analyzers | `ruff`, `mypy`, `bandit`, `gitleaks`, and `actionlint` unavailable | No result is claimed for these tools. |

## Current Source Findings

- MCP teaching now targets the `2026-07-28` stateless, per-request negotiation model instead of initialization-era assumptions.
- A2A teaching is pinned to released specification `1.0.0`.
- OpenTelemetry GenAI teaching points to the dedicated semantic-conventions repository and remains a protocol/telemetry lab requirement rather than a reference-harness claim.
- Hermes Agent evidence is pinned to `v2026.8.13`; ChatGPT Work and xAI claims are dated public-contract claims with private internals marked `unknown`.
- OpenClaw stable remains `v2026.7.1-2`, npm extended-stable remains `2026.6.34`, and beta was observed at `2026.8.1-beta.2`. Stable release drift was false at review time.
- OpenClaw advisory metadata showed 647 published records, latest publication `2026-06-30T01:11:32Z`, and latest update `2026-08-13T17:27:46Z`. The earlier review covered the 112 advisories published after the prior cutoff; this audit did not reread all 647 records.

## Findings Repaired In Candidate

1. Replaced stale MCP/A2A/OpenTelemetry assumptions with current pinned source boundaries.
2. Added dated claim ledgers for Hermes Agent, ChatGPT Work, and xAI agent tooling without inferring managed internals.
3. Added bounded memory, orchestration, integration/export, per-attempt persistence, and policy-based evaluation fixtures.
4. Rejected reused provider call identities, invalid memory-policy outputs, invalid worker outputs, malformed adapter shapes, and contaminated export event streams.
5. Clarified advisory publication versus update timestamps and recorded stable, extended-stable, and beta channels separately.
6. Pinned the GitHub checkout action and prevented drift-check authentication tokens from entering request URLs.

## Residual Blockers

- A bounded pinned MCP `2.0.0` in-process proof and A2A SDK `1.1.2` JSON-RPC/ASGI proof are now instructor-executed, but neither proves external network transport, TLS/OAuth, disconnect/timeout/retry, cancellation, side-effect approval, streaming, duplicate handling, or cross-implementation compatibility.
- A bounded OpenTelemetry SDK `1.44.0` in-memory span proof is instructor-executed against a commit-pinned development GenAI schema, but no OTLP backend, metrics/logs, SLO/alert path, production redaction audit, network model provider, or real provider compatibility fixture is reproduced.
- Durable workflow, process isolation, handler timeout/cancellation, egress control, redaction, concurrency, distributed state, and hostile multi-tenant fixtures remain absent.
- Authored labs have not been independently run in clean WSL/Linux, container, VPS, and constrained-budget lanes with retained evidence.
- No representative maintained evaluation corpus, validated graders, uncertainty analysis, leakage study, or cost/latency baseline exists.
- No accessibility audit, learner timing study, measured assessor calibration, delayed unaided changed-task transfer result, or cohort pilot exists.
- No independent academic, practitioner, security, privacy/legal, or enterprise-governance review has evaluated the migrated scope.
- Optional static, security, secret-history, and workflow linters were unavailable during this audit.

## Maturity Snapshot

At the 2026-08-15 audit, planning estimates were approximately **74% artifact implementation**, **25% hands-on reproducibility evidence**, and **30% institution/enterprise proof**. They are historical prioritization aids only; the addendum below supersedes them. The completion-gate ledger in `PROJECT_STATE.md` overrides every percentage.

## Next Gate

Reproduce the critical lab path in a clean learner environment and retain commands, inputs, outputs, failures, environment fingerprints, timing, and assessor decisions. Do not promote readiness claims until that evidence is reviewed and the residual blockers are materially reduced.

## 2026-08-16 Interoperability Addendum

This addendum is still author-session evidence, not independent review. The reference harness gained one optional exact-version lane: MCP Python SDK `2.0.0`, A2A Python SDK `1.1.2`, and OpenTelemetry SDK `1.44.0`. The default standard-library lane remains dependency-free.

The full 24-test suite passed on Windows Python 3.11.9 and from a Git archive of implementation commit `25d06ae` extracted into a fresh WSL `/tmp` directory. The commit-bound run used CPython 3.14.2, Linux 6.18.33.2 x86-64, glibc 2.35, and an offline Linux wheelhouse; tests took 3.182 seconds. It observed MCP `2026-07-28` discovery and schema rejection, an authenticated A2A JSON-RPC task/artifact exchange plus `401` denial, and linked in-memory agent/tool spans that omitted supplied sensitive values. A2A emitted three upstream protobuf `label()` deprecation warnings.

The fixture is `executed`; LAB-C4, LAB-C5, and LAB-C8 remain `authored`. No second person reproduced the work. Updated planning estimates are approximately **76% artifact implementation**, **28% hands-on reproducibility evidence**, and **30% institution/enterprise proof**. The strong readiness verdicts remain rejected.
