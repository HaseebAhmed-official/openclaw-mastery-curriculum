# OpenClaw Mastery Curriculum — Independent Panel Validation Review

**Validation date:** April 22, 2026  
**Reviewer model:** Combined 7-persona independent panel (OpenClaw platform expert · AI systems architect · Security engineer · DevOps/production engineer · University curriculum designer · Assessment and certification expert · Adversarial red-team reviewer)  
**Curriculum root:** `E:\Study\Openclaw mastery\`  
**Primary entry file:** `README.md`  
**Total curriculum files reviewed:** 23 files, ~1,200 lines  
**Audience:** University-first; enterprise-reusable  
**Prior review in repository:** `Validations/codex-review/` — this is an independent second opinion with fresh source verification, not a derivative  
**Platform status:** OpenClaw is confirmed real — MIT-licensed, self-hosted AI assistant gateway — GitHub: https://github.com/openclaw/openclaw — Docs: https://docs.openclaw.ai/ — npm: `openclaw` — Latest release at validation date: v2026.4.21

---

## 1. Executive Verdict

This curriculum is a **Strong Draft**, firmly on the path toward near-production-quality but not yet there. Its most distinguishing quality is intellectual honesty: the trust model is correctly framed at every level, the distinction between stable and preview features is a stated commitment rather than an afterthought, and the security strand is genuinely threaded rather than bolted on. The pedagogical sequence is coherent, the lab catalog is realistic for the intended environments, and the cross-file consistency is high. For a first-pass university-grade curriculum pack on a relatively new platform, it would pass academic committee review in most institutions without embarrassment.

However, three classes of problems prevent it from being rated higher. First, feature coverage has meaningful blind spots: the dreaming/DREAMS.md memory promotion system is a significant and documented OpenClaw capability that is completely absent, the six-layer skill precedence model is taught as four layers, and multi-agent workspace configuration files (SOUL.md, USER.md) are never explicitly taught even though LAB-C1 implicitly requires students to use them. Second, production and operational depth is thin in places that matter to enterprise teams: webhook security has no dedicated module, CI/CD integration for the security audit tool (`--json` flag) is never mentioned, session recall security semantics are unaddressed, and cost/rate-limiting considerations are absent. Third, the curriculum is dated in a specific way: it does not account for the release-cadence reality of OpenClaw (multiple releases per week), so model defaults (Opus 4.7 is now the Anthropic default since v2026.4.15), security hardening changes (v2026.4.20), and dreaming-reliability improvements (v2026.4.12) go unacknowledged. These are not disqualifying failures, but they are the difference between a capable teaching pack and a world-class one.

**Readiness tier:** Strong Draft  
**Confidence:** 81% — all major platform claims have been source-checked; confidence reduction comes from five individual feature pages not directly fetched (voice wake, sessions CLI, channels CLI, models CLI, approvals CLI), from uncertainty about the Node.js version EOL timeline (the rendered release page returned ambiguous data), and from the absence of any student-tested iteration data.

---

## 2. Scorecard

| Dimension | Score | Justification |
|---|---|---|
| Technical correctness | 8/10 | Gateway, trust model, sandboxing, approvals, manifest, memory, remote access all verified against official docs. Skill precedence is wrong (4 layers stated, 6 exist). DREAMS.md absent. |
| Freshness / current accuracy | 7/10 | Baseline date set correctly (April 22, 2026). But v2026.4.15 model default change (Opus 4.7), v2026.4.20 security hardening, and the dreaming-reliability story from v2026.4.12 are not reflected. |
| Completeness | 7/10 | Strong on architecture, channels, security controls, and extensibility. Missing: dreaming system, webhook security, session recall, SOUL.md/USER.md, image generation, CI/CD security integration, cost modeling. |
| Pedagogical sequencing | 8.5/10 | Prerequisite bridge → S1 foundations → S2 production is a sound progression. Role-based tracks preserve a shared core. The 16-week cadence is achievable. One sequencing flaw: LAB-C1 (multi-agent isolation) requires workspace config files never explicitly taught. |
| Hands-on quality | 7.5/10 | Lab catalog is realistic and well-organized. Success criteria are present but light on failure-mode guidance. Lane 1 local-models "theory only" creates a two-tier student experience. Capstones are generally implementable. |
| Security realism | 8.5/10 | Trust model is correctly and consistently described. All six security stages (trust, ingress, tool, external content, deployment, formal assurance) are present. Missing: webhook attack surface, session recall token-stripping semantics, ElevenLabs TTS dependency as an operational risk in talk-mode deployments. |
| Production / enterprise readiness | 6.5/10 | Remote access patterns, reverse proxy risks, and trusted proxy auth are well-covered. Missing: webhook governance, CI/CD audit pipeline, cost and rate-limit modeling, session store backup/recovery, log rotation, dreaming configuration for production. |
| Extensibility / contributor readiness | 7/10 | Plugin manifest, JSON Schema, skill install flow are solid. Skill precedence count is wrong. Contributor track doesn't name the actual toolchain (pnpm, scoped AGENTS.md files, `pnpm check:changed`). ClawHub ecosystem maturity signal (50 plugins, beta-heavy) not provided to students. |
| Assessment quality | 7.5/10 | Project-heavy philosophy is correct for an operational platform. Rubric is functional but thin (5 dimensions, 4 levels). Missing downgrade trigger: failing to demonstrate prompt injection awareness. Capstone defense questions are adversarially strong. |
| Internal consistency | 8.5/10 | Excellent cross-file coherence. Lab IDs referenced in semester indices exist in the lab catalog. MEMORY.md, `openclaw security audit`, `openclaw onboard`, and `gateway probe` are all consistent with official docs. Minor: S1 Week 13 references talk mode and voice wake that are not separately verified from the nodes overview page (though dedicated pages exist). |
| Overall world-class readiness | 7.5/10 | Would pass first review at a strong university. Would be rejected at top-tier CS departments or enterprise L&D teams for the production-depth gaps and the three correctness issues. With two targeted improvement phases, it can reach 9/10. |

---

## 3. Critical Findings

---

### Finding 1

**Severity:** High  
**Area:** Extensibility / Plugin Developer Track  
**What is wrong:** The curriculum's skill precedence model is understated. LAB-D2 (`curriculum/labs/lab-catalog.md:97`) teaches "bundled, local, agent, and workspace skill behavior" — four layers. The official Skills documentation defines **six** distinct layers with explicit override order: workspace > project-agent > personal-agent > managed/local > bundled > skills.load.extraDirs.  
**Why it matters:** Graduates of the Plugin Developer track who rely on the four-layer model will have incorrect mental models for debugging skill-collision bugs, especially in multi-agent deployments where the distinction between project-agent and personal-agent skills is operationally significant.  
**Evidence from curriculum:** `curriculum/labs/lab-catalog.md` line 98: "focus: bundled, local, agent, and workspace skill behavior"; `curriculum/tracks/plugin-developer.md` line 17: "skills and precedence"  
**Evidence from source:** Official Skills docs at https://docs.openclaw.ai/skills — "If a skill name conflicts, precedence is: `<workspace>/skills` (highest) → `<workspace>/.agents/skills` → `~/.agents/skills` → `~/.openclaw/skills` → bundled skills → `skills.load.extraDirs` (lowest)" — six distinct layers  
**Fix recommendation:** Update LAB-D2 description and the Plugin Developer track emphasis section to name all six layers accurately. Add a "skill precedence map" exercise that requires students to trace a name collision through all six layers, not four.

---

### Finding 2

**Severity:** High  
**Area:** Completeness — Memory system  
**What is wrong:** The dreaming/DREAMS.md memory promotion system is a documented, actively developed, production-relevant OpenClaw feature that is completely absent from the curriculum. The official Memory docs describe DREAMS.md (dream diary and promotion summaries), a scoring-based promotion from daily notes to long-term memory, and memory flush before conversation compaction. The 2026.4.12 release specifically focused on "memory and dreaming reliability." The Control UI has a dedicated "Dream monitoring" panel. This is not an edge case.  
**Why it matters:** Any learner building a production deployment who configures memory strategy without understanding dreaming will make suboptimal or incorrect choices. S2 Week 12 ("Memory strategy and advanced knowledge layers") is precisely where this belongs, but it is silent on dreaming.  
**Evidence from curriculum:** `curriculum/semester-2/index.md` line 24 mentions "compare default memory, wiki layer, and search/indexing choices" — no dreaming reference anywhere in the pack  
**Evidence from source:** https://docs.openclaw.ai/concepts/memory — confirms DREAMS.md, dreaming system, memory flush. GitHub release v2026.4.12 notes: "memory and dreaming reliability." Control UI page: "Dream monitoring (memory/dreaming status and diary access)" — https://docs.openclaw.ai/web/control-ui  
**Fix recommendation:** Add a dedicated sub-section to S2 Week 12 on the dreaming system: what DREAMS.md is, how promotion works, how to configure scoring thresholds, and operational implications (dreaming as an asynchronous background process).

---

### Finding 3

**Severity:** High  
**Area:** Multi-agent / Completeness  
**What is wrong:** SOUL.md and USER.md are documented workspace configuration files that define agent personality, rules, and user context. They are first-class multi-agent configuration surfaces per the official multi-agent routing docs. The curriculum's S2 Week 2 ("multi-agent routing") and LAB-C1 ("multi-agent isolation design") require students to reason about per-agent workspaces, but these files are never taught, named, or referenced anywhere in the 23-file pack.  
**Why it matters:** A student completing LAB-C1 without knowing about SOUL.md and USER.md cannot correctly configure agent behavior differentiation, which is the core distinguishing purpose of multi-agent routing. AGENTS.md is referenced in the Contributor track via GitHub AGENTS.md, but the gateway-level workspace AGENTS.md (distinct from the repo contributor file) is also unnamed.  
**Evidence from curriculum:** `curriculum/semester-2/index.md` line 12 references "Multi-agent routing"; `curriculum/labs/lab-catalog.md` lines 64-65 reference "workspaces, sessions, auth profiles, isolation" — no SOUL.md or USER.md  
**Evidence from source:** https://docs.openclaw.ai/multi-agent — "Each agent gets its own workspace with `SOUL.md`, `AGENTS.md`, and optional `USER.md`, plus a dedicated `agentDir`"  
**Fix recommendation:** Add explicit teaching of SOUL.md, USER.md, and the workspace-level AGENTS.md to S2 Week 2 and LAB-C1. Add "create and differentiate two agents using distinct SOUL.md and USER.md files" as an explicit lab deliverable for LAB-C1.

---

### Finding 4

**Severity:** Medium  
**Area:** Production readiness — Webhook security  
**What is wrong:** Webhook security is a distinct attack surface that the `openclaw security audit` command explicitly checks (token strength, path restrictions, session key controls). It appears in the official security documentation and is audited in production environments. The curriculum has no dedicated teaching module, no lab, and no mention of webhook configuration or its risks.  
**Why it matters:** Production deployments that use webhook-driven integrations have a distinct security surface that is not covered by the general tool-policy and channel-pairing modules. A security track graduate who has never seen webhook audit findings will miss this class of finding in real engagements.  
**Evidence from curriculum:** LAB-C2 is titled "Security audit and remediation" — `curriculum/labs/lab-catalog.md` lines 67-70 — but webhook security is not mentioned as a focus area  
**Evidence from source:** https://docs.openclaw.ai/cli/security — security audit checks "Webhook configuration: Validates token strength, path restrictions, and session key controls"  
**Fix recommendation:** Add webhook security as an explicit sub-topic in LAB-C2. Add a rubric indicator in the Security capstone requiring identification and remediation of webhook configuration findings.

---

### Finding 5

**Severity:** Medium  
**Area:** Freshness — Release-cadence awareness  
**What is wrong:** The curriculum does not address the release-cadence reality of OpenClaw (multiple releases per week). Between v2026.4.12 and v2026.4.21 (the range covering the curriculum's April 22 baseline), three changes are directly relevant to curriculum claims: (a) the default Anthropic model changed to Claude Opus 4.7 in v2026.4.15, (b) security hardening restricted certain command access patterns in v2026.4.20, (c) dreaming reliability was improved in v2026.4.12. The curriculum's model selection module (S1 Week 10, LAB-B4) says nothing about which models are current defaults or how defaults change across releases.  
**Why it matters:** Students entering a course mid-year will have different default behaviors than early-semester students. Without guidance on checking current defaults and release notes, the "provider and model selection" lab produces inconsistent outcomes across cohorts.  
**Evidence from curriculum:** `curriculum/semester-1/index.md` Week 10: "Configure a model, understand fallback ordering, inspect model status" — no guidance on checking release notes or current defaults  
**Evidence from source:** https://github.com/openclaw/openclaw/releases — v2026.4.15: "Defaulted Anthropic selections to Claude Opus 4.7"; v2026.4.20: security hardening changes  
**Fix recommendation:** Add a "checking release notes and migration behavior" exercise to S1 Week 10. Add a standing instruction in the program overview: "Before delivering any week involving provider selection or security controls, check the most recent release notes for behavioral changes."

---

### Finding 6

**Severity:** Medium  
**Area:** Contributor / Core Developer Track  
**What is wrong:** The Contributor track specifies "validation and docs generation" as emphasis areas but does not name the actual development toolchain: pnpm (not npm) as the package manager, `pnpm check:changed` for scoped typecheck/lint, `pnpm test:changed` for affected tests, and the existence of scoped AGENTS.md files for subsystem-specific contributor guidance. The extra labs ("repo-reading and architecture tracing", "doc-to-code consistency review") are correctly motivated but lack the operational detail a contributor actually needs on day one.  
**Why it matters:** A contributor who arrives at the repo not knowing about `pnpm check:changed` or scoped AGENTS.md files will fail their first pre-commit gate and lack the navigation tools to understand subsystem boundaries.  
**Evidence from curriculum:** `curriculum/tracks/contributor-core.md` lines 13-18: emphasis areas; lines 22-25: extra labs — no pnpm, no `check:changed`, no scoped AGENTS.md  
**Evidence from source:** https://github.com/openclaw/openclaw/blob/main/AGENTS.md — "Use `scripts/committer`; `pnpm check:changed` for scoped typecheck/lint; `pnpm test:changed` for affected tests; Scoped AGENTS.md files exist for specific subsystems"  
**Fix recommendation:** Add a "contributor toolchain orientation" section to the Contributor track document and a dedicated sub-exercise in its extra labs: "run `pnpm check:changed` on a targeted change and interpret the output."

---

### Finding 7

**Severity:** Medium  
**Area:** Assessment — Rubric completeness  
**What is wrong:** The master rubric's automatic downgrade triggers (`curriculum/rubrics/master-rubric.md` lines 41-45) include five conditions but omit two critical ones: (a) failure to demonstrate awareness of prompt injection as an attack vector in any tool-enabled deployment, and (b) failure to account for the dreaming system in a memory strategy design. Given that prompt injection is Stage 4 of the curriculum's own governance strand and is explicitly listed in the validation register as `official-ecosystem` priority, the absence of a rubric enforcement mechanism is inconsistent.  
**Why it matters:** Without an automatic downgrade trigger for prompt injection omission, students can produce A-grade capstones that ignore the most prominent documented attack class for LLM-connected systems. The rubric weakens the security strand's own enforcement.  
**Evidence from curriculum:** `curriculum/rubrics/master-rubric.md` lines 41-45; `curriculum/governance-and-security-strand.md` line 32 (Stage 4: prompt injection as a required topic)  
**Evidence from source:** OWASP Prompt Injection at https://owasp.org/www-community/attacks/PromptInjection — industry-standard attack taxonomy. OpenClaw security docs explicitly address this class.  
**Fix recommendation:** Add two downgrade triggers to master-rubric.md: (1) "produces a tool-enabled deployment design without addressing prompt injection or unsafe external content"; (2) "designs a production memory strategy without considering dreaming configuration and promotion thresholds."

---

### Finding 8

**Severity:** Low  
**Area:** Technical correctness — Talk mode TTS dependency  
**What is wrong:** The curriculum's S1 Week 13 correctly identifies talk mode and voice wake as real node features. However, it omits the operational dependency on ElevenLabs as the primary TTS provider. This is a production-relevant detail: ElevenLabs is an external third-party service with its own availability, latency, and cost profile. Android has a local TTS fallback, but macOS does not have an equivalent documented fallback.  
**Why it matters:** A production deployment relying on talk mode without understanding the ElevenLabs dependency will experience silent failures or degraded UX when the TTS provider is unavailable. This is exactly the kind of third-party dependency risk the curriculum emphasizes in the security strand but fails to apply to its own feature coverage.  
**Evidence from curriculum:** `curriculum/semester-1/index.md` Week 13: "Explain node role, pairing, command surface, talk mode, and voice wake" — no dependency context  
**Evidence from source:** https://docs.openclaw.ai/nodes/talk — "uses ElevenLabs as the primary TTS provider"; Android has "local system TTS fallback"  
**Fix recommendation:** Add a "provider dependencies for talk mode" note to the S1 Week 13 module description: ElevenLabs as primary TTS, Android fallback exists, macOS fallback is not documented.

---

## 4. False / Weak / Unverified Claims Table

| Claim | Where it appears | Status | Source(s) | Notes |
|---|---|---|---|---|
| "OpenClaw recommends Node 24 and supports Node 22.14+" | `curriculum/sources/validation-register.md` line 15 | **Officially verified** | https://docs.openclaw.ai/start/getting-started — exact language confirmed | ✅ |
| "The gateway is the long-lived owner of messaging surfaces and control-plane APIs" | `curriculum/sources/validation-register.md` line 17 | **Officially verified** | https://docs.openclaw.ai/concepts/architecture — "A single long‑lived Gateway owns all messaging surfaces" | ✅ |
| "Personal-assistant trust model: one trusted operator boundary per gateway" | `curriculum/sources/validation-register.md` line 18; `curriculum/governance-and-security-strand.md` line 12 | **Officially verified** | https://docs.openclaw.ai/security — exact language confirmed | ✅ |
| "OpenClaw should not be taught as hostile multi-tenant isolation on one shared gateway" | `curriculum/sources/validation-register.md` line 19 | **Officially verified** | https://docs.openclaw.ai/security — "OpenClaw is not a hostile multi-tenant security boundary" | ✅ |
| "Memory is persisted in markdown files in the agent workspace; no hidden memory state" | `curriculum/sources/validation-register.md` line 20 | **Officially verified** | https://docs.openclaw.ai/concepts/memory — "The model only 'remembers' what gets saved to disk -- there is no hidden state." | ✅ |
| "Docker-based sandboxing reduces blast radius but is not a perfect security boundary" | `curriculum/sources/validation-register.md` line 21 | **Officially verified** | https://docs.openclaw.ai/sandboxing — "This is not a perfect security boundary, but it materially limits filesystem and process access" | ✅ |
| "Loopback plus SSH or Tailscale Serve is the safer default remote-access pattern" | `curriculum/sources/validation-register.md` line 22 | **Officially verified** | https://docs.openclaw.ai/gateway/remote — "Loopback + SSH/Tailscale Serve is the safest default (no public exposure)" | ✅ |
| "Telegram is one of the fastest beginner channel paths" | `curriculum/sources/validation-register.md` line 23 | **Officially verified** | AI/ML API quickstart docs independently corroborate: "Telegram recommended as easiest entry point"; OpenClaw getting-started docs confirm | ✅ |
| "Skills load from layered locations with precedence rules and workspace-level override power" | `curriculum/sources/validation-register.md` line 24 | **Officially verified but understated** | https://docs.openclaw.ai/skills — 6 layers exist, not 4 as implied by LAB-D2. The general claim is correct; the detail is wrong. | ⚠️ Lab description understates precision |
| "Native plugins require `openclaw.plugin.json`" | `curriculum/sources/validation-register.md` line 25 | **Officially verified** | https://docs.openclaw.ai/plugins/manifest — "Every native OpenClaw plugin must ship a `openclaw.plugin.json` file" | ✅ |
| "Host exec must be governed by tool policy plus approvals/allowlists when enabled" | `curriculum/sources/validation-register.md` line 26 | **Officially verified** | https://docs.openclaw.ai/tools/exec-approvals — three modes (deny/allowlist/full), per-command approvals, canonical binding confirmed | ✅ |
| "`doctor`, `status`, `gateway probe`, and `security audit` form the operational debugging backbone" | `curriculum/sources/validation-register.md` line 27 | **Officially verified** | Troubleshooting docs confirm a 7-command ladder. All four named tools exist. The curriculum simplifies correctly; the ladder also includes `gateway status` and `channels status --probe`. | ✅ (simplification, not error) |
| "Formal security models are bounded models, not proof of total implementation security" | `curriculum/sources/validation-register.md` line 28 | **Officially verified** | https://docs.openclaw.ai/security/formal-verification/ — TLA+/TLC, "not...a proof that 'OpenClaw is secure in all respects'" | ✅ |
| LAB-D2 "bundled, local, agent, and workspace skill behavior" | `curriculum/labs/lab-catalog.md` line 98 | **Incorrect / understated** | https://docs.openclaw.ai/skills — 6 layers, not 4. project-agent and personal-agent are distinct layers not named | ❌ Needs correction |
| Dreaming/DREAMS.md as part of memory system | Not present anywhere in the curriculum | **Absent — unverified by omission** | https://docs.openclaw.ai/concepts/memory confirms DREAMS.md is real and significant. Control UI has dedicated dream monitoring panel. | ❌ Missing feature |
| SOUL.md and USER.md as workspace configuration files | Not present in curriculum | **Absent — unverified by omission** | https://docs.openclaw.ai/multi-agent — "Each agent gets its own workspace with `SOUL.md`, `AGENTS.md`, and optional `USER.md`" | ❌ Missing configuration surface |
| ElevenLabs as primary TTS provider for talk mode | Not mentioned in curriculum | **Weakly supported / uncertain** | https://docs.openclaw.ai/nodes/talk confirms ElevenLabs dependency; Android has local fallback | ⚠️ Operational dependency gap |
| "Windows learners should prefer WSL2 for the full experience" | `curriculum/program-overview.md` line 81 | **Officially verified** | https://docs.openclaw.ai/start/getting-started — "WSL2...more stable and recommended for the full experience" | ✅ |
| `openclaw onboard` as the onboarding command | `curriculum/semester-1/index.md` Week 7 | **Strongly supported inference** | Getting-started docs describe the onboarding flow; command mentioned in the curriculum is consistent with naming conventions but the page WebFetch returned the install.sh/ps1 installer rather than the exact CLI syntax | ~verified; not explicitly contradicted |
| Webhook security as a security audit check | Not mentioned in curriculum | **Officially verified (for source) — missing from curriculum** | https://docs.openclaw.ai/cli/security — audit explicitly checks webhook token strength, path restrictions, session key controls | Gap, not error |
| Control UI served at loopback port | `curriculum/labs/lab-catalog.md` line 33 (implicit) | **Officially verified** | https://docs.openclaw.ai/web/control-ui — served at `http://127.0.0.1:18789/` | ✅ |

