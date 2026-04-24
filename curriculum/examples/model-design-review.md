# Model Design Review

## Context

This example shows the level of clarity expected in a strong production-oriented design review.

## Design title

Trusted-Team Remote Access Design for a Shared OpenClaw Gateway

## Problem statement

A small trusted internal team wants remote access to a shared OpenClaw gateway for collaborative use, but does not want the gateway exposed publicly. The system must preserve operational clarity and avoid pretending that the gateway can safely host adversarial users.

## Proposed solution

Deploy a single OpenClaw gateway on a managed Linux host, keep the service loopback-bound, and provide remote access through Tailscale Serve for trusted team members only. Restrict dangerous tool authority by default, document a clear DM/shared-inbox policy, and require explicit review before enabling any hooks or plugin installs.

## Context and assumptions

- intended users: one lead operator plus a small trusted internal team
- trust model: cooperative trusted users only
- environment: managed Linux host with Docker available
- version / release assumptions: reviewed against current stable release on 2026-04-24
- constraints: no public exposure, no hostile multi-tenant use, no unreviewed webhook ingress

## Architecture summary

- gateway location: managed Linux VPS
- access method: Tailscale Serve to a loopback-bound service
- provider / model strategy: hosted provider with strong default model; version-sensitive defaults checked before deployment
- channels or nodes used: web UI and one approved team channel
- plugins or skills involved: only reviewed built-in or explicitly approved additions
- automation or detached work involved: none in phase 1; standing orders reviewed separately if added later

## Trust boundary analysis

### Who is trusted?

- lead operator
- explicitly approved internal team members with tailnet access

### Who is not trusted?

- the public internet
- unreviewed plugin authors
- external content sources by default

### Where does authority widen?

- when a user can message the gateway
- when tools can touch host resources
- when plugins or hooks can execute code

### What authority is durable?

- gateway configuration
- standing orders if enabled later
- skill/plugin installation state

## Operational design

- install or deployment method: pinned stable install with documented update process
- health checks: `openclaw status`, `doctor`, `gateway probe`, and log review
- logging and diagnostics: retained diagnostic ladder plus release-aware note for each change window
- rollback expectations: version-aware rollback and config backup before major updates
- update strategy: review release notes before provider/security-affecting changes

## Security review

- prompt injection exposure: any external-content workflow must be reviewed before adoption
- sandboxing / exec policy: sandbox enabled where relevant, host execution kept restricted
- webhook or hook exposure: not enabled in baseline
- plugin or supply-chain concerns: no plugin installs without provenance review
- remote ingress concerns: ingress limited to trusted tailnet users; no public reverse proxy

## Alternatives considered

### Alternative 1

- why considered: public reverse proxy is convenient
- why rejected: widens exposure and creates unnecessary ingress risk for this trust model

### Alternative 2

- why considered: one gateway for any user in the organization
- why rejected: drifts toward a hostile or mixed-trust model that OpenClaw docs do not support as a secure boundary

## Failure modes

1. Provider degradation or default drift across releases
2. Team members assuming shared access implies adversarial isolation
3. Plugin or automation additions widening authority without review

## Evidence and references

- official docs used:
  - architecture
  - security
  - remote access
  - trusted proxy / remote access guidance
  - release notes

## Final recommendation

Approve with conditions:

1. keep the gateway non-public
2. document team-use policy explicitly
3. require review before enabling plugins, hooks, or detached automation

## Why this is a strong example

- It matches OpenClaw's actual trust model.
- It rejects attractive but unsafe convenience.
- It distinguishes architecture, security, and operational choices clearly.
