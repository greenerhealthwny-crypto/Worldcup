# First Agent Team: "Country Crop Story" content team

Built for Greener Health / Steven Jeanty (Modern Farmer · System Thinker).
Source material: `wc-final.pdf` (2026 World Cup Agricultural Bracket) and `.claude/skills/new-marketing/`.
Queue: `agent-team/queue.csv` (47 countries, already filled in from the bracket).

---

## 1) Recommended agent team

Three agents and one human. No orchestrator agent, no "CEO agent".

| # | Agent | One-line job |
|---|-------|--------------|
| A | **Researcher** | Turns one queue row (country + crop) into a sourced fact sheet. |
| B | **Writer** | Turns the fact sheet into a post package in Steven's voice. |
| C | **Checker** | Checks every claim in the draft against the fact sheet and runs the brand checklist. Passes it, fixes it, or kicks it back. |
| H | **Steven (human)** | Picks the row, approves or edits the final draft, posts it, logs the result. |

The work moves in a straight line: **Queue → Researcher → Writer → Checker → Steven → Post → Log.**

---

## 2) Why this use case

**What you already have:** a 48-slot bracket that pairs each country with its signature crop. It ran June 11–July 19, 2026. The tournament is over, but the content still works. "What does Ghana grow, and why does it matter?" is a good post any week of the year.

**The narrowed use case:** *One country per week becomes one fact-checked post package for LinkedIn and Instagram/Facebook.*

It passes the "good first team" test:

| Criterion | How this fits |
|---|---|
| Clear inputs | One CSV row: country + crop. Nothing else. |
| Repeatable steps | Research → write → check → approve. Same steps every week. |
| Measurable quality | Every claim has a source or it gets cut. Steven's edit time is easy to measure. |
| Obvious business value | 47 weeks of on-brand content that shows off your global-ag expertise (Rutgers MBS, 10+ years in CEA). It keeps your name in front of farm, food, and consulting buyers. |
| Low risk | A human approves every post. A bad draft costs you 10 minutes, not a client. |

**What I narrowed out:** live match-day content (the tournament has ended), auto-posting, images and video, and newsletters. Those come after version one.

**Assumptions (correct me if any are wrong):**
- You post on LinkedIn first, with Instagram/Facebook second.
- One post a week is the right pace.
- You have a Claude plan that includes Projects and web search.
- The goal is reputation and inbound leads, not direct sales.

---

## 3) Agent-by-agent blueprint

### A. Researcher
| Field | Spec |
|---|---|
| Owns | Facts. Nothing else. It never writes copy. |
| Trigger | Steven pastes one queue row. |
| Receives | `country`, `signature_crop`, `flag`, `notes` from `queue.csv`. |
| Outputs | A fact sheet with 6–10 numbered facts. Each fact has a source URL and a confidence level (high/med/low). It also lists one "surprising angle" and one "Western NY / CEA link". |
| Tools | Web search. Sources must be FAO, USDA FAS, the country's ag ministry, a university extension service, or a major news outlet. |
| Human checkpoint | None. The Checker covers this step. |
| Escalates when | The crop label in the queue is wrong or misleading (for example, Belgium "Chocolate"). It flags `LABEL_ISSUE` and suggests a fix. |

### B. Writer
| Field | Spec |
|---|---|
| Owns | Voice, story, and format. |
| Trigger | It receives the Researcher's fact sheet. |
| Receives | The fact sheet plus the original queue row. |
| Outputs | A post package with: a LinkedIn post (150–250 words), an IG/FB caption (60–120 words), 3 hook options, an image brief (1 line), and a claim map that ties each sentence's facts to fact #s. |
| Tools | None. It may use only facts that are in the fact sheet. |
| Human checkpoint | None. It goes to the Checker. |
| Escalates when | The fact sheet has fewer than 4 high/med facts. It returns `NEED_MORE_RESEARCH`. |

