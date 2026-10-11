---
name: plan
description: "Shortcut /plan (Organize). Use when the user types /plan or asks to build a short structured plan for a goal or project. Short, capped output (default 200 words) to save tokens."
---

# /plan

Shortcut · Organize · cap: 200 words

## Produce
Goal (1 line) / Milestones (3-5, with rough dates) / First 3 actions / Main risk. Nothing else.

Need the full, detailed deliverable instead? Use the `project-plan-from-brief` skill.

## Lean output rules
- No preamble, no restating the request, no closing recap or "let me know" line.
- Stay inside the length cap. If the user adds `long` or `full`, the cap doubles; `short` halves it.
- Ask at most one question, and only if you truly cannot start. Otherwise state one assumption and go.
- Work from what is already in the conversation or the named file. Don't re-read files you already have.
- Plain words, short sentences, bullets over paragraphs.
