---
name: checklist
description: "Shortcut /checklist (Organize). Use when the user types /checklist or asks to turn a task, process or document into an actionable checklist. Short, capped output (default 150 words) to save tokens."
---

# /checklist

Shortcut · Organize · cap: 150 words

## Produce
Markdown checkboxes (- [ ]), grouped under 2-4 short headings if needed, each item a concrete action.

Need the full, detailed deliverable instead? Use the `workflow-documentation` skill.

## Lean output rules
- No preamble, no restating the request, no closing recap or "let me know" line.
- Stay inside the length cap. If the user adds `long` or `full`, the cap doubles; `short` halves it.
- Ask at most one question, and only if you truly cannot start. Otherwise state one assumption and go.
- Work from what is already in the conversation or the named file. Don't re-read files you already have.
- Plain words, short sentences, bullets over paragraphs.
