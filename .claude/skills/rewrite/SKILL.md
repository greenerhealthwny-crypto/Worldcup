---
name: rewrite
description: "Shortcut /rewrite (Content). Use when the user types /rewrite or asks to improve the clarity and flow of a draft. Short, capped output (default input length + 40 words) to save tokens."
---

# /rewrite

Shortcut · Content · cap: input length + 40 words

## Produce
Return only the improved text, then at most 3 bullets on what changed and why.

## Lean output rules
- No preamble, no restating the request, no closing recap or "let me know" line.
- Stay inside the length cap. If the user adds `long` or `full`, the cap doubles; `short` halves it.
- Ask at most one question, and only if you truly cannot start. Otherwise state one assumption and go.
- Work from what is already in the conversation or the named file. Don't re-read files you already have.
- Plain words, short sentences, bullets over paragraphs.
