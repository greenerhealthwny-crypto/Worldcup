"""Check docs/agent-status.json (the Agent Roster's data) before it is synced to the page.

Usage: python3 tools/agents/check_status.py
Exits 1 with a list of problems if the file is unreadable, malformed, or out of step
with the agents in .claude/agents/.
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
STATUS_FILE = REPO / "docs" / "agent-status.json"
AGENTS_DIR = REPO / ".claude" / "agents"
REQUIRED = ["num", "name", "title", "does", "greatFor", "status", "reason", "nextStep", "connectors", "prompt", "lastTested"]
STATUSES = {"active", "needs_work"}


def load_rows(path):
    """Return the list of agent rows, or raise ValueError with a readable message."""
    try:
        rows = json.loads(path.read_text())
    except OSError as e:
        raise ValueError(f"cannot read {path.name}: {e}")
    except json.JSONDecodeError as e:
        raise ValueError(f"{path.name} is not valid JSON: {e}")
    if not isinstance(rows, list):
        raise ValueError(f"{path.name} must be a list of agents")
    return rows


def find_problems(rows, agent_names):
    problems = []
    seen = set()
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            problems.append(f"row {i}: not an object")
            continue
        name = row.get("name", f"row {i}")
        missing = [k for k in REQUIRED if k not in row]
        if missing:
            problems.append(f"{name}: missing {missing}")
        if row.get("status") not in STATUSES:
            problems.append(f"{name}: status must be one of {sorted(STATUSES)}")
        if row.get("status") == "needs_work" and not row.get("nextStep"):
            problems.append(f"{name}: needs_work but no nextStep")
        if name not in agent_names:
            problems.append(f"{name}: no matching agent file in .claude/agents/")
        if name in seen:
            problems.append(f"{name}: listed twice")
        seen.add(name)
    for missing_agent in sorted(agent_names - seen):
        problems.append(f"{missing_agent}: agent has no row in {STATUS_FILE.name}")
    return problems


def main():
    try:
        agent_names = {f.stem for f in AGENTS_DIR.glob("*.md")}
        rows = load_rows(STATUS_FILE)
    except (OSError, ValueError) as e:
        sys.exit(f"FAIL: {e}")
    problems = find_problems(rows, agent_names)
    if problems:
        print("\n".join(problems))
        sys.exit(f"FAIL: {len(problems)} problem(s)")
    active = sum(r["status"] == "active" for r in rows)
    print(f"OK: {len(rows)} agents in roster ({active} active, {len(rows) - active} need work)")


if __name__ == "__main__":
    main()
