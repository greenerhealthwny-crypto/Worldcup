---
name: error-log-analysis
description: "Use whenever the user wants to analyze error logs or recurring system errors, even if they don't name this skill. Business prompt #60 (Error Log Analysis, Systems & Automation). Delivers: Recurring error patterns; Likely root cause for each; Ranked by severity; Where to start fixing."
---

# Error Log Analysis

Business prompt #60 · Systems & Automation

## The prompt

> Here is a batch of error logs from our system: [PASTE LOGS]. Identify the patterns. What errors are recurring? What is the likely root cause of each? Rank them by severity and suggest where we should start fixing.

## Inputs to collect

- **Logs (pasted)** (`[PASTE LOGS]`)

Use whatever the user has already given you (in the message, attached files or earlier in the conversation). If something essential is missing, ask for all missing inputs in one short message. If the user wants you to go ahead anyway, fill the gaps with reasonable assumptions and list them at the top of your answer.

## How to run it

1. Fill the placeholders above with the user's details and treat the completed prompt as the brief.
2. Produce the deliverable directly. No preamble about what you're going to do.
3. Check the result against the checklist below and fix anything that misses before you reply.
4. Finish with at most one short line offering a sensible next step (a variation, a tighter version, or a related prompt).

## Deliverable checklist

- [ ] Recurring error patterns
- [ ] Likely root cause for each
- [ ] Ranked by severity
- [ ] Where to start fixing

## Quality rules (Systems & Automation)

- Be concrete: exact tool names, field types, triggers and steps that someone can build from directly.
- Call out platform limits, costs and failure points honestly. Tag anything about a tool's current features that you haven't checked as something to confirm.
- Prefer the simplest setup that does the job. Explain why you structured it that way.