---

## 5. Missing Topics Table

| Missing topic | Why it matters | Audience affected | Where to add |
|---|---|---|---|
| **DREAMS.md and the dreaming/memory-promotion system** | A documented, production-relevant memory feature; v2026.4.12 release improved it; Control UI has a dedicated panel for it | All tracks, especially Operator and Production DevOps | `curriculum/semester-2/index.md` Week 12; new sub-section in memory strategy module |
| **SOUL.md and USER.md workspace configuration files** | Required to configure distinct agent behavior in multi-agent setups; LAB-C1 implicitly requires them | All tracks that touch multi-agent; especially Operator and Production DevOps | `curriculum/semester-2/index.md` Week 2; LAB-C1 spec |
| **Webhook security and audit** | Security audit explicitly checks webhook token strength and path restrictions; a real attack surface in production | Security/Hardening track; Production DevOps track | LAB-C2 sub-focus; Security capstone rubric |
| **CI/CD integration for security audit** | `openclaw security audit --json` enables policy-as-code and automated hardening gates in pipelines | Production DevOps track; Security track | LAB-C2 extension exercise; Production track extra labs |
| **Session recall and token-stripping semantics** | Security-relevant: strips thinking tags, tool-call scaffolding, and control tokens from recalled transcripts; prevents raw context injection | Security/Hardening track; Contributor track | `curriculum/semester-2/index.md` Week 2 (multi-agent) or Week 7 (shared inboxes) |
| **Skill precedence layers 2 and 3** (project-agent and personal-agent) | Real layers distinct from each other; needed for correct multi-agent skill isolation reasoning | Plugin Developer track | LAB-D2; Plugin Developer track emphasis section |
| **Image generation and multimodal skills** | A significant class of production capability; `aimlapi-media-gen` skill confirmed; real use case driver | Operator track; Plugin Developer track | New optional sub-module in tracks or a specialization note |
| **ElevenLabs TTS dependency for talk mode** | Third-party production dependency with availability and cost implications | Production DevOps track; Operator track | `curriculum/semester-1/index.md` Week 13; environment-lanes.md note |
| **Release-cadence awareness and how to check migration notes** | OpenClaw releases multiple times per week; defaults and security controls change; students need to know how to track this | All tracks | Program overview; S1 Week 10 (provider selection) |
| **API cost modeling and rate-limit management** | Hosted provider API costs are real operational expenses; no guidance exists on how to model or contain spend | Operator track; Production DevOps track; Local Models specialization | S1 Week 10 (provider lab); S2 Week 1 (production framing) |
| **Log rotation and retention policy** | Production deployments accumulate logs; no guidance on management | Production DevOps track | Production/DevOps track extra labs; S2 Week 6 (remote access/proxy) |
| **Session store backup and recovery** | Session stores persist under `~/.openclaw/agents/<agentId>/sessions`; recovery after data loss is not addressed | Production DevOps track | Production capstone spec; S2 Week 6 |
| **Feishu/Lark channel** | Explicitly improved in 2026.4.12 release; a significant enterprise channel for Asian market deployments | Enterprise audience | Channels module (S1 Week 12); channel list in program overview |
| **ClawHub ecosystem maturity** | 50 plugins currently, many in beta; curriculum implies a more mature ecosystem; students need accurate signal | Plugin Developer track | Plugin Developer track intro; LAB-D1 context |
| **Contributor toolchain specifics (pnpm, scoped AGENTS.md)** | Real contributor gates; not naming them leaves contributor-track students under-prepared for day-one repo work | Contributor track | Contributor track emphasis section; extra labs |
| **`openclaw gateway status` and `openclaw channels status --probe`** | Both appear in official 7-step diagnostic ladder but are absent from the curriculum's diagnostic teaching | Operator track; Production DevOps track | LAB-B2 (diagnostics ladder); S1 Week 8 |
| **Dreaming configuration and scoring thresholds** | Configurable production behavior affecting memory quality; no guidance exists | Production DevOps track; Operator track | S2 Week 12 extension |
| **`openclaw logs --follow`** | Step 7 of the official diagnostic ladder; useful for real-time triage but not named in any lab | Operator track; Production DevOps track | LAB-B2; troubleshooting module |

