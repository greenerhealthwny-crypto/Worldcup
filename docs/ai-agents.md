# 12 AI Agents

Built from the "12 AI Agents You Can Build This Weekend" list, following the 8-step method in "How to Build AI Agents From Scratch": role and goal, workflow, model and prompt, tools, memory, safety, testing and deployment.

Each agent lives in `.claude/agents/<name>.md` and remembers your preferences in `.claude/agent-memory/<name>/MEMORY.md`. It asks before sending, posting, booking, paying or deleting anything.

**How to use one:** describe the job ("sort my inbox and draft replies") and Claude hands it to the right agent. You can also name the agent: "use the travel-planner-agent to plan 4 days in Lisbon".

| # | Agent | Name | Great for | Preloaded skills |
|---|---|---|---|---|
| 01 | Content Research Agent | [`content-research-agent`](../.claude/agents/content-research-agent.md) | Creators, bloggers, marketers | `trend-report`, `seo-blog-brief` |
| 02 | Social Media Scheduler Agent | [`social-media-scheduler-agent`](../.claude/agents/social-media-scheduler-agent.md) | Creators, businesses, freelancers | `content-calendar-90-day`, `repurpose-article-five-formats` |
| 03 | Customer Support Agent | [`customer-support-agent`](../.claude/agents/customer-support-agent.md) | Online stores, service businesses | `complaint-reply`, `refund-request-response`, `internal-escalation-summary`, `faq-from-support-tickets` |
| 04 | Email Assistant Agent | [`email-assistant-agent`](../.claude/agents/email-assistant-agent.md) | Professionals, freelancers, teams | `lost-deal-follow-up`, `meeting-notes-action-items` |
| 05 | Personal Finance Agent | [`personal-finance-agent`](../.claude/agents/personal-finance-agent.md) | Individuals, side hustlers, families | `expense-report-summary`, `cash-flow-projection-template` |
| 06 | Learning & Study Agent | [`learning-study-agent`](../.claude/agents/learning-study-agent.md) | Students, self-learners, professionals | — |
| 07 | Market Analysis Agent | [`market-analysis-agent`](../.claude/agents/market-analysis-agent.md) | Entrepreneurs, creators, small businesses | `competitor-analysis`, `market-research-brief`, `swot-analysis` |
| 08 | Recruitment Agent | [`recruitment-agent`](../.claude/agents/recruitment-agent.md) | Hiring managers, founders, HR | `job-description`, `interview-question-set`, `candidate-rejection-email` |
| 09 | Travel Planner Agent | [`travel-planner-agent`](../.claude/agents/travel-planner-agent.md) | Travelers, digital nomads | — |
| 10 | Sales & Lead Gen Agent | [`sales-lead-gen-agent`](../.claude/agents/sales-lead-gen-agent.md) | Marketers, sales teams, service providers | `icp-profile`, `cold-email-replies`, `lost-deal-follow-up`, `discovery-call-script` |
| 11 | File & Document Agent | [`file-document-agent`](../.claude/agents/file-document-agent.md) | Professionals, researchers, businesses | `industry-report-summary`, `vendor-contract-summary`, `meeting-notes-action-items` |
| 12 | Creative Assistant Agent | [`creative-assistant-agent`](../.claude/agents/creative-assistant-agent.md) | Creators, designers, small teams | `facebook-ad-variations`, `brand-positioning-statements`, `repurpose-article-five-formats` |

## What needs a connector

These agents draft and plan on their own. Taking real actions needs the matching service connected in Claude:

- **Email Assistant:** Gmail (read, label, draft).
- **Social Media Scheduler:** a scheduler such as Buffer or Hootsuite, or Zapier. Without one it delivers a CSV to import.
- **Customer Support:** your helpdesk or inbox, to send approved replies.
- **Sales & Lead Gen:** your CRM, to save leads (it can also give you a CSV).
- **Travel Planner and Creative Assistant:** web search, plus an image tool for visuals.

## Regenerating

Edit `tools/agents/generate.py` and run `python3 tools/agents/generate.py`. Memory files are never overwritten.

## Tests

- `python3 tests/validate_agents.py`: structure (frontmatter, skills exist, memory folders, approval rules).
- `python3 tests/run_agent_evals.py`: sends a realistic request for each agent through headless Claude Code and checks the right agent handles it.
