"""Generate the 25 shortcut skills (sections 1-5 of "30 Claude Shortcut Hacks").

Each shortcut is a tiny SKILL.md with a hard default length cap, so a slash command
costs fewer output tokens than a free-form request. Edit SHORTCUTS below and re-run:

    python3 tools/shortcuts/generate.py
"""
import sys
from pathlib import Path

SKILLS = Path(__file__).resolve().parent.parent.parent / ".claude" / "skills"

# Shared rules every shortcut follows. Kept short on purpose: this text is loaded each call.
LEAN = """## Lean output rules
- No preamble, no restating the request, no closing recap or "let me know" line.
- Stay inside the length cap. If the user adds `long` or `full`, the cap doubles; `short` halves it.
- Ask at most one question, and only if you truly cannot start. Otherwise state one assumption and go.
- Work from what is already in the conversation or the named file. Don't re-read files you already have.
- Plain words, short sentences, bullets over paragraphs."""

# (name, section, trigger description, what to produce, cap, related full skill or "")
SHORTCUTS = [
    # 1. Understand Information Faster
    ("tldr", "Understand", "summarize text, a file, a book, a PDF or a thread into key points",
     "A one-line bottom line, then the 3-5 key points as bullets. For a book or long PDF: add one line per chapter only if asked.",
     "120 words", ""),
    ("eli5", "Understand", "explain something in very simple words, as if to a 5-year-old or a beginner",
     "One plain analogy, then the idea in 3-4 short sentences. No jargon; if a term is unavoidable, define it in five words.",
     "100 words", ""),
    ("deep-dive", "Understand", "get a detailed, structured breakdown of a topic, file or idea",
     "Sections: What it is / How it works / Why it matters / Limits / Next step. Bullets under each. Cite file:line or source when making factual claims.",
     "400 words", ""),
    ("compare", "Understand", "compare two (or a few) things, tools, options or versions",
     "One table: rows = the 4-6 criteria that actually differ, columns = the options. Then one line: which to pick and when.",
     "180 words", "vendor-comparison"),
    ("examples", "Understand", "learn a concept through concrete examples",
     "3 examples, simple to advanced, each 1-2 lines, plus one line on the pattern they share.",
     "150 words", ""),
    # 2. Improve Your Thinking
    ("step-by-step", "Thinking", "break a task or goal into ordered steps",
     "Numbered steps, each starting with a verb, each doable in one sitting. Mark the one step to do first.",
     "150 words", ""),
    ("pros-cons", "Thinking", "see the advantages and risks of an option or decision",
     "Two short lists (pros, cons/risks), max 4 each, strongest first. Then one line: the deciding factor.",
     "150 words", "swot-analysis"),
    ("pitfalls", "Thinking", "find the common mistakes or traps in a plan, task or draft",
     "The top 5 pitfalls, each as: mistake -> how to avoid it (one line each). Most likely first.",
     "150 words", "project-risk-assessment"),
    ("challenge", "Thinking", "challenge assumptions, play devil's advocate or stress-test an idea",
     "List the 3-4 assumptions the idea rests on. For each: why it might be wrong + a cheap way to test it. End with the single riskiest one.",
     "200 words", "business-model-stress-test"),
    ("root-cause", "Thinking", "find the real underlying problem behind a symptom or recurring issue",
     "5-Whys chain (stop when you hit something actionable), then: Root cause / Fix / How to confirm it worked.",
     "180 words", "error-log-analysis"),
    # 3. Create Better Content
    ("hooks", "Content", "generate scroll-stopping hooks, headlines or opening lines",
     "10 hooks, one line each, mixed types (question, number, bold claim, story, contrarian). Star the best 2.",
     "150 words", ""),
    ("humanize", "Content", "make text sound natural and human, less like AI or a corporate template",
     "Return only the rewritten text. Use contractions, plain verbs, varied sentence length. Cut filler like 'leverage', 'delve', 'I hope this finds you well'. Keep the meaning and length.",
     "same length as input", ""),
    ("rewrite", "Content", "improve the clarity and flow of a draft",
     "Return only the improved text, then at most 3 bullets on what changed and why.",
     "input length + 40 words", ""),
    ("tone", "Content", "change the tone or style of text (e.g. friendlier, more formal, punchier)",
     "Return only the text in the requested tone. If no tone named, give two short versions: warmer and more direct.",
     "same length as input", ""),
    ("repurpose", "Content", "turn one idea, post or article into several formats",
     "Short versions for: social post, email blurb, short-video script (3 beats), and a headline. Label each.",
     "300 words", "repurpose-article-five-formats"),
    # 4. Work Smarter & Stay Organized
    ("checklist", "Organize", "turn a task, process or document into an actionable checklist",
     "Markdown checkboxes (- [ ]), grouped under 2-4 short headings if needed, each item a concrete action.",
     "150 words", "workflow-documentation"),
    ("prioritize", "Organize", "organize a list of tasks or ideas by importance",
     "Three groups: Do now / Schedule / Drop or delegate. One-line reason per item only if it isn't obvious.",
     "150 words", "weekly-priorities-from-brain-dump"),
    ("action-items", "Organize", "extract next steps or action items from notes, a chat or a document",
     "Table: Action / Owner / Due. Use '?' where unknown; never invent owners or dates. Then any open questions as bullets.",
     "150 words", "meeting-notes-action-items"),
    ("template", "Organize", "create a reusable template, form, or SKILL.md from an example or process",
     "The template only, with [PLACEHOLDERS] in caps. If the user wants a Claude skill, output a SKILL.md with name/description frontmatter, Inputs, Steps, Checklist; keep it under 60 lines.",
     "250 words", ""),
    ("plan", "Organize", "build a short structured plan for a goal or project",
     "Goal (1 line) / Milestones (3-5, with rough dates) / First 3 actions / Main risk. Nothing else.",
     "200 words", "project-plan-from-brief"),
    # 5. Coding & Technical Productivity
    ("debug", "Code", "find and fix an error, bug or failing command",
     "Cause (1-2 lines, cite file:line) / Fix (minimal diff or command) / How to verify. Apply the fix if the code is in the repo.",
     "200 words + code", ""),
    ("explain-code", "Code", "understand what a piece of code, file or script does",
     "One-line purpose, then the flow as 3-6 numbered steps citing file:line. Flag anything surprising.",
     "200 words", ""),
    ("optimize", "Code", "improve the performance or efficiency of code, a query, a prompt or a workflow",
     "Top 3 changes ranked by impact, each: what / why / expected gain. Apply the top one if asked or obvious.",
     "200 words + code", ""),
    ("test-cases", "Code", "generate test scenarios or test cases",
     "Table: Case / Input / Expected. Cover happy path, edge cases and one failure case. Write runnable tests only if the user asks.",
     "200 words", ""),
    ("document", "Code", "create clear documentation for code, a tool, a skill or a process",
     "README-style: What it does / How to use (example) / Inputs-outputs / Gotchas. Match the repo's existing doc style.",
     "300 words", ""),
]


def render(name, section, trigger, produce, cap, related):
    desc = (f"Shortcut /{name} ({section}). Use when the user types /{name} or asks to {trigger}. "
            f"Short, capped output (default {cap}) to save tokens.")
    full = (f"\n\nNeed the full, detailed deliverable instead? Use the `{related}` skill."
            if related else "")
    return f"""---
name: {name}
description: "{desc}"
---

# /{name}

Shortcut · {section} · cap: {cap}

## Produce
{produce}{full}

{LEAN}
"""


def main():
    names = [s[0] for s in SHORTCUTS]
    if len(names) != len(set(names)):
        sys.exit("duplicate shortcut names")
    for s in SHORTCUTS:
        path = SKILLS / s[0] / "SKILL.md"
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(render(*s))
        except OSError as e:
            sys.exit(f"could not write {path}: {e}")
    print(f"wrote {len(SHORTCUTS)} shortcut skills to {SKILLS}")


if __name__ == "__main__":
    main()
