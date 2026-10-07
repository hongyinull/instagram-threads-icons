#!/usr/bin/env python3
"""Regenerate icons.json and the index embedded in index.html.

Run from the repository root:

    python3 tools/build_manifest.py
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

COLLECTIONS = [
    # label,            platform,    variant,  path,                      extension
    ("Instagram Web",    "instagram", "web",    "icons/instagram/web",    ".svg"),
    ("Instagram iOS",    "instagram", "ios",    "icons/instagram/ios",    ".png"),
    ("Instagram Vector", "instagram", "vector", "icons/instagram/vector", ".svg"),
    ("Threads Web",      "threads",   "web",    "icons/threads/web",      ".svg"),
]

PREFIXES = re.compile(r"^(IGDS|FBNucleus|Barcelona|Comet)")


def slugify(stem: str, variant: str) -> str:
    """Turn a Meta filename into a lowercase, searchable slug."""
    if variant == "ios":
        s = re.sub(r"^ig_icon_", "", stem)
        s = re.sub(r"@3x$", "", s)
        return s.replace("_", "-")
    s = PREFIXES.sub("", stem)
    s = re.sub(r"(Pano|Icon)$", "", s).replace("Pano", "")
    s = re.sub(r"(?<!^)(?=[A-Z])", "-", s)
    s = re.sub(r"(?<=[A-Za-z])(?=\d)", "-", s)
    return re.sub(r"-+", "-", s).strip("-").lower()


def parse(slug: str):
    """Split a slug into its base name, style and point size."""
    style = "filled" if "filled" in slug else ("outline" if "outline" in slug else None)
    match = re.search(r"-(\d+)$", slug)
    size = int(match.group(1)) if match else None
    base = re.sub(r"-\d+$", "", slug)
    base = re.sub(r"-(outline|filled)$", "", base)
    return base, style, size


def view_box(path: str):
    with open(path, encoding="utf-8", errors="ignore") as fh:
        match = re.search(r'viewBox="([^"]+)"', fh.read(400))
    return match.group(1) if match else None


def collect():
    icons, index = [], {}
    for label, platform, variant, rel, ext in COLLECTIONS:
        directory = os.path.join(ROOT, rel)
        if not os.path.isdir(directory):
            print(f"  skipped (missing): {rel}", file=sys.stderr)
            continue
        files = sorted(
            f for f in os.listdir(directory)
            if f.endswith(ext) and not f.startswith((".", "_"))
        )
        index[label] = {"path": rel, "files": files}
        for name in files:
            stem = name[: -len(ext)]
            slug = slugify(stem, variant)
            base, style, size = parse(slug)
            icon = {
                "name": base,
                "slug": slug,
                "file": name,
                "path": f"{rel}/{name}",
                "platform": platform,
                "variant": variant,
                "format": ext.lstrip("."),
            }
            if style:
                icon["style"] = style
            if size:
                icon["size"] = size
            if ext == ".svg":
                box = view_box(os.path.join(directory, name))
                if box:
                    icon["viewBox"] = box
            icons.append(icon)
        print(f"  {label:<18} {len(files):>5}")
    return icons, index


def write_manifest(icons):
    path = os.path.join(ROOT, "icons.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(
            {"version": 1, "count": len(icons), "icons": icons},
            fh, ensure_ascii=False, separators=(",", ":"),
        )
    return path


def write_index(index):
    """Replace the embedded data block in index.html."""
    path = os.path.join(ROOT, "index.html")
    if not os.path.exists(path):
        return None
    html = open(path, encoding="utf-8").read()
    payload = json.dumps(index, ensure_ascii=False, separators=(",", ":"))
    html, count = re.subn(
        r"window\.__ICONS__ = .*?;\n",
        f"window.__ICONS__ = {payload};\n",
        html, count=1, flags=re.S,
    )
    if not count:
        print("  index.html: data block not found, left untouched", file=sys.stderr)
        return None
    open(path, "w", encoding="utf-8").write(html)
    return path


def main():
    print("Collecting icons…")
    icons, index = collect()
    manifest = write_manifest(icons)
    page = write_index(index)
    unique = len({i["name"] for i in icons})
    print(f"\n{len(icons)} icons, {unique} unique names")
    print(f"  wrote {os.path.relpath(manifest, ROOT)}")
    if page:
        print(f"  wrote {os.path.relpath(page, ROOT)}")


if __name__ == "__main__":
    main()
