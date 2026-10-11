---
name: examples
description: "Shortcut /examples (Understand). Use when the user types /examples or asks to learn a concept through concrete examples. Short, capped output (default 150 words) to save tokens."
---

# /examples

Shortcut · Understand · cap: 150 words

## Produce
3 examples, simple to advanced, each 1-2 lines, plus one line on the pattern they share.

## Lean output rules
- No preamble, no restating the request, no closing recap or "let me know" line.
- Stay inside the length cap. If the user adds `long` or `full`, the cap doubles; `short` halves it.
- Ask at most one question, and only if you truly cannot start. Otherwise state one assumption and go.
- Work from what is already in the conversation or the named file. Don't re-read files you already have.
- Plain words, short sentences, bullets over paragraphs.
