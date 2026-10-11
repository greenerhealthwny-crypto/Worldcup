"""Change one agent's row in docs/agent-status.json (the Agent Roster's data).

Usage:
  python3 tools/agents/update_status.py <agent-name> status=active reason="..." nextStep=""
Only the fields you pass change. The result is checked with check_status.py and is
written only if it passes, through a temp file so a failed write never leaves a half file.
"""
import json
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_status  # noqa: E402


def write_rows_atomically(path, rows):
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=".agent-status-", suffix=".json")
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(rows, f, indent=2)
            f.write("\n")
        os.replace(tmp, path)
    except OSError:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def main(argv):
    if len(argv) < 2 or any("=" not in a for a in argv[1:]):
        sys.exit(__doc__)
    name, changes = argv[0], dict(a.split("=", 1) for a in argv[1:])
    unknown = set(changes) - set(check_status.REQUIRED)
    if unknown:
        sys.exit(f"FAIL: unknown field(s) {sorted(unknown)}; allowed: {check_status.REQUIRED}")
    try:
        rows = check_status.load_rows(check_status.STATUS_FILE)
    except ValueError as e:
        sys.exit(f"FAIL: {e}")
    row = next((r for r in rows if isinstance(r, dict) and r.get("name") == name), None)
    if row is None:
        sys.exit(f"FAIL: no agent named {name!r} in {check_status.STATUS_FILE.name}")
    row.update(changes)
    problems = check_status.find_problems(rows, {f.stem for f in check_status.AGENTS_DIR.glob("*.md")})
    if problems:
        sys.exit("FAIL: not saved, the change would break the roster:\n" + "\n".join(problems))
    try:
        write_rows_atomically(check_status.STATUS_FILE, rows)
    except OSError as e:
        sys.exit(f"FAIL: could not save {check_status.STATUS_FILE.name}: {e}")
    print(f"Saved {name}: " + ", ".join(f"{k}={v!r}" for k, v in changes.items()))


if __name__ == "__main__":
    main(sys.argv[1:])
