# Semester 1

## Goal

Move learners from prerequisite readiness to safe, competent OpenClaw operation.

By the end of Semester 1, a learner should be able to install OpenClaw, onboard a provider, run the gateway, use the Control UI, understand sessions and memory, connect at least one channel safely, use nodes conceptually, and troubleshoot a baseline environment without guesswork.

## Weekly sequence

| Week | Theme | Core outcomes | Hands-on focus | Assessment |
| --- | --- | --- | --- | --- |
| 1 | Environment baseline | Verify WSL2/Linux, shell, editor, package tooling | WSL2/Linux setup checklist | Environment verification |
| 2 | Git and repo hygiene | Read diffs, branch safely, inspect state | Git mini-workflow | Git workflow check |
| 3 | Node.js, JSON, TypeScript literacy | Understand runtime, packages, and config shape | Node versioning and JSON drill | Config reading quiz |
| 4 | Docker and networking basics | Explain containers, localhost, ports, and tunnels | Docker and port-mapping lab | Networking worksheet |
| 5 | LLM agent fundamentals | Explain provider, model, tools, and prompt injection basics | Tool-risk analysis | Reflection memo |
| 6 | OpenClaw overview and trust model | Explain gateway, control plane, channels, nodes, and personal-assistant trust model | Architecture mapping lab | Concept check |
| 7 | Installation and onboarding | Install OpenClaw, run `openclaw onboard`, understand auth and daemon setup | First install and onboarding | Install lab |
| 8 | Control UI, doctor, status, health | Use the basic operational commands and browser UI | Local ops and diagnostics ladder | Midterm practical 1 |
| 9 | Sessions, workspace, and memory | Explain session boundaries, workspace files, and memory model | Workspace + memory inspection lab | Session/memory quiz |
| 10 | Models, providers, and release-aware defaults | Configure a model, understand fallback ordering, inspect model status, and check current release notes before trusting defaults | Provider auth, model selection, and release-note diff lab | Provider setup review |
| 11 | Tools, sandboxing, and approvals | Distinguish sandbox vs host execution and approval flows | Sandbox + exec policy lab | Safety review |
| 12 | Channels and pairing | Safely connect a channel and reason about DM/group policy | Telegram or WhatsApp lab | Channel policy check |
| 13 | Nodes and multimodal surfaces | Explain node role, pairing, command surface, talk mode, voice wake, and third-party dependencies like TTS providers | Node architecture walkthrough | Node concept check |
| 14 | Remote access patterns | Compare loopback, SSH tunnels, and Tailscale Serve patterns | Remote access lab | Remote access review |
| 15 | Troubleshooting and hardening baseline | Run a full diagnosis ladder and fix a broken setup | Troubleshooting drill | Secure baseline review |
| 16 | Practical exam and mini-project | Demonstrate safe baseline deployment competence | End-to-end build | Semester defense |

## Required Semester 1 deliverables

- a verified development environment
- a successful OpenClaw installation
- a working local gateway with Control UI access
- one configured provider and model baseline
- one release-aware note describing what defaults were current during the lab run
- one safe channel or equivalent webchat-only baseline
- one troubleshooting runbook
- one secure baseline design note

## Core readings

- official OpenClaw overview
- getting started and onboarding docs
- gateway architecture
- Windows and remote access docs
- memory, models, tools, channels, nodes, doctor, and troubleshooting docs

See the [Official Reading Map](../sources/official-reading-map.md) for the exact links.

## Teaching support

- [Semester 1 Teaching Guide](teaching-guide.md)
- [Core Lab Guides](../labs/core-lab-guides.md)
- [Question Bank](../assessment/question-bank.md)
- [Practical Exams](../assessment/practical-exams.md)
