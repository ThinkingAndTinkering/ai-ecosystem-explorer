"""Headless verification for the-machine.html (prototype 2).
Run: python3 -m http.server 8123 (project root), then python3 verify/check_machine.py
"""
import os, sys, time
from playwright.sync_api import sync_playwright

BASE = "http://localhost:8123/the-machine.html"
OUT = os.path.dirname(os.path.abspath(__file__))
errors = []

with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(viewport={"width": 1380, "height": 900}, device_scale_factor=2)
    pg = ctx.new_page()
    pg.on("console", lambda m: errors.append(f"console.{m.type}: {m.text}") if m.type == "error" else None)
    pg.on("pageerror", lambda e: errors.append(f"pageerror: {e}"))
    pg.goto(BASE, wait_until="networkidle", timeout=45000)
    time.sleep(1.5)
    pg.screenshot(path=f"{OUT}/m1-hero.png")

    # cards rendered?
    n = pg.locator("details.card").count()
    assert n == 61, f"expected 61 cards, got {n}"
    rows = pg.locator(".mrow").count()
    assert rows == 11, f"expected 11 machine rows (10 layers + totals), got {rows}"
    total = pg.text_content(".mrow.mtotal .mr .v")
    assert "T" in total, f"totals row value odd: {total}"
    # six hero stats are links into sections
    stats = pg.locator("a.stat").count()
    assert stats == 6, f"expected 6 linked hero stats, got {stats}"

    # power calculator interaction
    pg.locator("#power").scroll_into_view_if_needed(); time.sleep(0.8)
    pg.screenshot(path=f"{OUT}/m2-power.png")
    before = pg.text_content("#oGW")
    pg.eval_on_selector("#pCapex", "el => { el.value = 1400; el.dispatchEvent(new Event('input')) }")
    after = pg.text_content("#oGW")
    assert before != after, "power calc did not react to slider"

    # gap calculator: Burry mode should FAIL
    pg.eval_on_selector("#gLife", "el => { el.value = 2; el.dispatchEvent(new Event('input')) }")
    pg.eval_on_selector("#gGrow", "el => { el.value = 30; el.dispatchEvent(new Event('input')) }")
    time.sleep(0.3)
    v = pg.text_content("#gVerdict")
    assert "close" in v.lower() or "FAIL" in v, f"gap verdict odd: {v}"
    pg.locator("#gap").scroll_into_view_if_needed(); time.sleep(0.6)
    pg.screenshot(path=f"{OUT}/m3-gap.png")

    # layers + card expand
    pg.locator("#L6").scroll_into_view_if_needed(); time.sleep(0.6)
    pg.locator("#L6 details.card summary").first.click(); time.sleep(0.4)
    pg.screenshot(path=f"{OUT}/m4-power-layer.png")

    # dark mode
    pg.click("#themeBtn"); time.sleep(0.8)
    pg.screenshot(path=f"{OUT}/m5-dark.png")
    ctx.close()

    m = b.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True, has_touch=True)
    mp = m.new_page()
    mp.on("pageerror", lambda e: errors.append(f"mobile pageerror: {e}"))
    mp.goto(BASE, wait_until="networkidle", timeout=45000)
    time.sleep(1.5)
    mp.screenshot(path=f"{OUT}/m6-mobile.png")
    m.close(); b.close()

print("ERRORS:" if errors else "NO ERRORS")
for e in errors[:15]: print("  ", e[:300])
sys.exit(1 if errors else 0)
