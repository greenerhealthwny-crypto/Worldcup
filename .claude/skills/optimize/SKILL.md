---
name: optimize
description: "Shortcut /optimize (Code). Use when the user types /optimize or asks to improve the performance or efficiency of code, a query, a prompt or a workflow. Short, capped output (default 200 words + code) to save tokens."
---

# /optimize

Shortcut · Code · cap: 200 words + code

## Produce
Top 3 changes ranked by impact, each: what / why / expected gain. Apply the top one if asked or obvious.

## Lean output rules
- No preamble, no restating the request, no closing recap or "let me know" line.
- Stay inside the length cap. If the user adds `long` or `full`, the cap doubles; `short` halves it.
- Ask at most one question, and only if you truly cannot start. Otherwise state one assumption and go.
- Work from what is already in the conversation or the named file. Don't re-read files you already have.
- Plain words, short sentences, bullets over paragraphs.
