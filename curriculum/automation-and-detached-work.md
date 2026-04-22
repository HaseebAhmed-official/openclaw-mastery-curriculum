# Automation and Detached Work

## Why this topic is core

OpenClaw is no longer just an interactive chat-and-tool system. It has a durable background execution model built around tasks, cron, hooks, heartbeat, standing orders, sub-agents, and ACP agents. Any mastery curriculum that omits these surfaces leaves learners with an incomplete mental model of authority, auditability, and production risk.

## Core mechanisms

### Scheduled tasks (cron)

- precise timing
- one-shot reminders and recurring jobs
- can deliver to channels or webhooks
- isolated runs create task records and can use their own model/tool restrictions

### Background tasks

- task ledger for detached work
- audit surface for cron jobs, sub-agent runs, ACP runs, and detached CLI operations
- should be part of any production troubleshooting workflow

### Task Flow

- durable orchestration layer above individual background tasks
- used when work spans multiple steps and needs revision-aware flow control

### Standing orders

- persistent authority and operating rules
- usually live in workspace files like `AGENTS.md`
- injected into every session

### Hooks

- event-driven scripts
- trigger on lifecycle and tool events
- create a real authority boundary and supply-chain surface

### Heartbeat

- periodic main-session turn
- best for routine awareness work with full session context
- does not create task records like cron does

### Sub-agents

- bounded delegated work inside the agent runtime
- introduce task ownership, auditability, and coordination concerns

### ACP agents

- external or protocol-based agent coordination surface
- must be taught as an integration and trust-boundary topic, not just a feature checkbox

## Security and governance implications

- cron and hooks widen execution authority
- webhook-driven automation creates its own ingress and token-management surface
- standing orders grant durable authority and must be reviewed like policy
- detached work must be auditable through task records and logs
- sub-agents and ACP agents require explicit ownership and result-tracking discipline

## What learners must be able to do

- choose the correct detached-work primitive for a use case
- explain the difference between cron, heartbeat, hooks, and standing orders
- inspect task records and defend an audit trail
- restrict tool/model/session scope for isolated background work
- identify webhook and hook-specific security risks

## Best insertion points in the program

- Semester 2 Week 5: approvals and host authority
- Semester 2 Week 10: automation, hooks, and standing orders
- Semester 2 Week 11: sub-agents, ACP agents, headless nodes, and detached task auditability
