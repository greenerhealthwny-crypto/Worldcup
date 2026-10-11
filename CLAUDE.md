# Project instructions

This repo contains 100 business workflow skills in `.claude/skills/` (index: `.claude/skills/BUSINESS-PROMPTS.md`), covering content and copywriting, customer support, operations, sales, research, automation, finance, hiring, marketing and strategy.

**Before answering any business writing, planning or analysis request, check the skill list for a matching skill and invoke it with the Skill tool first.** Do this even for short requests like "write a cold email", "reply to this complaint", "turn these notes into action items", "organize these expenses" or "follow up with a prospect who went quiet". The skills carry word limits, required sections and quality rules that a direct answer will miss.

Only skip the skill when nothing in the list fits the request.

## AI agents

There are also 12 AI agents in `.claude/agents/` (index: `docs/ai-agents.md`). **When a request matches one of these jobs, delegate it to that agent with the Agent tool** (`subagent_type` = the agent name), passing along everything the user gave you. The agent will use the business skills itself.

| Job | Agent |
|---|---|
| Trending topics, article summaries, content ideas for a niche | `content-research-agent` |
| Social posts, visual briefs, posting schedule | `social-media-scheduler-agent` |
| Answering customer questions, FAQs, support replies | `customer-support-agent` |
| Inbox triage, email replies, follow-ups | `email-assistant-agent` |
| Expenses, budgets, saving money on bills | `personal-finance-agent` |
| Study plans, explaining topics, quizzes | `learning-study-agent` |
| Market trends, competitor tracking, business insights | `market-analysis-agent` |
| Resume screening, shortlists, interview kits | `recruitment-agent` |
| Trips, flights, hotels, itineraries, local tips | `travel-planner-agent` |
| Finding and qualifying leads, sales outreach | `sales-lead-gen-agent` |
| Summarizing, converting or organizing files | `file-document-agent` |
| Creative ideas, drafts, images and visuals | `creative-assistant-agent` |

Use a single skill directly instead when the user wants one specific deliverable (for example "write a cold email"), and an agent when the job spans several steps (find leads *and* write outreach, sort the inbox *and* draft replies).
