"""Build the style gallery page and the landing-page style shelf from the style index.

Usage: python site/build-gallery.py

Reads skill/slidefly/assets/styles/index.json and the demo decks gallery/NN_demo-<slug>.html, then writes
gallery/00-gallery.html (filter, search, copy-command buttons) and the #shelf block plus style counts in
index.html. Run it again after adding or retiring a style.
"""
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GAL = ROOT / 'gallery'
SHELF_FIRST = 12   # tiles shown before "Hiện cả N style"


def styles():
    idx = json.loads((ROOT / 'skill/slidefly/assets/styles/index.json').read_text(encoding='utf-8'))
    decks = {m.group(2): (int(m.group(1)), p.name) for p in GAL.glob('*_demo-*.html')
             if (m := re.match(r'(\d+)_demo-(.+)\.html$', p.name))}
    out = [dict(s, num=decks[s['slug']][0], deck=decks[s['slug']][1]) for s in idx if s['slug'] in decks]
    return sorted(out, key=lambda s: s['num'])


def card(s):
    e = html.escape
    mood = list(s.get('mood', [])) + (['hai lớp'] if s.get('art') else [])
    text = ' '.join([s['name'], s['slug'], *mood, s.get('best_for', ''), 'minh họa' if s.get('art') else '']).lower()
    tags = ' '.join(f'<span class="tag">{e(m)}</span>' for m in mood)
    return f'''<article class="card" data-scheme="{e(s['scheme'])}"{' data-art="1"' if s.get('art') else ''} data-text="{e(text)}">
  <a class="thumb" href="{e(s['deck'])}"><img src="anh/{e(s['slug'])}-1.jpg" alt="" loading="lazy"><img class="alt" src="anh/{e(s['slug'])}-4.jpg" alt="" loading="lazy"></a>
  <div class="meta"><a class="name" href="{e(s['deck'])}"><b>{s['num']:02d}. {e(s['name'])}</b></a> <code>{e(s['slug'])}</code>
  <p>{e(s.get('best_for', ''))}</p><div>{tags}</div><small>{e(s.get('fonts', ''))}</small>
  <div class="use"><button type="button" data-cmd="{e(s['slug'])}">Chép lệnh</button><button type="button" class="ghost" data-name="{e(s['slug'])}">Chép tên style</button></div></div></article>'''


