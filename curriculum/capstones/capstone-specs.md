# Capstone Specifications

## Common System Contract

Every capstone must include:

- a problem definition, users, constraints, success criteria, and non-goals
- a deterministic baseline and evidence that agentic behavior is justified
- a provider/model interface with deterministic test path
- bounded loop/orchestration with explicit stop, cancel, and budget behavior
- typed least-authority tools with validation and structured errors
- context provenance and budget policy
- sessions/events, durable state, idempotency/recovery, and artifact handling
- memory only when justified, with isolation, retention, provenance, and deletion
- policy, exact approval for material effects, execution boundaries, and audit evidence
- correlated observability and a realistic repeated-trial evaluation corpus
- authorized attack, mitigation, variant retest, and residual-risk decision
- deployment, SLO, latency/cost, data lifecycle, incident, backup/migration/rollback evidence
- current source/version ledger and change triggers
- one meaningful portability exercise across providers, frameworks, or protocols
- team contribution record plus individual defense and transfer

## Scope Limits

Capstones must fit the environment, time, compute, budget, privacy, and assessor capacity. A smaller deeply verified system is preferred over a broad untested platform. High-stakes medical, legal, financial, public-safety, or offensive-security systems require qualified supervision and may be restricted to synthetic learning environments.

## Specialization Options

### Product / Operator

Build and evaluate a bounded workflow or assistant for a real user group. Emphasize requirements, human control, task outcomes, accessibility, adoption, privacy, and operating policy.

### Platform / SRE

Build the durable execution and operating plane for a harness. Emphasize deployment, queues/state, SLOs, capacity, observability, incidents, migrations, backups, and rollback.

### Security / Assurance

Build an agentic security testbed and control suite. Emphasize authority graphs, exploit evidence, layered controls, detection, recovery, assurance limits, and control-evidence mapping.

### Tools / Protocols

Build a high-quality tool/plugin plus MCP or A2A integration. Emphasize schemas, least authority, compatibility, identity/auth, lifecycle, errors, cancellation, tests, and supply chain.

### Core / Framework

Implement or materially improve a harness runtime subsystem such as orchestration, context, event state, evaluation, or observability. Emphasize contracts, performance, compatibility, tests, and maintainability.

### Local-Model Infrastructure

Build and operate a local/private model-serving and routing layer for the harness. Emphasize measured quality, hardware fit, throughput, latency, privacy, fallbacks, capacity, cost, and incidents.

## Product Case-Study Requirement

Compare the capstone against at least two current systems or frameworks. At least one comparison should use source-visible evidence. Map differences to stable harness contracts and label product facts by date and evidence status. No learner is required to reproduce a proprietary internal architecture.

## Release Packet

- executive summary with claim limits
- architecture/data/trust/failure diagrams
- source/version and decision ledger
- source code, tests, fixtures, and reproduction instructions
- task corpus, raw trial results, graders, and release verdict
- threat model, exploit traces, mitigation, and retest
- deployment/runbook/SLO/incident/rollback evidence
- privacy/accessibility/governance review
- portability comparison
- unresolved risks and ownership
- contribution and assistance disclosure

## Stop-Ship Conditions

- critical security/privacy defect without explicit authorized containment
- unreproducible core behavior
- fabricated or selectively omitted evidence
- learner/team cannot explain material system behavior
- evaluation criteria changed after results to create a pass
- no safe recovery or rollback for material side effects
- current product/framework claims without current evidence
