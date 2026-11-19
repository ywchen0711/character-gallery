# 人物圖庫 Character Gallery

A pixel-art character library for the games in this collection. Each character can come in several art styles ("variants"). Every variant has a portrait and an animated full body.

| Style id | Look (imitated, original art) | Portrait | Sprite |
|---|---|---|---|
| `nes` (**main**) | 8-bit Famicom, in the manner of 三國志 霸王の大陸 (Namco, 1992): bold black lines, flat 2-3 tone shading | 48×56 on black; only NES (2C02) palette colours, one 3-colour sub-palette per 16×16 area (max 4), sprite overlays for eye whites and lips | 16×24 NES field sprite, 3 colours + transparent, 2-frame front and side walk; Josh 20 and Jasper 16 rows tall |
| `family` | HD-2D (Octopath-like), cuter: round faces, small dark eyes, warm soft light | 72×80 painterly, bokeh background | 40×60 cell, one baseline for everyone; idle, walk in 4 directions, signature action |
| `koei` | 16-bit Three Kingdoms strategy portraits (霸王の大陸-like) × pixel-baseball chibis | 56×64, 3/4 view, side-lit | 56×64 cell, about 2.3 heads |
| `hd2d` | HD-2D (Octopath-like) | 80×104 painterly, bokeh background | 40×56 cell, about 3 heads, soft ramps, tiny dark eyes |
| `snes` | SNES JRPG (FF6-like) | 48×48 in a blue menu window | 16×24 field sprite, 4-direction walk |
| `gba` | GBA tactics (Fire Emblem-like) | 64×64, strict 16 colours, cel-shaded | 48×48 chunky battle sprite |
| `dq` | 8-bit NES (Dragon Quest-like) | 48×48 window, 4 colours per 16×16 block | 16×16, 3 colours per 8×8 sprite, 2-frame walk |

Characters so far:
- The family from *Saga of Jiangdong*, drawn in the main 8-bit `nes` style, with their earlier styles kept as alternates:
  - Jeff, the father (also `family`, `hd2d` and `koei`)
  - Erin, the mother (also `family`, `snes` and `koei`)
  - Josh, 10 (also `family`, `gba` and `koei`)
  - Jasper, 8 (also `family`, `dq` and `koei`)
- 關羽 Guan Yu (`nes`, also `koei`).

Group pictures in `chars/family/`: `group-nes.png` (the main-style roster: four framed portraits with their sprites on one baseline) and `group-nes-2x2.png` for narrow screens; the older `group.png` (transparent) and `group-scene.png`. Each also at 4x.

`compare.html` lays the styles side by side so you can pick one.

**Style note:** all art is original, drawn *in the style of* those games. Nothing is traced, copied or downloaded from them. The main style is 8-bit: the Famicom portraits are hand-typed palette-indexed grids (`src/nes_portraits.py`), and `src/nes.py` checks the Famicom colour rules on every export.

## Using the assets in a game

```
chars/index.json                    styles, and every character: id, names (zh/en), faction, bio, variants[]
chars/<id>/<style>/portrait.png     the portrait, plus portrait@4x.png
chars/<id>/<style>/body.png         first idle frame, plus body@4x.png
chars/<id>/<style>/sheet.png        sprite sheet, one animation per row, plus sheet@4x.png
chars/<id>/<style>/sheet.json       frameWidth/Height, anchor (feet), animations {row, frames, fps, loop, note}
```

- Animation names include:
  - `idle`
  - `walk` (front)
  - `walk_side` (faces right; mirror it for left)
  - `walk_down`, `walk_up`, `walk_left`, `walk_right`
  - `action` / `guard` (signature moves)
- Each variant's `animations` list in `index.json` says which names it has.
- Draw with nearest-neighbour scaling (`image-rendering: pixelated`, `imageSmoothingEnabled = false`) at whole-number scales.

## Editing or adding a character

The pixels live as text grids in Python under `src/`. Each character is one per pixel. `.` is transparent, and letters are colour slots.

- `src/nes.py`: the NES palette table and the Famicom rule checker; `src/nes_portraits.py`: the 8-bit portraits (rows of exactly 48 pixels ending in `|`); `src/nes_sprites.py`: the 16x24 field sprites; `src/nes_variant.py`: the variant and the roster picture
- `src/pixlib.py`: grids, run-length rows, layers, palettes, strand/stroke/rotation helpers
- `src/paint.py`: soft per-material shading used by the HD-2D styles
- `src/family.py`, `src/family_portraits.py`: family portraits; `src/family_sprites.py`, `src/family_members.py`: family sprites (heads, body sizes, props, actions); `src/family_variant.py`: the variant and group picture
- `src/faces.py`: the hand-drawn portrait heads (male and female templates, jaw/age overlays)
- `src/portrait.py`, `src/chibi.py`: the `koei` portrait and chibi builders
- `src/variants.py`: what a variant provides; `src/styles.py`: style names and descriptions
- `src/chars/<id>.py`: one file per character, holding metadata, palettes, grids and `variants()`
- `src/roster.py`: the characters to export

To add a character:
1. Copy the file of the character whose style you want, e.g. `src/chars/guanyu.py` for `koei`.
2. Change `META`, `FACTION` (`wu`, `shu`, `wei`, `qun` or `west`), the palettes and the grids.
3. Add the id to `ROSTER` in `src/roster.py`.
4. Run `python tools/export.py`. It writes `chars/<id>/<style>/` and rebuilds `chars/index.json`.

Helpers (Python 3 with Pillow):
- `python tools/look.py <id> <style> out.png 6`: one variant zoomed
- `python tools/contact.py out.png`: every variant at 4x
- `python tools/preview.py in.png out.png 12`: zoomed grid for editing
- `python tools/thumb.py`: lobby thumbnail

## Licence

Art and code © the repository owner (ywchen0711), released under **CC BY 4.0**: you may reuse and adapt them with credit. This is a default chosen for you; change it here if you prefer another licence.
