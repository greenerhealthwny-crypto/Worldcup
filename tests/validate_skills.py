"""Structural checks for the business prompt skills in .claude/skills.

Run: python3 tests/validate_skills.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / ".claude" / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
PLACEHOLDER_RE = re.compile(r"\[([A-Z][A-Z0-9 /_\-]*)\]")
OUTPUT_ONLY = {15: {"NAME", "SPECIFIC DETAIL"}}  # placeholders the output itself must contain

errors = []
numbers = {}


def err(path, msg):
    errors.append(f"{path.relative_to(ROOT.parent.parent)}: {msg}")


for skill_md in sorted(ROOT.glob("*/SKILL.md")):
    text = skill_md.read_text()
    m = re.match(r"^---\nname: (.+)\ndescription: \"?(.+?)\"?\n---\n", text)
    if not m:
        err(skill_md, "missing or malformed frontmatter")
        continue
    name, desc = m.groups()
    if name != skill_md.parent.name:
        err(skill_md, f"name '{name}' does not match folder")
    if not NAME_RE.match(name) or len(name) > 64:
        err(skill_md, f"invalid name '{name}'")
    if len(desc) > 1024:
        err(skill_md, f"description too long ({len(desc)})")

    num_m = re.search(r"^Business prompt #(\d+) · ", text, re.M)
    if not num_m:
        continue  # not one of the business prompt skills (e.g. new-marketing)
    num = int(num_m.group(1))
    if num in numbers:
        err(skill_md, f"duplicate prompt #{num} (also {numbers[num]})")
    numbers[num] = name

    for section in ("## The prompt", "## Inputs to collect", "## How to run it",
                    "## Deliverable checklist", "## Quality rules"):
        if section not in text:
            err(skill_md, f"missing section '{section}'")

    prompt_m = re.search(r"## The prompt\n\n> (.+)\n", text)
    if not prompt_m:
        err(skill_md, "prompt text not found")
        continue
    inputs = text.split("## Inputs to collect", 1)[1].split("## How to run it", 1)[0]
    for ph in set(PLACEHOLDER_RE.findall(prompt_m.group(1))) - OUTPUT_ONLY.get(num, set()):
        if f"`[{ph}]`" not in inputs:
            err(skill_md, f"placeholder [{ph}] not listed under inputs")

    checklist = text.split("## Deliverable checklist", 1)[1].split("## Quality rules", 1)[0]
    if checklist.count("- [ ] ") < 1:
        err(skill_md, "empty deliverable checklist")

missing = sorted(set(range(1, 101)) - set(numbers))
if missing:
    errors.append(f"missing prompt numbers: {missing}")

index = (ROOT / "BUSINESS-PROMPTS.md").read_text()
for link in re.findall(r"\]\(([^)]+/SKILL\.md)\)", index):
    if not (ROOT / link).exists():
        errors.append(f"BUSINESS-PROMPTS.md: broken link {link}")
if len(re.findall(r"^\| \d+ \|", index, re.M)) != 100:
    errors.append("BUSINESS-PROMPTS.md: expected 100 rows")

if errors:
    print("\n".join(errors))
    print(f"FAIL: {len(errors)} problem(s)")
    sys.exit(1)
print(f"OK: {len(numbers)} business prompt skills valid")
