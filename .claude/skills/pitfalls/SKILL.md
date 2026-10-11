---
name: pitfalls
description: "Shortcut /pitfalls (Thinking). Use when the user types /pitfalls or asks to find the common mistakes or traps in a plan, task or draft. Short, capped output (default 150 words) to save tokens."
---

# /pitfalls

Shortcut · Thinking · cap: 150 words

## Produce
The top 5 pitfalls, each as: mistake -> how to avoid it (one line each). Most likely first.

Need the full, detailed deliverable instead? Use the `project-risk-assessment` skill.

## Lean output rules
- No preamble, no restating the request, no closing recap or "let me know" line.
- Stay inside the length cap. If the user adds `long` or `full`, the cap doubles; `short` halves it.
- Ask at most one question, and only if you truly cannot start. Otherwise state one assumption and go.
- Work from what is already in the conversation or the named file. Don't re-read files you already have.
- Plain words, short sentences, bullets over paragraphs.