### C. Checker
| Field | Spec |
|---|---|
| Owns | Accuracy and brand fit. It is the only gate before Steven. |
| Trigger | It receives the post package plus the fact sheet. |
| Receives | Both documents. |
| Outputs | A verdict (`PASS`, `PASS_WITH_FIXES`, or `FAIL`), a claim-by-claim table, a brand checklist score, and a corrected draft if it made fixes. |
| Tools | None in v1. It checks against the fact sheet, not the open web. |
| Human checkpoint | **Yes. Every output goes to Steven.** |
| Escalates when | There is any `FAIL`, any sensitive topic (labor, politics, conflict, health claims), or a claim with no source. |

### H. Steven (human)
- Picks the row and pastes it into the Researcher.
- Reads the Checker's output, then approves, edits, or rejects it. Aim for 10 minutes or less.
- Posts it by hand and fills in `status`, `post_url`, and `approved_on` in the queue.
- After 7 days, logs reactions, comments, and DMs/leads.

---

## 4) System prompts

Paste each prompt into its own Claude Project as the Project instructions. Also upload `.claude/skills/new-marketing/SKILL.md` to the **Writer** project as a knowledge file.

### A. Researcher: system prompt

```text
<role>
You are the Researcher on a three-agent content team for Greener Health, the brand of
Steven Jeanty — a modern farmer and systems thinker (Rutgers MBS Global Agriculture,
10+ years in cannabis, vertical farms, and controlled-environment agriculture, based in
Western New York). You find facts. You never write marketing copy.
</role>

<responsibilities>
Given one country and its "signature crop" from Steven's World Cup Agricultural Bracket,
produce a fact sheet that a writer can safely build a post from.
</responsibilities>

<decision_rules>
- Every fact needs a source URL you actually opened. No source = do not include it.
- Prefer, in order: FAO/FAOSTAT, USDA Foreign Agricultural Service, the country's
  agriculture ministry, university extension or peer-reviewed work, major news outlets.
  Avoid content farms, recipe blogs, and AI-generated listicles.
- Prefer numbers with a year ("~X tonnes in 2023"). Never present an old number as current.
- Rank each fact: high (primary/official source), med (reputable secondary), low (single
  weak source — include only if it's the surprising angle, and say so).
- If the crop label is inaccurate or misleading (e.g., a processed product, not a crop;
  an animal product; a crop the country imports rather than grows), output LABEL_ISSUE
  with a one-line suggested reframe. Keep researching using the reframe.
- If the topic touches labor abuse, conflict, politics, or health claims, flag SENSITIVE
  and stick to well-sourced facts.
</decision_rules>

<tool_use>
Use web search. Run separate searches for: production volume/rank, history/origin,
growing conditions, economic importance, and one surprising or human story.
Stop at 10 facts. Do not pad.
</tool_use>

<output_format>
FACT SHEET — {country}: {crop}
Flags: [NONE | LABEL_ISSUE: ... | SENSITIVE: ...]

| # | Fact | Source URL | Confidence |
|---|------|-----------|------------|
| 1 | ...  | ...       | high       |

Surprising angle: <one sentence, cite fact #>
WNY / CEA link: <one honest sentence connecting this crop to Western NY farming or
controlled-environment growing — or "none that's honest">
Gaps: <what you could not verify>
</output_format>

<failure_handling>
If you find fewer than 4 high/med facts, say INSUFFICIENT_SOURCES and list what you tried.
Never invent a statistic, a quote, or a URL.
</failure_handling>
```

### B. Writer: system prompt

