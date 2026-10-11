---
name: compare
description: "Shortcut /compare (Understand). Use when the user types /compare or asks to compare two (or a few) things, tools, options or versions. Short, capped output (default 180 words) to save tokens."
---

# /compare

Shortcut · Understand · cap: 180 words

## Produce
One table: rows = the 4-6 criteria that actually differ, columns = the options. Then one line: which to pick and when.

Need the full, detailed deliverable instead? Use the `vendor-comparison` skill.

## Lean output rules
- No preamble, no restating the request, no closing recap or "let me know" line.
- Stay inside the length cap. If the user adds `long` or `full`, the cap doubles; `short` halves it.
- Ask at most one question, and only if you truly cannot start. Otherwise state one assumption and go.
- Work from what is already in the conversation or the named file. Don't re-read files you already have.
- Plain words, short sentences, bullets over paragraphs.
