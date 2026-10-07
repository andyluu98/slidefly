"""SlideFly -> PPTX: a CSS background stack as one SVG picture (PowerPoint 365 draws SVG as vectors).

Handles what the 57 styles use for paper, grids, stripes, dot screens and stamps: background-color, linear and
repeating-linear gradients, radial gradients, inline SVG data URIs (nested <svg>, PowerPoint skips <image> data URIs),
background-size / -position / -repeat, an SVG mask (mask / -webkit-mask), border-radius, clip-path polygon and border.
"""
import base64
import math
import re
from urllib.parse import unquote

from pptx_css import color, px, resolve, split_top

N = [0]


def _id(p):
    N[0] += 1
    return f'{p}{N[0]}'


def _col(v, tok):
    c = color(resolve(v, [tok])) if v else None
    return c or ('000000', 0)


def _stops(args, tok, length):
    """'color [pos [pos]]' list -> [(offset 0..1, hex, alpha)] with CSS defaults for missing positions."""
    raw = []
    for a in args:
        m = re.match(r'(.+?)((?:\s+-?[\d.]+(?:px|%)?){0,2})\s*$', a.strip())
        c, pos = (m.group(1), m.group(2).split()) if m else (a, [])
        hexa = _col(c.strip(), tok)
        ps = [(px(p) / 100 * length if p.endswith('%') else px(p)) for p in pos] or [None]
        raw += [(p, hexa) for p in ps]
    if raw[0][0] is None:
        raw[0] = (0, raw[0][1])
    if raw[-1][0] is None:
        raw[-1] = (length, raw[-1][1])
    out, last = [], 0
    for i, (p, c) in enumerate(raw):   # missing positions: spread evenly between known neighbours
        if p is None:
            j = next(k for k in range(i, len(raw)) if raw[k][0] is not None)
            p = last + (raw[j][0] - last) / (j - i + 1)
        p = max(p, last)
        out.append((p, c))
        last = p
    return [(p / length if length else 0, c[0], c[1]) for p, c in out]


def _grad_xml(gid, kind, stops, attrs):
    st = ''.join(f'<stop offset="{max(0, min(1, o)):.4f}" stop-color="#{h}" stop-opacity="{a:.3f}"/>' for o, h, a in stops)
    return f'<{kind} id="{gid}" gradientUnits="userSpaceOnUse" {attrs}>{st}</{kind}>'


def _angle(first):
    sides = {'to top': 0, 'to right': 90, 'to bottom': 180, 'to left': 270, 'to top right': 45, 'to right top': 45,
             'to bottom right': 135, 'to right bottom': 135, 'to bottom left': 225, 'to left bottom': 225, 'to top left': 315, 'to left top': 315}
    f = first.strip()
    if f in sides:
        return sides[f], True
    m = re.fullmatch(r'(-?[\d.]+)(deg|turn|rad)', f)
    if m:
        v = float(m.group(1))
        return (v * 360 if m.group(2) == 'turn' else math.degrees(v) if m.group(2) == 'rad' else v), True
    return 180, False


def _svg_doc(url):
    """data:image/svg+xml URL -> (viewBox, preserveAspectRatio, inner markup) or None."""
    m = re.match(r"""url\(\s*['"]?data:image/svg\+xml(;base64)?,(.*?)['"]?\s*\)$""", url.strip(), re.S)
    if not m:
        return None
    text = base64.b64decode(m.group(2)).decode('utf-8', 'ignore') if m.group(1) else unquote(m.group(2))
    root = re.search(r'<svg\b([^>]*)>(.*)</svg>', text, re.S)
    if not root:
        return None
    vb = re.search(r'viewBox=["\']([^"\']+)', root.group(1))
    par = re.search(r'preserveAspectRatio=["\']([^"\']+)', root.group(1))
    if not vb:
        w, h = (re.search(rf'{k}=["\']([\d.]+)', root.group(1)) for k in ('width', 'height'))
        vb = f'0 0 {w.group(1) if w else 100} {h.group(1) if h else 100}'
    return (vb if isinstance(vb, str) else vb.group(1)), (par.group(1) if par else 'xMidYMid meet'), root.group(2)


