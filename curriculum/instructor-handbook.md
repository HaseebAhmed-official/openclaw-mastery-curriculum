# Instructor Handbook

## Purpose

This handbook turns the curriculum from a roadmap into a deliverable teaching system. It is written for instructors who want to run the course without inventing structure, policies, or operational controls from scratch.

## Default delivery model

### Recommended university format

- 2 semesters
- 16 teaching weeks per semester
- 1 live session of 150 to 180 minutes per week, or 2 sessions of 75 to 90 minutes each
- 1 lab section or supervised build block every week

### Accelerated format

- 1 intensive semester
- keep Semester 1 mandatory
- compress Semester 2 into operator, production, and security essentials
- keep only one specialization track

### Enterprise adaptation

- use the prerequisite bridge selectively
- run Semester 1 as operator onboarding
- run selected Semester 2 weeks for platform, security, and plugin teams
- assign one track-specific capstone per operational role

## Instructor readiness checklist

### Four to six weeks before the course

- validate the current OpenClaw version and release channel
- review current release notes for any breaking changes to providers, channels, automation, or security controls
- choose the environment lane
- decide whether students will use shared institutional provider keys or personal keys
- decide whether real channels are allowed or whether webchat-only delivery is required
- prepare a safe baseline lab image for WSL2/Linux if the institution can provide one
- confirm whether Docker is available for sandboxing labs

### One week before the course

- complete the full prerequisite bridge yourself using the same environment students will use
- run the current versions of all mandatory Semester 1 labs
- update any screenshots or commands that drifted with the latest release
- pre-stage failure cases for diagnostics and troubleshooting labs
- verify policy around tokens, phone numbers, messaging channels, and cloud accounts

### Every week

- re-check release notes before provider, security, automation, plugin, or deployment modules
- re-run the week's lab on the same channel used for teaching
- note any current operational warnings students should see before they start
- review student artifacts for recurring failure patterns and address them at the start of the next class

## Infrastructure baseline

### Required minimum

- Windows with WSL2, Linux, or macOS
- stable internet connection
- browser access
- Node.js version aligned with current OpenClaw support
- git
- terminal access

### Required for full curriculum

- Docker for sandboxing labs
- SSH client
- controlled access to one hosted model provider
- optional VPS for production deployment labs

### Optional but valuable

- Tailscale access for remote access labs
- institution-managed secrets vault
- shared LMS for rubric-based submissions
- private GitHub classroom or equivalent repo workflow

## Teaching philosophy

### Principle 1: do not teach magical thinking

Students must be able to explain what OpenClaw is doing, what authority it has, and what assumptions make a design safe or unsafe.

### Principle 2: security is not a side unit

If a student can make something work but cannot explain trust boundaries, they are not demonstrating mastery.

### Principle 3: operational artifacts matter

Students should produce runbooks, risk reviews, and evidence logs, not only demos.

### Principle 4: release drift is normal

Students must be taught to verify current defaults and release notes, not to memorize frozen screenshots.

## Classroom operating rules

- do not let students expose gateways publicly unless that is part of a supervised security or deployment exercise
- prefer loopback plus SSH or Tailscale Serve for remote access labs
- keep real channels opt-in unless your institution is comfortable supporting them
- require students to document any dangerous flag, bypass, or widened authority
- require students to identify at least one failure mode for each production-facing design

## Safety and privacy policy

- never require students to share private provider keys in public chat or repositories
- separate student experimentation from any shared production OpenClaw deployment
- treat plugins, hook code, and externally sourced skills as untrusted until reviewed
- remind students that OpenClaw is not a hostile multi-tenant security boundary
- require prompt injection analysis for any workflow that consumes external content

## Grading model

### Recommended weights

- 20% concept checks and reading accountability
- 35% to 50% labs depending on the semester
- 15% to 20% design reviews
- 20% to 30% capstone and oral defense

### Minimum passing evidence

- successful completion of required labs
- demonstrated understanding of the trust model
- documented troubleshooting competence
- at least one defended production or security design
- one track-specific capstone artifact

## Teaching with the repository

### Required docs for every cohort

- [Program Overview](program-overview.md)
- [Prerequisite Bridge](prerequisite-bridge.md)
- [Submission Templates](templates/index.md)
- [Semester 1 Teaching Guide](semester-1/teaching-guide.md)
- [Semester 2 Teaching Guide](semester-2/teaching-guide.md)
- [Lab Guides](labs/core-lab-guides.md)
- [Advanced Lab Guides](labs/advanced-lab-guides.md)
- [Specialization Lab Guides](labs/specialization-lab-guides.md)
- [Model Artifacts](examples/index.md)
- [Question Bank](assessment/question-bank.md)
- [Practical Exams](assessment/practical-exams.md)
- [Oral Defense Bank](assessment/oral-defense-bank.md)
- [Assessor Calibration Guide](assessment/assessor-calibration-guide.md)
- [Grading Packet Templates](assessment/grading-packet-templates.md)
- [Answer Key Guidance](assessment/answer-key-guidance.md)
- [Feedback Bank](assessment/feedback-bank.md)
- [Track Evaluation Sheets](assessment/track-evaluation-sheets.md)
- [Track Rubrics](rubrics/track-rubrics.md)
- [Maintenance System](maintenance/index.md)

## Remediation policy

Students should repeat a lab or resubmit a design review if they:

- rely on insecure exposure without explanation
- cannot explain what tool authority exists
- ignore release drift in provider or security-sensitive work
- skip evidence and only submit screenshots
- fail to distinguish between baseline stable behavior and preview material

## Capstone management

- approve topics by mid-Semester 2
- require a milestone review before build week
- require written architecture and risk notes before demo day
- require oral defense even for strong build artifacts
- fail capstones that violate the trust model or ignore major security constraints

## Standalone readiness checklist

This pack is ready to teach when the instructor can answer yes to all of these:

- I can run the current required labs on the chosen environment lane
- I know which weekly modules depend on current release notes
- I know which real channels are allowed in my course
- I have a grading workflow for labs, reviews, and capstones
- I can articulate the OpenClaw trust model clearly to students
- I have reviewed the validation register and current official reading map
