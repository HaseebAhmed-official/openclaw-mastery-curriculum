# Upstream Review Playbook

## When to use this

Run this playbook when:

- the automated drift check reports a newer upstream release
- an advisory or security note affects curriculum content
- a major documentation change invalidates teaching assumptions

## Review sequence

### 1. Read the upstream release note first

Do not start rewriting curriculum files before understanding what actually changed.

Then review any new official security advisories published after the last baseline if the same review window includes security-sensitive changes.

### 2. Classify the change

- provider or model default change
- security hardening change
- installation or deployment change
- automation or tasking change
- plugin or skill ecosystem change
- contributor workflow change
- documentation clarity change only

### 3. Map the impact surface

Check at minimum:

- `curriculum/update-and-release-discipline.md`
- `curriculum/sources/official-reading-map.md`
- `curriculum/sources/validation-register.md`
- `curriculum/governance-and-security-strand.md`
- `curriculum/semester-1/index.md`
- `curriculum/semester-2/index.md`
- relevant lab guides
- relevant templates if operational assumptions changed

### 4. Decide the change level

- no curriculum change needed
- wording update only
- module update needed
- lab or rubric update needed
- major sequencing or policy review needed

### 5. Apply only necessary edits

Keep the patch targeted and evidence-backed.

### 6. Record the review

Update:

- `curriculum/maintenance/review-log.md`
- `curriculum/maintenance/upstream-state.json`

If advisories were part of the review window, update the advisory fields there as well.

## Special review triggers

### Provider or default model changes

Review:

- Semester 1 Week 10
- LAB-B4
- release-aware template guidance

### Security hardening changes

Review:

- governance and security strand
- Semester 2 Week 4 and Week 5
- security audit lab
- track rubrics where relevant

### Automation or detached-work changes

Review:

- automation and detached work guide
- Semester 2 Week 10 and Week 11
- advanced lab guides

### Plugin or ecosystem changes

Review:

- plugin developer track
- supply-chain teaching
- assessment guidance that references installation review
