"""Regenerate the 100 business prompt skills.

Usage: python3 tools/business-prompts/generate.py tools/business-prompts/prompts.txt .claude/skills
Edit prompts.txt (prompt text + checklist) or when.txt (trigger phrase), then rerun.
"""
import re, sys, pathlib

src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])

CATS = [
    ("Content & Copywriting", "content-copywriting",
     ["Write in plain, specific language. Cut filler, clichés and hype words.",
      "Match the voice of any source material the user provides. When there is none, use a direct, human tone.",
      "Respect every word, length and count limit exactly, and check them before you deliver."]),
    ("Customer Support & Comms", "customer-support-comms",
     ["Sound like a real person on the team, not a policy document. No corporate language.",
      "Acknowledge feelings without grovelling. Don't promise anything the business can't deliver. If a refund, credit or policy is involved and you don't know the rules, mark it as [CONFIRM] instead of inventing them.",
      "Keep messages short enough to read on a phone."]),
    ("Operations & Project Management", "operations-project-management",
     ["Make every output something the user can act on today: owners, dates, next steps.",
      "When the input is missing information (owners, deadlines, scope), flag it clearly rather than guessing silently.",
      "Use tables or numbered lists where they make the plan easier to scan."]),
    ("Sales & Revenue", "sales-revenue",
     ["Lead with the buyer's problem and outcomes, not product features.",
      "Use the prospect's own words whenever notes or context are provided.",
      "Every asset ends with a clear, low-friction next step. Never invent pricing, discounts or testimonials. Use [PLACEHOLDER] instead."]),
    ("Research & Analysis", "research-analysis",
     ["Be specific to the user's business. Never write points that could apply to any company.",
      "Separate what the data shows from what you're inferring. Label estimates and assumptions.",
      "Don't fabricate statistics, market sizes, competitor facts or sources. If you lack live data, say so, give ranges or a method, and list what the user should verify. Use web search if it is available and the task depends on current facts."]),
    ("Systems & Automation", "systems-automation",
     ["Be concrete: exact tool names, field types, triggers and steps that someone can build from directly.",
      "Call out platform limits, costs and failure points honestly. Tag anything about a tool's current features that you haven't checked as something to confirm.",
      "Prefer the simplest setup that does the job. Explain why you structured it that way."]),
    ("Finance & Admin", "finance-admin",
     ["Show your arithmetic and state your assumptions. Double-check totals.",
      "Use plain English. Explain what the numbers mean, not just what they are.",
      "For legal, tax or contract matters, flag issues and questions, add a short note that this isn't legal or financial advice, and suggest when to involve a professional."]),
    ("Hiring & Talent", "hiring-talent",
     ["Be specific about the role and honest about what it really involves.",
      "Keep language inclusive and fair. Avoid requirements or questions that could be discriminatory (age, family status, health, etc.).",
      "Write like a thoughtful manager talking to a person, not HR boilerplate."]),
    ("Marketing & Growth", "marketing-growth",
     ["Tie every recommendation to the target customer and to one measurable goal.",
      "Be concrete: channels, cadence, numbers and examples, not abstract advice.",
      "Don't invent performance benchmarks or audience data. Label estimates and say how to validate them."]),
    ("Product & Strategy", "product-strategy",
     ["Be honest and direct, even when the answer is uncomfortable. The user is asking for judgment, not cheerleading.",
      "Ground conclusions in the data or description provided, and name the assumptions you're making.",
      "End with a clear recommendation or the one thing to do next."]),
]

OUTPUT_ONLY = {15: {"NAME", "SPECIFIC DETAIL"}}  # placeholders that belong in the output, not inputs

WHEN = {int(a): b for a, b in (l.split('|', 1) for l in (src.parent / 'when.txt').read_text().splitlines() if l)}
text = src.read_text()
entries = [b for b in text.strip().split("\n\n") if b.strip()]
assert len(entries) == 100, len(entries)

