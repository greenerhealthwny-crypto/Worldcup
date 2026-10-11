---
name: action-items
description: "Shortcut /action-items (Organize). Use when the user types /action-items or asks to extract next steps or action items from notes, a chat or a document. Short, capped output (default 150 words) to save tokens."
---

# /action-items

Shortcut · Organize · cap: 150 words

## Produce
Table: Action / Owner / Due. Use '?' where unknown; never invent owners or dates. Then any open questions as bullets.

Need the full, detailed deliverable instead? Use the `meeting-notes-action-items` skill.

## Lean output rules
- No preamble, no restating the request, no closing recap or "let me know" line.
- Stay inside the length cap. If the user adds `long` or `full`, the cap doubles; `short` halves it.
- Ask at most one question, and only if you truly cannot start. Otherwise state one assumption and go.
- Work from what is already in the conversation or the named file. Don't re-read files you already have.
- Plain words, short sentences, bullets over paragraphs.
