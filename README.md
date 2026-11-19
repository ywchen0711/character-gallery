# 人物圖庫 Character Gallery

A pixel-art character library for the games in this collection. Each character can come in several art styles ("variants"). Every variant has a portrait and an animated full body.

| Style id | Look (imitated, original art) | Portrait | Sprite |
|---|---|---|---|
| `family` (**main**) | HD-2D (Octopath-like), cuter: round faces, small dark eyes, warm soft light | 72×80 painterly, bokeh background | 40×60 cell, one baseline for everyone; idle, walk in 4 directions, signature action |
| `koei` | 16-bit Three Kingdoms strategy portraits (霸王の大陸-like) × pixel-baseball chibis | 56×64, 3/4 view, side-lit | 56×64 cell, about 2.3 heads |
| `hd2d` | HD-2D (Octopath-like) | 80×104 painterly, bokeh background | 40×56 cell, about 3 heads, soft ramps, tiny dark eyes |
| `snes` | SNES JRPG (FF6-like) | 48×48 in a blue menu window | 16×24 field sprite, 4-direction walk |
| `gba` | GBA tactics (Fire Emblem-like) | 64×64, strict 16 colours, cel-shaded | 48×48 chunky battle sprite |
| `nes` | 8-bit NES (Dragon Quest-like) | 48×48 window, 4 colours per 16×16 block | 16×16, 3 colours per 8×8 sprite, 2-frame walk |

Characters so far:
- The family from *Saga of Jiangdong*, drawn in the main `family` style, with their earlier style tests kept:
  - Jeff, the father (also `hd2d` and `koei`)
  - Erin, the mother (also `snes` and `koei`)
  - Josh, 10 (also `gba` and `koei`)
  - Jasper, 8 (also `nes` and `koei`)
- 關羽 Guan Yu (`koei`).

The group picture is `chars/family/group.png` (transparent) and `group-scene.png` (with background), each also at 4x.

`compare.html` lays the styles side by side so you can pick one.

**Style note:** all art is original, drawn *in the style of* those games. Nothing is traced, copied or downloaded from them.

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
