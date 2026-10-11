---
name: deep-dive
description: "Shortcut /deep-dive (Understand). Use when the user types /deep-dive or asks to get a detailed, structured breakdown of a topic, file or idea. Short, capped output (default 400 words) to save tokens."
---

# /deep-dive

Shortcut · Understand · cap: 400 words

## Produce
Sections: What it is / How it works / Why it matters / Limits / Next step. Bullets under each. Cite file:line or source when making factual claims.

## Lean output rules
- No preamble, no restating the request, no closing recap or "let me know" line.
- Stay inside the length cap. If the user adds `long` or `full`, the cap doubles; `short` halves it.
- Ask at most one question, and only if you truly cannot start. Otherwise state one assumption and go.
- Work from what is already in the conversation or the named file. Don't re-read files you already have.
- Plain words, short sentences, bullets over paragraphs.