def _tile(defs, layer, tw, th, tok):
    """One background layer drawn in a tw x th tile -> markup (gradients go to defs)."""
    doc = _svg_doc(layer) if layer.startswith('url(') else None
    if doc:
        vb, par, inner = doc
        return f'<svg x="0" y="0" width="{tw:.2f}" height="{th:.2f}" viewBox="{vb}" preserveAspectRatio="{par}">{inner}</svg>'
    m = re.match(r'(repeating-)?(linear|radial)-gradient\((.*)\)$', layer.strip(), re.S)
    if not m:
        return ''
    rep, kind, args = bool(m.group(1)), m.group(2), split_top(m.group(3))
    gid = _id('g')
    if kind == 'linear':
        ang, has = _angle(args[0])
        args = args[1:] if has else args
        rad = math.radians(ang)
        length = abs(tw * math.sin(rad)) + abs(th * math.cos(rad))
        if rep:   # one period, laid out along x, turned to the gradient angle
            pos =[px(p) for a in args for p in re.findall(r'(-?[\d.]+px)', a)]
            period = max(pos) if pos else 10
            stops = _stops(args, tok, period)
            pid = _id('p')
            defs.append(_grad_xml(gid, 'linearGradient', stops, f'x1="0" y1="0" x2="{period}" y2="0"'))
            defs.append(f'<pattern id="{pid}" patternUnits="userSpaceOnUse" width="{period}" height="{period}" '
                        f'patternTransform="rotate({ang - 90:.2f})"><rect width="{period}" height="{period}" fill="url(#{gid})"/></pattern>')
            return f'<rect width="{tw:.2f}" height="{th:.2f}" fill="url(#{pid})"/>'
        stops = _stops(args, tok, length)
        dx, dy = math.sin(rad) * length / 2, -math.cos(rad) * length / 2
        defs.append(_grad_xml(gid, 'linearGradient', stops,
                              f'x1="{tw / 2 - dx:.2f}" y1="{th / 2 - dy:.2f}" x2="{tw / 2 + dx:.2f}" y2="{th / 2 + dy:.2f}"'))
        return f'<rect width="{tw:.2f}" height="{th:.2f}" fill="url(#{gid})"/>'
    head = args[0] if not re.match(r'\s*(#|rgb|hsl|var|transparent|color-mix|[a-z]+\s+[\d.]+(px|%))', args[0]) or ' at ' in args[0] else ''
    args = args[1:] if head else args
    at = re.search(r'at\s+(\S+)\s*(\S+)?', head)
    cx = (px(at.group(1)) / 100 * tw if at.group(1).endswith('%') else px(at.group(1))) if at else tw / 2
    cy = (px(at.group(2)) / 100 * th if at and at.group(2) and at.group(2).endswith('%') else px(at.group(2)) if at and at.group(2) else th / 2)
    far = max(math.hypot(cx - x, cy - y) for x in (0, tw) for y in (0, th))
    pos = [px(p) for a in args for p in re.findall(r'(-?[\d.]+px)', a)]
    r = max(pos) if pos and all('%' not in a for a in args) else far
    defs.append(_grad_xml(gid, 'radialGradient', _stops(args, tok, r), f'cx="{cx:.2f}" cy="{cy:.2f}" r="{max(r, 0.1):.2f}"'))
    return f'<rect width="{tw:.2f}" height="{th:.2f}" fill="url(#{gid})"/>'


def _size(v, w, h):
    parts = (v or 'auto').split()
    if parts[0] in ('cover', 'contain', 'auto') and len(parts) == 1:
        return w, h
    def one(p, full):
        return full if p == 'auto' else px(p) / 100 * full if p.endswith('%') else px(p)
    return one(parts[0], w), one(parts[1] if len(parts) > 1 else 'auto', h)


def _pos(v, w, h, tw, th):
    parts = (v or '0 0').replace('left', '0%').replace('top', '0%').replace('right', '100%').replace('bottom', '100%').replace('center', '50%').split()
    parts += ['50%'] * (2 - len(parts))
    one = lambda p, full, t: (full - t) * px(p) / 100 if p.endswith('%') else px(p)  # noqa: E731
    return one(parts[0], w, tw), one(parts[1], h, th)


