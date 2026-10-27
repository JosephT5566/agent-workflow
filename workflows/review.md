# Workflow: review → merge

1. Review PR diff independently of the implementing session. pstack `/review`, `/cso`, `/qa-only`, or `/codex` can provide specialized checks; run only those appropriate to the change.
2. Validate acceptance criteria, tests, failure paths, security, migration safety and changed file scope.
3. Require the human owner to approve **auth, payments, secrets, permissions, infrastructure, database migrations, CI/workflow files, and major UX or architecture changes**.
4. Default to human merge. Do not invoke pstack's fast push-to-main shipping behavior for this PR-based workflow.
5. Low-risk auto-merge is **opt-in and not configured by default**. A future docs-only automation must verify every changed path against an allowlist, reject symlinks and executable/config changes, require green checks and enforce branch protections. If unsure, stop and require human review.
6. After merge, update/close the issue and document any follow-ups.

A policy document does not enforce GitHub permissions. Until branch protection and actual CI enforcement exist, do not claim automatic merge is safe or enabled.