---

## 6. Curriculum Architecture Review

### Prerequisite Bridge

**Assessment: Strong, with one gap.**

The eight-module bridge is well-scoped and covers the right foundational topics for a platform that runs on Node.js, WSL2, Docker, SSH, and Tailscale. The exit criteria are concrete and testable. The recommended deliverables (environment checklist, SSH tunnel demo, Docker sandbox demo, security reflection) are appropriate for gating entry to Semester 1.

The one gap is LLM-agent fundamentals (Bridge 8): the curriculum says "understand model providers, auth, and tool invocation" and "reason about prompt injection" but does not include a deliverable tied to this bridge module. Every other bridge module has a deliverable. This is an oversight — a prompt-injection scenario analysis belongs here as an exit artifact, not just a "reflection memo" relegated to S1 Week 5.

### Semester Structure

**Assessment: Sound architecture, one sequencing issue.**

The 16-week structure is achievable. Weeks 1–6 build prerequisite and conceptual depth; Weeks 7–15 are operational; Week 16 is a practical exam. This mirrors successful software engineering pedagogy and avoids the common curriculum failure of jumping to platform specifics before learners have systems context.

The sequencing issue: S1 Week 13 introduces nodes, talk mode, and voice wake — but these are not hands-on labs (the entry in the weekly table says "node architecture walkthrough" and the assessment is a "concept check"). Given that talk mode requires hardware (microphone, speaker), TTS provider API key (ElevenLabs), and platform-specific support (macOS/Android/iOS), theory-only treatment is appropriate — but the curriculum should explicitly acknowledge WHY it stays theoretical, so students do not mistake absence for a gap.

