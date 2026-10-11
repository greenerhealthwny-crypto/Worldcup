---
name: humanize
description: "Shortcut /humanize (Content). Use when the user types /humanize or asks to make text sound natural and human, less like AI or a corporate template. Short, capped output (default same length as input) to save tokens."
---

# /humanize

Shortcut · Content · cap: same length as input

## Produce
Return only the rewritten text. Use contractions, plain verbs, varied sentence length. Cut filler like 'leverage', 'delve', 'I hope this finds you well'. Keep the meaning and length.

## Lean output rules
- No preamble, no restating the request, no closing recap or "let me know" line.
- Stay inside the length cap. If the user adds `long` or `full`, the cap doubles; `short` halves it.
- Ask at most one question, and only if you truly cannot start. Otherwise state one assumption and go.
- Work from what is already in the conversation or the named file. Don't re-read files you already have.
- Plain words, short sentences, bullets over paragraphs.
