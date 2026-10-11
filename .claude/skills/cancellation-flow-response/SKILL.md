---
name: cancellation-flow-response
description: "Use whenever the user wants to respond to a customer who cancelled or wants to cancel a subscription, even if they don't name this skill. Business prompt #18 (Cancellation Flow Response, Customer Support & Comms). Delivers: Acknowledges and respects the decision; Addresses the root reason; Relevant retention incentive; Not desperate."
---

# Cancellation Flow Response

Business prompt #18 · Customer Support & Comms

## The prompt

> A user just cancelled their subscription and gave this reason: [PASTE REASON]. Write a response that acknowledges their decision, addresses the root reason, and offers a relevant retention incentive without sounding desperate.

## Inputs to collect

- **Reason (pasted)** (`[PASTE REASON]`)

Use whatever the user has already given you (in the message, attached files or earlier in the conversation). If something essential is missing, ask for all missing inputs in one short message. If the user wants you to go ahead anyway, fill the gaps with reasonable assumptions and list them at the top of your answer.

## How to run it

1. Fill the placeholders above with the user's details and treat the completed prompt as the brief.
2. Produce the deliverable directly. No preamble about what you're going to do.
3. Check the result against the checklist below and fix anything that misses before you reply.
4. Finish with at most one short line offering a sensible next step (a variation, a tighter version, or a related prompt).

## Deliverable checklist

- [ ] Acknowledges and respects the decision
- [ ] Addresses the root reason
- [ ] Relevant retention incentive
- [ ] Not desperate

## Quality rules (Customer Support & Comms)

- Sound like a real person on the team, not a policy document. No corporate language.
- Acknowledge feelings without grovelling. Don't promise anything the business can't deliver. If a refund, credit or policy is involved and you don't know the rules, mark it as [CONFIRM] instead of inventing them.
- Keep messages short enough to read on a phone.