index_rows = []
for block in entries:
    lines = block.strip().splitlines()
    num, slug, title = [x.strip() for x in lines[0].split("|")]
    num = int(num)
    prompt = next(l[3:] for l in lines if l.startswith("P: "))
    checks = [c.strip() for c in next(l[3:] for l in lines if l.startswith("C: ")).split(";")]
    cat_name, cat_slug, rules = CATS[(num - 1) // 10]
    phs = []
    for p in re.findall(r"\[([A-Z][A-Z0-9 /_\-]*)\]", prompt):
        if p not in phs and p not in OUTPUT_ONLY.get(num, set()):
            phs.append(p)

    lower_title = title[0].lower() + title[1:]
    delivers = "; ".join(checks)
    if len(delivers) > 260:
        delivers = delivers[:260].rsplit(";", 1)[0]
    desc = (f"Use whenever the user wants to {WHEN[num]}, even if they don't name this skill. "
            f"Business prompt #{num} ({title}, {cat_name}). Delivers: {delivers}.")
    desc = desc.replace('"', "'")
    assert len(desc) <= 1024, (num, len(desc))

    def label(p):
        special = {"DESCRIBE IN PLAIN ENGLISH": "Process to automate (plain English)", "TYPE": "Influencer type", "PASTE": "Pasted description", "DESCRIBE": "Description",
                   "ICP": "Ideal customer profile (ICP)", "PASTE JD": "Job description (pasted)"}
        if p in special: return special[p]
        s = p.replace("_", " ")
        for verb, suffix in (("PASTE ", " (pasted)"), ("DESCRIBE ", " (described)"), ("LIST ", " (list)")):
            if s.startswith(verb):
                s = s[len(verb):]; break
        else:
            suffix = ""
        s = s.capitalize().replace("Icp", "ICP")
        return s + suffix
    inputs = "\n".join(f"- **{label(p)}** (`[{p}]`)" for p in phs) \
        or "- None required. Ask about the business or audience only if it would clearly improve the result."
    checklist = "\n".join(f"- [ ] {c}" for c in checks)
    rules_md = "\n".join(f"- {r}" for r in rules)

    body = f"""---
name: {slug}
description: "{desc}"
---

# {title}

Business prompt #{num} · {cat_name}

## The prompt

> {prompt}

## Inputs to collect

{inputs}

Use whatever the user has already given you (in the message, attached files or earlier in the conversation). If something essential is missing, ask for all missing inputs in one short message. If the user wants you to go ahead anyway, fill the gaps with reasonable assumptions and list them at the top of your answer.

## How to run it

1. Fill the placeholders above with the user's details and treat the completed prompt as the brief.
2. Produce the deliverable directly. No preamble about what you're going to do.
3. Check the result against the checklist below and fix anything that misses before you reply.
4. Finish with at most one short line offering a sensible next step (a variation, a tighter version, or a related prompt).

## Deliverable checklist

{checklist}

## Quality rules ({cat_name})

{rules_md}
"""
    d = out / slug
    d.mkdir(parents=True, exist_ok=True)
    (d / "SKILL.md").write_text(body)
    index_rows.append((num, cat_name, title, slug))

# Index
md = ["# Business Prompt Skills", "",
      "100 skills, one per prompt from the \"100 business workflow prompts\" series (@ChrisKE), in 10 categories.",
      "Each skill is in `.claude/skills/<name>/SKILL.md` and contains the original prompt, the inputs to collect, a deliverable checklist and quality rules.",
      "", "Invoke one by name (for example `/cold-email-replies`) or just describe the task and Claude will pick the matching skill.", ""]
cur = None
for num, cat, title, slug in index_rows:
    if cat != cur:
        md += ["", f"## {cat}", "", "| # | Skill | Name |", "|---|---|---|"]
        cur = cat
    md.append(f"| {num} | {title} | [`{slug}`]({slug}/SKILL.md) |")
(out / "BUSINESS-PROMPTS.md").write_text("\n".join(md) + "\n")
print("ok", len(index_rows))
