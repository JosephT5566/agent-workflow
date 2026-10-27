# Workflow: implement from approved issue

**Precondition:** a complete, owner-approved GitHub Issue. Planning sessions do not have to remain active.

1. Read the approved issue, acceptance criteria, decision log, design selection, project `AGENTS.md` / `CLAUDE.md`, and tests.
2. If the issue is ambiguous or changed substantially since approval, stop and request clarification. Do not invent product decisions.
3. Check dependencies and overlapping tasks. Create a dedicated branch and preferably a Git worktree; avoid shared edits with parallel workers.
4. Implement only the agreed scope. A new child session may use Codex or Claude; pstack provides optional review / investigation skills, not a required runtime.
5. Run the project-prescribed lint, type checking, tests, and build; collect actual results.
6. Open a PR referencing the issue, with summary, tests, screenshots for UI work, risks and follow-ups.
7. Hand off to an independent review session using [review workflow](review.md); record status in GitHub.

**Parallelism:** approved issues may run concurrently if dependencies and file ownership allow. Separate worktrees are not a substitute for dependency coordination.

**Recovery:** store durable decisions in GitHub, not only chat. A failed session should leave its branch/worktree and a concise status note so another session can resume.
