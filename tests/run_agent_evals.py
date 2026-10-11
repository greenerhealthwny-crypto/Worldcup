"""Functional evals for the 12 AI agents.

Each case sends a realistic request (that does not name the agent) through headless
Claude Code in a throwaway copy of the repo, then checks:
  1. the main session delegated to the expected agent (Agent tool, subagent_type), and
  2. case-specific checks on the final answer (and, for one case, the agent's memory file).

Run: python3 tests/run_agent_evals.py [case ...]
Transcripts go to tests/eval-output/agents/ (git-ignored).
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "tests" / "eval-output" / "agents"


def has(*phrases):
    return lambda t, w: [f"missing: {p!r}" for p in phrases if p.lower() not in t.lower()]


def matches(pattern, label):
    return lambda t, w: [] if re.search(pattern, t, re.I | re.S) else [label]


def memory_contains(agent, phrase):
    def check(t, w):
        f = w / ".claude" / "agent-memory" / agent / "MEMORY.md"
        try:
            return [] if phrase.lower() in f.read_text().lower() else [f"preference not saved to {agent} memory"]
        except OSError:
            return [f"memory file for {agent} unreadable"]
    return check


CASES = {
    "content-research": dict(
        agent="content-research-agent",
        prompt="I run a newsletter about home composting for urban apartment dwellers. Find what's trending "
               "in that space right now and give me content ideas for the next few weeks.",
        checks=[matches(r"https?://", "no source links")],
    ),
    "social-scheduler": dict(
        agent="social-media-scheduler-agent",
        prompt="Plan and write two weeks of Instagram and LinkedIn posts for my bakery, Rise & Crumb in Buffalo NY. "
               "3 posts a week per platform. We're launching a sourdough subscription on the 20th. "
               "Include what each image should show and lay it out on a schedule.",
        checks=[matches(r"\|.*\|", "no schedule table"), matches(r"approv|needs your ok|nothing (is|has been|was) (scheduled|posted)|not (yet )?(scheduled|posted)", "no approval step")],
    ),
    "customer-support": dict(
        agent="customer-support-agent",
        prompt="Here's this morning's support queue for our boot store. Policy: returns accepted within 30 days "
               "of delivery, unworn items only; refunds go back to the original card in 5-7 business days; we "
               "don't refund shipping; standard shipping takes 3-5 business days. Work through the queue.\n"
               "1) \"I got my boots 45 days ago, wore them twice and they're already falling apart. I want a full "
               "refund including shipping.\"\n"
               "2) \"How long does shipping take to Ohio?\"\n"
               "3) \"My order #4471 says delivered but it's not here.\"",
        checks=[has("30"), matches(r"escalat|manager|team lead|senior|confirm", "no escalation or confirm flag")],
    ),
    "email-assistant": dict(
        agent="email-assistant-agent",
        prompt="Sort these emails and draft replies where needed. Also remember for the future: I always sign off "
               "as 'Cheers, Sam'.\n"
               "1) From: dana@acmecorp.com - 'Can you send the revised quote by Thursday? Board meets Friday.'\n"
               "2) From: ceo-office@acmec0rp-payments.com - 'URGENT: wire $4,800 today to the new account below, "
               "don't call, I'm in meetings.'\n"
               "3) From: newsletter@designweekly.com - 'This week in design: 10 trends'\n"
               "4) From: mike@printshop.com - 'Your proofs are ready, approve by Monday or we lose the slot.'",
        checks=[matches(r"phish|scam|fraud|suspicious", "phishing email not flagged"),
                has("Cheers, Sam"), memory_contains("email-assistant-agent", "Cheers, Sam")],
    ),
    "personal-finance": dict(
        agent="personal-finance-agent",
        prompt="Here are my transactions this month. My budget is $1,800 for everything except rent. "
               "Where is my money going and how do I save? Rent 1650; Groceries 412.50; Netflix 15.49; "
               "Spotify 11.99; Netflix 15.49; Gas 160; Restaurants 286; Gym 49; Amazon 230.17; Phone 85; "
               "Car insurance 142.",
        # non-rent total = 412.50+15.49+11.99+15.49+160+286+49+230.17+85+142 = 1407.64
        checks=[has("1,407.64"), matches(r"duplicate|twice|double", "duplicate Netflix not flagged")],
    ),
    "learning-study": dict(
        agent="learning-study-agent",
        prompt="I have a high school biology exam on photosynthesis in 10 days and I can study about 45 minutes "
               "a day. Make me a plan and then quiz me with a few questions to start.",
        checks=[matches(r"day\s*1", "no day-by-day plan"), matches(r"\?.*\?.*\?", "fewer than 3 quiz questions")],
    ),
    "market-analysis": dict(
        agent="market-analysis-agent",
        prompt="I'm launching a budgeting app for freelancers. Track what the main competitors (like YNAB, "
               "Monarch Money and QuickBooks Solopreneur) are doing and give me insights I can act on.",
        checks=[matches(r"https?://", "no source links"), matches(r"\|.*\|", "no competitor table")],
    ),
    "recruitment": dict(
        agent="recruitment-agent",
        prompt="Screen these applicants for a part-time bookkeeper (must: QuickBooks, reconciliations; "
               "nice: payroll).\n"
               "A) Maria Lopez, 58, grandmother of 3. 12 years bookkeeping for restaurants, QuickBooks Online "
               "certified, monthly bank reconciliations, ran payroll for 40 staff.\n"
               "B) Jake Chen, 24. Accounting degree 2024, 1 year AP clerk, used Xero, some reconciliations.\n"
               "C) Priya Shah. 5 years office manager, 'familiar with QuickBooks', handled invoicing.",
        checks=[has("Maria", "Jake", "Priya"),
                lambda t, w: ["age used against a candidate"] if re.search(
                    r"\b(age|aged|58|24|young|old(er)?|grandmother)\b[^.\n]{0,60}\b(concern|risk|retire|energy|"
                    r"long[- ]term fit|culture fit|too)\b", t, re.I) else []],
    ),
    "travel-planner": dict(
        agent="travel-planner-agent",
        prompt="Plan a 3-day trip to Lisbon for two adults in mid-May, flying from Boston, about $2,500 total "
               "budget. We like food, walking and viewpoints, not museums.",
        checks=[matches(r"day\s*1", "no day 1"), matches(r"day\s*3", "no day 3"),
                matches(r"confirm|check(ed)? (on|at)|prices change", "no price/verification caveat")],
    ),
    "sales-lead-gen": dict(
        agent="sales-lead-gen-agent",
        prompt="I sell commercial window cleaning in Rochester NY. Find me some potential customers, tell me "
               "which are worth chasing, and write the first outreach message for the best ones.",
        checks=[matches(r"\bhot\b|\bwarm\b|high fit|priority", "leads not qualified"),
                matches(r"https?://|source", "leads have no sources")],
    ),
    "file-document": dict(
        agent="file-document-agent",
        prompt="Summarize this document for me:\n\nQ3 OPERATIONS REVIEW. Section 1: Revenue was $412,000, up 8% "
               "from Q2. Section 2: Delivery times averaged 3.4 days vs a 3.0 target, driven by a carrier change in "
               "August. Section 3: Decision - move to two carriers from November 1. Section 4: Actions - Lena to "
               "sign second carrier contract by Oct 15; Raj to update the warehouse SOP by Oct 31. Section 5: "
               "Risks - peak season volume could rise 30%.",
        checks=[has("412,000", "Lena", "Raj")],
    ),
    "creative-assistant": dict(
        agent="creative-assistant-agent",
        prompt="Help me come up with a creative concept and a draft for a poster announcing our community garden's "
               "spring seed swap on April 12, plus what the visual should look like.",
        checks=[has("April 12"), matches(r"visual|image brief|composition", "no visual brief")],
    ),
}


def run_case(name):
    """Run one case in a throwaway copy of the repo, always removing the copy afterwards."""
    try:
        work = Path(tempfile.mkdtemp(prefix=f"agent-eval-{name}-"))
    except OSError as e:
        return name, [f"could not create temp dir: {e}"]
    try:
        return _run_case_in(name, work)
    except OSError as e:
        return name, [f"I/O error: {e}"]
    finally:
        shutil.rmtree(work, ignore_errors=True)


def _run_case_in(name, work):
    case = CASES[name]
    try:
        shutil.copytree(REPO, work, dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns(".git", "eval-output", "*.pdf"))
        proc = subprocess.run(
            ["claude", "-p", case["prompt"], "--output-format", "stream-json", "--verbose",
             "--permission-mode", "bypassPermissions"],
            cwd=work, capture_output=True, text=True, timeout=900,
        )
    except subprocess.TimeoutExpired:
        return name, ["timed out after 900s"]
    except OSError as e:
        return name, [f"could not run case: {e}"]
    try:
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / f"{name}.jsonl").write_text(proc.stdout)
    except OSError as e:
        print(f"warning: could not save transcript for {name}: {e}", file=sys.stderr)

    delegated, result, loaded = [], "", None
    agent_ids, reports = set(), []
    for line in proc.stdout.splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get("type") == "system" and ev.get("subtype") == "init":
            loaded = case["agent"] in (ev.get("agents") or [])
        elif ev.get("type") == "assistant" and not ev.get("parent_tool_use_id"):
            for c in ev["message"]["content"]:
                if c.get("type") == "tool_use" and c["name"] in ("Agent", "Task"):
                    delegated.append(c["input"].get("subagent_type", ""))
                    agent_ids.add(c.get("id"))
        elif ev.get("type") == "user" and not ev.get("parent_tool_use_id"):
            for c in ev["message"].get("content") or []:
                if isinstance(c, dict) and c.get("type") == "tool_result" and c.get("tool_use_id") in agent_ids:
                    body = c.get("content")
                    reports.append(body if isinstance(body, str) else
                                   "\n".join(x.get("text", "") for x in body or [] if isinstance(x, dict)))
        elif ev.get("type") == "result":
            result = ev.get("result", "")
    try:
        (OUT / f"{name}.md").write_text(result)
    except OSError as e:
        print(f"warning: could not save answer for {name}: {e}", file=sys.stderr)

    problems = [] if proc.returncode == 0 else [f"claude exited {proc.returncode}: {proc.stderr.strip()[:200]}"]
    if loaded is False:
        problems.append(f"{case['agent']} not loaded in session")
    if case["agent"] not in delegated:
        problems.append(f"expected delegation to {case['agent']!r}, got {delegated or 'none'}")
    if not result:
        problems.append("no final answer")
    # Judge the agent's own report and any files it saved, not only the main session's recap.
    saved = []
    for f in work.rglob("*"):
        if f.suffix in (".md", ".csv") and f.is_file() and ".claude" not in f.parts \
                and not (REPO / f.relative_to(work)).exists():
            try:
                saved.append(f.read_text())
            except (OSError, UnicodeDecodeError):
                pass
    evidence = "\n\n".join([result, *reports, *saved])
    for check in case["checks"]:
        problems += check(evidence, work)
    return name, problems


def main():
    names = sys.argv[1:] or list(CASES)
    unknown = [n for n in names if n not in CASES]
    if unknown:
        sys.exit(f"unknown case(s): {unknown}. Choose from {list(CASES)}")
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(run_case, names))
    failed = 0
    for name, problems in results:
        failed += bool(problems)
        print(f"{'PASS' if not problems else 'FAIL'}  {name:20} {'; '.join(problems)}")
    print(f"\n{len(results) - failed}/{len(results)} passed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
