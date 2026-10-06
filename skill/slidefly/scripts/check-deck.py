"""Check a SlideFly deck in headless Chrome (Playwright).

Usage: python check-deck.py <deck.html> [out_dir]

- Captures console errors; runs deck.audit() (needs morph-audit.js) and prints the fill report.
- Screenshots every slide in its FINAL pose and builds one contact sheet <out_dir>/sheet.jpg.
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
  if (s.dataset.frame) return `khung ${s.dataset.frame}`;
  return v ? `sơ đồ ${v.dataset.viz}` : `kiểu ${s.dataset.kind || s.dataset.layout || 'content'}`;
}
"""


# Text lying on other text on the active slide (a title over a highlight, a label over a caption).
# Left out: decoration (aria-hidden), svg labels, faded or hidden text, the before/after compare diagram
# (two stacked panels by design) and anything marked data-layer (a stamp laid over a figure on purpose).
OVERLAP = """
() => {
  const s = document.querySelector('.deck-stage > .slide.active'), lines = [], out = [];
  const w = document.createTreeWalker(s, NodeFilter.SHOW_TEXT);
  while (w.nextNode()) {
    const n = w.currentNode, el = n.parentElement;
    if (!n.textContent.trim() || el.closest('[aria-hidden="true"], svg, [data-layer], .viz[data-viz="compare"]')) continue;
    let o = 1; for (let e = el; e && e !== s; e = e.parentElement) o *= +getComputedStyle(e).opacity;
    if (o < 0.3 || getComputedStyle(el).visibility === 'hidden') continue;
    const r = document.createRange(); r.selectNodeContents(n);
    // a line box is taller than its letters (big type above all): keep the band the glyphs really use
    for (const q of r.getClientRects()) if (q.width > 4 && q.height > 4) {
      const b = { left: q.left, right: q.right, top: q.top + q.height * 0.25, bottom: q.bottom - q.height * 0.2 };
      b.height = b.bottom - b.top;
      lines.push({ el, b, t: n.textContent.trim().slice(0, 22) });
    }
  }
  for (let i = 0; i < lines.length; i++) for (let j = i + 1; j < lines.length; j++) {
    const A = lines[i], B = lines[j];
    if (A.el === B.el || A.el.contains(B.el) || B.el.contains(A.el)) continue;
    const x = Math.min(A.b.right, B.b.right) - Math.max(A.b.left, B.b.left);
    const y = Math.min(A.b.bottom, B.b.bottom) - Math.max(A.b.top, B.b.top);
    if (x > 6 && y > Math.min(A.b.height, B.b.height) * 0.4 && out.length < 3) out.push(`"${A.t}" đè "${B.t}"`);
  }
  return out;
}
"""


# Composition of an inner slide: its data-frame, or the default "title top-left, body block" grid.
# Display slides (cover, chapter, quote...) are their own compositions and are not counted.
FRAME = """
() => {
  const s = document.querySelector('.deck-stage > .slide.active');
  const shown = ['cover', 'section', 'quote', 'closing', 'photo', 'chapter', 'qa', 'statement', 'cta', 'big-number', 'portrait-quote', 'split-photo'];
  // a drawn diagram shapes its slide itself, so it does not count toward the default grid
  if (shown.includes(s.dataset.kind || s.dataset.layout) || (!s.dataset.frame && s.querySelector('.viz[data-viz]'))) return null;
  return s.dataset.frame || 'mặc định';
}
"""


def crowded(frames, share=1 / 3, min_inner=12):
    """One composition on more than a third of the inner slides of a long deck."""
    inner = [f for f in frames if f]
    if len(inner) < min_inner:
        return []
    out = []
    for f in sorted(set(inner)):
        n = inner.count(f)
        if n > len(inner) * share:
            out.append(f"khung {f}: {n}/{len(inner)} slide bên trong (nên dưới 1/3, đổi vài slide sang data-frame khác)")
    return out


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

        shots, parts, frames = [], [], []
        for i in range(count):
            page.evaluate(f"deck.go({i})")
            page.wait_for_timeout(120)
            parts.append(page.evaluate(COMPONENT))
            frames.append(page.evaluate(FRAME))
            hit = page.evaluate(OVERLAP)
            if hit:  # a real defect: counts like an audit finding
                report.append({"slide": i + 1, "layout": "", "density": "", "gapY": "", "gapX": "", "status": "SỬA",
                               "issues": "chữ đè chữ: " + "; ".join(hit)})
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
    for r in crowded(frames):
        print(f"  NHÀM: {r}")
    for e in errors:
        print(f"  CONSOLE ERROR: {e}")
    sheet = contact_sheet(shots, out_dir / "sheet.jpg")
    print(f"Screenshots: {out_dir}" + (f" | sheet: {sheet}" if sheet else ""))
    print("RESULT: " + ("OK" if not bad and not errors else f"FIX {len(bad)} slide(s), {len(errors)} error(s)"))
    return 0 if not bad and not errors else 1


if __name__ == "__main__":
    sys.exit(main())
