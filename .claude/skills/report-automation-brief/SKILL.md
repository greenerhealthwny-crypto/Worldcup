---
name: report-automation-brief
description: "Recurring Report Automation Brief (business prompt #58, Systems & Automation). I need to automate this weekly report: [DESCRIBE REPORT]. Write a brief for a developer to build it. Include: data sources, how the data should be pulled, how the report should be..."
---

# Recurring Report Automation Brief

Business prompt #58 · Systems & Automation

## The prompt

> I need to automate this weekly report: [DESCRIBE REPORT]. Write a brief for a developer to build it. Include: data sources, how the data should be pulled, how the report should be formatted, and where it should be delivered.

## Inputs to collect

- **Report (described)** (`[DESCRIBE REPORT]`)

Use whatever the user has already given you (in the message, attached files or earlier in the conversation). If something essential is missing, ask for all missing inputs in one short message. If the user wants you to go ahead anyway, fill the gaps with reasonable assumptions and list them at the top of your answer.

## How to run it

1. Fill the placeholders above with the user's details and treat the completed prompt as the brief.
2. Produce the deliverable directly. No preamble about what you're going to do.
3. Check the result against the checklist below and fix anything that misses before you reply.
4. Finish with at most one short line offering a sensible next step (a variation, a tighter version, or a related prompt).

## Deliverable checklist

- [ ] Data sources
- [ ] How the data is pulled
- [ ] Report format
- [ ] Delivery destination

## Quality rules (Systems & Automation)

- Be concrete: exact tool names, field types, triggers and steps that someone can build from directly.
- Call out platform limits, costs and failure points honestly. Tag anything about a tool's current features that you haven't checked as something to confirm.
- Prefer the simplest setup that does the job. Explain why you structured it that way.