Semester 2's sequence from production framing → multi-agent → config architecture → security audit → approvals → remote access is pedagogically correct: each week builds on the prior. The capstone sprint in Week 15 is appropriately placed after all major content is delivered.

### Tracks

**Assessment: Well-differentiated, capstones well-calibrated.**

The six tracks (Operator, Production/DevOps, Security/Hardening, Plugin Developer, Contributor/Core, Local Models) cover the relevant role landscape without redundancy. Local Models is correctly labeled as a specialization, not a baseline — this framing is honest and important.

All six track files follow the same structure (Goal / Best fit / Additional emphasis / Extra labs / Capstone) which produces consistency at the cost of minimal depth. Each track file is 29–33 lines — sufficient for a track index entry, but likely insufficient as standalone teaching guidance without supplementary materials (module notes, lab instructions). The curriculum promises these as "companion documents" but they do not yet exist as separate files.

The track-capstone alignment is strong. The Security capstone's "residual risk statement" defense question ("what risks remain even after your controls?") is exactly the right adversarial framing for security practitioners. The Contributor capstone's "what did you intentionally avoid changing, and why?" is genuinely sophisticated and would differentiate expert from advanced-beginner performance.

### Labs

**Assessment: Realistic and well-organized; success criteria need depth.**

The three-phase lab structure (A: bridge, B: OpenClaw core, C: production/governance, D: specialization) mirrors the curriculum's knowledge progression and is the correct organizational choice. The minimum lab sets for different institution types are practical and reasonable.

