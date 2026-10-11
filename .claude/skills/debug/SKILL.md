---
name: debug
description: "Shortcut /debug (Code). Use when the user types /debug or asks to find and fix an error, bug or failing command. Short, capped output (default 200 words + code) to save tokens."
---

# /debug

Shortcut · Code · cap: 200 words + code

## Produce
Cause (1-2 lines, cite file:line) / Fix (minimal diff or command) / How to verify. Apply the fix if the code is in the repo.

## Lean output rules
- No preamble, no restating the request, no closing recap or "let me know" line.
- Stay inside the length cap. If the user adds `long` or `full`, the cap doubles; `short` halves it.
- Ask at most one question, and only if you truly cannot start. Otherwise state one assumption and go.
- Work from what is already in the conversation or the named file. Don't re-read files you already have.
- Plain words, short sentences, bullets over paragraphs.
