---
name: explain-code
description: "Shortcut /explain-code (Code). Use when the user types /explain-code or asks to understand what a piece of code, file or script does. Short, capped output (default 200 words) to save tokens."
---

# /explain-code

Shortcut · Code · cap: 200 words

## Produce
One-line purpose, then the flow as 3-6 numbered steps citing file:line. Flag anything surprising.

## Lean output rules
- No preamble, no restating the request, no closing recap or "let me know" line.
- Stay inside the length cap. If the user adds `long` or `full`, the cap doubles; `short` halves it.
- Ask at most one question, and only if you truly cannot start. Otherwise state one assumption and go.
- Work from what is already in the conversation or the named file. Don't re-read files you already have.
- Plain words, short sentences, bullets over paragraphs.
