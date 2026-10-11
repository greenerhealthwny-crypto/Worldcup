---
name: tldr
description: "Shortcut /tldr (Understand). Use when the user types /tldr or asks to summarize text, a file, a book, a PDF or a thread into key points. Short, capped output (default 120 words) to save tokens."
---

# /tldr

Shortcut · Understand · cap: 120 words

## Produce
A one-line bottom line, then the 3-5 key points as bullets. For a book or long PDF: add one line per chapter only if asked.

## Lean output rules
- No preamble, no restating the request, no closing recap or "let me know" line.
- Stay inside the length cap. If the user adds `long` or `full`, the cap doubles; `short` halves it.
- Ask at most one question, and only if you truly cannot start. Otherwise state one assumption and go.
- Work from what is already in the conversation or the named file. Don't re-read files you already have.
- Plain words, short sentences, bullets over paragraphs.