```text
<role>
You are the Writer for Greener Health. You write in Steven Jeanty's voice: a modern
farmer who thinks in systems and can't watch soccer without thinking about soil.
Curious, plain-spoken, a little playful, never preachy. You follow the New Marketing
principles in the attached SKILL.md: lead with value and story, 80% value / 20% brand,
emotion over information, clarity over cleverness.
</role>

<responsibilities>
Turn one fact sheet into one post package. Use ONLY facts from the fact sheet.
</responsibilities>

<decision_rules>
- Every factual sentence must map to a fact # in the claim map. If it can't, cut it.
- Do not use any fact marked "low" unless it is phrased as "reportedly" or "one study found".
- If the fact sheet has a LABEL_ISSUE, use the suggested reframe — never repeat the
  inaccurate label as fact.
- If SENSITIVE, keep tone neutral and factual; no jokes about that topic.
- One soft brand line max (e.g., the bracket, Greener Health, CEA). No hard sell.
- Short sentences. No hashtag walls (max 3). No emojis in LinkedIn body; max 2 in IG/FB.
- Banned: "delve", "game-changer", "in today's fast-paced world", "unlock", "revolutionize".
</decision_rules>

<output_format>
POST PACKAGE — {country}: {crop}

HOOKS (3 options, ≤12 words each):
1. ...
2. ...
3. ...

LINKEDIN (150–250 words, uses hook 1):
...

IG/FB CAPTION (60–120 words):
...

IMAGE BRIEF (1 line): ...

CLAIM MAP:
| Sentence (short quote) | Fact # |
|---|---|
</output_format>

<failure_handling>
If the fact sheet has fewer than 4 high/med facts, or says INSUFFICIENT_SOURCES,
output NEED_MORE_RESEARCH and say what's missing. Do not write a thin post.
</failure_handling>
```

### C. Checker: system prompt

```text
<role>
You are the Checker for Greener Health — the last gate before a human approves a post.
You are skeptical by default. Your job is to catch errors, not to be nice.
</role>

<responsibilities>
Compare the post package against the fact sheet. Verify every factual claim. Run the
brand checklist. Fix small problems yourself; fail anything you can't fix safely.
</responsibilities>

<decision_rules>
Claim check — for EVERY factual sentence in both the LinkedIn post and the IG/FB caption:
- SUPPORTED: matches the cited fact # in meaning and number.
- STRETCHED: roughly right but exaggerated, rounded wrong, or missing a year → fix it.
- UNSUPPORTED: not in the fact sheet → delete it.
- CONTRADICTED: conflicts with the fact sheet → FAIL.

Brand checklist (score each 0/1):
1. Opens with a hook, not a definition.
2. Teaches something real (value > promotion).
3. At most one brand mention, and it's soft.
4. Sounds like a person, not a press release.
5. No banned words; ≤3 hashtags.
6. Within word limits.
7. LABEL_ISSUE / SENSITIVE flags handled correctly.

Verdict:
- PASS: all claims SUPPORTED, checklist ≥6/7.
- PASS_WITH_FIXES: only STRETCHED/UNSUPPORTED items, all fixed; checklist ≥5/7 after fixes.
- FAIL: any CONTRADICTED claim, checklist <5/7, or a SENSITIVE topic handled badly.
</decision_rules>

<output_format>
VERDICT: PASS | PASS_WITH_FIXES | FAIL
Reason (1 line): ...

CLAIMS:
| Sentence | Fact # | Status | Action |
|---|---|---|---|

BRAND CHECKLIST: x/7 — list any misses.

FINAL DRAFT (only if PASS or PASS_WITH_FIXES):
<LinkedIn post>
---
<IG/FB caption>

FOR STEVEN: <the 1–3 things a human should eyeball before posting>
</output_format>

<failure_handling>
Never approve on vibes. If you are unsure whether a claim is supported, mark it
UNSUPPORTED and delete it. Always route to the human — you never publish.
</failure_handling>
```

---

## 5) Task templates (reusable inputs)

**To the Researcher** (copy one row from `queue.csv`):
```text
Queue row:
country: Ghana
signature_crop: Cocoa
flag:
notes:
Build the fact sheet.
```

**To the Writer:**
```text
Original row: <paste row>
Fact sheet:
<paste the Researcher's full output>
Write the post package.
```

**To the Checker:**
```text
Fact sheet:
<paste Researcher output>
Post package:
<paste Writer output>
Check it.
```

**Weekly log line** (add to `queue.csv`, or keep a "results" tab in a Google Sheet):
```text
id, status=posted, post_url, approved_on, edit_minutes, verdict, reactions_7d, comments_7d, leads_7d
```

---

## 6) Workflow diagram

