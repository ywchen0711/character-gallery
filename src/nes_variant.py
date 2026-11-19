"""The `nes` style variant: a 霸王の大陸-like Famicom portrait (nes_portraits) and a 16x24
NES field sprite (nes_sprites), both under real Famicom colour rules (nes.py)."""
from variants import Variant
import nes_portraits
import nes_sprites


class NESVariant(Variant):
    style = 'nes'
    primary = True
    fps = {'idle': 2, 'walk': 4, 'walk_side': 4}
    anchor = (8, 23)
    notes = {'walk': 'front; frame 2 has the same body as frame 1, only the legs step (the bottom rows)',
             'walk_side': 'faces right (stride, then legs together; same body); mirror horizontally for left'}

    def __init__(self, cid):
        self.cid = cid

    def portrait(self):
        return nes_portraits.portrait(self.cid)

    def frames(self):
        return nes_sprites.frames(self.cid)


class SangoVariant(NESVariant):
    """A character's look as the main general of 三國志 霸王之路 (drawings keyed '<cid>_sango')."""
    style = 'sango'
    primary = False

    def portrait(self):
        return nes_portraits.portrait(self.cid + '_sango')

    def frames(self):
        return nes_sprites.frames(self.cid + '_sango')


def window(img, border=0x30):
    """An NES text-window frame around a portrait: 1px black gap, 1px white line."""
    from PIL import Image
    import nes
    w, h = img.width + 4, img.height + 4
    out = Image.new('RGBA', (w, h), nes.rgba(0x0F))
    line = nes.rgba(border)
    for x in range(w):
        out.putpixel((x, 0), line); out.putpixel((x, h - 1), line)
    for y in range(h):
        out.putpixel((0, y), line); out.putpixel((w - 1, y), line)
    out.alpha_composite(img, (2, 2))
    return out


def group(members=('jeff', 'erin', 'josh', 'jasper'), cols=4):
    """The family as an NES roster screen: framed portraits, and under each its field sprite
    on a grey road with one shared baseline (so the children's heights read directly).
    cols=4 is one wide row (desktop); cols=2 is a 2x2 block (phones)."""
    from PIL import Image
    import nes
    wins = [window(nes_portraits.portrait(c)) for c in members]
    ww, wh = wins[0].size
    gap, pad, road = 4, 6, 28
    rows = (len(wins) + cols - 1) // cols
    cell_h = wh + 2 + road
    W = pad * 2 + cols * ww + (cols - 1) * gap
    H = pad * 2 + rows * cell_h + (rows - 1) * gap
    out = Image.new('RGBA', (W, H), nes.rgba(0x0F))
    for i, (c, w) in enumerate(zip(members, wins)):
        col, row = i % cols, i // cols
        x, y = pad + col * (ww + gap), pad + row * (cell_h + gap)
        out.alpha_composite(w, (x, y))
        if col == 0:     # one grey road per row of portraits
            out.alpha_composite(Image.new('RGBA', (W - pad * 2, road), nes.rgba(0x00)), (pad, y + wh + 2))
        spr = nes_sprites.frames(c)['walk'][0]
        out.alpha_composite(spr, (x + (ww - 16) // 2, y + wh + 4))
    return out
