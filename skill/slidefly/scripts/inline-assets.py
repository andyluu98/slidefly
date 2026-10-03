"""Inline local CSS/JS into one self-contained HTML file.

Usage: python inline-assets.py <input.html> <output.html>

- <link rel="stylesheet" href="x.css"> -> <style>...</style> (attribute order does not matter)
- <script src="x.js"></script>          -> <script>...</script>
- Remote URLs (http/https, e.g. Google Fonts) and anything inside <!-- comments --> are left untouched.
- Only .css / .js files located under the input file's folder or this skill's folder are inlined
  (protects against embedding arbitrary files from the machine into a deck you share).
- Refuses to overwrite the input file. Creates the output folder if needed.
Exit code: 0 ok, 1 error, 2 local references left in the output.
"""
import re
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
LINK_RE = re.compile(r"<link\b[^>]*>", re.I)
SCRIPT_RE = re.compile(r"<script\b([^>]*)>\s*</script>", re.I)


def attr(tag: str, name: str) -> str | None:
    m = re.search(rf'\b{name}\s*=\s*(["\'])(.*?)\1', tag, re.I | re.S)
    return m.group(2) if m else None


def is_remote(href: str) -> bool:
    return href.startswith(("http://", "https://", "//", "data:"))


def read_asset(base: Path, href: str, ext: str) -> str:
    path = Path(href)
    path = (path if path.is_absolute() else base / href).resolve()
    if path.suffix.lower() != ext:
        raise ValueError(f"Refusing to inline non-{ext} file: {path}")
    if not (path.is_relative_to(base.resolve()) or path.is_relative_to(SKILL_DIR)):
        raise ValueError(f"Refusing to inline file outside the deck folder or skill folder: {path}")
    if not path.is_file():
        raise FileNotFoundError(f"Asset not found: {path}")
    return path.read_text(encoding="utf-8")


def inline_part(html: str, base: Path) -> str:
    def css(m):
        tag = m.group(0)
        href = attr(tag, "href")
        if (attr(tag, "rel") or "").lower() != "stylesheet" or not href or is_remote(href):
            return tag
        code = read_asset(base, href, ".css").replace("</style", "<\\/style")
        return f"<style>\n{code}\n</style>"

    def js(m):
        src = attr(m.group(0), "src")
        if not src or is_remote(src):
            return m.group(0)
        # "</script" inside JS would close the tag early
        code = read_asset(base, src, ".js").replace("</script", "<\\/script")
        return f"<script>\n{code}\n</script>"

    return SCRIPT_RE.sub(js, LINK_RE.sub(css, html))


def inline(html: str, base: Path) -> str:
    """Process only the text between HTML comments."""
    out, pos = [], 0
    for m in COMMENT_RE.finditer(html):
        out += [inline_part(html[pos:m.start()], base), m.group(0)]
        pos = m.end()
    out.append(inline_part(html[pos:], base))
    return "".join(out)


def local_refs_left(html: str) -> list[str]:
    html = COMMENT_RE.sub("", html)
    refs = [attr(t, "href") for t in LINK_RE.findall(html) if (attr(t, "rel") or "").lower() == "stylesheet"]
    refs += [attr(m.group(0), "src") for m in SCRIPT_RE.finditer(html)]
    return [r for r in refs if r and not is_remote(r)]


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 1
    src, dst = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    if src == dst:
        print("Error: output must differ from input (back up and write to a new path).")
        return 1
    try:
        out = inline(src.read_text(encoding="utf-8"), src.parent)
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(out, encoding="utf-8")
    except (OSError, ValueError, UnicodeDecodeError) as err:
        print(f"Error: {err}")
        return 1
    left = local_refs_left(out)
    print(f"Wrote {dst} ({len(out):,} chars). Local refs left: {len(left)} {left if left else ''}")
    return 0 if not left else 2


if __name__ == "__main__":
    sys.exit(main())
