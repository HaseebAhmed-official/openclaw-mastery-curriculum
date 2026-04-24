# Reference Screenshot Manifest

## Purpose

This manifest defines the exact screenshot slots that should exist for a fully visual teaching pack. It keeps future captures consistent across instructors, cohorts, and OpenClaw release updates.

## Canonical lane

- target environment: WSL Ubuntu learner lane
- browser lane: local browser for Control UI and docs checks
- versioning rule: every screenshot set must record the OpenClaw version and validation date

## Directory convention

- core labs: `curriculum/lab-manuals/assets/core/`
- advanced labs: `curriculum/lab-manuals/assets/advanced/`
- specialization labs: `curriculum/lab-manuals/assets/specialization/`

## Naming convention

Use this pattern:

- `LAB-<id>-step-<nn>-<short-label>.png`

Example:

- `LAB-B2-step-03-status-healthy.png`

## Core lab screenshot slots

### LAB-A1

- `LAB-A1-step-01-shell-baseline.png`
- `LAB-A1-step-02-home-path.png`
- `LAB-A1-step-03-package-manager.png`
- `LAB-A1-step-04-browser-access.png`

### LAB-A2

- `LAB-A2-step-01-branch-created.png`
- `LAB-A2-step-02-diff-view.png`
- `LAB-A2-step-03-clean-tree-after-recovery.png`

### LAB-A3

- `LAB-A3-step-01-node-version.png`
- `LAB-A3-step-02-valid-config-example.png`
- `LAB-A3-step-03-invalid-config-example.png`

### LAB-A4

- `LAB-A4-step-01-container-running.png`
- `LAB-A4-step-02-port-mapping.png`
- `LAB-A4-step-03-browser-or-curl-success.png`

### LAB-B1

- `LAB-B1-step-01-install-complete.png`
- `LAB-B1-step-02-onboarding-entry.png`
- `LAB-B1-step-03-first-healthy-status.png`

### LAB-B2

- `LAB-B2-step-01-control-ui-overview.png`
- `LAB-B2-step-02-status-healthy.png`
- `LAB-B2-step-03-doctor-healthy.png`
- `LAB-B2-step-04-gateway-probe-broken.png`
- `LAB-B2-step-05-logs-follow.png`

### LAB-B3

- `LAB-B3-step-01-workspace-tree.png`
- `LAB-B3-step-02-memory-md.png`
- `LAB-B3-step-03-daily-note.png`

### LAB-B4

- `LAB-B4-step-01-provider-auth-success.png`
- `LAB-B4-step-02-model-status.png`
- `LAB-B4-step-03-release-note-reference.png`

### LAB-B5

- `LAB-B5-step-01-policy-config.png`
- `LAB-B5-step-02-risky-setting-example.png`
- `LAB-B5-step-03-mitigation-example.png`

### LAB-B6

- `LAB-B6-step-01-channel-status.png`
- `LAB-B6-step-02-policy-note.png`
- `LAB-B6-step-03-safe-send-receive.png`

### LAB-B7

- `LAB-B7-step-01-remote-path-diagram.png`
- `LAB-B7-step-02-tunnel-or-serve-proof.png`
- `LAB-B7-step-03-trust-note.png`

## Advanced lab screenshot slots

### LAB-C1

- `LAB-C1-step-01-workspace-a-tree.png`
- `LAB-C1-step-02-workspace-b-tree.png`
- `LAB-C1-step-03-identity-file-diff.png`

### LAB-C2

- `LAB-C2-step-01-audit-baseline.png`
- `LAB-C2-step-02-audit-deep.png`
- `LAB-C2-step-03-json-artifact.png`
- `LAB-C2-step-04-advisory-reference.png`
- `LAB-C2-step-05-remediation-priority-table.png`

### LAB-C3

- `LAB-C3-step-01-ingress-comparison.png`
- `LAB-C3-step-02-rejected-loopback-proxy.png`
- `LAB-C3-step-03-accepted-bounded-ingress.png`

### LAB-C4

- `LAB-C4-step-01-routing-policy-table.png`
- `LAB-C4-step-02-trust-boundary-note.png`

### LAB-C5

- `LAB-C5-step-01-trust-boundary-diagram.png`
- `LAB-C5-step-02-threat-register.png`
- `LAB-C5-step-03-control-mapping.png`

### LAB-C6

- `LAB-C6-step-01-primitive-selection-matrix.png`
- `LAB-C6-step-02-rejected-wrong-choice.png`
- `LAB-C6-step-03-authority-note.png`

### LAB-C7

- `LAB-C7-step-01-delegation-diagram.png`
- `LAB-C7-step-02-child-constraint-table.png`
- `LAB-C7-step-03-task-record-example.png`

## Specialization lab screenshot slots

### LAB-D1

- `LAB-D1-step-01-manifest-excerpt.png`
- `LAB-D1-step-02-risk-classification.png`

### LAB-D2

- `LAB-D2-step-01-precedence-diagram.png`
- `LAB-D2-step-02-collision-example.png`
- `LAB-D2-step-03-resolution-note.png`

### LAB-D3

- `LAB-D3-step-01-node-surface-diagram.png`
- `LAB-D3-step-02-policy-note.png`

### LAB-D4

- `LAB-D4-step-01-tradeoff-matrix.png`
- `LAB-D4-step-02-fallback-decision-tree.png`

### LAB-D5

- `LAB-D5-step-01-repo-scope-map.png`
- `LAB-D5-step-02-validation-plan.png`
- `LAB-D5-step-03-change-proposal-note.png`

## Maintenance rule

When screenshots drift because OpenClaw changes:

1. update the affected capture files
2. note the new version and validation date
3. update the related lab manual if the visible workflow changed
4. record the change in the maintenance review log if it reflects upstream drift rather than local polish
