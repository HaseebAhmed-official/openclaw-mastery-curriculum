# Plugin Developer Answer Pack

## Target standard

This track should produce an extension that is not only functional, but also governable, schema-backed, and operationally understandable.

## Model capstone answer shape

1. Define the plugin purpose, capability boundary, and why a plugin is the right abstraction.
2. Present the manifest, bundle or distribution assumptions, and config surfaces.
3. Show schema-backed validation and compatibility reasoning.
4. Explain install, update, rollback, and support expectations.
5. Document risks from precedence, permissions, external services, or ecosystem dependency.

## Strong evidence bundle

- manifest with field rationale
- schema or config validation note
- install and update notes
- compatibility assumptions and version boundaries
- test or validation plan

## Strong-answer signals

- capability ownership is explicit
- config documentation is aligned with the manifest
- install/update behavior is treated as part of the design
- precedence or interoperability issues are considered early

## Weak-answer signals

- plugin works locally but no update or compatibility story exists
- manifest fields have no rationale
- schema validation omitted from a config-heavy plugin
- operational notes reduced to "run npm install"

## Oral defense prompts

- Why is this a plugin instead of a skill-only solution?
- What breaks first if the host OpenClaw version drifts?
- How would you review this plugin before allowing it in a serious deployment?
