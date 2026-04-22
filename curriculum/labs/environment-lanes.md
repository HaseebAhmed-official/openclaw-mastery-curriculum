# Environment Lanes

## Purpose

Not every institution has the same budget, hardware, or operational risk tolerance. These lanes keep the curriculum usable without flattening the learning goals.

## Lane 1: low-cost student path

- primary environment: personal Windows laptop with WSL2 or Linux laptop
- provider strategy: hosted provider, minimal spend
- deployment scope: local gateway plus one remote-access exercise
- channel scope: webchat first, one optional mobile-friendly channel
- local models: theory or lightweight comparison only

## Lane 2: standard university lab path

- primary environment: managed WSL2/Linux lab images
- provider strategy: institution-managed API keys or controlled auth
- deployment scope: local gateway, remote host lab, and controlled VPS exercise
- channel scope: at least one real channel integration under policy
- security scope: mandatory audit and hardening lab

## Lane 3: enterprise reference path

- primary environment: Linux or managed remote hosts
- provider strategy: controlled provider auth profiles and change management
- deployment scope: persistent gateway, remote access, and operational runbooks
- channel scope: explicit business-use channel policies
- security scope: full governance strand and capstone defense

## Canonical recommendation

Use Lane 2 as the default academic path. It balances realism, cost, and production relevance.

## Hardware and software minimums

- Node.js version meeting current OpenClaw support
- Docker available where sandboxing labs are required
- SSH client and stable internet connectivity
- a browser for Control UI
- a Windows machine with WSL2 or a Linux/macOS machine for the canonical baseline
