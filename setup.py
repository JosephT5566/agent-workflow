#!/usr/bin/env python3
"""Small, safe installer for the personal agent-workflow repository.

No external Python dependencies. No automatic upstream downloads.
"""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parent
SKILLS = ROOT / "skills"
GLOBAL_SKILLS = Path.home() / ".agents" / "skills"
PROJECT_FILES = {
    ".agents/project.yaml": ROOT / "templates" / "project-config.yaml",
    ".github/ISSUE_TEMPLATE/idea.md": ROOT / "templates" / "issue-idea.md",
    ".github/ISSUE_TEMPLATE/implementation.md": ROOT / "templates" / "issue-implementation.md",
}


def doctor() -> int:
    print("Agent Workflow environment checks")
    for command in ("git", "gh", "claude", "codex", "bun"):
        location = shutil.which(command)
        print(f"  {command}: {location or 'not found (optional except git)'}")
    pstack = Path.home() / ".claude" / "skills" / "pstack"
    print(f"  pstack: {'found' if pstack.is_dir() else 'not installed'} ({pstack})")
    print(f"  global skills target: {GLOBAL_SKILLS}")
    print("  Note: pstack must be installed separately using upstream instructions.")
    return 0


def global_setup() -> int:
    if not SKILLS.is_dir():
        print("No skills directory found; nothing to install.", file=sys.stderr)
        return 1
    GLOBAL_SKILLS.mkdir(parents=True, exist_ok=True)
    conflicts = []
    for skill in sorted(p for p in SKILLS.iterdir() if p.is_dir() and (p / "SKILL.md").exists()):
        target = GLOBAL_SKILLS / skill.name
        if target.is_symlink() and target.resolve() == skill.resolve():
            print(f"OK already linked: {target}")
        elif target.exists() or target.is_symlink():
            print(f"CONFLICT, not overwritten: {target}")
            conflicts.append(str(target))
        else:
            target.symlink_to(skill.resolve(), target_is_directory=True)
            print(f"Linked {target} -> {skill.resolve()}")
    print("Restart your agent session to ensure updated instructions are loaded.")
    return 1 if conflicts else 0


def project_setup(path: Path) -> int:
    project = path.expanduser().resolve()
    if not project.is_dir() or not (project / ".git").exists():
        # Support git worktrees, whose .git may be a file.
        print(f"Not a local Git project: {project}", file=sys.stderr)
        return 1
    for name, template in PROJECT_FILES.items():
        target = project / name
        if target.exists() or target.is_symlink():
            print(f"Unchanged existing file: {target}")
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(template.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"Created {target}")
    print("Review generated configuration and merge project-specific AGENTS.md / CLAUDE.md manually.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("doctor", "global", "project"))
    parser.add_argument("--path", default=".", help="Git repository path for project setup")
    args = parser.parse_args()
    if args.command == "doctor":
        return doctor()
    if args.command == "global":
        return global_setup()
    return project_setup(Path(args.path))


if __name__ == "__main__":
    raise SystemExit(main())
