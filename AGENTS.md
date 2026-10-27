# Instructions for agents working on this repository

This is a **lightweight personal agent workflow**. Do not build a CLI framework, daemon, database, notification service, or bespoke agent orchestrator unless explicitly requested.

## Before changes

1. Read `README.md`, the relevant file in `workflows/`, and `integrations/pstack/README.md` if using pstack.
2. Inspect existing user configuration before proposing setup changes.
3. Keep definitions reusable across projects, but put project-specific instructions in the project's own repository.
4. Preserve unrelated files and avoid copying pstack prompts into this repository.
5. Never add credentials, session transcripts, local worktrees, or machine-specific paths to commits.

## Installation / maintenance

- Run `python3 setup.py doctor` to check prerequisites.
- Run `python3 setup.py global` only after checking what will be linked.
- Run `python3 setup.py project --path <repo>` to create missing project templates; existing files must be left unchanged.
- pstack installation is a separate **explicit** step using documented upstream instructions. Never download and execute an unreviewed installer automatically.
- Global skills are symlinked to this checkout; after `git pull`, newly started sessions can read updated content. Re-run setup when new skills are added.
- If installation is blocked by a conflicting file, report it and ask the user how to proceed rather than overwriting.

## Workflow contract

- Capture ideas as raw issues; do not treat them as immediate implementation orders.
- Claude/pstack may grill and enhance specifications, but decisions must be persisted in GitHub Issues.
- Before any UI implementation, present 2–3 distinct mockups with tradeoffs and obtain the user's selection.
- An implementation session must start with a complete approved issue. If incomplete, return it to clarification.
- Use distinct worktrees/branches for parallel implementation. Avoid simultaneous edits to the same critical files.
- Never merge a critical-path PR without the owner's explicit approval.
- Docs-only auto-merge is an optional future integration; do not assume it is active just because a policy file exists.

## Safe completion

Summarize files changed, validations executed, approvals pending, and any limitation. Do not claim a test, installation, or approval occurred unless verified.
