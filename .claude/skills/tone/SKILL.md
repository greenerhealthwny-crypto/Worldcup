---
name: tone
description: "Shortcut /tone (Content). Use when the user types /tone or asks to change the tone or style of text (e.g. friendlier, more formal, punchier). Short, capped output (default same length as input) to save tokens."
---

# /tone

Shortcut · Content · cap: same length as input

## Produce
Return only the text in the requested tone. If no tone named, give two short versions: warmer and more direct.

## Lean output rules
- No preamble, no restating the request, no closing recap or "let me know" line.
- Stay inside the length cap. If the user adds `long` or `full`, the cap doubles; `short` halves it.
- Ask at most one question, and only if you truly cannot start. Otherwise state one assumption and go.
- Work from what is already in the conversation or the named file. Don't re-read files you already have.
- Plain words, short sentences, bullets over paragraphs.
