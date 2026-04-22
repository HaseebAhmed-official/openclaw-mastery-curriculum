# OpenClaw Curriculum Pack Validation Review

Validation date baseline: April 22, 2026  
Reviewer mode: adversarial, source-backed, current-state validation  
Target pack root: `E:\Study\Openclaw mastery`  
Primary entry file reviewed: `README.md`  
Intended audience claimed by pack: university-first, reusable for enterprise teams  
Latest official release checked during validation: [`v2026.4.21`](https://github.com/openclaw/openclaw/releases)

## Scope

This review validates the curriculum pack currently present in:

- `README.md`
- `curriculum/program-overview.md`
- `curriculum/prerequisite-bridge.md`
- `curriculum/competency-framework.md`
- `curriculum/assessment-map.md`
- `curriculum/governance-and-security-strand.md`
- `curriculum/semester-1/index.md`
- `curriculum/semester-2/index.md`
- `curriculum/labs/*`
- `curriculum/tracks/*`
- `curriculum/capstones/*`
- `curriculum/rubrics/*`
- `curriculum/sources/*`

Primary source priority used for validation:

1. Official OpenClaw docs
2. Official OpenClaw GitHub repo and releases
3. Official OpenClaw security advisories
4. Official prerequisite docs where relevant

Secondary/community material was not used for any major conclusion unless explicitly labeled. This review is intentionally strict because the stated goal is university-grade plus enterprise-usable mastery material.

## Method

1. Read the local curriculum pack in full.
2. Extracted structural promises and platform claims.
3. Cross-checked current-state claims against official docs, repo pages, releases, and advisories.
4. Red-teamed the pack for technical drift, security overclaim, pedagogical gaps, and certification weakness.
5. Converted the findings into a rewrite-oriented brief.

## 1. Executive Verdict

Overall judgment: **Strong draft**, not near-production-quality and not world-class.

The curriculum's strongest quality is that it gets the **OpenClaw trust model** more correct than most third-party material. It explicitly avoids treating OpenClaw as a hostile multi-tenant boundary, emphasizes loopback-first deployment, keeps security in the core path, and tries to anchor claims to official sources. Those are the right instincts, and they align with current OpenClaw documentation on gateway security, architecture, memory, remote access, and operational posture: [Gateway Security](https://docs.openclaw.ai/gateway/security), [Architecture](https://docs.openclaw.ai/concepts/architecture), [Memory Overview](https://docs.openclaw.ai/concepts/memory), [Remote Access](https://docs.openclaw.ai/gateway/remote), [Getting Started](https://docs.openclaw.ai/start/getting-started).

The pack still fails a world-class review because it **overclaims mastery**, **under-specifies hands-on delivery**, and **misses major current OpenClaw domains** that now materially affect real deployments: automation/tasks, hooks, standing orders, sub-agents, ACP agents, update/rollback governance, plugin supply-chain realities, and current advisory-driven security lessons. It also says it is stable-first and properly labels preview/source-build content, but that rule is not consistently enforced in the core sequence.

Current confidence: **91%**

Why not higher:

- I validated the full local pack and multiple official sources.
- I confirmed the latest official release state as of April 22, 2026.
- I confirmed the formal verification page and threat-model status directly.
- I confirmed current plugin-install and security-risk surfaces through official docs and advisories.
- I am not above 95% because some channel-specific curriculum claims are only thinly sourced and because the official docs themselves are moving fast.

## 2. Scorecard

| Dimension | Score (0-10) | Justification |
| --- | --- | --- |
| Technical correctness | 7 | Core architecture, trust model, memory, remote access, and baseline ops are mostly right, but several claims are weakly sourced or now incomplete. |
| Freshness / current accuracy | 6 | The pack has a validation mindset, but some baseline claims are stale or inconsistently sourced, and draft/advanced material leaks into the core path without labels. |
| Completeness | 5 | Major current OpenClaw domains are missing, especially automation/tasks, hooks, standing orders, sub-agents, ACP, update policy, and plugin supply-chain handling. |
| Pedagogical sequencing | 7 | The high-level progression is reasonable, but "near zero to expert" is overstated and some advanced topics are misplaced. |
| Hands-on quality | 4 | The labs are topic stubs, not deliverable-grade lab guides with procedures, evidence, timing, rollback, or instructor support. |
| Security realism | 7 | Strong trust-model correctness, but incomplete current-state treatment of plugin-install risk, upload/path issues, device auth, and automation/hook exposure. |
| Production / enterprise readiness | 5 | Good starting posture on remote access and hardening, but weak on updates, rollback, release lanes, backup/restore, retention, and operational governance. |
| Extensibility / contributor readiness | 5 | Tracks exist, but the extension model taught is narrower than current OpenClaw reality. |
| Assessment quality | 4 | Rubrics are too generic for credible certification or cross-instructor grading consistency. |
| Internal consistency | 6 | The pack’s own stable-first rule is not consistently followed, and the validation register contains at least one disputed baseline claim. |
| Overall world-class readiness | 4 | Strong framework, insufficient execution depth. |

## 3. Critical Findings

### Finding 1

- Severity: **Critical**
- Area: Stable-vs-draft boundary
- What is wrong:
  The curriculum says stable-release behavior is the teaching baseline and preview/source-build topics must be labeled. It then places formal verification and the ATLAS threat model into the mandatory Semester 2 core without labeling their current maturity status.
- Why it matters:
  Institutions will read core-week content as baseline curriculum. The official threat model is explicitly labeled `Version: 1.0-draft`, and the formal verification page explicitly says the work is bounded, model-based, and not proof that the TypeScript implementation is secure in all respects.
- Evidence from curriculum:
  - `README.md:14`
  - `README.md:84`
  - `curriculum/program-overview.md:18-20`
  - `curriculum/semester-2/index.md:25`
  - `curriculum/sources/official-reading-map.md:43-44`
- Evidence from official sources:
  - [Threat Model (MITRE ATLAS)](https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS)
  - [Formal Verification](https://docs.openclaw.ai/security/formal-verification/)
- Validation status: **Incorrect**
- Fix recommendation:
  Move formal verification out of the mandatory core into an explicitly labeled advanced/draft module. Keep threat modeling in the core, but label the official threat model artifact as draft and living.

### Finding 2

- Severity: **Critical**
- Area: Completeness against current OpenClaw state
- What is wrong:
  The pack claims expert/mastery coverage, but omits several now-important product surfaces: automation/tasks, hooks, standing orders, heartbeat, task flow, sub-agents, ACP agents, and webhook-driven automation.
- Why it matters:
  These are not edge cases. They affect authority boundaries, detached work, background execution, auditability, integration design, and enterprise governance.
- Evidence from curriculum:
  - `curriculum/program-overview.md:85-97`
  - `curriculum/semester-2/index.md`
  - `curriculum/sources/official-reading-map.md`
- Evidence from official sources:
  - [Automation & Tasks](https://docs.openclaw.ai/automation)
  - [Standing Orders](https://docs.openclaw.ai/automation/standing-orders)
  - [Hooks](https://docs.openclaw.ai/automation/)
  - [Sub-Agents](https://docs.openclaw.ai/tools/subagents)
  - [ACP Agents](https://docs.openclaw.ai/tools/acp-agents)
  - [ACP CLI](https://docs.openclaw.ai/cli/acp)
- Validation status: **Incorrect by omission**
- Fix recommendation:
  Add a mandatory module on durable automation, event hooks, standing authority, detached task auditability, sub-agent runtime controls, and ACP integration strategy.

### Finding 3

- Severity: **High**
- Area: Hands-on feasibility
- What is wrong:
  The lab system is mostly a catalog of names and output labels. It is not a runnable lab program.
- Why it matters:
  A curriculum cannot honestly claim hands-on rigor or certification worthiness if instructors still have to invent the actual procedures, failure injections, evidence criteria, grading materials, and rollback notes from scratch.
- Evidence from curriculum:
  - `curriculum/labs/lab-catalog.md`
  - `curriculum/labs/index.md:7-12`
  - `curriculum/labs/environment-lanes.md`
- Evidence from official sources:
  Official docs provide real operator workflows for install, onboarding, remote access, security audit, plugins, and updating, but the curriculum has not converted them into student-ready labs:
  - [Getting Started](https://docs.openclaw.ai/start/getting-started)
  - [Onboarding (CLI)](https://docs.openclaw.ai/start/wizard)
  - [Remote Access](https://docs.openclaw.ai/gateway/remote)
  - [Security CLI](https://docs.openclaw.ai/cli/security)
  - [Plugins CLI](https://docs.openclaw.ai/cli/plugins)
  - [Updating](https://docs.openclaw.ai/install/updating)
- Validation status: **Incorrectly overstated**
- Fix recommendation:
  Replace catalog-only labs with full lab guides: prerequisites, duration, step list, expected outputs, break/fix scenarios, rollback, security note, cost note, and evidence submission requirements.

### Finding 4

- Severity: **High**
- Area: Assessment and certification
- What is wrong:
  The rubric is too generic to support serious certification claims.
- Why it matters:
  Terms like "Operator," "Production," "Developer," "Contributor," and "Specialist" imply defensible competence thresholds. The current rubric does not define track-specific anchors, assessor calibration, anti-shortcut evidence, or failure criteria that reflect real OpenClaw risk.
- Evidence from curriculum:
  - `curriculum/assessment-map.md`
  - `curriculum/rubrics/master-rubric.md`
  - `curriculum/capstones/capstone-specs.md`
- Evidence from official sources:
  Current OpenClaw competence spans auth, remote access, approvals, tasking, plugin install safety, and fast release drift:
  - [Gateway Security](https://docs.openclaw.ai/gateway/security)
  - [Trusted Proxy Auth](https://docs.openclaw.ai/gateway/trusted-proxy-auth)
  - [ClawHub](https://docs.openclaw.ai/tools/clawhub)
  - [Release Policy](https://docs.openclaw.ai/RELEASING)
- Validation status: **Weak**
- Fix recommendation:
  Create track-specific rubrics, assessor notes, mandatory artifact sets, oral-defense challenge banks, and explicit fail gates tied to actual OpenClaw failure modes.

### Finding 5

- Severity: **High**
- Area: Security realism and current threat landscape
- What is wrong:
  The security strand correctly centers trust boundaries and prompt injection, but it undercovers current plugin-install supply-chain risk, browser/file path handling, and real advisory-driven lessons.
- Why it matters:
  A 2026 curriculum must teach current OpenClaw risk, not only generic AI-agent risk.
- Evidence from curriculum:
  - `curriculum/governance-and-security-strand.md:28-45`
  - `curriculum/tracks/plugin-developer.md`
- Evidence from official sources:
  - [OpenClaw security advisories](https://github.com/openclaw/openclaw/security/advisories)
  - [GHSA-m3mh-3mpg-37hw](https://github.com/openclaw/openclaw/security/advisories/GHSA-m3mh-3mpg-37hw)
  - [GHSA-cv7m-c9jx-vg7q](https://github.com/advisories/GHSA-cv7m-c9jx-vg7q)
  - [ClawHub](https://docs.openclaw.ai/tools/clawhub)
  - [Plugins CLI](https://docs.openclaw.ai/cli/plugins)
- Validation status: **Incomplete**
- Fix recommendation:
  Add a current-vulnerabilities unit and make official advisories required reading in the security and plugin tracks.

### Finding 6

- Severity: **Medium**
- Area: Source hygiene / validation register reliability
- What is wrong:
  The validation register presents some claims as settled official-doc facts when the supporting evidence is either thin or in tension with other official surfaces.
- Why it matters:
  The validation register is supposed to be the curriculum’s control plane for correctness. If it is loose, every future module built on it inherits that looseness.
- Evidence from curriculum:
  - `curriculum/sources/validation-register.md:15-27`
- Evidence from official sources:
  - [Getting Started](https://docs.openclaw.ai/start/getting-started)
  - [Repo README](https://github.com/openclaw/openclaw)
- Example:
  The pack records "Node 24 recommended and Node 22.14+ supported" as official-doc baseline. That still appears in current getting-started docs, but the repo README has also shown newer patch-floor guidance in nearby periods. The curriculum should record exact validation date and source, not freeze the claim as timeless truth.
- Validation status: **Weak**
- Fix recommendation:
  Add date-stamped notes and downgrade any disputed or rapidly moving claims to `validated-inference` until sources clearly align.

### Finding 7

- Severity: **Medium**
- Area: Extensibility / contributor coverage
- What is wrong:
  The extension track mainly teaches native plugin manifests plus skills, but current OpenClaw extension reality also includes bundle formats, hook packs, plugin architecture, ClawHub distribution, install/update behavior, and compatibility gating.
- Why it matters:
  Learners trained on this pack will have an incomplete developer mental model.
- Evidence from curriculum:
  - `curriculum/tracks/plugin-developer.md`
  - `curriculum/capstones/capstone-specs.md:21-25`
  - `curriculum/sources/official-reading-map.md:48-51`
- Evidence from official sources:
  - [Plugin Manifest](https://docs.openclaw.ai/plugins/manifest)
  - [Plugin Bundles](https://docs.openclaw.ai/plugins/bundles)
  - [Plugin Architecture](https://docs.openclaw.ai/plugins/architecture)
  - [Plugin Setup and Config](https://docs.openclaw.ai/plugins/sdk-setup)
  - [ClawHub](https://docs.openclaw.ai/tools/clawhub)
- Validation status: **Incomplete**
- Fix recommendation:
  Expand the developer track to cover native vs bundle plugins, hook packs, distribution, compatibility metadata, and install/update safety.

## 4. False / Weak / Unverified Claims Table

| Claim | Where it appears | Status | Source(s) | Notes |
| --- | --- | --- | --- | --- |
| Stable-release-first material is clearly separated from preview/source-build topics | `README.md`, `program-overview.md`, `semester-2/index.md` | Incorrect | [Threat Model](https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS), [Formal Verification](https://docs.openclaw.ai/security/formal-verification/) | Core sequence includes draft/advanced material without labels. |
| OpenClaw recommends Node 24 and supports Node 22.14+ | `validation-register.md` | Verified but fragile | [Getting Started](https://docs.openclaw.ai/start/getting-started) | Keep date-stamped because runtime floors can move quickly. |
| WSL2 is the recommended Windows path for the full experience | `program-overview.md`, `validation-register.md` | Verified | [Getting Started](https://docs.openclaw.ai/start/getting-started), [Windows](https://docs.openclaw.ai/platforms/windows) | Strong claim. Keep it. |
| The gateway is the long-lived owner of messaging surfaces and control-plane APIs | `validation-register.md` | Verified | [Architecture](https://docs.openclaw.ai/concepts/architecture) | Strong claim. |
| OpenClaw should not be taught as hostile multi-tenant isolation on one shared gateway | multiple files | Verified | [Gateway Security](https://docs.openclaw.ai/gateway/security), [Repo SECURITY.md](https://github.com/openclaw/openclaw/blob/main/SECURITY.md) | One of the best parts of the pack. |
| Memory is persisted in markdown files; there is no hidden memory state | `validation-register.md` | Verified | [Memory Overview](https://docs.openclaw.ai/concepts/memory) | Strong claim. |
| Telegram is one of the fastest beginner channel paths; WhatsApp is production-ready via WhatsApp Web plugin | `validation-register.md`, labs/semester assumptions | Weak | [Getting Started](https://docs.openclaw.ai/start/getting-started) | "Telegram fastest beginner path" is supported. The stronger WhatsApp production-readiness framing needs better sourcing. |
| Plugins extend channels, providers, tools, and skills, and native plugins require `openclaw.plugin.json` | `validation-register.md` | Inferred / incomplete | [Plugin Manifest](https://docs.openclaw.ai/plugins/manifest), [Plugin Architecture](https://docs.openclaw.ai/plugins/architecture) | True for native plugins, but incomplete because bundle plugins are also current reality. |
| `doctor`, `status`, `gateway probe`, and `security audit` form the operational debugging backbone | `validation-register.md` | Inferred | [Doctor](https://docs.openclaw.ai/gateway/doctor), [Status](https://docs.openclaw.ai/cli/status), [Security CLI](https://docs.openclaw.ai/cli/security) | Reasonable synthesis, but still curriculum framing. |
| Formal models are bounded rather than proof of total implementation security | `validation-register.md`, security strand | Verified | [Formal Verification](https://docs.openclaw.ai/security/formal-verification/) | This part is accurate. The issue is presentation and placement, not the claim itself. |

## 5. Missing Topics Table

| Missing topic | Why it matters | Affected audience | Where it should be added |
| --- | --- | --- | --- |
| Automation & tasks | Core runtime pattern for detached work, auditability, cron, heartbeat, task ledger | All advanced learners | Semester 2 core |
| Standing orders | Defines durable authority and escalation boundaries | Operators, governance, enterprise | Semester 2 security/governance |
| Hooks | Major event-driven automation and risk surface | Plugin, contributor, enterprise | Semester 2 core + extension track |
| Task flow | Durable multi-step orchestration is now part of realistic operations | Enterprise, advanced operator | Semester 2 core |
| Sub-agents | Delegated runtime controls affect cost, security, and authority | Operator, security, contributor | Semester 2 core |
| ACP agents | External coding-harness orchestration is now a real integration surface | Contributor, advanced operator | Contributor track + advanced core |
| Device pairing lifecycle | Real auth boundary for Control UI and nodes | Operators, security | Semester 1 + security strand |
| SecretRef / auth profile handling | Essential for safe provider config and remote deployment | Operators, DevOps, enterprise | Prerequisite bridge + Semester 2 config |
| Update / rollback / release channels | OpenClaw moves fast; change management is mandatory | DevOps, enterprise | Production track + core ops |
| Backup / restore / state retention | Production durability and incident recovery | DevOps, enterprise | Production track |
| Plugin supply-chain security | Required due to current registry/install threat model | Plugin, security, enterprise | Security strand + plugin track |
| Plugin bundles | Current extension reality is not manifest-only | Plugin developers | Plugin track |
| Hook packs and hook policy | Current install surface and operational risk | Plugin, security | Plugin track + security strand |
| Filesystem hardening and workspace-only controls | Important for tool risk reduction | Security, enterprise | Semester 2 security |
| Webhook ingress patterns | Real automation/integration surface | DevOps, enterprise | Semester 2 integration module |
| Advisory-driven case studies | Needed for current-state realism | All advanced learners | Security strand |

## 6. Curriculum Architecture Review

### Prerequisite bridge

The bridge is logically sound, but the pack undersells how demanding it is. A learner who starts "near zero" but is expected to absorb shell literacy, WSL2/Linux, Git, Node.js, JSON, TypeScript, Docker, SSH, networking, and AI-agent security is not really near zero. The audience statement should narrow or the bridge should become a real multi-week prep course with deliverables and exit gates.

### Semester structure

Semester 1 is mostly the right shape:

- environment and tooling first
- OpenClaw concepts before advanced exposure
- onboarding and diagnostics early enough
- tools/channels/nodes/remote access after trust-model framing

Semester 2 is the weaker half:

- it lacks automation/tasks despite those being operationally central
- it lacks update/rollback governance despite the rapid release cadence
- it includes formal verification in the mandatory flow without maturity labeling

### Tracks

The role-based track split is good:

- Operator
- Production / DevOps
- Security / Hardening
- Plugin Developer
- Contributor / Core
- Local Models

The gaps are not the existence of tracks but the depth of track-specific material.

### Labs

The labs do not yet qualify as a serious delivery system. They need:

- a numbered procedure
- a prepared environment
- expected outputs
- verification checks
- failure injection
- recovery / rollback
- instructor notes
- estimated time and cost

### Capstones

The capstone directions are better than average and sensibly track role differences. The problem is lack of precision:

- no acceptance checklist
- no required evidence bundle
- no assessor calibration
- no minimum viable artifact standard
- no red-team challenge prompt bank

### Rubrics

The rubric philosophy is correct, especially the automatic downgrade triggers. The scoring bands are still too coarse for serious accreditation or cross-instructor consistency.

### Competency framework

The competency ladder is plausible at a high level. The problem is that Levels 5-7 are not fully backed by the actual teaching assets currently in the pack.

## 7. Security and Production Audit

### Trust model correctness

This is the strongest part of the curriculum. The pack correctly reflects the official trust model:

- OpenClaw is not a hostile multi-tenant security boundary for adversarial users sharing one gateway.
- The default model is a trusted operator / trusted assistant boundary.
- Widening exposure requires deliberate auth, policy, and access decisions.

Primary sources:

- [Gateway Security](https://docs.openclaw.ai/gateway/security)
- [Repo SECURITY.md](https://github.com/openclaw/openclaw/blob/main/SECURITY.md)

### Approvals / sandboxing coverage

The curriculum covers approvals and sandboxing conceptually, but it is incomplete in current-state terms. Missing or underdeveloped areas include:

- delegated-run/sub-agent approvals and inheritance
- workspace-only filesystem constraints
- hook execution risk
- the distinction between operator guardrails and true hostile-user authorization

Primary sources:

- [Exec Tool](https://docs.openclaw.ai/tools/exec)
- [Exec Approvals](https://docs.openclaw.ai/tools/exec-approvals)
- [Plugins CLI](https://docs.openclaw.ai/cli/plugins)

### Remote access guidance

The loopback-first, SSH, Tailscale, and trusted proxy direction is broadly correct. Good. What is missing:

- device identity and secure context requirements
- `allowInsecureAuth` downgrade risks in browser/control flows
- exact same-host proxy caveats

Primary sources:

- [Remote Access](https://docs.openclaw.ai/gateway/remote)
- [Trusted Proxy Auth](https://docs.openclaw.ai/gateway/trusted-proxy-auth)
- [Security](https://docs.openclaw.ai/security)

### Auth and ingress guidance

The curriculum mentions pairing, allowlists, DM scope, and mention gating, which is good. It should also explicitly teach:

- device pairing and expiry
- owner-only command behavior
- auth mode interactions
- Tailscale header auth scope limits

### Enterprise governance gaps

Still missing for enterprise-grade quality:

- update policy
- stable/beta/dev release lane decisions
- rollback and version pinning
- plugin provenance policy
- backup and restore
- retention policy for state, sessions, memory, logs
- formal runbooks and incident procedures

Primary sources:

- [Release Policy](https://docs.openclaw.ai/RELEASING)
- [Updating](https://docs.openclaw.ai/install/updating)
- [ClawHub](https://docs.openclaw.ai/tools/clawhub)
- [Plugins CLI](https://docs.openclaw.ai/cli/plugins)

### Operational realism gaps

The pack treats production as design-review-heavy but not enough as runbook-heavy. Real production teaching needs:

- day-2 operations
- upgrade drills
- break/fix drills
- recovery drills
- postmortem exercises

## 8. Best Parts

These should largely be kept:

1. The explicit rejection of false hostile multi-tenant framing.
2. Security as a first-class strand rather than an elective add-on.
3. The broad Semester 1 progression from environment literacy to safe operation.
4. The role-based track architecture.
5. The insistence on official-source-backed instruction.
6. The rubric downgrade triggers that punish unsafe trust assumptions.

## 9. Top 20 Improvements

1. Add explicit maturity labels to every module: stable, advanced, beta-sensitive, draft, source-build-only.
2. Remove formal verification from the mandatory baseline and relabel it as advanced research-grade content.
3. Add a required Automation & Tasks module.
4. Add a required Hooks + event-driven risk module.
5. Add a required Standing Orders / durable authority module.
6. Add a required Sub-Agents + ACP module.
7. Add an Updates / Release Policy / Rollback module.
8. Add a device-auth and remote browser/node pairing lab.
9. Expand security coverage with current 2026 advisories.
10. Add plugin supply-chain safety and provenance as mandatory material.
11. Expand the plugin track to include bundle formats and hook packs.
12. Convert every lab into a full step-by-step lab guide.
13. Create instructor packs for Lane 2 academic delivery.
14. Add state backup/restore and retention guidance.
15. Add SecretRef, auth profile, and credential-management instruction.
16. Add filesystem hardening and workspace-bound execution instruction.
17. Create track-specific rubrics with evidence requirements.
18. Add assessor calibration notes and oral-defense prompts.
19. Add a source-drift maintenance process for the validation register.
20. Add file-by-file revision notes in the curriculum itself to show freshness and last validation date.

## 10. Final Rewrite Priority Plan

### Phase 1: must-fix blockers

- Enforce the stable-vs-draft labeling rule across all files.
- Add missing core domains: automation/tasks, hooks, standing orders, sub-agents, ACP, updates/rollback.
- Repair weak or disputed entries in `curriculum/sources/validation-register.md`.
- Replace lab stubs with real lab specs.
- Replace the generic rubric with track-specific rubrics.

### Phase 2: major quality improvements

- Expand the security strand with advisory-based case studies.
- Expand plugin/contributor coverage to match the current extension model.
- Add production governance modules for updates, rollback, retention, and recovery.
- Add reusable instructor delivery assets and environment templates.

### Phase 3: polish and excellence upgrades

- Add assessor calibration packs and defense question banks.
- Add example high-quality capstone submissions.
- Add revision history, freshness metadata, and source-check cadence.
- Add alternate delivery variants: university semester, enterprise onboarding, contributor bootcamp.

## Appendix A: File-Specific Rewrite Targets

### `README.md`

Problems:

- Claims stable-first and correctly labeled preview/source-build material, but the downstream curriculum does not fully honor it.
- Does not signal that the current pack is still a draft and not yet institution-ready.

Rewrite actions:

1. Add a visible status banner: `Current status: strong draft, not yet production-quality`.
2. Add a "Known Gaps" section listing automation/tasks, hooks, ACP, update policy, and rubric expansion as pending.
3. Add a line pointing readers to the validation date and latest checked release.

### `curriculum/program-overview.md`

Problems:

- Overclaims "expert level" readiness relative to actual content depth.
- Learning outcomes mention risks in hooks and remote control, but hooks are not actually taught in the program sequence.

Rewrite actions:

1. Replace "expert level" wording with staged competence wording.
2. Add automation/tasks, hooks, standing orders, sub-agents, and update governance to the listed scope.
3. Add a maturity legend section.

### `curriculum/prerequisite-bridge.md`

Problems:

- Too compressed for the difficulty implied by the audience.

Rewrite actions:

1. Add estimated duration per bridge module.
2. Add mandatory exit checks and failure conditions.
3. Add separate minimum bridge for university-first learners vs experienced operators.

### `curriculum/competency-framework.md`

Problems:

- Levels 5-7 outpace actual content support.

Rewrite actions:

1. Tie each level to concrete curriculum assets.
2. Add missing domains for automation, updates, and plugin supply-chain handling.
3. Add assessor evidence requirements by level.

### `curriculum/assessment-map.md`

Problems:

- Not strong enough for certification claims.

Rewrite actions:

1. Add evidence bundles per assessment category.
2. Add anti-shortcut controls.
3. Add required oral-defense challenge types.

### `curriculum/governance-and-security-strand.md`

Problems:

- Good spine, incomplete current-state realism.

Rewrite actions:

1. Add advisories as mandatory case studies.
2. Add plugin install provenance and supply-chain review.
3. Add automation/hook security.
4. Add device-auth and browser secure-context considerations.

### `curriculum/semester-1/index.md`

Problems:

- Reasonable sequence, but channels and node content should include device/auth nuance.

Rewrite actions:

1. Add pairing/auth/device identity specifics.
2. Add secure-context and Control UI auth cautions.
3. Add exact lab references once labs are fully rewritten.

### `curriculum/semester-2/index.md`

Problems:

- Missing automation/tasks, hooks, updates/rollback.
- Formal verification is misplaced as unlabeled core content.

Rewrite actions:

1. Insert weeks for automation/tasks and update/rollback governance.
2. Move formal verification into an advanced labeled unit.
3. Add hooks and plugin-install security to core material.

### `curriculum/labs/*`

Problems:

- Outline-grade only.

Rewrite actions:

1. Create one markdown file per lab.
2. Include: objective, prerequisites, time, environment lane, steps, expected outputs, failure injection, rollback, evidence, grading.

### `curriculum/tracks/plugin-developer.md`

Problems:

- Too narrow.

Rewrite actions:

1. Add bundle formats, hook packs, ClawHub distribution, compatibility gating, and install/update safety.
2. Add required threat modeling for extension packages.

### `curriculum/tracks/production-devops.md`

Problems:

- Missing updates, rollback, backup/restore, retention.

Rewrite actions:

1. Add explicit day-2 operations module.
2. Add release lane decision-making and rollback drills.

### `curriculum/tracks/contributor-core.md`

Problems:

- Underspecified relative to current architecture surface.

Rewrite actions:

1. Add automation/hook/runtime architecture tracing.
2. Add source-of-truth mapping between docs, config schema, and code.

### `curriculum/capstones/capstone-specs.md`

Problems:

- Good prompts, insufficient acceptance criteria.

Rewrite actions:

1. Add mandatory artifact checklist per capstone.
2. Add minimum viable evidence and red-team questions.
3. Add fail conditions.

### `curriculum/rubrics/master-rubric.md`

Problems:

- Too generic.

Rewrite actions:

1. Split into track-specific rubrics.
2. Add explicit scoring anchors per band.
3. Add required evidence mapping.

### `curriculum/sources/official-reading-map.md`

Problems:

- Missing major current docs.

Rewrite actions:

Add:

- [Automation & Tasks](https://docs.openclaw.ai/automation)
- [Standing Orders](https://docs.openclaw.ai/automation/standing-orders)
- [ACP Agents](https://docs.openclaw.ai/tools/acp-agents)
- [Sub-Agents](https://docs.openclaw.ai/tools/subagents)
- [ClawHub](https://docs.openclaw.ai/tools/clawhub)
- [Plugin Bundles](https://docs.openclaw.ai/plugins/bundles)
- [Plugin Architecture](https://docs.openclaw.ai/plugins/architecture)
- [Updating](https://docs.openclaw.ai/install/updating)
- [Release Policy](https://docs.openclaw.ai/RELEASING)

### `curriculum/sources/validation-register.md`

Problems:

- Needs freshness discipline and stronger source annotations.

Rewrite actions:

1. Add `validated_on` date per claim.
2. Add `source URL` per claim, not only doc title.
3. Add claim statuses: `officially verified`, `strongly supported inference`, `weak`, `incorrect`.
4. Add an explicit drift-review procedure.

## Appendix B: Official Sources Used

Core OpenClaw:

- [Getting Started](https://docs.openclaw.ai/start/getting-started)
- [Onboarding (CLI)](https://docs.openclaw.ai/start/wizard)
- [Architecture](https://docs.openclaw.ai/concepts/architecture)
- [Memory Overview](https://docs.openclaw.ai/concepts/memory)
- [Gateway Security](https://docs.openclaw.ai/gateway/security)
- [Security](https://docs.openclaw.ai/security)
- [Remote Access](https://docs.openclaw.ai/gateway/remote)
- [Trusted Proxy Auth](https://docs.openclaw.ai/gateway/trusted-proxy-auth)
- [Automation & Tasks](https://docs.openclaw.ai/automation)
- [Standing Orders](https://docs.openclaw.ai/automation/standing-orders)
- [ACP Agents](https://docs.openclaw.ai/tools/acp-agents)
- [ACP CLI](https://docs.openclaw.ai/cli/acp)
- [Plugin Manifest](https://docs.openclaw.ai/plugins/manifest)
- [Plugin Bundles](https://docs.openclaw.ai/plugins/bundles)
- [Plugin Architecture](https://docs.openclaw.ai/plugins/architecture)
- [Plugin Setup and Config](https://docs.openclaw.ai/plugins/sdk-setup)
- [Plugins CLI](https://docs.openclaw.ai/cli/plugins)
- [ClawHub](https://docs.openclaw.ai/tools/clawhub)
- [Threat Model (MITRE ATLAS)](https://docs.openclaw.ai/security/THREAT-MODEL-ATLAS)
- [Formal Verification](https://docs.openclaw.ai/security/formal-verification/)
- [Release Policy](https://docs.openclaw.ai/RELEASING)

Official repo / release / advisory sources:

- [OpenClaw GitHub repository](https://github.com/openclaw/openclaw)
- [OpenClaw releases](https://github.com/openclaw/openclaw/releases)
- [Repo SECURITY.md](https://github.com/openclaw/openclaw/blob/main/SECURITY.md)
- [Security advisories](https://github.com/openclaw/openclaw/security/advisories)
- [GHSA-m3mh-3mpg-37hw](https://github.com/openclaw/openclaw/security/advisories/GHSA-m3mh-3mpg-37hw)
- [GHSA-cv7m-c9jx-vg7q](https://github.com/advisories/GHSA-cv7m-c9jx-vg7q)

## Bottom Line for the Rewrite Session

If the goal is for another Codex session to improve the pack, the correct stance is:

- do **not** polish wording first
- do **not** add more marketing language
- do **not** widen mastery claims

Instead:

1. fix the source-of-truth layer
2. fill the missing core domains
3. turn outline-grade labs and rubrics into real delivery assets
4. relabel maturity honestly
5. add current operational and security realism

Only after those changes would this pack be a credible candidate for "near production-quality curriculum."
