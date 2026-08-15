# Prerequisite Bridge

## Purpose

Establish the minimum foundations required to build and debug an agent harness. This is diagnostic and repair work, not a passive pre-course reading list. Learners may test out of a module only by producing the exit evidence.

## Diagnostic Rule

For each bridge module, require one unaided explanation and one changed-condition practical. Route failure to the smallest repair unit, then retest with a different task. Framework familiarity does not substitute for foundations.

## Bridge Modules

### B0: Computer and Filesystem Literacy

Concepts: processes, files, directories, paths, environment variables, permissions, standard streams, editors, archives, and safe command execution.

Evidence: navigate an unfamiliar project, identify its execution entry point, explain where configuration and generated state live, and recover from a path or permission error.

### B1: Shell, Linux, and WSL

Concepts: shell expansion, quoting, pipes, exit codes, process inspection, signals, package boundaries, services, logs, and Windows/WSL path and network boundaries.

Evidence: run and diagnose a small service in Linux or WSL, capture logs and exit status, and explain host-versus-guest ownership.

### B2: Git and Collaborative Change

Concepts: repository state, commits, branches, remotes, diffs, merge conflicts, review, provenance, secret avoidance, and non-destructive recovery.

Evidence: make a scoped change, test it, inspect the diff, resolve a controlled conflict, and explain exactly what will be committed.

### B3: Python and Type-Driven Programming

Concepts: values, control flow, functions, modules, exceptions, classes/protocols, type hints, dataclasses, JSON serialization, dependency isolation, and command-line programs.

Evidence: implement and test a typed adapter plus a parser that rejects malformed input with a useful error.

### B4: TypeScript and Schema Literacy

Concepts: JavaScript runtime model, TypeScript types, interfaces, discriminated unions, async/await, package manifests, JSON Schema, and runtime validation.

Evidence: trace a typed request through validation and asynchronous handling; explain where compile-time types do not protect runtime data.

### B5: Testing, Debugging, and Software Design

Concepts: unit/integration/end-to-end tests, fixtures, test doubles, invariants, property boundaries, logs, debuggers, root-cause analysis, contracts, dependency inversion, and refactoring.

Evidence: reproduce a defect, isolate the cause, add a failing regression test, repair the implementation, and explain why the test distinguishes cause from symptom.

### B6: HTTP, APIs, Authentication, and Data

Concepts: request/response, streaming, status codes, timeouts, retries, idempotency, webhooks, authentication versus authorization, OAuth concepts, databases, transactions, indexes, queues, and serialization.

Evidence: implement a small client/server interaction with timeout and idempotency behavior, then diagnose an authentication or data-consistency failure.

### B7: Operating Systems, Networking, and Concurrency

Concepts: processes/threads, scheduling, files and sockets, localhost, DNS, ports, TLS, proxies, SSH, containers, async tasks, race conditions, locks, queues, cancellation, and resource limits.

Evidence: trace a request across process and network boundaries, demonstrate one concurrency failure, and repair it with an explicit synchronization or ownership argument.

### B8: Security and Privacy Foundations

Concepts: assets, actors, trust boundaries, least privilege, secure defaults, secrets, input validation, injection, confused deputy, isolation, dependency risk, logging sensitivity, data minimization, retention, and incident response.

Evidence: threat-model a small tool-using application, demonstrate one safe exploit, prioritize mitigations, and identify residual risk.

### B9: Probability, Measurement, and Experiments

Concepts: distributions, sampling, variance, confidence intervals, base rates, measurement error, repeated trials, test leakage, selection bias, and practical versus statistical significance.

Evidence: analyze repeated nondeterministic task results, report uncertainty, and reject an unsupported conclusion drawn from a single successful run.

### B10: LLM and Agent-System Fundamentals

Concepts: tokens, context windows, sampling, structured output, embeddings, retrieval, tool calling, prompt injection, hallucination, evaluation, workflows, agents, harnesses, and human oversight.

Evidence: draw and defend the control/data flow for a tool-using model system, distinguish model error from harness error, and choose a deterministic alternative when autonomy is unnecessary.

### B11: Technical Communication and Reasoning

Concepts: precise claims, assumptions, evidence, audience, diagrams, design records, incident writing, oral explanation, counterexamples, tradeoffs, and uncertainty.

Evidence: write a one-page design note and deliver a five-minute defense that clearly separates fact, inference, decision, and unresolved risk.

## Bridge Exit Gate

A learner is core-ready only when they can, without step-by-step agent guidance:

- implement and test a typed Python component
- read and trace a small TypeScript/JSON code path
- use Git safely and explain a diff
- diagnose a process, path, network, or permission failure
- explain timeout, retry, idempotency, and authentication boundaries
- construct a basic threat model
- interpret repeated-trial evidence
- distinguish workflow, agent, model, tool, and harness
- communicate a technical decision and uncertainty precisely

## Required Bridge Portfolio

- environment verification record
- Git change and conflict-resolution evidence
- tested Python adapter
- TypeScript/schema tracing note
- API reliability exercise
- concurrency or process-debugging report
- basic threat model
- repeated-trial analysis
- short design note and oral-defense rubric
