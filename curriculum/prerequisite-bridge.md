# Prerequisite Bridge

## Purpose

The bridge exists so learners can enter OpenClaw with enough systems literacy to understand what they are doing, not just copy commands. OpenClaw becomes dangerous and confusing when learners lack basic command-line, configuration, and security habits.

## Bridge modules

### Bridge 1: Terminal and filesystem literacy

- navigate directories
- inspect files and processes
- understand stdout, stderr, exit codes, and logs
- use shells safely on Windows and Linux

### Bridge 2: WSL2 and Linux basics

- install and verify WSL2
- understand home directory, permissions, and package managers
- differentiate host Windows paths from Linux paths
- know when to prefer WSL2 over native Windows for OpenClaw

### Bridge 3: Git and GitHub workflow

- clone, branch, commit, pull, push
- read diffs and blame output
- manage clean and dirty worktrees
- understand PR review as part of an AI systems workflow

### Bridge 4: Node.js, npm, and package hygiene

- install and verify Node.js
- use npm and pnpm safely
- understand global CLI installs vs project-local dependencies
- reason about package provenance and official package sources

### Bridge 5: JSON, TypeScript, and schema literacy

- read structured config
- understand JSON Schema as a validation contract
- read basic TypeScript types and docs
- trace a config key from docs to runtime expectations

### Bridge 6: Docker and containers

- understand images, containers, volumes, networks
- run basic commands
- understand why sandboxing depends on Docker
- know when Docker is optional and when it is operationally important

### Bridge 7: Networking, SSH, and tailnets

- understand localhost, LAN, and remote hosts
- use SSH tunnels
- understand why loopback-only is safer
- understand Tailscale Serve and identity-header implications

### Bridge 8: LLM and agent systems fundamentals

- understand model providers, auth, and tool invocation
- reason about prompt injection and unsafe external content
- understand why "smart model" does not mean "safe system"

## Exit criteria

Before entering Semester 1 proper, a learner should be able to:

- set up WSL2 or a Linux environment
- install Node.js and verify version constraints
- use Git without damaging a repository
- read and edit JSON config
- run Docker commands and explain sandboxing at a high level
- create an SSH tunnel and explain what port forwarding does
- explain prompt injection risk in tool-enabled agents

## Recommended bridge deliverables

- environment setup checklist
- WSL2 verification worksheet
- Git mini-project with branching and diff review
- Node.js and JSON config drill
- Docker sandbox demo
- SSH tunnel demo
- short security reflection on prompt injection and trust boundaries
