---
name: meeting-notes-action-items
description: "Use whenever the user wants to turn meeting notes into action items and a summary, even if they don't name this skill. Business prompt #24 (Meeting Notes Into Action Items, Operations & Project Management). Delivers: Every action item with owner, deadline and context; Missing owners or deadlines flagged; One summary paragraph for absentees."
---

# Meeting Notes Into Action Items

Business prompt #24 · Operations & Project Management

## The prompt

> Here are the raw notes from a team meeting: [PASTE NOTES]. Extract all action items with the owner, deadline, and context. Then write a clean summary paragraph for anyone who missed the meeting.

## Inputs to collect

- **Notes (pasted)** (`[PASTE NOTES]`)

Use whatever the user has already given you (in the message, attached files or earlier in the conversation). If something essential is missing, ask for all missing inputs in one short message. If the user wants you to go ahead anyway, fill the gaps with reasonable assumptions and list them at the top of your answer.

## How to run it

1. Fill the placeholders above with the user's details and treat the completed prompt as the brief.
2. Produce the deliverable directly. No preamble about what you're going to do.
3. Check the result against the checklist below and fix anything that misses before you reply.
4. Finish with at most one short line offering a sensible next step (a variation, a tighter version, or a related prompt).

## Deliverable checklist

- [ ] Every action item with owner, deadline and context
- [ ] Missing owners or deadlines flagged
- [ ] One summary paragraph for absentees

## Quality rules (Operations & Project Management)

- Make every output something the user can act on today: owners, dates, next steps.
- When the input is missing information (owners, deadlines, scope), flag it clearly rather than guessing silently.
- Use tables or numbered lists where they make the plan easier to scan.
