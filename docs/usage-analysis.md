# Claude usage analysis and shortcut kit

Written 2026-10-11. Source: the session list for this account (titles, status summaries, token and cost totals) and this repo's git history. Full transcripts weren't read word for word. They're too big to page through cheaply.

## 1. Your sessions so far

| Date | Session | Cost | Share |
|---|---|---|---|
| 09-27 → 10-01 | Book → skill (ADHD 2.0) | $49.47 | 31% |
| 10-04 → 10-06 | Convert items to skills (Glute Lab, Laws of Power, Ministry of Healing…) | $48.96 | 31% |
| 10-04 → 10-11 | Google Docs project (recall-watch, iPhone Shortcut) | $37.33 | 24% |
| 10-11 | Prompts → 100 skills + 12 agents + Agents page | $20.19 | 13% |
| 10-10 | Execute (Country Crop Story agent plan) | $1.63 | 1% |
| 10-01 | Claude delays / freezing | $0.32 | <1% |
| 08-26 | Test coverage analysis | $0.30 | <1% |
| | **Total** | **$158.20** | |

## 2. Your most-used features

1. **Turning content into skills and agents.** This covers books, prompt lists and plans. It took 4 of 7 sessions and about 76% of spend.
2. **Summarizing long sources.** Book PDFs and the World Cup PDF were condensed into rules and checklists.
3. **Planning and organizing.** This includes agent team plans, queues, rosters and status pages.
4. **Build, test and review loops.** Validators, evals and security/stop-hook reviews ran on every session.
5. **Mobile-first use.** You start sessions mostly from the iOS and desktop apps.

## 3. Where the coins go

- **Long sessions.** The three costly sessions reached 377k–723k tokens of context and 72M–101M cache-read tokens. A long session re-reads its whole history on every turn. The cheap sessions ($0.30–$1.63) each did one task.
- **Stop-hook loop.** A "review the work…" stop hook fired 7–8 times in a row at the end of two sessions. Each firing was one more full-context turn, and it kept failing on the same unfixable item. The hook isn't in this repo, so it lives in your user-level settings.
- **Huge plugin load.** Every session loads hundreds of plugin skills: legal, finance, biotech, CockroachDB, Unity and more. Their descriptions are re-sent on every turn.
- **Long default answers.** Free-form requests get full-length replies. The shortcuts below cap the length.

## 4. Coin-saving habits (biggest win first)

1. **One task per session.** Start a new session when the topic changes, and don't keep a 5-day thread alive.
2. **Fix the stop hook.** Remove it, or add "if the same finding repeats, stop" to its prompt.
3. **Turn off unused plugins.** Keep small-business, productivity, marketing and brand-voice. Turn off legal, finance-banking, bio and database plugins unless you use them.
4. **Use a shortcut instead of a paragraph.** For example, type `/tldr wc-final.pdf` instead of "can you read this and summarize the key points…".
5. **Say `short` for less.** Add `short` to halve a shortcut's length cap, or `long` to double it.

## 5. Shortcut cheat sheet (sections 1–5)

Each one lives in `.claude/skills/<name>/SKILL.md`. To change one, edit `tools/shortcuts/generate.py` and re-run it.

| Section | Shortcut | Gives you | Default cap |
|---|---|---|---|
| Understand | `/tldr` | bottom line + 3–5 points | 120 words |
| | `/eli5` | analogy + plain explanation | 100 |
| | `/deep-dive` | what / how / why / limits / next | 400 |
| | `/compare` | one criteria table + pick | 180 |
| | `/examples` | 3 examples, simple → advanced | 150 |
| Thinking | `/step-by-step` | numbered verb-first steps | 150 |
| | `/pros-cons` | 4 pros, 4 risks, deciding factor | 150 |
| | `/pitfalls` | top 5 mistakes → fixes | 150 |
| | `/challenge` | assumptions + cheap tests | 200 |
| | `/root-cause` | 5 whys → fix → check | 180 |
| Content | `/hooks` | 10 hooks, best 2 starred | 150 |
| | `/humanize` | natural rewrite only | same length |
| | `/rewrite` | clearer text + 3 change notes | +40 |
| | `/tone` | text in the new tone | same length |
| | `/repurpose` | post, email, video, headline | 300 |
| Organize | `/checklist` | checkbox list | 150 |
| | `/prioritize` | do now / schedule / drop | 150 |
| | `/action-items` | action / owner / due table | 150 |
| | `/template` | reusable template or SKILL.md | 250 |
| | `/plan` | goal, milestones, first 3 actions, risk | 200 |
| Code | `/debug` | cause → fix → verify | 200 + code |
| | `/explain-code` | purpose + flow with file:line | 200 |
| | `/optimize` | top 3 changes by impact | 200 + code |
| | `/test-cases` | case / input / expected table | 200 |
| | `/document` | README-style doc | 300 |

**Chain them** (the "productivity stack"): `/tldr` → `/challenge` → `/plan` → `/checklist`.

Section 6 (Act-as, Role-play, Research, Quality-check, Build-workflow) is still to do. We'll go through it together.
