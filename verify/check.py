"""Headless verification for the AI Ecosystem Explorer.
Loads the page, exercises intro → search/select → table → tour, captures
console/page errors, and saves desktop + mobile screenshots into verify/.
Run: python3 -m http.server 8123 (in project root), then python3 verify/check.py
"""
import os, sys, time
from playwright.sync_api import sync_playwright

BASE = "http://localhost:8123/index.html"
OUT = os.path.dirname(os.path.abspath(__file__))
errors, warnings = [], []

with sync_playwright() as p:
    browser = p.chromium.launch()
    ctx = browser.new_context(viewport={"width": 1440, "height": 900}, device_scale_factor=2)
    page = ctx.new_page()
    page.on("console", lambda m: errors.append(f"console.{m.type}: {m.text}") if m.type == "error" else None)
    page.on("pageerror", lambda e: errors.append(f"pageerror: {e}"))

    page.goto(BASE, wait_until="networkidle", timeout=45000)
    time.sleep(2.5)
    page.screenshot(path=f"{OUT}/01-intro.png")

    page.click("#enterBtn")
    time.sleep(3.5)  # intro flight
    page.screenshot(path=f"{OUT}/02-scene.png")

    # search → select NVIDIA → panel
    page.fill("#search", "nvidia")
    time.sleep(0.6)
    page.click("#results button >> nth=0")
    time.sleep(2.0)
    page.screenshot(path=f"{OUT}/03-panel-nvda.png")
    name = page.text_content("#pName")
    assert name and "NVIDIA" in name, f"panel name wrong: {name}"

    # data table + sort
    page.keyboard.press("Escape")
    page.click("#btnTable")
    time.sleep(0.8)
    rows = page.locator("#dataTable tbody tr").count()
    assert rows == 36, f"expected 36 rows, got {rows}"
    page.screenshot(path=f"{OUT}/04-table.png")
    page.keyboard.press("Escape")

    # tour step 2
    page.click("#btnTours")
    time.sleep(0.5)
    page.click(".tourcard >> nth=0")
    time.sleep(1.2)
    page.click("#tourNext")
    time.sleep(2.2)
    page.screenshot(path=f"{OUT}/05-tour.png")
    page.click("#tourExit")

    # light theme
    page.click("#btnTheme")
    time.sleep(1.2)
    page.screenshot(path=f"{OUT}/06-light.png")
    ctx.close()

    # mobile
    mctx = browser.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2,
                               is_mobile=True, has_touch=True)
    mpage = mctx.new_page()
    mpage.on("pageerror", lambda e: errors.append(f"mobile pageerror: {e}"))
    mpage.goto(BASE, wait_until="networkidle", timeout=45000)
    time.sleep(2)
    mpage.click("#enterBtn")
    time.sleep(3)
    mpage.screenshot(path=f"{OUT}/07-mobile.png")
    mctx.close()
    browser.close()

print("ERRORS:" if errors else "NO ERRORS")
for e in errors[:20]:
    print("  ", e[:300])
sys.exit(1 if errors else 0)
