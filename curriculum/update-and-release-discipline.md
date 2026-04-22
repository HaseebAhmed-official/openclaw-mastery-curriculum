# Update and Release Discipline

## Why this matters

OpenClaw moves quickly. Defaults, security checks, model selections, plugin behavior, and deployment guidance can shift across releases. A world-class curriculum must therefore teach not only platform features, but also how to check whether those features changed.

## Required release discipline

Before any week involving providers, security controls, plugins, channels, automation, or deployment, instructors and learners should:

1. check the current installed version
2. read the latest release notes relevant to that module
3. verify the current update channel
4. note any behavior changes that affect labs or grading

## Operational topics learners must know

### Updating

- `openclaw update`
- `openclaw update --dry-run`
- channel switching
- version pinning and one-off tag targeting
- rollback awareness

### Release channels

- `stable`: normal baseline for teaching
- `beta`: candidate or pre-promoted stable
- `dev`: active development and not a production baseline

### Cohort consistency

- freeze teaching cohorts to a known version or channel when needed
- document any module that depends on a rapidly moving surface
- avoid grading students against unstated defaults

## Teaching rule

Any curriculum statement about defaults, model choices, or current behavior must either:

- cite the official docs and validation date, or
- tell the learner to check the current release notes before proceeding

## Best insertion points in the program

- Semester 1 Week 10: providers and model defaults
- Semester 2 Week 1: production framing
- Production / DevOps track
- Contributor / Core track