```text
 ┌─────────────┐
 │ queue.csv   │  Steven picks next row (status=todo)
 └──────┬──────┘
        ▼
 ┌─────────────┐   LABEL_ISSUE / SENSITIVE flags travel with the sheet
 │ A Researcher│──────────────────────────────────────────┐
 │ (web search)│                                          │
 └──────┬──────┘                                          │
        │ fact sheet                                      │
        ▼                                                 │
 ┌─────────────┐  NEED_MORE_RESEARCH ──► back to A (once) │
 │ B Writer    │                                          │
 └──────┬──────┘                                          │
        │ post package + claim map                        │
        ▼                                                 ▼
 ┌─────────────┐  FAIL ──► back to B with Checker notes (max 1 retry)
 │ C Checker   │          2nd FAIL ──► Steven decides: fix by hand or skip row
 └──────┬──────┘
        │ PASS / PASS_WITH_FIXES + "For Steven" notes
        ▼
 ┌─────────────────────┐
 │ H Steven  ✋ APPROVE │  edit ≤10 min → post by hand
 └──────┬──────────────┘
        ▼
 ┌─────────────┐
 │ Log results │  7 days later: reactions, comments, leads → queue.csv
 └─────────────┘
```

**How context is shared:** by copy and paste. Each agent sees only what the next step needs. The fact sheet is the single source of truth, and the Writer and Checker both work from it.
**When agents ask for clarification:** only through the fixed flags (`LABEL_ISSUE`, `SENSITIVE`, `INSUFFICIENT_SOURCES`, `NEED_MORE_RESEARCH`). There are no open-ended questions.
**Feedback loop:** every Friday, read the log. If Steven keeps making the same edit, add it to the Writer's or Checker's rules.

---

## 7) Tools and setup

| Tool | Why it's needed | Setup |
|---|---|---|
| **Claude (3 Projects)** | Each Project holds one agent's system prompt, so the roles stay separate and you never re-paste prompts. | Create "CCS-Researcher", "CCS-Writer", and "CCS-Checker". Paste each prompt into its Project instructions. |
| **Web search in Claude** | Only the Researcher needs live facts. | Turn web search on in the Researcher project only. |
| **`new-marketing/SKILL.md`** | Gives the Writer your marketing principles, so you don't have to re-explain them. | Upload it as a knowledge file in the Writer project. |
| **`queue.csv` → Google Sheet** | Your work queue and results log in one place. | Import the CSV into a Sheet with File → Import. |
| **A notes doc or folder** | Archives each week's fact sheet, so you can reuse facts and prove sources if someone asks. | One doc per country, or one running doc. |

That's the whole stack. No code, no API keys, no automation platform.

---

## 8) QA checkpoints

### Five test cases (run all five before posting anything)

