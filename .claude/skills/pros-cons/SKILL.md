---
name: pros-cons
description: "Shortcut /pros-cons (Thinking). Use when the user types /pros-cons or asks to see the advantages and risks of an option or decision. Short, capped output (default 150 words) to save tokens."
---

# /pros-cons

Shortcut · Thinking · cap: 150 words

## Produce
Two short lists (pros, cons/risks), max 4 each, strongest first. Then one line: the deciding factor.

Need the full, detailed deliverable instead? Use the `swot-analysis` skill.

## Lean output rules
- No preamble, no restating the request, no closing recap or "let me know" line.
- Stay inside the length cap. If the user adds `long` or `full`, the cap doubles; `short` halves it.
- Ask at most one question, and only if you truly cannot start. Otherwise state one assumption and go.
- Work from what is already in the conversation or the named file. Don't re-read files you already have.
- Plain words, short sentences, bullets over paragraphs.
