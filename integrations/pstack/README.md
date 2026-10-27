# pstack integration

Upstream: https://github.com/no-session/pstack

pstack is a **separately installed Claude Code skill pack**. This repo does not vendor or fork its prompts and does not silently execute upstream setup scripts.

## Manual installation

Review the upstream README and installation script before executing. At the time this integration was drafted, upstream documents:

```bash
git clone --single-branch --depth 1 https://github.com/no-session/pstack.git ~/.claude/skills/pstack
cd ~/.claude/skills/pstack
./setup
```

Upstream lists Claude Code, Git and Bun 1.0+ as requirements. Check current upstream instructions on later installations; the above commands are documentation, **not executed by our setup.py**.

## Skill mapping

| Our workflow | Optional pstack tools |
| --- | --- |
| Grill and enhance | `/plan`, `/plan-eng-review`, `/plan-design-review` |
| Design variations | `/design-shotgun`, `/design-consultation` |
| Debug and second opinion | `/investigate`, `/codex` |
| Code review / QA | `/review`, `/qa-only`, `/cso`, `/benchmark` |

pstack's default shipping philosophy favors quick push-to-main. **Our workflow instead requires issue approval, isolated implementation, PR review and explicit merge gates.** Do not use `/ship` to bypass those gates.

pstack is not the orchestration engine and its skills do not automatically understand our markdown files. The agent must read the relevant workflow and explicitly invoke the skill when appropriate. Verify skill availability for the installed version.
