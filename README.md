<div align="center">

# Meta Icons

**The icon set behind Instagram and Threads — extracted, organised and searchable.**

[![Icons](https://img.shields.io/badge/icons-2%2C055-black?style=flat-square)](#whats-inside)
[![Unique](https://img.shields.io/badge/unique%20names-965-black?style=flat-square)](#whats-inside)
[![Format](https://img.shields.io/badge/format-SVG%20%2B%20PNG-black?style=flat-square)](#whats-inside)
[![License](https://img.shields.io/badge/code-MIT-black?style=flat-square)](LICENSE)
[![Browse](https://img.shields.io/badge/browse-online-black?style=flat-square)](https://hongyinull.github.io/meta-icons/)

<img src="previews/hero.png" width="760" alt="A grid of Instagram icons: heart, camera, home, search, direct, comment, save, settings and more">

[**Browse all icons →**](https://hongyinull.github.io/meta-icons/)

</div>

---

Meta has never published the icon set used in Instagram and Threads. Their design system (IGDS) is internal, and the assets are scattered across web bundles and app resource archives, under names nobody can search.

This repository collects **2,055 icons** — **965 unique symbols** across outline and filled styles — and gives them consistent names, a machine-readable manifest, and a search page that works offline.

## Install

```bash
# Clone
git clone https://github.com/hongyinull/meta-icons.git

# Or download a single icon
curl -O https://raw.githubusercontent.com/hongyinull/meta-icons/main/icons/instagram/web/IGDSHeartPanoOutlineIcon.svg
```

## Usage

Every SVG uses `fill="currentColor"`, so icons inherit the text colour of their container — no editing required.

```html
<!-- Inherits the parent's colour -->
<span style="color: #e1306c">
  <img src="icons/instagram/web/IGDSHeartPanoFilledIcon.svg" width="24" alt="Like">
</span>
```

```css
/* Inline SVGs recolour with plain CSS */
.icon { width: 24px; height: 24px; color: currentColor; }
.icon:hover { color: #e1306c; }
```

```jsx
// React — inline the SVG to make it themeable
import { ReactComponent as Heart } from './icons/instagram/web/IGDSHeartPanoOutlineIcon.svg'

<Heart className="w-6 h-6 text-neutral-500" />
```

For iOS, the PNGs are `@3x`. Drop them into an Asset Catalog and Xcode will pick up the scale from the filename.

## What's inside

| Collection | Path | Count | Format |
|---|---|---:|---|
| Instagram Web | `icons/instagram/web/` | 322 | SVG |
| Instagram iOS | `icons/instagram/ios/` | 1,483 | PNG `@3x` |
| Instagram Vector | `icons/instagram/vector/` | 24 | SVG |
| Threads Web | `icons/threads/web/` | 226 | SVG |

Icons that fail to render are kept in `_broken/` inside each collection rather than deleted, so nothing is silently lost.

### Naming

Files keep their original Meta names so you can trace them back to the source. The searchable, normalised names live in [`icons.json`](icons.json):

```json
{
  "name": "heart",
  "slug": "heart-outline-24",
  "file": "ig_icon_heart_outline_24@3x.png",
  "path": "icons/instagram/ios/ig_icon_heart_outline_24@3x.png",
  "platform": "instagram",
  "variant": "ios",
  "format": "png",
  "style": "outline",
  "size": 24
}
```

Original prefixes, for reference:

- `IGDS…` — Instagram Design System (web)
- `Barcelona…` — Threads (internal codename)
- `ig_icon_<name>_<style>_<size>` — Instagram iOS

Styles are `outline` and `filled`. Sizes are in points: 10, 12, 16, 18, 20, 24, 44.

### Query the manifest

```bash
# Every filled heart icon
jq '.icons[] | select(.name=="heart" and .style=="filled") | .path' icons.json

# Everything available at 24pt in SVG
jq -r '.icons[] | select(.size==24 and .format=="svg") | .slug' icons.json
```

## Browse

[**hongyinull.github.io/meta-icons**](https://hongyinull.github.io/meta-icons/) — search by name, filter by collection, click to copy a path. Dark mode included.

The same page works offline: open `index.html` directly, no server or build step needed.

## Contributing

Missing an icon, or found one that renders wrong? [Open an issue](https://github.com/hongyinull/meta-icons/issues) — include the icon name and where you saw it. See [CONTRIBUTING.md](CONTRIBUTING.md) for how the collection is updated.

## Licence

The tooling, manifest, organisation and documentation in this repository are MIT licensed — see [LICENSE](LICENSE).

**The icon artwork is not.** It is the property of Meta Platforms, Inc., extracted from publicly served Instagram and Threads web assets and the Instagram iOS app (build 436). This repository is an unofficial reference for design and research. It is not affiliated with, endorsed by, or sponsored by Meta.

Instagram, Threads, WhatsApp, Meta and their logos are trademarks of Meta Platforms, Inc. Evaluate your own risk before using these assets commercially, or obtain permission through [Meta's brand guidelines](https://about.meta.com/brand/resources/). Takedown requests will be honoured — [open an issue](https://github.com/hongyinull/meta-icons/issues) or email the maintainer.