Specific issues:
- LAB-B3's reference to "`MEMORY.md`, daily notes" is verified and correct, but DREAMS.md is not mentioned
- LAB-B2 lists "`status`, `doctor`, `gateway probe`" but omits `gateway status` and `channels status --probe` from the diagnostic ladder, creating incomplete hands-on coverage
- LAB-C1 (multi-agent isolation design) requires workspace configuration (SOUL.md, USER.md, AGENTS.md) as preconditions but these are never taught before this lab
- All labs have output descriptions but no failure modes or rollback guidance — an omission that matters in enterprise/production contexts where bad configurations survive beyond the lab session

### Capstones

**Assessment: Well-specified, defense questions are strong.**

The six capstone specs in `curriculum/capstones/capstone-specs.md` are appropriately differentiated by track. Required elements for each capstone are specific enough to grade but not so prescriptive as to produce cookie-cutter deliverables.

Notable strengths:
- Security capstone requires "risky assumptions" and "residual risk statement" — sophisticated and defensible
- Production capstone requires "rollback plan and change-management note" — operationally mature
- Plugin capstone requires "validation plan" and "deployment notes" — goes beyond basic build exercises

Missing from all capstones: no explicit requirement to address the dreaming/memory system for Operator or Production capstones, and no requirement to address `pnpm check:changed` or scoped AGENTS.md files for the Contributor capstone.

### Rubrics

**Assessment: Functional but thin; two downgrade triggers missing.**

The master rubric's five dimensions (technical correctness, operational maturity, security/trust reasoning, documentation/explanation, capstone defense) cover the essential territory. The four-level scale (4/3/2/1) is appropriately granular for capstone assessment without creating false precision.

The five existing downgrade triggers are well-chosen and directly connected to the curriculum's own stated non-negotiables. However, as documented in Finding 7 above, two triggers are missing: prompt injection awareness and dreaming/memory consideration in production designs.

The rubric lacks a dimension explicitly scoring multi-agent reasoning. For S2-heavy programs where LAB-C1, LAB-C4, and the multi-agent routing week are significant components, this is an assessment gap.

### Competency Framework

**Assessment: Excellent structure; role mapping is useful.**

The seven-domain, eight-level competency framework is one of the curriculum's strongest components. The evidence-of-mastery requirements (artifacts, not quizzes) are the correct philosophy for an operational platform. The certification-style outcomes (Foundation through Specialist) give institutions a concrete mapping to grade or credential structures.

The role mapping table is honest about mastery ceiling by role — Operator targets Levels 1–4 while Specialist targets Levels 4–7. This prevents credential inflation.

One concern: Level 6 (Core Contributor) evidence requires "contributor-level code or design artifact" — but the contributor track's extra labs and capstone description do not specify what repository standards this artifact must meet. Without alignment to the actual repo contribution gates (pnpm, `check:changed`, conventional commits), the evidence requirement is aspirationally stated but not operationally grounded.

---

## 7. Security and Production Audit

### Trust Model Correctness

**Verdict: Correct and consistently applied throughout the pack. [Officially verified]**

The personal-assistant trust model is taught accurately. The curriculum never claims OpenClaw provides hostile multi-tenant isolation. The master rubric auto-downgrades projects that make this claim. The governance strand's Stage 1 explicitly teaches the one-operator-boundary model. The official docs use the exact phrase "Personal assistant trust model: this guidance assumes one trusted operator boundary per gateway (single-user/personal assistant model)" — identical framing.

Source: https://docs.openclaw.ai/security

---

### Approvals and Sandboxing Coverage

**Verdict: Good coverage, missing three-mode taxonomy precision. [Officially verified for general claims; weakly supported for specifics]**

LAB-B5 ("Sandbox and exec policy") and S1 Week 11 cover sandboxing and approvals. The curriculum correctly states Docker-based sandboxing "is not a perfect security boundary" and that exec approvals govern host execution. 

However, the curriculum does not explicitly teach the three exec approval modes (deny / allowlist / full) or the `ask` parameter variants (off / on-miss / always). This level of precision matters for security practitioners who need to design policy, not just enable it.

The official approval docs confirm: "commands are allowed only when policy + allowlist + (optional) user approval all agree." The per-command (not per-session) approval scope is also not explicitly stated in the curriculum.

Source: https://docs.openclaw.ai/tools/exec-approvals

---

### Remote Access Guidance

**Verdict: Correctly represented, well-structured. [Officially verified]**

