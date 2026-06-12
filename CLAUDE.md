# AI Ecosystem Explorer

## Purpose
Two-part educational reference on the AI ecosystem, researched and current as of **June 11, 2026**:
1. **`handbook.md`** — "Understanding the AI Ecosystem: A Beginner's Handbook", **second (expanded) edition, June 12, 2026** (~17.7k words, 8 chapters, 18 figure suggestions, glossary, 149 references). Now matches the-machine's **10-layer / 61-company** universe: Ch3 has the ten-layer machine table with combined value + revenue run-rate columns (mirrors the-machine §05 exactly — update both together); Ch4 adds §4.9 Networking & Optics, §4.10 Systems & Data Centers, §4.11 Power Layer, storage duopoly inside §4.3, MPWR/updated QCOM in §4.8, NBIS/IREN in the neocloud sidebar. Section numbering: clouds = 4.12–4.15, apps = 4.16–4.18, labs = 4.19.
2. **`handbook.pdf`** — typeset print edition (**37 pp** Letter), built by `verify/build_pdf.py`: pandoc (gfm+smart−tex_math_dollars) → editorial HTML template (Fraunces/Source Serif 4) → Chromium print-to-PDF with cover, takeaway boxes, two-column references, page numbers. **Rebuild after any handbook.md edit.**
3. **`index.html`** — "AI Ecosystem Explorer" (prototype 1) — self-contained interactive 3D web app (Three.js + GSAP via CDN). Layered floating platforms (Equipment → Fabrication/Memory → Chips → Cloud → Models → Applications), 36 company nodes, ~55 typed dependency edges, guided tours, timeline, synced data table with CSV/JSON/PNG export, dark/light themes, mobile + reduced-motion support.
4. **`the-machine.html`** — "The $725 Billion Machine" (prototype 2) — interactive quantitative ESSAY in the style of andrewmccalip.com/space-datacenters (paper background, serif claims, mono numbers, slider calculators with PASS/FAIL verdicts, "⚠ STOP" technical divider). **Expanded universe: 61 companies in 10 layers**, adding Power & Energy (GEV, CEG, VST, NEE, TLN, OKLO), Networking & Optics (ANET, ALAB, COHR, CIEN, CRDO, LITE, APH), Systems & DCs (DELL, SMCI, CLS, VRT, ETN, EQIX, DLR), storage (WDC, STX), MPWR, and neoclouds (NBIS, IREN). Three live calculators: Power Wall (capex→GW→TWh→grid %), Revenue Gap (depreciation treadmill vs revenue growth, PASS/FAIL + SVG chart), per-query footprint. No 3D, no external JS libs — vanilla. Light default + dark toggle (localStorage). Verified by `verify/check_machine.py` (61-card assert, slider reactivity, Burry-mode FAIL check, mobile).
   - New-ticker caps are Jun 11–12, 2026 (some intraday); 12-mo perf badges only where verified. Researched via 3 agents (power; networking/optics; systems/storage/neoclouds) — flagged soft spots: Dell $51B backlog (call-sourced), NBIS Meta $27B (unverified value), Eaton +240% DC orders (call), intraday caps for WDC/STX/NBIS on a fast tape.
   - **Machine diagram (§05)** right column = two computed consistent metrics per layer: combined market value (from card caps; privates at last-round valuation; excludes SMIC/DeepSeek/in-parent labs) + combined revenue run-rate (the `REV` map in JS: latest qtr ×4 or FY guide, $B; whole-company figures — methodology note rendered under diagram). Totals row Σ ≈ $39.5T / ~$4.5T-yr. Hero stat strip = 6 anchors ("the argument in six numbers"), each linking to its section; 3×2 grid. If card caps change, the diagram sums update automatically; if revenues change, update `REV`.

## Design Language
Muted editorial palette (per user request — **no neon**): warm off-white ink `#e7e4db` on `#0d0f14` dark / ivory `#f4f1ea` light; layer colors steel `#7c97b5`, sage `#7da794`, dusty violet `#9a8cb5`, muted rose `#b48794`, old gold `#c0a468`, moss `#8aa179`. Low emissive (.3 dark/.2 light), soft halos, matte materials (roughness .5). Layer colors live in three places that must match: CSS `--l0..--l5`, JS `LAYERS[]`, JS `ETYPES`/`ERA_C`.

## Tech Stack
- Handbook: plain Markdown (render/print via pandoc: `pandoc handbook.md -o handbook.pdf --toc` or paste into Word/Docs).
- App: single HTML file. Three.js **0.160.0** via ES-module importmap (jsdelivr) + OrbitControls addon; GSAP **3.13.0** (cdnjs, global); Google Fonts (Fraunces, Inter, JetBrains Mono). No build step. Needs internet for CDNs.
- Verification: `verify/check.py` (Playwright headless Chromium) — loads the page, captures console errors, takes desktop + mobile screenshots into `verify/`.
- PDF: `verify/build_pdf.py` (pandoc + Playwright). Gotchas it works around: pandoc gfm enables `tex_math_dollars` by default (paired `$` amounts become math — disable it!); numbered lists not starting at 1 can't interrupt a paragraph (blank line required before each references group); cover div must be < 9.43in printable height or it spills a blank page.

## How to Run
- App: open `index.html` directly, or `python3 -m http.server 8123` in this directory → http://localhost:8123/
- Verify: `python3 verify/check.py` (requires `pip install playwright && playwright install chromium`).

## Data & Consistency Rules
- All market caps = **June 11, 2026 closes** (stockanalysis.com); private-lab valuations dated to their round. Latest reported quarters as of 2026-06-11 (e.g., NVDA Q1 FY27, MSFT FY26 Q3, Oracle Q4 FY26 reported 2026-06-10).
- Handbook and app **must stay in sync**: company metrics live in the app's `DATA` const and in handbook Ch. 4 — update both together.
- Sourcing came from 7 parallel research agents (chip designers; fabs/equipment/memory; hyperscalers; platforms/apps; AI labs; policy/geopolitics; economics/energy/adoption) hitting primary IR releases + Reuters/CNBC/TrendForce/IEA/Stanford HAI etc. Known soft spots are flagged inline ("company-stated", "reported") — e.g., Anthropic's $47B run-rate claim, NVIDIA–OpenAI $100B LOI status ("on ice").
- Figures dated "as of June 2026"; markets move — refresh before reuse.

## Architecture Notes (app)
- One `DATA` object: `layers[6]`, `companies[36]` (id, ticker, layer, metrics, strengths/risks, dependsOn), `edges` (typed: supply/fab/memory/compute/cloud/invest/model/owns), `milestones` (timeline 1950→2026), `tours` (3 guided camera flights).
- Scene: glass platforms + glowing sphere nodes sized by sqrt(market cap), bezier edges with animated flow particles, star field. Raycast hover/click → detail panel. GSAP camera flights for tours/focus.
- Reduced-motion path disables autorotate/particles/intro animation. PixelRatio capped at 2.

## Status
- Complete: research, handbook, app, verification harness. Not deployed (local file). Could be deployed as a Render/Netlify static site if wanted.

## TODOs / Known Issues
- Data snapshot will age; "as of" stamps included everywhere.
- PNG export uses `preserveDrawingBuffer` (slight perf cost, acceptable).
- Equipment-layer edges are representative, not exhaustive (noted in app footer).
