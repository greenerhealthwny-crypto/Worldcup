---
name: test-cases
description: "Shortcut /test-cases (Code). Use when the user types /test-cases or asks to generate test scenarios or test cases. Short, capped output (default 200 words) to save tokens."
---

# /test-cases

Shortcut · Code · cap: 200 words

## Produce
Table: Case / Input / Expected. Cover happy path, edge cases and one failure case. Write runnable tests only if the user asks.

## Lean output rules
- No preamble, no restating the request, no closing recap or "let me know" line.
- Stay inside the length cap. If the user adds `long` or `full`, the cap doubles; `short` halves it.
- Ask at most one question, and only if you truly cannot start. Otherwise state one assumption and go.
- Work from what is already in the conversation or the named file. Don't re-read files you already have.
- Plain words, short sentences, bullets over paragraphs.
