---
name: project-risk-assessment
description: "Risk Assessment for a New Project (business prompt #25, Operations & Project Management). We are about to launch [PROJECT]. Identify the top 10 risks, rate each one by likelihood and impact, and suggest a mitigation action for each. Flag the two you think I should..."
---

# Risk Assessment for a New Project

Business prompt #25 · Operations & Project Management

## The prompt

> We are about to launch [PROJECT]. Identify the top 10 risks, rate each one by likelihood and impact, and suggest a mitigation action for each. Flag the two you think I should prioritize immediately.

## Inputs to collect

- **Project** (`[PROJECT]`)

Use whatever the user has already given you (in the message, attached files or earlier in the conversation). If something essential is missing, ask for all missing inputs in one short message. If the user wants you to go ahead anyway, fill the gaps with reasonable assumptions and list them at the top of your answer.

## How to run it

1. Fill the placeholders above with the user's details and treat the completed prompt as the brief.
2. Produce the deliverable directly. No preamble about what you're going to do.
3. Check the result against the checklist below and fix anything that misses before you reply.
4. Finish with at most one short line offering a sensible next step (a variation, a tighter version, or a related prompt).

## Deliverable checklist

- [ ] Top 10 risks
- [ ] Likelihood and impact rating for each
- [ ] Mitigation action for each
- [ ] Two priority risks flagged

## Quality rules (Operations & Project Management)

- Make every output something the user can act on today: owners, dates, next steps.
- When the input is missing information (owners, deadlines, scope), flag it clearly rather than guessing silently.
- Use tables or numbered lists where they make the plan easier to scan.
