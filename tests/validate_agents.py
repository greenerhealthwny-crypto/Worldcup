"""Structural checks for the 12 AI agents in .claude/agents.

Run: python3 tests/validate_agents.py
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
AGENTS = REPO / ".claude" / "agents"
SKILLS = REPO / ".claude" / "skills"
MEMORY = REPO / ".claude" / "agent-memory"
KNOWN_TOOLS = {"Read", "Write", "Edit", "Glob", "Grep", "Bash", "WebSearch", "WebFetch", "Skill"}
REQUIRED_SECTIONS = ["## 1. Role and goal", "## 2. Workflow", "## 3. Output", "## 4. Tools and skills",
                     "## 5. Memory", "## 6. Safety rules", "## 7. Quality check"]

errors = []
seen = set()

for f in sorted(AGENTS.glob("*.md")):
    rel = f.relative_to(REPO)
    try:
        text = f.read_text()
    except (OSError, UnicodeDecodeError) as e:
        errors.append(f"{rel}: cannot read file: {e}")
        continue
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        errors.append(f"{rel}: missing frontmatter")
        continue
    fm = m.group(1)
    name = re.search(r"^name: (.+)$", fm, re.M)
    desc = re.search(r"^description: \"?(.+?)\"?$", fm, re.M)
    if not name or name.group(1) != f.stem:
        errors.append(f"{rel}: name must match file name")
    if not desc or "Use proactively whenever" not in desc.group(1):
        errors.append(f"{rel}: description needs a 'Use proactively whenever...' trigger")
    if "memory: project" not in fm:
        errors.append(f"{rel}: memory: project not set")
    if not (MEMORY / f.stem / "MEMORY.md").exists():
        errors.append(f"{rel}: memory file .claude/agent-memory/{f.stem}/MEMORY.md missing")
    tools = re.search(r"^tools: (.+)$", fm, re.M)
    if tools:
        unknown = {t.strip() for t in tools.group(1).split(",")} - KNOWN_TOOLS
        if unknown:
            errors.append(f"{rel}: unknown tools {sorted(unknown)}")
    for skill in re.findall(r"^- ([a-z0-9-]+)$", fm, re.M):
        if not (SKILLS / skill / "SKILL.md").exists():
            errors.append(f"{rel}: preloaded skill '{skill}' does not exist")
    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"{rel}: missing section '{section}'")
    if not re.search(r"(?i)ask before|without (explicit )?approval|needs your ok", text):
        errors.append(f"{rel}: no human-approval rule")
    num = re.search(r"AI agent #(\d+)", text)
    if num:
        seen.add(int(num.group(1)))

if seen != set(range(1, 13)):
    errors.append(f"expected agents #1-12, found {sorted(seen)}")

try:
    claude_md = (REPO / "CLAUDE.md").read_text()
    for f in AGENTS.glob("*.md"):
        if f"`{f.stem}`" not in claude_md:
            errors.append(f"CLAUDE.md: agent {f.stem} not in routing table")
except OSError as e:
    errors.append(f"cannot read CLAUDE.md: {e}")

if errors:
    print("\n".join(errors))
    print(f"FAIL: {len(errors)} problem(s)")
    sys.exit(1)
print(f"OK: {len(seen)} agents valid")
