# Competency Framework

## Competency domains

### Domain A: Systems and environment literacy

- shells, WSL2, Linux basics
- Node.js runtime and package management
- Docker and networking basics
- SSH and remote host access

### Domain B: OpenClaw conceptual model

- gateway architecture
- sessions, routing, and multi-agent boundaries
- memory and workspace model
- channels, nodes, and control-plane clients

### Domain C: Operator execution

- onboarding
- config editing
- model/provider setup
- diagnostics, doctor, status, and logs
- release and update awareness
- remote access and persistent operation

### Domain D: Security and governance

- trust model
- prompt injection and unsafe external content
- hardening controls
- exec approvals and tool policy
- security audit and incident response

### Domain E: Production design

- environment selection
- remote host design
- reverse proxy and trusted proxy patterns
- Tailscale / SSH patterns
- webhook ingress and detached-work auditability
- change control and operational review

### Domain F: Extensibility

- skills
- plugins
- plugin bundles and distribution surfaces
- manifests and schema validation
- capability ownership and configuration surfaces

### Domain G: Contribution and architecture depth

- repo literacy
- architecture and codegen surfaces
- tests, docs, and contribution standards
- formal models and threat-model contribution

## Mastery levels

### Level 0: Bridge-ready

Can work safely in the terminal, WSL2/Linux, Git, JSON, Node.js, and Docker with supervision.

### Level 1: OpenClaw literate

Can explain what OpenClaw is, how the gateway works, and why trust boundaries matter.

### Level 2: Hands-on operator

Can install, onboard, chat, configure a baseline model/provider, and troubleshoot common issues.

### Level 3: Secure operator

Can run OpenClaw with explicit tool policy, safe channel exposure, and documented access controls.

### Level 4: Production practitioner

Can design and defend a remote or persistent deployment with governance, webhook and automation controls, and operational controls.

### Level 5: Extension developer

Can create or adapt skills/plugins and reason about manifest-driven configuration and capability surfaces.

### Level 6: Core contributor

Can navigate the repo, contributor workflows, architecture surfaces, and validation/testing expectations.

### Level 7: Specialist

Can lead one of the specialization areas: production, security, plugin ecosystem, local models, or advanced operations.

## Evidence of mastery

Each level must be demonstrated by artifacts, not only quizzes.

- Levels 0 to 1: bridge exercises and concept checks
- Level 2: working installation, safe setup, and troubleshooting evidence
- Level 3: hardening review and secure baseline lab
- Level 4: production architecture document and operational runbook
- Level 5: extension or plugin implementation with validation
- Level 6: contributor-level code or design artifact
- Level 7: capstone defense with explicit tradeoff analysis

## Role mapping

### Student / foundational graduate

- target: Levels 0 to 3

### Operator / power user

- target: Levels 1 to 4

### Production / DevOps engineer

- target: Levels 2 to 5

### Security / governance practitioner

- target: Levels 2 to 5

### Plugin developer

- target: Levels 2 to 5

### Contributor / maintainer candidate

- target: Levels 2 to 6

### Specialist

- target: Levels 4 to 7

## Certification-style outcomes

- Foundation: Level 1 plus prerequisite bridge
- Operator: Level 2
- Secure Operator: Level 3
- Production: Level 4
- Developer: Level 5
- Contributor: Level 6
- Specialist: Level 7
