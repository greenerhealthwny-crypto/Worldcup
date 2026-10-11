---
name: ai-agent-prompt-from-job-description
description: "AI Agent Prompt From a Job Description (business prompt #52, Systems & Automation). Here is the job description for a role I want to automate with an AI agent: [PASTE JD]. Write a system prompt that turns Claude into this role. Include the persona, the rules, the..."
---

# AI Agent Prompt From a Job Description

Business prompt #52 · Systems & Automation

## The prompt

> Here is the job description for a role I want to automate with an AI agent: [PASTE JD]. Write a system prompt that turns Claude into this role. Include the persona, the rules, the output format, and three example tasks it should handle.

## Inputs to collect

- **Job description (pasted)** (`[PASTE JD]`)

Use whatever the user has already given you (in the message, attached files or earlier in the conversation). If something essential is missing, ask for all missing inputs in one short message. If the user wants you to go ahead anyway, fill the gaps with reasonable assumptions and list them at the top of your answer.

## How to run it

1. Fill the placeholders above with the user's details and treat the completed prompt as the brief.
2. Produce the deliverable directly. No preamble about what you're going to do.
3. Check the result against the checklist below and fix anything that misses before you reply.
4. Finish with at most one short line offering a sensible next step (a variation, a tighter version, or a related prompt).

## Deliverable checklist

- [ ] Persona
- [ ] Rules
- [ ] Output format
- [ ] Three example tasks

## Quality rules (Systems & Automation)

- Be concrete: exact tool names, field types, triggers and steps that someone can build from directly.
- Call out platform limits, costs and failure points honestly. Tag anything about a tool's current features that you haven't checked as something to confirm.
- Prefer the simplest setup that does the job. Explain why you structured it that way.
