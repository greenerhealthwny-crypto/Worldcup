"""Functional evals for the business prompt skills.

Runs each case through headless Claude Code (`claude -p`) in this repo, with a
natural request that does NOT name the skill, then checks:
  1. the expected skill was invoked (Skill tool call), and
  2. case-specific checks on the final answer.

Run: python3 tests/run_skill_evals.py [case-name ...]
Transcripts are written to tests/eval-output/ (git-ignored).
"""
import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "tests" / "eval-output"


def words(s):
    return len(re.findall(r"\b[\w'’-]+\b", s))


def sections(text):
    """Split an answer into chunks on markdown headings / bold labels / horizontal rules."""
    return [c.strip() for c in re.split(r"\n(?=#{1,4} |\*\*[^*\n]+\*\*\s*\n|---)", text) if c.strip()]


def no(*phrases):
    return lambda t: [f"contains banned phrase: {p!r}" for p in phrases if p.lower() in t.lower()]


def no_in_email(*phrases):
    """Like no(), but only inspects the email body (greeting to sign-off), not Claude's notes."""
    def check(t):
        m = re.search(r"\n(Hi|Hey|Hello|Dear)\b.*?(?=\n---|\Z)", t, re.S)
        body = m.group(0) if m else t
        return [f"email contains banned phrase: {p!r}" for p in phrases if p.lower() in body.lower()]
    return check


def has(*phrases):
    return lambda t: [f"missing: {p!r}" for p in phrases if p.lower() not in t.lower()]


def max_words_in_email(limit):
    """Body between the greeting ('Hi ...') and the sign-off must be under `limit` words."""
    def check(t):
        m = re.search(r"\n(Hi|Hey|Hello)\b.*?(?=\n\s*(\[Your name\]|\[Name\]|Thanks|Best|Cheers|—|---))", t, re.S)
        if not m:
            return ["could not locate email body"]
        n = words(m.group(0))
        return [] if n < limit else [f"email body {n} words (limit {limit})"]
    return check


CASES = {
    "cold-email": dict(
        skill="cold-email-replies",
        prompt="Write a cold email to the head of operations at a mid-size logistics company. "
               "I'm offering fractional bookkeeping.",
        checks=[max_words_in_email(100)],
    ),
    "complaint": dict(
        skill="complaint-reply",
        prompt="A customer just emailed us this: \"This is the third time my order has arrived late and "
               "nobody has answered my last two emails. I'm done with you guys.\" We sell coffee beans on "
               "subscription. Help me write back.",
        checks=[no("we apologize for any inconvenience", "valued customer", "per our policy")],
    ),
    "meeting-notes": dict(
        skill="meeting-notes-action-items",
        prompt="Raw notes from today's team sync: - website relaunch slipping, Priya to send new copy by Fri "
               "- Tom asked about hiring a contractor for photos, no decision - need to renew domain before it "
               "lapses (someone) - Sam will chase the Acme invoice - next sync moved to Thursday. "
               "Can you pull out who's doing what?",
        checks=[has("Priya", "Sam", "Acme")],
    ),
    "ghosted-prospect": dict(
        skill="lost-deal-follow-up",
        prompt="A prospect went silent after our demo two weeks ago. They liked the reporting feature but said "
               "budget was tight until Q1. What should I send them?",
        checks=[],
    ),
    "swot": dict(
        skill="swot-analysis",
        prompt="Do a SWOT on my business: a two-person bakery in Buffalo NY that sells sourdough at two "
               "farmers markets and to three cafes wholesale. No storefront, $180k revenue last year.",
        checks=[has("strength", "weakness", "opportunit", "threat")],
    ),
    "zapier": dict(
        skill="zapier-workflow-from-plain-english",
        prompt="When someone fills out our Typeform contact form I want them added to HubSpot, a Slack "
               "message posted in #leads, and if their budget answer is over $10k, an email sent to me. "
               "How do I set that up in Zapier?",
        checks=[has("trigger", "filter")],
    ),
    "expenses": dict(
        skill="expense-report-summary",
        prompt="Here are this month's expenses, can you organize them for my accountant? Rent 2000; "
               "Canva 15; Google Workspace 36; QuickBooks 90; Facebook ads 750; Google ads 500; "
               "client lunch 85; flight to Denver 1240; office chair 410; Facebook ads 750.",
        checks=[has("5,876"),  # grand total
                lambda t: [] if re.search(r"duplicate|twice|double", t, re.I) else ["repeated Facebook ads charge not flagged"]],
    ),
    "rejection": dict(
        skill="candidate-rejection-email",
        prompt="I need to turn down a candidate for our marketing coordinator role. She did really well in the "
               "final round but we went with someone who had more paid-ads experience. Draft the email.",
        checks=[no_in_email("keep your cv on file", "keep your resume on file", "we will keep your")],
    ),
    "influencer": dict(
        skill="influencer-outreach-email",
        prompt="Draft an email to a fitness micro-influencer (about 40k followers on Instagram) asking them to "
               "collaborate on the launch of our plant-based protein bar.",
        checks=[max_words_in_email(120)],
    ),
    "stress-test": dict(
        skill="business-model-stress-test",
        prompt="Poke holes in my business model: I run a meal-prep delivery service, $129/week subscriptions, "
               "220 subscribers, one commercial kitchen I rent, 70% of signups come from Instagram ads.",
        checks=[has("40%")],
    ),
}


def run_case(name):
    case = CASES[name]
    proc = subprocess.run(
        ["claude", "-p", case["prompt"], "--output-format", "stream-json", "--verbose",
         "--permission-mode", "bypassPermissions"],
        cwd=REPO, capture_output=True, text=True, timeout=600,
    )
    OUT.mkdir(exist_ok=True)
    (OUT / f"{name}.jsonl").write_text(proc.stdout)
    skills_called, result = [], ""
    for line in proc.stdout.splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get("type") == "assistant":
            for c in ev["message"]["content"]:
                if c.get("type") == "tool_use" and c["name"] == "Skill":
                    skills_called.append(c["input"].get("skill", "").split(":")[-1])
        elif ev.get("type") == "result":
            result = ev.get("result", "")
    (OUT / f"{name}.md").write_text(result)
    problems = []
    if case["skill"] not in skills_called:
        problems.append(f"expected skill {case['skill']!r}, called {skills_called or 'none'}")
    if not result:
        problems.append("no final answer")
    for check in case["checks"]:
        problems += check(result)
    return name, problems


def main():
    names = sys.argv[1:] or list(CASES)
    with ThreadPoolExecutor(max_workers=5) as pool:
        results = list(pool.map(run_case, names))
    failed = 0
    for name, problems in results:
        status = "PASS" if not problems else "FAIL"
        failed += bool(problems)
        print(f"{status}  {name:18} {'; '.join(problems)}")
    print(f"\n{len(results) - failed}/{len(results)} passed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
