"""Check a SlideFly deck in headless Chrome (Playwright).

Usage: python check-deck.py <deck.html> [out_dir]

- Captures console errors.
- Runs deck.audit() (needs morph-audit.js in the deck) and prints the fill report.
- Screenshots every slide in its FINAL pose (transitions disabled) and
  builds one contact sheet <out_dir>/sheet.jpg to review the whole deck at once.
Exit code: 0 = all OK, 1 = audit asks for fixes or console errors, 2 = usage/load error.
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

NO_MOTION = """
() => {
  const r = document.documentElement.style;
  r.setProperty('--morph-dur', '0s'); r.setProperty('--reveal-base', '0s'); r.setProperty('--fade-dur', '0s');
  const s = document.createElement('style');
  s.textContent = '*,*::before,*::after{transition-duration:0s!important;transition-delay:0s!important;animation:none!important}';
  document.head.append(s);
}
"""

# What the active slide is built from: a UI mock (with its side), a drawn diagram, or its layout.
COMPONENT = """
() => {
  const s = document.querySelector('.deck-stage > .slide.active');
  const m = s.querySelector('.mock');
  if (m) {
    const r = m.getBoundingClientRect(), b = s.getBoundingClientRect();
    const kind = [...m.classList].find((c) => c.startsWith('mock-')) || 'mock';
    return `khung ${kind.slice(5)} bên ${r.left + r.width / 2 < b.left + b.width / 2 ? 'trái' : 'phải'}`;
  }
  const v = s.querySelector('.viz[data-viz]');
  return v ? `sơ đồ ${v.dataset.viz}` : `kiểu ${s.dataset.kind || s.dataset.layout || 'content'}`;
}
"""


def repeats(parts, run=3):
    """Runs of `run`+ consecutive slides built the same way (a deck that feels like one slide on repeat)."""
    out, start = [], 0
    for i in range(1, len(parts) + 1):
        if i == len(parts) or parts[i] != parts[start]:
            if i - start >= run:
                out.append(f"slide {start + 1}-{i}: {i - start} slide liền cùng {parts[start]}")
            start = i
    return out


def contact_sheet(shots, out_file, cols=2, w=640, h=360, gap=12):
    """Combine slide screenshots into one numbered image (Pillow optional)."""
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        return None
    rows = (len(shots) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * (w + gap) + gap, rows * (h + gap) + gap), "#888")
    draw = ImageDraw.Draw(sheet)
    for i, shot in enumerate(shots):
        x, y = gap + (i % cols) * (w + gap), gap + (i // cols) * (h + gap)
        with Image.open(shot) as im:
            sheet.paste(im.resize((w, h)), (x, y))
        draw.rectangle([x, y, x + 34, y + 24], fill="black")
        draw.text((x + 8, y + 6), str(i + 1), fill="white")
    sheet.save(out_file, quality=82)
    return out_file


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    sys.stdout.reconfigure(encoding="utf-8")  # Vietnamese output on any Windows code page
    deck = Path(sys.argv[1]).resolve()
    out_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else deck.parent / f"_check-{deck.stem}"
    out_dir.mkdir(parents=True, exist_ok=True)
    errors, warnings = [], []

    def on_console(m):
        if m.type != "error":
            return
        url = (m.location or {}).get("url", "")
        # offline: Google Fonts failing is a warning (fallback fonts), not a deck bug
        (warnings if "fonts.g" in url or "fonts.g" in m.text else errors).append(m.text)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 720}, reduced_motion="no-preference")
        page.on("console", on_console)
        page.on("pageerror", lambda e: errors.append(str(e)))
        try:
            page.goto(deck.as_uri(), wait_until="load")
            page.evaluate("document.fonts.ready")
            page.wait_for_function("window.deck && deck.count > 0", timeout=5000)
        except Exception as err:  # noqa: BLE001 - report any load failure plainly
            print(f"Load error: {err}")
            browser.close()
            return 2
        page.wait_for_timeout(1800)  # let the opening fly-in finish before freezing motion
        page.evaluate(NO_MOTION)
        count = page.evaluate("deck.count")
        report = page.evaluate("deck.audit ? deck.audit() : []")

        shots, parts = [], []
        for i in range(count):
            page.evaluate(f"deck.go({i})")
            page.wait_for_timeout(120)
            parts.append(page.evaluate(COMPONENT))
            shot = out_dir / f"{i + 1:02d}.jpg"
            page.screenshot(path=str(shot), type="jpeg", quality=80)
            shots.append(shot)
        browser.close()

    print(f"Deck: {deck.name} ({count} slides)")
    bad = [r for r in report if r["status"] != "OK"]
    for r in report:
        print(f"  {r['slide']:>2} {r['layout']:<9} {r['density']:<2} dọc {r['gapY']:>4} ngang {r['gapX']:>4}  {r['status']} {r['issues']}")
    if not report:
        errors.append("deck.audit missing: add morph-audit.js after morph-engine.js")
    for w in warnings:
        print(f"  WARNING (font): {w}")
    for r in repeats(parts):  # a hint, not a failure: vary the component, its side or the layout
        print(f"  NHÀM: {r}")
    for e in errors:
        print(f"  CONSOLE ERROR: {e}")
    sheet = contact_sheet(shots, out_dir / "sheet.jpg")
    print(f"Screenshots: {out_dir}" + (f" | sheet: {sheet}" if sheet else ""))
    print("RESULT: " + ("OK" if not bad and not errors else f"FIX {len(bad)} slide(s), {len(errors)} error(s)"))
    return 0 if not bad and not errors else 1


if __name__ == "__main__":
    sys.exit(main())
