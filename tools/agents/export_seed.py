"""Write one JSON file per agent from docs/agent-status.json, ready to load into the
Agent Roster page's `agents` collection (ArtifactData batch with file_path).

Usage: python3 tools/agents/export_seed.py <output-dir>
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_status  # noqa: E402


def export_rows(rows, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for row in rows:
        path = out_dir / f"{row['name']}.json"
        path.write_text(json.dumps(row, indent=1))
        written.append(path)
    return written


def main(argv):
    if len(argv) != 1:
        sys.exit(__doc__)
    try:
        rows = check_status.load_rows(check_status.STATUS_FILE)
    except ValueError as e:
        sys.exit(f"FAIL: {e}")
    problems = check_status.find_problems(rows, {f.stem for f in check_status.AGENTS_DIR.glob("*.md")})
    if problems:
        sys.exit("FAIL: fix the roster first:\n" + "\n".join(problems))
    try:
        written = export_rows(rows, Path(argv[0]))
    except OSError as e:
        sys.exit(f"FAIL: could not write seed files: {e}")
    print(f"Wrote {len(written)} files to {argv[0]}")


if __name__ == "__main__":
    main(sys.argv[1:])
