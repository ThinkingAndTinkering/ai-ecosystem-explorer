"""Builds handbook.pdf from handbook.md.
Pipeline: pandoc (gfm+smart -> HTML body) -> editorial print template ->
DOM post-processing (cover, takeaway boxes, figure/sidebar styling) ->
headless Chromium print-to-PDF with page numbers.
Run from project root: python3 verify/build_pdf.py
"""
import subprocess, os, time
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
body = subprocess.run(
    ["pandoc", os.path.join(ROOT, "handbook.md"), "-f", "gfm+smart-tex_math_dollars", "-t", "html"],
    capture_output=True, text=True, check=True).stdout

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,420;9..144,560;9..144,640&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');
:root{ --ink:#23262e; --dim:#5a5e66; --faint:#8f9097; --hair:#d8d3c6; --wash:#f4f1ea;
  --accent:#56648f; --gold:#8a734a;
  --l0:#7c97b5; --l1:#7da794; --l2:#9a8cb5; --l3:#b48794; --l4:#c0a468; --l5:#8aa179; }
*{box-sizing:border-box}
html{-webkit-print-color-adjust:exact; print-color-adjust:exact}
body{font-family:'Source Serif 4',Georgia,serif; font-size:10pt; line-height:1.62; color:var(--ink);
  margin:0; font-kerning:normal; text-rendering:optimizeLegibility}
p{margin:0 0 8pt; orphans:3; widows:3}
strong{font-weight:600}
a{color:var(--accent); text-decoration:none; word-break:break-all}

h1{font-family:Fraunces,serif; font-weight:560; font-size:23pt; line-height:1.15; letter-spacing:.005em;
  margin:0 0 14pt; padding-bottom:10pt; border-bottom:2pt solid var(--ink); break-after:avoid; page-break-before:always}
h2{font-family:Fraunces,serif; font-weight:560; font-size:14.5pt; line-height:1.25; margin:18pt 0 7pt; break-after:avoid}
h3{font-family:Inter,sans-serif; font-weight:600; font-size:10.5pt; letter-spacing:.04em; margin:14pt 0 6pt; break-after:avoid}
h4{font-family:'JetBrains Mono',monospace; font-size:8pt; letter-spacing:.18em; text-transform:uppercase;
  color:var(--faint); margin:12pt 0 5pt; break-after:avoid}

hr{border:none; border-top:.5pt solid var(--hair); margin:14pt 0}
hr.hide{display:none}

ul,ol{margin:0 0 9pt; padding-left:16pt}
li{margin:0 0 3.5pt}
li::marker{color:var(--gold)}

blockquote{margin:10pt 0 12pt; padding:9pt 12pt; background:var(--wash);
  border:.5pt solid var(--hair); border-left:2.5pt solid var(--l0); border-radius:3pt;
  break-inside:avoid; font-size:9.2pt; line-height:1.55}
blockquote p{margin:0 0 5pt} blockquote p:last-child{margin:0}
blockquote.figure{border-left-color:var(--l4)}
blockquote.figure::before{content:"SUGGESTED VISUAL"; display:block; font-family:'JetBrains Mono',monospace;
  font-size:6.8pt; letter-spacing:.2em; color:var(--gold); margin-bottom:4pt}
blockquote.sidebar{border-left-color:var(--l1); background:#f0f3ef}

div.takeaways{margin:14pt 0 4pt; padding:11pt 14pt 7pt; background:#eef0f4;
  border:.5pt solid var(--hair); border-radius:4pt; break-inside:avoid}
div.takeaways h3{margin:0 0 6pt; font-family:Fraunces,serif; font-size:11.5pt; font-weight:640}
div.takeaways ul{margin:0; padding-left:14pt}
div.takeaways li{font-size:9.3pt}

table{border-collapse:collapse; width:100%; margin:10pt 0 12pt; font-size:8.2pt; line-height:1.45;
  font-family:Inter,sans-serif}
th{font-family:'JetBrains Mono',monospace; font-size:6.9pt; letter-spacing:.1em; text-transform:uppercase;
  text-align:left; color:var(--dim); border-bottom:1pt solid var(--ink); padding:4pt 6pt; background:var(--wash)}
td{border-bottom:.5pt solid var(--hair); padding:4.5pt 6pt; vertical-align:top}
tr{break-inside:avoid}

code{font-family:'JetBrains Mono',monospace; font-size:8.3pt; background:var(--wash); padding:0 2.5pt; border-radius:2pt}

ol.refs{column-count:2; column-gap:18pt; font-size:7.4pt; line-height:1.5; font-family:Inter,sans-serif; color:var(--dim); padding-left:14pt}
ol.refs li{break-inside:avoid; margin-bottom:3pt}

/* cover */
.cover{height:9.15in; display:flex; flex-direction:column; align-items:center; justify-content:center;
  text-align:center; page-break-after:always}
.cover .kick{font-family:'JetBrains Mono',monospace; font-size:8.5pt; letter-spacing:.38em;
  text-transform:uppercase; color:var(--accent); margin-bottom:22pt}
.cover h1.t{font-family:Fraunces,serif; font-weight:300; font-size:41pt; line-height:1.08; border:none;
  margin:0 0 10pt; padding:0; page-break-before:avoid}
.cover .sub{font-family:Fraunces,serif; font-size:15pt; font-weight:420; color:var(--dim); margin-bottom:26pt}
.cover .bars{display:flex; gap:6pt; margin-bottom:26pt}
.cover .bars i{width:34pt; height:5pt; border-radius:99pt}
.cover .ed{font-family:Inter,sans-serif; font-size:9.5pt; color:var(--dim); line-height:1.8; max-width:4.6in}
.cover .fine{margin-top:40pt; font-family:'JetBrains Mono',monospace; font-size:6.8pt;
  letter-spacing:.16em; text-transform:uppercase; color:var(--faint); line-height:2}
.contents-page{page-break-before:always}
"""

TEMPLATE = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="cover">
  <div class="kick">From sand · to chips · to clouds · to minds</div>
  <h1 class="t">Understanding<br>the AI Ecosystem</h1>
  <div class="sub">A Beginner&rsquo;s Handbook</div>
  <div class="bars"><i style="background:var(--l0)"></i><i style="background:var(--l1)"></i><i style="background:var(--l2)"></i><i style="background:var(--l3)"></i><i style="background:var(--l4)"></i><i style="background:var(--l5)"></i></div>
  <div class="ed">The companies, supply chains, money flows, and ideas behind artificial intelligence — explained from first principles, with no background assumed.<br><br><b>Second (expanded) edition · June 2026</b> &nbsp;·&nbsp; market data as of June 11–12, 2026<br>61 companies · 10 layers · companion to the interactive <i>AI Ecosystem Explorer</i> &amp; <i>The $725 Billion Machine</i></div>
  <div class="fine">~17,500 words · ~150 referenced sources · 18 suggested visuals<br>Educational use only · not investment advice</div>
</div>
{body}
</body></html>"""

src = os.path.join(ROOT, "verify", "handbook_print.html")
open(src, "w").write(TEMPLATE)

POST = """
() => {
  // drop the markdown's own title block (the cover replaces it)
  const kill = [];
  let el = document.querySelector('.cover').nextElementSibling;
  while (el && !(el.tagName === 'H3' && el.textContent.trim() === 'Contents')) {
    kill.push(el); el = el.nextElementSibling;
    if (kill.length > 40) break;
  }
  // keep "About This Handbook" section: only remove up to (not incl.) the first H3 'About...'
  const about = kill.findIndex(e => e.tagName === 'H3' && /About This Handbook/.test(e.textContent));
  (about >= 0 ? kill.slice(0, about) : []).forEach(e => e.remove());

  // contents page break
  document.querySelectorAll('h3').forEach(h => {
    if (h.textContent.trim() === 'Contents') h.classList.add('contents-page');
  });

  // figure & sidebar blockquotes
  document.querySelectorAll('blockquote').forEach(b => {
    const t = b.textContent.trim();
    if (/^Figure \\d+/.test(t)) b.classList.add('figure');
    if (t.startsWith('📦')) b.classList.add('sidebar');
  });
  // sidebar paragraphs written outside blockquotes
  document.querySelectorAll('body > p').forEach(p => {
    if (p.textContent.trim().startsWith('📦')) {
      const bq = document.createElement('blockquote');
      bq.className = 'sidebar'; p.replaceWith(bq); bq.appendChild(p);
    }
  });

  // key-takeaways boxes: h3 starting with ✅ + following ul
  document.querySelectorAll('h3').forEach(h => {
    if (h.textContent.trim().startsWith('✅')) {
      const box = document.createElement('div'); box.className = 'takeaways';
      const ul = h.nextElementSibling;
      h.replaceWith(box); box.appendChild(h);
      if (ul && ul.tagName === 'UL') box.appendChild(ul);
    }
  });

  // compact two-column references (all <ol> after the References heading)
  const refH = [...document.querySelectorAll('h2')].find(h => /References/.test(h.textContent));
  if (refH) { let n = refH.nextElementSibling;
    while (n) { if (n.tagName === 'OL') n.classList.add('refs'); n = n.nextElementSibling; } }

  // hide hr immediately before a page-breaking h1
  document.querySelectorAll('hr').forEach(r => {
    const nx = r.nextElementSibling;
    if (nx && (nx.tagName === 'H1')) r.classList.add('hide');
  });
}
"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("file://" + src, wait_until="networkidle")
    page.evaluate(POST)
    page.evaluate("document.fonts.ready.then(()=>{})")
    time.sleep(2.5)
    page.pdf(
        path=os.path.join(ROOT, "handbook.pdf"),
        format="Letter", print_background=True,
        margin={"top": "0.72in", "bottom": "0.85in", "left": "0.85in", "right": "0.85in"},
        display_header_footer=True,
        header_template="<div></div>",
        footer_template="""<div style="width:100%;font-size:6.5px;color:#8f9097;
          font-family:Helvetica,Arial,sans-serif;letter-spacing:1.5px;
          padding:0 0.85in;display:flex;justify-content:space-between;">
          <span>UNDERSTANDING THE AI ECOSYSTEM &nbsp;·&nbsp; JUNE 2026</span>
          <span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>""",
    )
    browser.close()
print("PDF written:", os.path.join(ROOT, "handbook.pdf"))