The curriculum's loopback-first → SSH tunnel → Tailscale Serve progression mirrors the official Remote Access docs' hierarchy. LAB-B7 ("Remote access baseline") and S2 Week 6 ("Remote access and proxy patterns") cover SSH, Tailscale Serve, and trusted proxy auth.

The official docs state explicitly: "keep the Gateway loopback-only unless you're sure you need a bind" and "Loopback + SSH/Tailscale Serve is the safest default (no public exposure)." The curriculum's teaching matches this.

Trusted proxy auth is correctly flagged as security-sensitive with header-spoofing risk — consistent with the official warning ("⚠️ Security-sensitive feature").

Source: https://docs.openclaw.ai/gateway/remote; https://docs.openclaw.ai/gateway/trusted-proxy-auth

---

### Auth and Ingress Guidance

**Verdict: Present but incomplete at enterprise depth. [Strongly supported inference]**

The curriculum teaches "pairing and allowlists," "DM scope and shared inbox isolation," and "mention gating" in the governance strand. These are correct. However, the three gateway authentication modes (token, password, trusted-proxy) are not explicitly taught as a taxonomy — they are mentioned contextually.

For enterprise deployments where auth mode choice is a policy decision, not a default, this is an operational gap. The `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` breakglass flag is not mentioned at all — an important safety communication for enterprise teams who may inadvertently use it.

---

### Enterprise Governance Gaps

**Key missing elements for enterprise-grade coverage:**

1. **Webhook security** — confirmed by security audit tool to be a real attack surface; no curriculum module
2. **CI/CD pipeline integration for security audit** — `--json` output enables automated policy gates; not mentioned
3. **Secrets management practices** — the curriculum says "handle secrets safely" at a high level but provides no guidance on secret management tooling (`.env` patterns, vault integration, environment variable handling)
4. **Provider credential rotation** — no guidance on rotating API keys after provider breach or policy rotation
5. **Multi-agent access profile governance** — per-agent auth profiles are documented (`~/.openclaw/agents/<agentId>/agent/auth-profiles.json`) but not taught for enterprise access-control purposes
6. **Audit trail and log management** — no guidance on log retention, rotation, or forwarding to SIEM tooling

---

### Operational Realism Gaps

1. **Dreaming system configuration** — an asynchronous background process that can affect memory quality; production environments need to configure scoring thresholds; not taught
2. **Session store backup and recovery** — sessions stored on disk; no backup strategy discussed
3. **Provider downtime and fallback** — curriculum references "fallback ordering" but does not provide an exercise where students experience fallback behavior
4. **Cost modeling** — API costs are real; students who complete S1 Week 10 without understanding token costs and rate limits will be surprised in production
5. **Performance and latency modeling** — the Local Models specialization addresses latency in theory, but no track addresses provider response-time monitoring or alerting
6. **Image generation / media skills** — a distinct operational surface with its own provider dependencies and cost profile; unaddressed except in the Local Models capstone tangentially

---

## 8. Best Parts

### 1. Trust model consistency across all files

The personal-assistant trust model is correctly described in the validation register, the governance strand, the master rubric downgrade triggers, the security track, and the program overview. Every file that touches the trust model says the same true thing. This level of conceptual consistency across 23 files is genuinely rare in curriculum design and reflects serious authorial discipline.

Files: `curriculum/sources/validation-register.md` line 18–19; `curriculum/governance-and-security-strand.md` lines 9–13; `curriculum/rubrics/master-rubric.md` line 42; `curriculum/program-overview.md` line 112

---

### 2. Governance strand as a mandatory spine, not an elective

`curriculum/governance-and-security-strand.md` explicitly threads security across six stages from trust-model literacy through formal assurance. The "Required instructor checks" section (lines 55–60) is particularly strong — requiring instructors to fail projects that treat a shared gateway as an adversarial-user boundary is the kind of enforcement lever that distinguishes a rigorous program from a checkbox one.

---

### 3. Validation register with source categories

`curriculum/sources/validation-register.md` distinguishes `official-docs`, `official-repo`, `official-ecosystem`, `validated-inference`, and `community-derived` categories, and maps 15 curriculum claims to source categories. This is not common practice in curriculum design and makes the pack auditable in ways that most curricula are not. It allowed this review to identify which claims were strongly backed and which were not, efficiently.

---

### 4. Capstone defense questions

The six capstone defense questions (`curriculum/capstones/capstone-specs.md`) are adversarially calibrated: "why is this safe enough for its audience?", "what risks remain even after your controls?", "how does your design avoid becoming an operational footgun?", "what did you intentionally avoid changing, and why?". These are not soft questions. They would separate genuine mastery from surface-level competence in any oral examination setting.

---

### 5. Competency framework with evidence requirements

`curriculum/competency-framework.md` requires evidence of mastery through artifacts, not quizzes, for all levels above 1. The eight-level taxonomy from Bridge-ready (0) through Specialist (7) is gradated in realistic increments and maps cleanly to real operator, DevOps, security, and contributor roles. The certification-style outcomes give institutional adopters a credential framing without overclaiming.

---

### 6. Prerequisite bridge design

The eight-module bridge covers exactly the right technical foundations without scope creep. The exit criteria are testable. The deliverables list is reasonable for an institution to implement as a gate. Most curriculum packs assume prerequisites are "handled elsewhere" — this one handles them explicitly and correctly.

---

### 7. Environment lanes with realistic budget differentiation

`curriculum/labs/environment-lanes.md` acknowledges institutional budget diversity explicitly. The three-lane system (low-cost student, standard university lab, enterprise) is realistic, non-patronizing about the cost reality, and correctly labels Lane 2 as canonical. The hardware minimums section is concrete and achievable.

---

### 8. Internal cross-file consistency

Lab IDs referenced in semester indices (LAB-B5, LAB-C2) exist in the lab catalog with matching descriptions. MEMORY.md is mentioned correctly in LAB-B3 and confirmed by official docs. `openclaw security audit` appears in S2 Week 4 and LAB-C2 and is confirmed as a real command. This level of internal consistency prevents the cross-reference confusion that undermines many multi-document curriculum packs.

---

## 9. Top 20 Improvements

1. **Add DREAMS.md and the dreaming system to S2 Week 12.** Describe what DREAMS.md is, how memory promotion scoring works, how to configure dreaming thresholds, and what production implications exist. This is a documented, release-noted, Control-UI-visible feature that belongs in a mastery curriculum. (`curriculum/semester-2/index.md` Week 12; new sub-section)

2. **Correct skill precedence to 6 layers in LAB-D2 and the Plugin Developer track.** Replace "bundled, local, agent, and workspace" with the correct six-layer hierarchy: workspace > project-agent > personal-agent > managed/local > bundled > extraDirs. Add an exercise that requires tracing a name collision through all six layers. (`curriculum/labs/lab-catalog.md` line 97; `curriculum/tracks/plugin-developer.md` lines 16-17)

3. **Add SOUL.md and USER.md to S2 Week 2 and LAB-C1.** These are first-class multi-agent configuration surfaces. LAB-C1 cannot be correctly completed without them. Add a deliverable: "create two agents with distinct SOUL.md files and demonstrate routing separation." (`curriculum/semester-2/index.md` Week 2; `curriculum/labs/lab-catalog.md` LAB-C1)

