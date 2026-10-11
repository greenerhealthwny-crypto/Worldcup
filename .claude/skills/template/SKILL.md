---
name: template
description: "Shortcut /template (Organize). Use when the user types /template or asks to create a reusable template, form, or SKILL.md from an example or process. Short, capped output (default 250 words) to save tokens."
---

# /template

Shortcut · Organize · cap: 250 words

## Produce
The template only, with [PLACEHOLDERS] in caps. If the user wants a Claude skill, output a SKILL.md with name/description frontmatter, Inputs, Steps, Checklist; keep it under 60 lines.

## Lean output rules
- No preamble, no restating the request, no closing recap or "let me know" line.
- Stay inside the length cap. If the user adds `long` or `full`, the cap doubles; `short` halves it.
- Ask at most one question, and only if you truly cannot start. Otherwise state one assumption and go.
- Work from what is already in the conversation or the named file. Don't re-read files you already have.
- Plain words, short sentences, bullets over paragraphs.
