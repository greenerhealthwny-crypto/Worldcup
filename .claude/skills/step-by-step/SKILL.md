---
name: step-by-step
description: "Shortcut /step-by-step (Thinking). Use when the user types /step-by-step or asks to break a task or goal into ordered steps. Short, capped output (default 150 words) to save tokens."
---

# /step-by-step

Shortcut · Thinking · cap: 150 words

## Produce
Numbered steps, each starting with a verb, each doable in one sitting. Mark the one step to do first.

## Lean output rules
- No preamble, no restating the request, no closing recap or "let me know" line.
- Stay inside the length cap. If the user adds `long` or `full`, the cap doubles; `short` halves it.
- Ask at most one question, and only if you truly cannot start. Otherwise state one assumption and go.
- Work from what is already in the conversation or the named file. Don't re-read files you already have.
- Plain words, short sentences, bullets over paragraphs.