4. **Add two downgrade triggers to master-rubric.md.** (1) "Produces a tool-enabled deployment design without addressing prompt injection or unsafe external content." (2) "Designs a production memory strategy without considering dreaming configuration and promotion thresholds." (`curriculum/rubrics/master-rubric.md` after line 45)

5. **Add a webhook security sub-focus to LAB-C2.** Specify that audit findings should include webhook token strength, path restrictions, and session key controls. Add a capstone rubric indicator for this in the Security track. (`curriculum/labs/lab-catalog.md` LAB-C2; `curriculum/tracks/security-hardening.md`)

6. **Add CI/CD integration for security audit to Production/DevOps track and LAB-C2.** Document `openclaw security audit --json` as a machine-readable output for policy-as-code pipelines. Add an extension exercise: "pipe the audit output to a CI gate that fails on critical findings." (`curriculum/tracks/production-devops.md`; `curriculum/labs/lab-catalog.md` LAB-C2)

7. **Add release-cadence awareness to S1 Week 10 and program overview.** Add an exercise: "check the most recent release notes and identify any behavioral changes to provider defaults or security controls." Add a standing instructor note in the program overview: "Before each delivery, check recent releases for changes that affect Week 10 and the security audit module." (`curriculum/semester-1/index.md` Week 10; `curriculum/program-overview.md`)

8. **Add contributor toolchain specifics to the Contributor/Core track.** Name pnpm as the package manager. Name `pnpm check:changed` and `pnpm test:changed` as the pre-commit gates. Name scoped AGENTS.md files as the mechanism for subsystem guidance. Add a lab exercise: "run `pnpm check:changed` on a targeted change, interpret the output, and resolve any failures." (`curriculum/tracks/contributor-core.md` lines 13-25)

9. **Complete the diagnostic ladder in LAB-B2.** Add `openclaw gateway status` and `openclaw channels status --probe` to the diagnostics ladder taught in LAB-B2. These appear in the official 7-step troubleshooting sequence. Also add `openclaw logs --follow` as step 7. (`curriculum/labs/lab-catalog.md` LAB-B2)

10. **Add API cost modeling to S1 Week 10 and the Local Models specialization.** Teach students to estimate token costs per provider, understand rate-limit behavior, and create a monthly spend estimate as part of the provider selection lab. This is a production-relevant skill absent from all tracks. (`curriculum/semester-1/index.md` Week 10; `curriculum/tracks/local-models.md`)

11. **Add ElevenLabs TTS dependency note to S1 Week 13.** State explicitly: talk mode requires ElevenLabs as the primary TTS provider. Android has a local fallback; macOS does not. This is a third-party dependency with availability, latency, and cost implications. (`curriculum/semester-1/index.md` Week 13)

12. **Add session recall security semantics to S2 Week 2 or Week 7.** Session recall strips thinking tags, tool-call scaffolding, and control tokens before surfacing historical context. This is a security-relevant behavior that security-track students should understand and that multi-agent designers need to know when reasoning about cross-session memory access. (`curriculum/semester-2/index.md` Week 2 or 7)

13. **Add exec approval three-mode taxonomy to S1 Week 11 and LAB-B5.** Explicitly teach deny / allowlist / full modes and the `ask` parameter variants (off / on-miss / always). Add a lab deliverable: "configure each of the three modes and document the behavioral difference." (`curriculum/semester-1/index.md` Week 11; `curriculum/labs/lab-catalog.md` LAB-B5)

14. **Add ClawHub ecosystem status note to the Plugin Developer track.** State that as of the curriculum baseline, ClawHub lists approximately 50 plugins in varying stages of maturity. This calibrates student expectations and contextualizes the opportunity space for new plugin development. (`curriculum/tracks/plugin-developer.md`)

15. **Add a multi-agent reasoning dimension to the master rubric.** The current five dimensions do not explicitly assess multi-agent isolation reasoning. Add: "Multi-agent reasoning: quality of workspace, session, and auth-profile isolation reasoning for agent-split scenarios." Score 4/3/2/1 on the same scale. (`curriculum/rubrics/master-rubric.md`)

16. **Add Bridge 8 deliverable (prompt injection scenario analysis).** Every other bridge module has a deliverable except Bridge 8 (LLM and agent fundamentals). Add: "produce a one-page prompt injection scenario analysis for a hypothetical OpenClaw deployment with web content ingestion." (`curriculum/prerequisite-bridge.md`)

17. **Add session store backup and recovery to the Production/DevOps capstone spec.** Session stores live on disk. A rollback plan should include session store state. Add "session store backup procedure" as a required element of the Production capstone. (`curriculum/capstones/capstone-specs.md`)

18. **Add Feishu/Lark channel to the channel coverage of S1 Week 12.** This channel was specifically improved in v2026.4.12. For enterprise deployments in Asian markets or organizations using Lark/Feishu, it is a primary channel. It should be acknowledged even if not a default lab target. (`curriculum/semester-1/index.md` Week 12)

19. **Add `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` breakglass flag to the security strand.** This flag bypasses the default loopback-only WebSocket restriction. It should be taught as a dangerous tool: named, documented, and explicitly flagged as requiring justification before use. (`curriculum/governance-and-security-strand.md` Stage 5)

20. **Add dreaming configuration to the memory strategy capstone and the master rubric.** For any Operator or Production capstone that includes a memory strategy, require learners to address: whether dreaming is enabled, what scoring thresholds are configured, and what the operational implications are for long-running deployments. (`curriculum/capstones/capstone-specs.md` Operator and Production specs; `curriculum/rubrics/master-rubric.md`)

---

## 10. Final Rewrite Priority Plan

### Phase 1: Must-Fix Blockers (ship-blocking for a rigorous institution)

These issues cause incorrect competency at graduation or directly contradict official documentation. They must be fixed before any formal delivery.

1. **Fix skill precedence to 6 layers** in LAB-D2 and the Plugin Developer track. (Finding 1)
2. **Add SOUL.md and USER.md to S2 Week 2 and LAB-C1 prerequisite materials.** Without these, LAB-C1 cannot be correctly completed. (Finding 3)
3. **Add dreaming/DREAMS.md to S2 Week 12.** A documented, release-noted production feature cannot be absent from a mastery curriculum. (Finding 2)
4. **Add two downgrade triggers to master-rubric.md** for prompt injection and dreaming strategy omission. These are enforcement-mechanism gaps that undermine the curriculum's own security requirements. (Finding 7)
5. **Add Bridge 8 deliverable.** The only bridge module without a concrete deliverable is the most security-relevant one. This creates an unverified exit gate for the most important prerequisite.

### Phase 2: Major Quality Improvements (required for near-production-quality rating)

These issues create meaningful gaps in operational readiness, professional coverage, or assessment quality. Address before wide institutional deployment.

