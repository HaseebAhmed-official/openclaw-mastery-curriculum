# Track Rubrics

## Use

Apply the [Master Rubric](master-rubric.md) first. These criteria add role-specific evidence; they do not remove common security, evaluation, operations, communication, or transfer gates.

## Product / Operator

Required evidence:

- user/workflow requirements and deterministic baseline
- bounded configuration with authority and escalation paths
- realistic task evaluation and human-override evidence
- adoption, accessibility, privacy, and operating guide

Distinction: improves user outcomes with less unnecessary autonomy and clear governance. Fail: feature demo without task evidence or hidden authority.

## Platform / SRE

Required evidence:

- durable state and recovery design
- deployment, secrets/config, migrations, backups, rollback
- SLOs, traces/metrics/logs, capacity and cost evidence
- incident simulation and corrective action

Distinction: recovers under multiple failure modes with low ambiguity and reproducible operations. Fail: “production-ready” without failure, rollback, or ownership evidence.

## Security / Assurance

Required evidence:

- concrete threat/data/identity model
- authorized exploit portfolio
- layered preventive/detective/recovery controls
- mitigation variants, residual risks, and control-evidence map

Distinction: discovers a non-obvious authority path and validates a reusable fix. Fail: generic threat list, unsafe testing, or unsupported assurance claim.

## Tools / Protocols

Required evidence:

- typed and discoverable interface
- least-authority and error design
- MCP/A2A or plugin/tool contract tests
- version compatibility, timeout/cancellation, dependency and supply-chain review

Distinction: interoperates across independent implementations with strong failure semantics. Fail: happy-path demo or discovery treated as authorization.

## Core / Framework

Required evidence:

- source-level control/data-flow trace
- runtime/orchestration/state subsystem implementation or scoped contribution
- performance, compatibility, regression, and maintenance evidence
- design alternatives and upstream conventions

Distinction: accepted upstream change or independently validated subsystem improvement. Fail: large untraceable rewrite or framework-specific code presented as universal core.

## Local-Model Infrastructure

Required evidence:

- declared hardware, workload, privacy, budget, and quality constraints
- measured serving/routing comparison
- throughput, latency, resource, failure, and quality evaluation
- fallback, capacity, deployment, and operations design

Distinction: adapts routing under changed constraints with measured improvement. Fail: universal model recommendation or benchmark-only decision.
