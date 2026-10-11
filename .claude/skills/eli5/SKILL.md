---
name: eli5
description: "Shortcut /eli5 (Understand). Use when the user types /eli5 or asks to explain something in very simple words, as if to a 5-year-old or a beginner. Short, capped output (default 100 words) to save tokens."
---

# /eli5

Shortcut · Understand · cap: 100 words

## Produce
One plain analogy, then the idea in 3-4 short sentences. No jargon; if a term is unavoidable, define it in five words.

## Lean output rules
- No preamble, no restating the request, no closing recap or "let me know" line.
- Stay inside the length cap. If the user adds `long` or `full`, the cap doubles; `short` halves it.
- Ask at most one question, and only if you truly cannot start. Otherwise state one assumption and go.
- Work from what is already in the conversation or the named file. Don't re-read files you already have.
- Plain words, short sentences, bullets over paragraphs.
