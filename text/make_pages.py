"""Wrap each built text email in an inbox-style preview page, plus an index."""
from pathlib import Path

HERE = Path(__file__).parent
FROM = "Jason at Crazy Creek &lt;jason@crazycreekresort.com&gt;"
# (email file, label, subject, preview text, kind, day, send dates, who gets it)
EMAILS = [
    ("e1", "E1", "Sled &amp; Stay Early Bird (from Jason)", "Early Bird pricing on Sled &amp; Stay", "Text", "Day 0", "Dec 2 / Dec 3", "Everyone"),
    ("e2a", "E2a", "which weekend are you thinking?", "I can tell you what's still open", "Text", "Day 4", "Dec 6 / Dec 7", "People who clicked E1"),
    ("e2b", "E2b", "Park the trailer at your cabin door", "Sled &amp; Stay, up to 30% off until Dec 20", "Designed", "Day 4", "Dec 6 / Dec 7", "People who didn't click E1"),
    ("e3", "E3", "the part of a sled trip people remember", "It happens after the ride", "Text", "Day 8", "Dec 10 / Dec 11", "Everyone still on the list"),
    ("dec17", "Dec 17", "3 days left on Early Bird", "Ends Sunday, December 20", "Designed", "Deadline", "Thu Dec 17", "Everyone still on the list"),
    ("dec17", "Dec 19", "Early Bird ends tomorrow", "Last chance to save up to 30%", "Designed", "Deadline", "Sat Dec 19", "People who didn't open Dec 17"),
    ("dec20", "Dec 20", "last day", "Early Bird ends tonight", "Text", "Deadline", "Sun Dec 20", "Everyone still on the list"),
]

CSS = """
:root{--night:#050e1d;--navy:#07132a;--card:#0b1d33;--ice:#f0f8ff;--dim:#b4c6d8;--cyan:#00c4e0;--line:#0c3346;--rule:#0a2234}
*{box-sizing:border-box} body{margin:0;background:var(--night);color:var(--ice);font:400 16px/1.65 'Open Sans','Segoe UI',Roboto,Arial,sans-serif}
::selection{background:var(--cyan);color:var(--night)} a{color:var(--cyan);text-underline-offset:4px}
a:focus-visible{outline:2px solid var(--cyan);outline-offset:3px;border-radius:6px}
.wrap{max-width:1080px;margin:0 auto;padding:36px 24px 64px}
.top{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap}
.logo{width:150px;height:auto;display:block}
.crumb{font:700 13px/18px 'JetBrains Mono',Consolas,monospace;letter-spacing:.08em;text-transform:uppercase}
h1{margin:28px 0 0;font:700 clamp(2.2rem,1.6rem + 2.6vw,3.4rem)/1.04 'Oswald','Arial Narrow',Arial,sans-serif;text-transform:uppercase}
h1 span{color:var(--cyan)} .lead{max-width:66ch;margin:16px 0 0;color:var(--dim);font-size:17px}
h2{margin:48px 0 0;font:700 26px/1.1 'Oswald','Arial Narrow',Arial,sans-serif;text-transform:uppercase}
.tag{display:inline-block;padding:1px 7px;border-radius:5px;font:700 12px/18px 'JetBrains Mono',Consolas,monospace;letter-spacing:.06em;text-transform:uppercase}
.t{border:1px solid var(--line);color:var(--dim)} .d{background:var(--cyan);color:var(--night)}
table{width:100%;margin-top:20px;border-collapse:separate;border-spacing:0;border:1px solid var(--line);border-radius:16px;overflow:hidden;font-size:15px}
th,td{padding:12px 16px;text-align:left;border-bottom:1px solid var(--rule);vertical-align:top}
th{font:700 13px/18px 'JetBrains Mono',Consolas,monospace;letter-spacing:.08em;text-transform:uppercase;color:var(--cyan);background:#06152a}
tr:last-child td{border-bottom:0} td.m{font-family:'JetBrains Mono',Consolas,monospace;color:var(--dim);white-space:nowrap}
.inbox{margin-top:28px;border:1px solid var(--line);border-radius:18px;overflow:hidden;background:linear-gradient(180deg,var(--card),var(--navy))}
.meta{margin:0;padding:18px 22px;display:grid;grid-template-columns:110px 1fr;gap:6px 14px;font-size:15px}
.meta dt{font:700 13px/22px 'JetBrains Mono',Consolas,monospace;letter-spacing:.06em;text-transform:uppercase;color:var(--cyan)}
.meta dd{margin:0} .subj{font-weight:700;color:#fff}
iframe{display:block;width:100%;border:0;background:#fff;min-height:420px}
.nav{display:flex;justify-content:space-between;gap:12px;margin-top:20px;font:700 15px/1 'Oswald','Arial Narrow',Arial,sans-serif;letter-spacing:.04em;text-transform:uppercase}
.note{margin-top:14px;color:var(--dim);font-size:14px}
footer{margin-top:48px;padding-top:18px;border-top:1px solid var(--rule);color:var(--dim);font:400 13px/20px 'JetBrains Mono',Consolas,monospace}
@media (max-width:620px){.wrap{padding:24px 16px 48px} .meta{grid-template-columns:1fr} .meta dt{margin-top:6px}
 table,thead,tbody,tr,th,td{display:block} thead{display:none} tr{border-bottom:1px solid var(--rule);padding:10px 0} td{border:0;padding:2px 14px}}
"""