PAGE = '''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Thư viện style SlideFly</title><style>
:root{--bg:#f4f2ee;--fg:#1b1b1b;--muted:#666;--card:#fff;--line:#ddd}
@media (prefers-color-scheme:dark){:root{--bg:#141414;--fg:#eee;--muted:#999;--card:#1f1f1f;--line:#333}}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.5 system-ui,sans-serif}
header{padding:24px 16px 8px;max-width:1400px;margin:auto}h1{margin:0 0 6px;font-size:26px}header p{margin:4px 0 12px}
.bar{display:flex;gap:8px;flex-wrap:wrap;align-items:center}.bar button,.bar input{font:inherit;padding:6px 12px;border:1px solid var(--line);border-radius:20px;background:var(--card);color:var(--fg);cursor:pointer}
.bar button.on{background:var(--fg);color:var(--bg)}.bar input{min-width:220px;cursor:text}#count{color:var(--muted);font-size:13px}
main{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px;padding:16px;max-width:1400px;margin:auto}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;overflow:hidden;display:flex;flex-direction:column}
.card a{color:inherit;text-decoration:none}.name:hover b{text-decoration:underline}
.thumb{position:relative;display:block;aspect-ratio:16/9;background:#000}.thumb img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:opacity .3s}
.thumb .alt{opacity:0}.card:hover .alt{opacity:1}.meta{padding:10px 12px;display:flex;flex-direction:column;gap:2px;flex:1}.meta p{margin:4px 0;color:var(--muted)}
code{font-size:12px;color:var(--muted)}.tag{display:inline-block;font-size:12px;padding:1px 8px;margin:2px 4px 2px 0;border-radius:10px;border:1px solid var(--line)}small{color:var(--muted)}
.use{display:flex;gap:8px;margin-top:auto;padding-top:10px}.use button{font:600 13px/1 system-ui,sans-serif;padding:8px 12px;border-radius:8px;border:1px solid var(--fg);background:var(--fg);color:var(--bg);cursor:pointer}
.use button.ghost{background:transparent;color:var(--fg);border-color:var(--line)}.use button:hover{opacity:.85}
.empty{grid-column:1/-1;color:var(--muted)}
.toast{position:fixed;left:50%;bottom:24px;transform:translate(-50%,20px);opacity:0;background:var(--fg);color:var(--bg);padding:10px 16px;border-radius:10px;font-size:14px;transition:.25s;pointer-events:none;max-width:calc(100% - 32px)}
.toast.show{opacity:1;transform:translate(-50%,0)}
</style></head><body><header><h1>Thư viện style SlideFly</h1>
<p>__TOTAL__ style (__ART__ style hai lớp có minh họa riêng từng slide). Rê chuột để xem slide nội dung, bấm ảnh để mở deck demo (mũi tên để chuyển slide). Bấm <b>Chép lệnh</b> rồi dán vào Claude Code, thay phần trong ngoặc vuông bằng chủ đề của bạn.</p>
<div class="bar"><button class="on" data-f="all">Tất cả</button><button data-f="art">Hai lớp, có minh họa</button><button data-f="dark">Nền tối</button><button data-f="light">Nền sáng</button><button data-f="mixed">Pha trộn</button>
<input id="q" placeholder="Tìm: công nghệ, sang trọng, Tết, giấy..."><span id="count"></span></div></header><main>
__CARDS__
<p class="empty" hidden>Chưa có style khớp. Thử "giấy", "tối", "Tết" hoặc "trẻ em".</p></main>
<div class="toast" id="toast" role="status"></div>
<script>let f='all';const cards=[...document.querySelectorAll('.card')],q=document.getElementById('q'),cnt=document.getElementById('count'),empty=document.querySelector('.empty');
const norm=s=>s.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').replace(/đ/g,'d');
cards.forEach(c=>c.dataset.n=norm(c.dataset.text));
function apply(){const t=norm(q.value.trim());let n=0;cards.forEach(c=>{const ok=!!(f==='all'||(f==='art'?c.dataset.art:c.dataset.scheme===f))&&(!t||c.dataset.n.includes(t));c.style.display=ok?'':'none';n+=ok});cnt.textContent=n+' / '+cards.length+' style';empty.hidden=n>0}
document.querySelectorAll('.bar button').forEach(b=>b.onclick=()=>{document.querySelectorAll('.bar button').forEach(x=>x.classList.remove('on'));b.classList.add('on');f=b.dataset.f;apply()});q.oninput=apply;apply();
const toast=document.getElementById('toast');function show(m){toast.textContent=m;toast.classList.add('show');clearTimeout(show.t);show.t=setTimeout(()=>toast.classList.remove('show'),2400)}
async function copy(text,msg){try{await navigator.clipboard.writeText(text);show(msg)}catch(e){window.prompt('Chép dòng này:',text)}}
document.querySelector('main').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;
if(b.dataset.cmd)copy(`/slidefly Làm [số] slide về [chủ đề của bạn], style ${b.dataset.cmd}`,'Đã chép lệnh, dán vào Claude Code và thay phần trong ngoặc vuông');
if(b.dataset.name)copy(b.dataset.name,'Đã chép tên style '+b.dataset.name)});</script>
</body></html>
'''


def tile(s, i):
    e = html.escape
    extra = ' extra' if i >= SHELF_FIRST else ''
    return (f'        <div class="tile{extra}"><a href="gallery/{e(s["deck"])}"><img src="gallery/anh/{e(s["slug"])}-1.jpg" alt="" loading="lazy" width="1280" height="720">'
            f'<span>{e(s["name"])}</span></a><button class="cp" type="button" data-cmd="{e(s["slug"])}" title="Chép lệnh dùng style {e(s["name"])}">Chép lệnh</button></div>')


def main():
    st = styles()
    total, art = len(st), sum(1 for s in st if s.get('art'))
    page = PAGE.replace('__TOTAL__', str(total)).replace('__ART__', str(art)).replace('__CARDS__', '\n'.join(card(s) for s in st))
    (GAL / '00-gallery.html').write_text(page, encoding='utf-8')
    land = ROOT / 'index.html'
    t = land.read_text(encoding='utf-8')
    shelf = '<div class="shelf" id="shelf">\n' + '\n'.join(tile(s, i) for i, s in enumerate(st)) + '\n      </div>'
    t, n = re.subn(r'<div class="shelf" id="shelf">.*?\n      </div>', lambda m: shelf, t, count=1, flags=re.S)
    assert n == 1, 'shelf block not found in index.html'
    t = re.sub(r'(?<![\w/_.-])\d{2,3}(?= style\b| bộ trang phục)', str(total), t)
    land.write_text(t, encoding='utf-8')
    print(f'gallery: {total} styles ({art} two-layer) -> {GAL / "00-gallery.html"}; shelf and counts -> {land}')


if __name__ == '__main__':
    main()
