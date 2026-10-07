#!/usr/bin/env python3
"""Build one SVG sprite per collection.

A sprite packs every icon in a collection into a single file as <symbol>
elements, so a page loads one request and references icons with <use>:

    <svg><use href="sprites/instagram-web.svg#heart"/></svg>

Run from the repository root:

    python3 tools/build_sprites.py
"""
import os
import re
import sys
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "sprites")

COLLECTIONS = [
    ("instagram-web",    "icons/instagram/web"),
    ("instagram-vector", "icons/instagram/vector"),
    ("threads-web",      "icons/threads/web"),
]

VIEWBOX = re.compile(r'viewBox="([^"]+)"')
SVG_OPEN = re.compile(r"<svg\b[^>]*>", re.S)
SVG_CLOSE = re.compile(r"</svg\s*>\s*$", re.S)
XML_DECL = re.compile(r"<\?xml[^>]*\?>\s*", re.S)
COMMENT = re.compile(r"<!--.*?-->", re.S)


def symbol_id(filename: str) -> str:
    """Stable, URL-safe id derived from the original filename."""
    return os.path.splitext(filename)[0]


def inner(svg_text: str):
    """Return (viewBox, inner markup) for a single SVG file."""
    text = XML_DECL.sub("", svg_text)
    text = COMMENT.sub("", text)
    match = SVG_OPEN.search(text)
    if not match:
        return None, None
    box = VIEWBOX.search(match.group(0))
    body = text[match.end():]
    body = SVG_CLOSE.sub("", body)
    return (box.group(1) if box else None), body.strip()


def build(name: str, rel: str) -> int:
    directory = os.path.join(ROOT, rel)
    if not os.path.isdir(directory):
        print(f"  skipped (missing): {rel}", file=sys.stderr)
        return 0

    files = sorted(
        f for f in os.listdir(directory)
        if f.endswith(".svg") and not f.startswith((".", "_"))
    )
    symbols, skipped = [], 0
    for filename in files:
        with open(os.path.join(directory, filename), encoding="utf-8", errors="ignore") as fh:
            box, body = inner(fh.read())
        if not body:
            skipped += 1
            continue
        attrs = f' viewBox="{escape(box)}"' if box else ""
        symbols.append(f'<symbol id="{escape(symbol_id(filename))}"{attrs}>{body}</symbol>')

    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, f"{name}.svg")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(
            '<svg xmlns="http://www.w3.org/2000/svg" style="display:none" '
            'fill="currentColor">'
            + "".join(symbols)
            + "</svg>\n"
        )
    size = os.path.getsize(path) / 1024
    note = f" ({skipped} skipped)" if skipped else ""
    print(f"  {name:<18} {len(symbols):>4} symbols  {size:>6.0f} KB{note}")
    return len(symbols)


def main():
    print("Building sprites…")
    total = sum(build(name, rel) for name, rel in COLLECTIONS)
    print(f"\n{total} symbols across {len(COLLECTIONS)} sprites in sprites/")


if __name__ == "__main__":
    main()
