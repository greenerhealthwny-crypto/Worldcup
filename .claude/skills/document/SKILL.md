---
name: document
description: "Shortcut /document (Code). Use when the user types /document or asks to create clear documentation for code, a tool, a skill or a process. Short, capped output (default 300 words) to save tokens."
---

# /document

Shortcut · Code · cap: 300 words

## Produce
README-style: What it does / How to use (example) / Inputs-outputs / Gotchas. Match the repo's existing doc style.

## Lean output rules
- No preamble, no restating the request, no closing recap or "let me know" line.
- Stay inside the length cap. If the user adds `long` or `full`, the cap doubles; `short` halves it.
- Ask at most one question, and only if you truly cannot start. Otherwise state one assumption and go.
- Work from what is already in the conversation or the named file. Don't re-read files you already have.
- Plain words, short sentences, bullets over paragraphs.