6. **Complete the diagnostic ladder in LAB-B2** with `gateway status`, `channels status --probe`, and `logs --follow`.
7. **Add exec approval three-mode taxonomy** to S1 Week 11 and LAB-B5.
8. **Add webhook security sub-focus to LAB-C2** and the Security capstone rubric.
9. **Add CI/CD integration for security audit** to Production/DevOps track and LAB-C2.
10. **Add contributor toolchain specifics** (pnpm, `check:changed`, scoped AGENTS.md) to the Contributor track.
11. **Add release-cadence awareness** to S1 Week 10 and a standing instructor note in the program overview.
12. **Add session recall security semantics** to S2 Week 2 or Week 7.
13. **Add API cost modeling** to S1 Week 10 and the Local Models specialization.
14. **Add a multi-agent reasoning dimension** to the master rubric.
15. **Add session store backup and recovery** to the Production capstone spec.

### Phase 3: Polish and Excellence Upgrades (required for world-class rating)

These improvements move the pack from "strong enough for a serious university" to "best-in-class reference curriculum."

16. **Add ElevenLabs TTS dependency note** to S1 Week 13 for operational risk completeness.
17. **Add ClawHub ecosystem status note** to the Plugin Developer track to calibrate expectations correctly.
18. **Add Feishu/Lark channel acknowledgment** to S1 Week 12 for enterprise completeness.
19. **Add `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` breakglass flag** to the security strand as a named danger.
20. **Add dreaming configuration to memory-strategy capstone requirements** for Operator and Production tracks.
21. **Develop per-module notes as companion files** for each track (currently track files are 29–33 lines each — sufficient as index entries, insufficient as standalone teaching guides).
22. **Add explicit lab failure modes and rollback guidance** to each Phase B and C lab — production-relevant skills that no current lab describes.
23. **Add a "checking official sources for this module" section** to each semester index week entry, linking to the official-reading-map entries that apply — making the source discipline tangible for students rather than a meta-document they may never open.

---

## Sources Consulted

### Primary — Official OpenClaw Documentation

| URL | Status | Used for |
|---|---|---|
| https://docs.openclaw.ai/start/getting-started | ✅ Verified accessible | Node.js version requirements; install command |
| https://docs.openclaw.ai/concepts/architecture | ✅ Verified accessible | Gateway architecture; control-plane claim |
| https://docs.openclaw.ai/security | ✅ Verified accessible | Trust model; personal-assistant framing |
| https://docs.openclaw.ai/sandboxing | ✅ Verified accessible | "Not a perfect boundary" language; escape hatches |
| https://docs.openclaw.ai/concepts/memory | ✅ Verified accessible | MEMORY.md; DREAMS.md; no hidden state; dreaming system |
| https://docs.openclaw.ai/plugins/manifest | ✅ Verified accessible | openclaw.plugin.json; required fields; JSON5 parsing |
| https://docs.openclaw.ai/gateway/remote | ✅ Verified accessible | Loopback-first; SSH/Tailscale safer default |
| https://docs.openclaw.ai/multi-agent | ✅ Verified accessible | Session stores; SOUL.md/USER.md/AGENTS.md; agentDir isolation |
| https://docs.openclaw.ai/security/formal-verification/ | ✅ Verified accessible | TLA+/TLC; bounded models; not full-system proof |
| https://docs.openclaw.ai/doctor | ✅ Verified accessible | Doctor command; plugin diagnostics |
| https://docs.openclaw.ai/cli/security | ✅ Verified accessible | `openclaw security audit`; webhook checks; `--json` flag |
| https://docs.openclaw.ai/help/troubleshooting | ✅ Verified accessible | Full 7-step diagnostic ladder; `gateway probe` confirmed |
| https://docs.openclaw.ai/skills | ✅ Verified accessible | 6-layer skill precedence; conflict resolution rule |
| https://docs.openclaw.ai/nodes | ✅ Verified accessible | Node definition; platform support; pairing model |
| https://docs.openclaw.ai/nodes/talk | ✅ Verified accessible | Talk mode real; ElevenLabs dependency; Android fallback |
| https://docs.openclaw.ai/gateway/trusted-proxy-auth | ✅ Verified accessible | Header spoofing risk; ⚠️ security-sensitive label |
| https://docs.openclaw.ai/web/control-ui | ✅ Verified accessible | Control UI real; port 18789; Dream monitoring panel confirmed |
| https://docs.openclaw.ai/tools/exec-approvals | ✅ Verified accessible | Three modes; per-command scope; canonical binding |
| https://docs.openclaw.ai/cli/status | ✅ Verified accessible | `openclaw status`; `--all`; `--deep`; note: no standalone "gateway probe" on this page |

### Primary — Official GitHub Repository

| URL | Status | Used for |
|---|---|---|
| https://github.com/openclaw/openclaw | ✅ Verified accessible | Repo identity; MIT license; active development confirmed |
| https://github.com/openclaw/openclaw/releases | ✅ Verified accessible | Latest v2026.4.21; model default change v2026.4.15; security hardening v2026.4.20 |
| https://github.com/openclaw/openclaw/blob/main/AGENTS.md | ✅ Verified accessible | Contributor toolchain; pnpm; `check:changed`; scoped AGENTS.md files |

### Secondary (explicitly labeled in review where cited)

| URL | Status | Used for |
|---|---|---|
| https://www.npmjs.com/package/openclaw | ❌ 403 Forbidden | Could not verify published version or download count |
| https://deepwiki.com/openclaw/docs/5.1-plugin-sdk-reference | Not fetched — npm access failed first | Plugin SDK cross-check |
| https://www.digitalocean.com/resources/articles/what-is-openclaw | ✅ Verified accessible (secondary) | Operational gap signal; real-world framing |
| https://docs.aimlapi.com/quickstart/openclaw | ✅ Verified accessible (secondary) | Provider integration; Telegram corroboration; model prefix conventions |
| https://clawhub.ai/plugins | ✅ Verified accessible (secondary) | 50 plugins; beta-heavy ecosystem; maturity signal |
| https://www.kdnuggets.com/openclaw-explained-the-free-ai-agent-tool-going-viral-already-in-2026 | Not fetched directly | Used earlier search-result summary only |
| https://generect.com/blog/openclaw-ai-agent/ | Not fetched directly | Not required after other sources were sufficient |

### Prerequisite Technology Docs

| URL | Status | Used for |
|---|---|---|
| https://nodejs.org/en/about/releases/ | ✅ Verified accessible (data ambiguous) | Node.js LTS schedule; Note: rendered page data was ambiguous on EOL dates — OpenClaw official docs' "Node 24 recommended, 22.14+ supported" claim was verified from the OpenClaw Getting Started page directly and is accepted as correct |
| https://owasp.org/www-community/attacks/PromptInjection | Not fetched — used knowledge | Prompt injection taxonomy for rubric gap assessment |

---

*This review was produced on April 22, 2026. All source verifications reflect the state of documentation accessible on that date. Claims depend on primary sources where available; secondary sources are labeled explicitly. This review is an independent second opinion and does not reference or derive from the prior review in `Validations/codex-review/`.*
