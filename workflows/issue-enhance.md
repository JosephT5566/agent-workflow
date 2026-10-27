# Workflow: capture → grill → enhance → approved issue

**Goal:** turn a loosely described idea into a standalone GitHub Issue that an independent coding agent can execute later.

1. **Capture.** Create a raw issue using `templates/issue-idea.md`. Do not start implementation.
2. **Grill.** Use Claude and (where helpful) pstack `/plan` or `/plan-eng-review` to challenge assumptions. Ask focused questions about goals, users, boundaries, unknowns, risks, alternatives, and tradeoffs. Avoid unnecessary questions that do not affect the implementation.
3. **Enhance.** Rewrite the issue with objective, current context, acceptance criteria, out-of-scope items, approach, dependencies, affected files/interfaces, test expectations, and a decision log. Link reference documents. Never paste secrets or private conversation history.
4. **UI branch.** If behavior or appearance of any UI changes, run [UI design](ui-design.md) *before* approval.
5. **Approval.** Show the final spec and uncertainties to the owner. Mark approved only with explicit confirmation. Record the approved scope and selected design reference in the issue.
6. **Handoff.** Link the approved issue in the implementation task. A new session must be able to understand and execute it without seeing the planning chat.

**Statuses (conceptual):** raw → enhancing → needs-info/design-review → approved → implementing → in-review → done.

Use one coherent status at a time (for example, a GitHub Project Status field). Status labels are not a concurrency lock. If multiple devices autonomously claim issues, introduce a real lease/claim mechanism.

## Approval checklist

- [ ] Objective, user value and boundaries are clear
- [ ] Acceptance criteria are observable
- [ ] Dependencies and potential overlapping work are recorded
- [ ] Risks / security / migrations are identified
- [ ] Tests and verification are specified
- [ ] UI mockups selected by owner, if applicable
- [ ] Owner explicitly approves scope
