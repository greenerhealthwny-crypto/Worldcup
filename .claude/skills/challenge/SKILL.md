---
name: challenge
description: "Shortcut /challenge (Thinking). Use when the user types /challenge or asks to challenge assumptions, play devil's advocate or stress-test an idea. Short, capped output (default 200 words) to save tokens."
---

# /challenge

Shortcut · Thinking · cap: 200 words

## Produce
List the 3-4 assumptions the idea rests on. For each: why it might be wrong + a cheap way to test it. End with the single riskiest one.

Need the full, detailed deliverable instead? Use the `business-model-stress-test` skill.

## Lean output rules
- No preamble, no restating the request, no closing recap or "let me know" line.
- Stay inside the length cap. If the user adds `long` or `full`, the cap doubles; `short` halves it.
- Ask at most one question, and only if you truly cannot start. Otherwise state one assumption and go.
- Work from what is already in the conversation or the named file. Don't re-read files you already have.
- Plain words, short sentences, bullets over paragraphs.
