---
name: root-cause
description: "Shortcut /root-cause (Thinking). Use when the user types /root-cause or asks to find the real underlying problem behind a symptom or recurring issue. Short, capped output (default 180 words) to save tokens."
---

# /root-cause

Shortcut · Thinking · cap: 180 words

## Produce
5-Whys chain (stop when you hit something actionable), then: Root cause / Fix / How to confirm it worked.

Need the full, detailed deliverable instead? Use the `error-log-analysis` skill.

## Lean output rules
- No preamble, no restating the request, no closing recap or "let me know" line.
- Stay inside the length cap. If the user adds `long` or `full`, the cap doubles; `short` halves it.
- Ask at most one question, and only if you truly cannot start. Otherwise state one assumption and go.
- Work from what is already in the conversation or the named file. Don't re-read files you already have.
- Plain words, short sentences, bullets over paragraphs.