| # | Row | What it tests | Pass looks like |
|---|-----|---------------|-----------------|
| 1 | **Ghana: Cocoa** | Happy path, well-documented crop | Checker gives PASS. Every claim maps to a fact. Steven edits for 10 minutes or less. |
| 2 | **Belgium: Chocolate & Beets** | Wrong label (Belgium doesn't grow cacao) | Researcher flags `LABEL_ISSUE`. The post frames chocolate as a processing story and beets as the crop. |
| 3 | **Uzbekistan: Cotton & Fruits** | Sensitive topic (forced-labor history) | Researcher flags `SENSITIVE`. The tone is neutral and sourced. The Checker sends it to Steven with a note. |
| 4 | **Curaçao: Aloe & Citrus Peel** | Thin data, small country | Researcher returns fewer facts or `INSUFFICIENT_SOURCES`. The Writer refuses to pad. No invented stats. |
| 5 | **Planted error:** take test 1's draft, change one number (e.g., double a production figure), and send it to the Checker only | Does the Checker actually check? | The Checker marks it `CONTRADICTED` and returns `FAIL`. |

### Three likely failure modes
1. **Made-up or stale numbers.** The Researcher "finds" a stat with no real source, or presents a 2015 figure as current.
   *Guard:* every fact needs a URL and a year. Spot-check 2 URLs each week by clicking them.
2. **The Writer adds its own "facts".** It drops in a fun detail that isn't in the fact sheet.
   *Guard:* the claim map, plus the Checker's rule to delete anything `UNSUPPORTED`.
3. **Everything sounds the same.** By week 6 every post opens with "Did you know...?"
   *Guard:* 3 hook options every time, and rotate the hook style (question, number, story, contrarian).

### What success looks like (version one)
- Five posts published, each one gets a Checker PASS, and each needs 10 minutes or less of human editing.
- No factual corrections from readers.

### Metrics to track after launch
| Metric | Why it matters | Target after 4 weeks |
|---|---|---|
| Steven edit minutes per post | Shows whether the team actually saves time | ≤10 |
| Checker first-pass rate | Shows how good the Writer is | ≥60% PASS or PASS_WITH_FIXES |
| Claims cut by the Checker per post | Shows how much the Writer makes things up | Trending toward 0 |
| Comments per post (7-day) | Real engagement, not vanity likes | Rising |
| DMs, inquiries, or leads | The business outcome | ≥1 per month |

---

## 9) 7-day launch plan

| Day | Do this | Done when |
|---|---|---|
| **1** | Import `queue.csv` into a Google Sheet. Fix the New Zealand duplicate in your bracket. Pick your first 5 test rows (§8). | The Sheet exists and the test rows are marked. |
| **2** | Create the 3 Claude Projects and paste in the prompts. Turn on web search for the Researcher. Upload SKILL.md to the Writer. | All 3 projects respond to a "hello" with their role. |
| **3** | Run test 1 (Ghana) end to end. Time each step. | You have a Checker verdict and a timing for each step. |
| **4** | Run tests 2–5. Write down every miss. | You have a list of misses. |
| **5** | Fix the prompts. Each miss becomes one new rule in the right agent. Re-run any test that failed. | All 5 tests pass. |
| **6** | Run one real row from start to finish. Approve it and post it. Log it. | Post #1 is live. |
| **7** | Batch the next 3 rows so you have a buffer. Set a weekly 45-minute calendar block. Review the Day 6 post's early numbers. | You have 3 approved drafts queued and a recurring time block. |

---

## 10) Common mistakes (and what not to build yet)

**Mistakes:**
- **Skipping the tests.** If you run the real queue first, you learn about failures in public.
- **One giant prompt.** Combining researcher, writer, and checker into one agent means nobody checks the work. The split is the whole point.
- **Letting the Checker browse.** In v1, it checks against the fact sheet only. Otherwise it "verifies" claims with new, unchecked sources.
- **Approving without reading the "For Steven" notes.** That's the one place a human matters most.
- **Fixing the same thing by hand every week.** If you make an edit twice, it belongs in a prompt.

**Do NOT build yet:**
- Auto-posting to LinkedIn or Instagram
- A scheduler or Zapier pipeline
- An "orchestrator" agent that manages the other three
- AI image or video generation
- A vector database or long-term memory
- More agents (an SEO agent, analytics agent, or reply agent)

Build these only once the manual loop has run for 4 weeks and you know where the real bottleneck is.

---

## 11) What to improve after version one

Once you have 4 weeks of logs, add **one** of these at a time, based on what the metrics show:

1. **If copy-pasting is the pain:** write a small script with the Claude API that chains A → B → C and drops the Checker output into a doc. Steven still approves.
2. **If the Checker misses things:** give it read-only web access to re-open the Researcher's cited URLs. It may not search for new sources.
3. **If engagement is flat:** add an "Angle" step before the Writer that proposes 3 story angles, and have Steven pick one (a second human checkpoint).
4. **If leads show up:** add a reply-drafting agent for comments and DMs, with human approval on every reply.
5. **Reuse:** turn each fact sheet into a monthly newsletter roundup ("4 countries, 4 crops").
6. **Next World Cup cycle:** the same team can produce match-day "crop vs crop" posts. Only the input row changes (two countries instead of one).

---

## START HERE FIRST

1. Open `agent-team/queue.csv` and import it into a Google Sheet.
2. Create one Claude Project called **CCS-Researcher** and paste in the Researcher prompt from §4. Turn web search on.
3. Paste this in and run it:
   ```text
   Queue row:
   country: Ghana
   signature_crop: Cocoa
   flag:
   notes:
   Build the fact sheet.
   ```
4. Click two of the source URLs it returns. If they're real and they say what the fact sheet says, set up the Writer and Checker. You're on Day 3 of the plan.
