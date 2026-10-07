# Contributing

## Reporting a missing or broken icon

[Open an issue](https://github.com/hongyinull/instagram-threads-icons/issues) with:

- The icon's name, or where you saw it in Instagram / Threads
- A screenshot if you have one
- Which collection you expected it in

Icons that render incorrectly live in `_broken/` inside each collection. If you
can fix one, a pull request moving it back with the corrected file is welcome.

## Adding icons

Icons come from two sources:

1. **Web** — SVG sprites served by instagram.com and threads.com
2. **iOS** — `Assets.car` inside the Instagram `.ipa`, unpacked to `@3x` PNGs

Keep the original filename. It is how an icon is traced back to its source, and
the manifest derives the searchable name from it.

## Regenerating the manifest

`icons.json` is generated, never edited by hand. After adding or removing files:

```bash
python3 tools/build_manifest.py
```

This rewrites `icons.json` and the data embedded in `index.html`.

## Conventions

- SVGs must use `fill="currentColor"` so they can be recoloured with CSS
- Do not reformat or re-optimise existing SVGs in an unrelated pull request
- One logical change per pull request