def head(title):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex,nofollow">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Open+Sans:wght@400;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body><main class="wrap">
<div class="top"><img class="logo" src="../img/logo.png" width="150" height="40" alt="Crazy Creek Resort">
<span class="crumb"><a href="index.html">Text emails</a> &nbsp;&middot;&nbsp; <a href="../index.html">Newsletters</a></span></div>
"""


FOOT = """<footer>Crazy Creek Resort &middot; Sled &amp; Stay Early Bird 2026 &middot; Review copy, not for distribution</footer></main>
<script>for(const f of document.querySelectorAll('iframe')){f.addEventListener('load',()=>{try{f.style.height=f.contentDocument.documentElement.scrollHeight+'px'}catch(e){}})}</script>
</body></html>"""


def tag(kind):
    return '<span class="tag d">Designed</span>' if kind == "Designed" else '<span class="tag t">Text</span>'


slugs = ["dec19" if e[1] == "Dec 19" else e[0] for e in EMAILS]

for i, (f, code, subj, pre, kind, day, dates, who) in enumerate(EMAILS):
    prev = f'<a href="{slugs[i-1]}.html">&larr; {EMAILS[i-1][1]}</a>' if i else "<span></span>"
    nxt = f'<a href="{slugs[i+1]}.html">{EMAILS[i+1][1]} &rarr;</a>' if i < len(EMAILS) - 1 else "<span></span>"
    extra = '<p class="note">Same body as Dec 17, with a new subject. Goes only to people who did not open Dec 17.</p>' if code == "Dec 19" else ""
    html = head(f"{code}: {subj}") + f"""
<h1>{code}<br><span>{subj}</span></h1>
<p class="lead">{tag(kind)} &nbsp;{day} &middot; {dates} &middot; {who}</p>
<div class="inbox"><dl class="meta">
<dt>From</dt><dd>{FROM}</dd><dt>Subject</dt><dd class="subj">{subj}</dd><dt>Preview</dt><dd>{pre}</dd></dl>
<iframe src="emails/{f}.html" title="{code} email body"></iframe></div>
{extra}<p class="note">[First name] is filled in by Constant Contact, with "there" when the name is missing. Constant Contact adds the address and unsubscribe link at the bottom.</p>
<div class="nav">{prev}{nxt}</div>
""" + FOOT
    (HERE / f"{slugs[i]}.html").write_text(html, encoding="utf-8")

rows = "".join(
    f'<tr><td class="m">{day}</td><td>{tag(kind)} <a href="{slugs[i]}.html">{code}</a></td><td>{subj}</td><td>{who}</td><td class="m">{dates}</td></tr>'
    for i, (f, code, subj, pre, kind, day, dates, who) in enumerate(EMAILS))

index = head("Sled & Stay Text Emails") + f"""
<h1>Sled &amp; Stay<br><span>text emails from Jason</span></h1>
<p class="lead">The 4 automation emails and 3 deadline emails for Crazy Creek's past guests. They run alongside the 3 newsletters, one email every 2 days. Most are written as a short personal note from Jason, with one text link to the Early Bird page. Open each one to see the subject line, preview text and the email as it sends.</p>
<h2>The sequence</h2>
<table><thead><tr><th>When</th><th>Email</th><th>Subject</th><th>Who gets it</th><th>Batch 1 / 2+3</th></tr></thead><tbody>{rows}</tbody></table>
<p class="note">Newsletters N1, N2 and N3 go out on days 2, 6 and 10, between these. <a href="../index.html">See the newsletters</a>.</p>
""" + FOOT
(HERE / "index.html").write_text(index, encoding="utf-8")
print("pages:", slugs)
