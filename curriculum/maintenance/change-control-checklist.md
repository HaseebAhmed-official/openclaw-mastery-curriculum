# Change Control Checklist

## Before editing

- identify the exact upstream source
- identify whether new official advisories are part of the review window
- identify whether the change is stable, preview, or draft
- identify which curriculum files are affected

## During editing

- keep edits narrow
- preserve the trust model
- preserve stable-vs-preview labeling
- update release-aware language where needed

## Before merging

- confirm the affected files now match the upstream change
- confirm no unrelated files drifted
- confirm examples, templates, and grading guidance still make sense
- update the review log
- update `upstream-state.json`

## If the change is large

- note whether a revalidation pass is needed
- update the README if the repository surface changed materially
- check whether instructors need a teaching note for the next cohort
