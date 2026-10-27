# Workflow: UI design gate

**Trigger:** any proposed change affecting UI layout, visual design, copy hierarchy, or interaction. Do this before implementation.

1. Gather existing styling, components, design tokens, constraints and target breakpoints.
2. Generate **2–3 meaningfully distinct** alternatives. pstack `/design-shotgun` may help produce variants; `/design-consultation` can help establish a design direction.
3. Prefer inspectable HTML / React / Storybook previews when practical; screenshots/mockups are acceptable for early exploration. Do not treat a visual sketch as a tested application.
4. Provide a comparison: visual hierarchy, mobile/responsive behavior, accessibility, complexity, and tradeoffs.
5. Request explicit selection or revisions from the owner. **No implementation before selection.**
6. Persist selected option, screenshot/preview links and design decisions in the GitHub Issue; include stable references in the acceptance criteria.

Do not pick a winner on behalf of the owner. If the change is strictly non-visual (e.g. backend), skip this gate and record why.