def background_svg(d, tok, w, h):
    """CSS declarations of a box (actor or stage) -> SVG markup, or None when it is one plain colour."""
    g = lambda k: resolve(d.get(k, ''), [d, tok]).strip()  # noqa: E731
    bg = g('background')
    imgs = g('background-image')
    if not imgs and re.search(r'gradient\(|url\(', bg):
        imgs = ', '.join(p.strip() for p in split_top(bg) if re.search(r'gradient\(|url\(', p))
    mask = g('mask') or g('-webkit-mask')
    if not imgs and 'url(' not in mask:
        return None
    w, h = max(w, 1), max(h, 1)
    base = g('background-color') or (bg if bg and not re.search(r'gradient\(|url\(', bg) else '')
    defs, body = [], ''
    if base:
        c = _col(base, tok)
        body += f'<rect width="{w:.2f}" height="{h:.2f}" fill="#{c[0]}" fill-opacity="{c[1]:.3f}"/>'
    layers = [re.match(r'((?:repeating-)?(?:linear|radial)-gradient\(.*\)|url\(.*?\))', s.strip(), re.S) for s in split_top(imgs)]
    sizes, poss, reps = (split_top(g(k)) or [''] for k in ('background-size', 'background-position', 'background-repeat'))
    pad = px(g('padding')) if g('background-origin') == 'content-box' else 0
    for i in reversed(range(len(layers))):   # the first CSS layer is on top
        if not layers[i]:
            continue
        pick = lambda lst: lst[i % len(lst)].strip() if lst else ''  # noqa: E731
        bw, bh = w - 2 * pad, h - 2 * pad
        tw, th = _size(pick(sizes), bw, bh)
        x0, y0 = _pos(pick(poss), bw, bh, tw, th)
        tile = _tile(defs, layers[i].group(1), tw, th, tok)
        rep = pick(reps) or 'repeat'
        if rep == 'no-repeat' or (tw >= bw and th >= bh):
            body += f'<g transform="translate({x0 + pad:.2f},{y0 + pad:.2f})">{tile}</g>'
        else:
            pid = _id('t')
            defs.append(f'<pattern id="{pid}" patternUnits="userSpaceOnUse" x="{x0 + pad:.2f}" y="{y0 + pad:.2f}" width="{tw:.2f}" height="{th:.2f}">{tile}</pattern>')
            body += f'<rect x="{pad}" y="{pad}" width="{bw:.2f}" height="{bh:.2f}" fill="url(#{pid})"/>'
    doc = _svg_doc(re.match(r'(url\(.*?\))', mask, re.S).group(1)) if 'url(' in mask else None
    if doc:
        mid = _id('m')
        defs.append(f'<mask id="{mid}" maskUnits="userSpaceOnUse" x="0" y="0" width="{w:.2f}" height="{h:.2f}">'
                    f'<svg width="{w:.2f}" height="{h:.2f}" viewBox="{doc[0]}" preserveAspectRatio="{doc[1]}" fill="#fff">{doc[2]}</svg></mask>')
        body = f'<g mask="url(#{mid})">{body}</g>'
    rad = g('border-radius')
    clip = re.search(r'polygon\(([^)]*)\)', g('clip-path'))
    if clip or (rad and px(rad) > 0):
        cid = _id('c')
        if clip:
            pts = ' '.join(f'{(px(a) / 100 * w if a.endswith("%") else px(a)):.2f},{(px(b) / 100 * h if b.endswith("%") else px(b)):.2f}'
                           for a, b in (p.split()[:2] for p in clip.group(1).split(',')))
            shape = f'<polygon points="{pts}"/>'
        else:
            r = min(w, h) / 2 if '%' in rad and px(rad) >= 40 else min(px(rad), min(w, h) / 2)
            shape = f'<rect width="{w:.2f}" height="{h:.2f}" rx="{r:.2f}"/>'
        defs.append(f'<clipPath id="{cid}">{shape}</clipPath>')
        body = f'<g clip-path="url(#{cid})">{body}</g>'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:.2f}" height="{h:.2f}" viewBox="0 0 {w:.2f} {h:.2f}">'
            f'<defs>{"".join(defs)}</defs>{body}</svg>')
