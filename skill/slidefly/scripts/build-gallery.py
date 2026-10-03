"""Build a gallery page of every style (thumbnails + filters + links to demo decks).

Usage: python build-gallery.py <out_dir> [--rebuild]

Reads assets/styles/index.json: [{"slug","name","scheme","mood":[...],"best_for","fonts"}, ...]
For style number N (1-based, index order) the demo deck is <out_dir>/NN_demo-<slug>.html.
- Missing demo (or --rebuild): built from templates/deck-mau.html + the style, then inlined.
- Thumbnails of slide 1 and slide 4 go to <out_dir>/anh/<slug>-1.jpg, -4.jpg.
- Writes <out_dir>/00-gallery.html.
"""
import html
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from playwright.sync_api import sync_playwright

SK = Path(__file__).resolve().parent.parent
PY = sys.executable
FREEZE = """() => { const s = document.createElement('style');
  s.textContent = '*,*::before,*::after{transition-duration:0s!important;transition-delay:0s!important;animation:none!important}';
  document.head.append(s); }"""


def build_demo(slug: str, dest: Path) -> None:
    tmp = SK / "templates" / f"_gallery-{slug}.html"
    src = (SK / "templates" / "deck-mau.html").read_text(encoding="utf-8")
    tmp.write_text(src.replace("styles/swiss-modern.css", f"styles/{slug}.css"), encoding="utf-8")
    try:
        subprocess.run([PY, str(SK / "scripts" / "inline-assets.py"), str(tmp), str(dest)], check=True, capture_output=True)
    finally:
        shutil.move(str(tmp), str(Path(tempfile.gettempdir()) / tmp.name))  # works across drives; never delete


def card(i: int, st: dict, demo: str) -> str:
    tags = " ".join(f'<span class="tag">{html.escape(m)}</span>' for m in st.get("mood", []))
    return f"""<a class="card" href="{demo}" data-scheme="{st['scheme']}" data-text="{html.escape(' '.join([st['name'], *st.get('mood', []), st.get('best_for', '')]).lower())}">
  <div class="thumb"><img src="anh/{st['slug']}-1.jpg" alt=""><img class="alt" src="anh/{st['slug']}-4.jpg" alt=""></div>
  <div class="meta"><b>{i:02d}. {html.escape(st['name'])}</b> <code>{st['slug']}</code>
  <p>{html.escape(st.get('best_for', ''))}</p><div>{tags}</div><small>{html.escape(st.get('fonts', ''))}</small></div></a>"""


PAGE = """<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Thư viện style SlideFly</title><style>
:root{--bg:#f4f2ee;--fg:#1b1b1b;--muted:#666;--card:#fff;--line:#ddd}
@media (prefers-color-scheme:dark){:root{--bg:#141414;--fg:#eee;--muted:#999;--card:#1f1f1f;--line:#333}}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,sans-serif}
header{padding:24px 16px 8px;max-width:1400px;margin:auto}h1{margin:0 0 6px;font-size:26px}
.bar{display:flex;gap:8px;flex-wrap:wrap;align-items:center}.bar button,.bar input{font:inherit;padding:6px 12px;border:1px solid var(--line);border-radius:20px;background:var(--card);color:var(--fg);cursor:pointer}
.bar button.on{background:var(--fg);color:var(--bg)}.bar input{min-width:220px;cursor:text}
main{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px;padding:16px;max-width:1400px;margin:auto}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden;color:inherit;text-decoration:none;display:block}
.thumb{position:relative;aspect-ratio:16/9;background:#000}.thumb img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:opacity .3s}
.thumb .alt{opacity:0}.card:hover .alt{opacity:1}.meta{padding:10px 12px}.meta p{margin:4px 0;color:var(--muted)}
code{font-size:12px;color:var(--muted)}.tag{display:inline-block;font-size:12px;padding:1px 8px;margin:2px 4px 2px 0;border-radius:10px;border:1px solid var(--line)}small{color:var(--muted)}
</style></head><body><header><h1>Thư viện style SlideFly</h1>
<p>__COUNT__ style. Rê chuột để xem slide nội dung, bấm để mở deck demo (mũi tên để chuyển slide).</p>
<div class="bar"><button class="on" data-f="all">Tất cả</button><button data-f="dark">Nền tối</button><button data-f="light">Nền sáng</button><button data-f="mixed">Pha trộn</button>
<input id="q" placeholder="Tìm: công nghệ, sang trọng, vui..."></div></header><main>__CARDS__</main>
<script>let f='all';const cards=[...document.querySelectorAll('.card')],q=document.getElementById('q');
function apply(){const t=q.value.trim().toLowerCase();cards.forEach(c=>{c.style.display=(f==='all'||c.dataset.scheme===f)&&(!t||c.dataset.text.includes(t))?'':'none'})}
document.querySelectorAll('.bar button').forEach(b=>b.onclick=()=>{document.querySelectorAll('.bar button').forEach(x=>x.classList.remove('on'));b.classList.add('on');f=b.dataset.f;apply()});q.oninput=apply;</script>
</body></html>"""


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    sys.stdout.reconfigure(encoding="utf-8")
    out = Path(sys.argv[1]).resolve()
    (out / "anh").mkdir(parents=True, exist_ok=True)
    rebuild = "--rebuild" in sys.argv
    styles = json.loads((SK / "assets" / "styles" / "index.json").read_text(encoding="utf-8"))
    cards = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 720}, reduced_motion="no-preference")
        for i, st in enumerate(styles, 1):
            slug = st["slug"]
            if not (SK / "assets" / "styles" / f"{slug}.css").is_file():
                print(f"skip {slug}: no css")
                continue
            demo = out / f"{i:02d}_demo-{slug}.html"
            if rebuild or not demo.is_file():
                build_demo(slug, demo)
            page.goto(demo.as_uri())
            page.wait_for_function("window.deck && deck.count > 0", timeout=8000)
            page.wait_for_timeout(1800)
            page.evaluate(FREEZE)
            for n in (1, 4):
                page.evaluate(f"deck.go({n - 1})")
                page.wait_for_timeout(150)
                page.screenshot(path=str(out / "anh" / f"{slug}-{n}.jpg"), type="jpeg", quality=72)
            cards.append(card(i, st, demo.name))
            print(f"ok {i:02d} {slug}")
        browser.close()
    page_html = PAGE.replace("__COUNT__", str(len(cards))).replace("__CARDS__", "\n".join(cards))
    (out / "00-gallery.html").write_text(page_html, encoding="utf-8")
    print(f"Gallery: {out / '00-gallery.html'} ({len(cards)} styles)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
