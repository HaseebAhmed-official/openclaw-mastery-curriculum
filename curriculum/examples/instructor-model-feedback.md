# Instructor Model Feedback

## Purpose

These examples show what effective instructor feedback sounds like in this course.

## High distinction feedback

Your submission was strong because it did not stop at "it works." You documented authority, failure modes, and release-aware assumptions clearly. The strongest part was the way you rejected unsafe convenience rather than trying to justify it after the fact.

## Pass with revision feedback

The design is directionally correct, but it is not fully defensible yet. You have the right topology, but your trust-boundary explanation is too thin and your update strategy is not specific enough. Revise the security section so it explicitly names who is trusted, how ingress works, and what would force a rollback.

## Fail feedback for trust-model misunderstanding

This submission cannot pass in its current form because it describes one shared gateway as safe for users who do not trust each other. That is not consistent with the official OpenClaw trust model and it changes the meaning of the whole architecture. Redesign around a trusted-user boundary or propose a different system.

## Fail feedback for weak operational evidence

The screenshots suggest the workflow may have worked, but the submission does not prove operational understanding. There is no diagnostic sequence, no failure analysis, and no recovery note. Rework the artifact using the runbook and lab submission templates.

## Fail feedback for security omission

The artifact demonstrates technical effort, but it does not address prompt injection or unsafe external content in a tool-enabled workflow. In this course, that omission is not minor. Add a real security review section and defend your choices explicitly.
