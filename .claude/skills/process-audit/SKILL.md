---
name: process-audit
description: "Use whenever the user wants to audit or streamline a team process or workflow, even if they don't name this skill. Business prompt #30 (Process Audit From a Team Description, Operations & Project Management). Delivers: Bottlenecks; Redundancies; Single points of failure; Leaner version with fewer steps."
---

# Process Audit From a Team Description

Business prompt #30 · Operations & Project Management

## The prompt

> Here is how our team currently handles [PROCESS]: [PASTE DESCRIPTION]. Audit this process. Identify the bottlenecks, redundancies, and single points of failure. Suggest a leaner version that gets the same result in fewer steps.

## Inputs to collect

- **Process** (`[PROCESS]`)
- **Description (pasted)** (`[PASTE DESCRIPTION]`)

Use whatever the user has already given you (in the message, attached files or earlier in the conversation). If something essential is missing, ask for all missing inputs in one short message. If the user wants you to go ahead anyway, fill the gaps with reasonable assumptions and list them at the top of your answer.

## How to run it

1. Fill the placeholders above with the user's details and treat the completed prompt as the brief.
2. Produce the deliverable directly. No preamble about what you're going to do.
3. Check the result against the checklist below and fix anything that misses before you reply.
4. Finish with at most one short line offering a sensible next step (a variation, a tighter version, or a related prompt).

## Deliverable checklist

- [ ] Bottlenecks
- [ ] Redundancies
- [ ] Single points of failure
- [ ] Leaner version with fewer steps

## Quality rules (Operations & Project Management)

- Make every output something the user can act on today: owners, dates, next steps.
- When the input is missing information (owners, deadlines, scope), flag it clearly rather than guessing silently.
- Use tables or numbered lists where they make the plan easier to scan.
