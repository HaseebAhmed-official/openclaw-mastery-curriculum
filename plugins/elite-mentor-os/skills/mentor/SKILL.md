---
name: mentor
description: Use when teaching a concept with practice, feedback, transfer, or repair.
---

# Mentor

Use this as the default teaching workflow.

## Read First

- `.mentor/MENTOR_STATE.md` when present
- `plugins/elite-mentor-os/core/MENTOR_OS.md`
- relevant local files, sources, and prior work

## Teaching Loop

1. State the session target and expected mastery level.
2. Check prerequisite knowledge with 2-5 concise questions or a small task.
3. Teach the concept with a mental model, example, non-example, and boundary.
4. Ask retrieval questions before giving more explanation.
5. Assign one guided task and one independent transfer task.
6. Review the learner's answer against an explicit rubric.
7. Identify the smallest weakness and give a repair drill.
8. Propose a `.mentor/MENTOR_STATE.md` update when progress, weakness, or evidence changes.

## Output Contract

Return:

- concise lesson
- prerequisite check
- practice task
- transfer task
- grading rubric
- repair loop
- portfolio evidence suggestion
