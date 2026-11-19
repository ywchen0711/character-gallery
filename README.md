# 人物圖庫 Character Gallery

A pixel-art character library for the Three Kingdoms games in this collection. Each character has:

- a **bust portrait** in the style of 16-bit Three Kingdoms strategy games (56×64, 3/4 view, side-lit, about 24 colours plus the panel), and
- a **chibi full body** in the style of pixel baseball games (about 2.3 heads tall, 56×64 cells) with idle, front walk, side walk and signature-move animations.

**Style note:** all art is original, drawn pixel by pixel *in the style of* those games. Nothing is traced or copied from them.

Live gallery: open `index.html` (GitHub Pages). The first character is 關羽 Guan Yu. More will follow.

## Using the assets in a game

```
chars/index.json              every character: id, names (zh/en), faction, bio, file paths
chars/<id>/portrait.png       56x64 portrait        portrait@4x.png  224x256
chars/<id>/body.png           56x64 chibi idle      body@4x.png      224x256
chars/<id>/sheet.png          sprite sheet, one animation per row (56x64 cells), sheet@4x.png too
chars/<id>/sheet.json         frameWidth/Height, anchor (feet at 28,62), animations {row, frames, fps, loop}
```

Animations: `idle` (2 frames), `walk` (front, 4), `walk_side` (faces right, 4; mirror it for left), `action` (signature move, 4).
Draw with nearest-neighbour scaling (`image-rendering: pixelated`, `imageSmoothingEnabled = false`) at whole-number scales.

## Editing or adding a character

The pixels live as text grids in Python, one character per pixel, under `src/`:

- `src/pixlib.py` - grid parsing, layers, palettes, strand/stroke helpers
- `src/faces.py` - the hand-drawn portrait heads (male and female templates, jaw/age overlays)
- `src/portrait.py` - the portrait builder: panel, shoulders, collar, armour, layering
- `src/chibi.py` - the chibi head/torso/arms/legs templates and the animation frames
- `src/chars/<id>.py` - one file per character: palettes, hat/hair/beard/prop grids, metadata
- `src/roster.py` - the list of characters to export

To add a character:

1. Copy `src/chars/guanyu.py` to `src/chars/<id>.py`. Change `META`, `FACTION` (`wu`, `shu`, `wei` or `qun`), the palettes `PAL` (portrait) and `CPAL` (chibi), and redraw the grids. Letters are colour slots and `.` is transparent.
2. Add the id to `ROSTER` in `src/roster.py`.
3. Run `python tools/export.py`. It writes `chars/<id>/` and rebuilds `chars/index.json`; the site picks it up.

Helpers: `python tools/sheet.py out.png 4 guanyu` (portrait contact sheet), `python tools/preview.py in.png out.png 12` (zoomed grid view for editing), `python tools/thumb.py` (lobby thumbnail). Requires Python 3 with Pillow.

## Licence

Art and code © the repository owner (ywchen0711), released under **CC BY 4.0**: you may reuse and adapt them with credit. This is a default chosen for you; change it here if you prefer another licence.
