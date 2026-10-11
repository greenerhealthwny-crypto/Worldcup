---
name: integration-map
description: "Use whenever the user wants to map integrations between the tools in their stack, even if they don't name this skill. Business prompt #59 (Integration Map From a Tool List, Systems & Automation). Delivers: Which tools connect; What data flows between them; Priority order for setting up connections."
---

# Integration Map From a Tool List

Business prompt #59 · Systems & Automation

## The prompt

> Here are all the tools in our stack: [PASTE LIST]. Build an integration map. Show which tools should talk to each other, what data should flow between them, and which connections are highest priority to set up first.

## Inputs to collect

- **List (pasted)** (`[PASTE LIST]`)

Use whatever the user has already given you (in the message, attached files or earlier in the conversation). If something essential is missing, ask for all missing inputs in one short message. If the user wants you to go ahead anyway, fill the gaps with reasonable assumptions and list them at the top of your answer.

## How to run it

1. Fill the placeholders above with the user's details and treat the completed prompt as the brief.
2. Produce the deliverable directly. No preamble about what you're going to do.
3. Check the result against the checklist below and fix anything that misses before you reply.
4. Finish with at most one short line offering a sensible next step (a variation, a tighter version, or a related prompt).

## Deliverable checklist

- [ ] Which tools connect
- [ ] What data flows between them
- [ ] Priority order for setting up connections

## Quality rules (Systems & Automation)

- Be concrete: exact tool names, field types, triggers and steps that someone can build from directly.
- Call out platform limits, costs and failure points honestly. Tag anything about a tool's current features that you haven't checked as something to confirm.
- Prefer the simplest setup that does the job. Explain why you structured it that way.
