"""Monsters & beasts (怪物與野獸) as gallery variants in the `nes` style.

The art lives in nes_beasts_art.py (hand-typed rows). A monster variant gives
  portrait()  the big front-view battle picture (transparent backdrop, size per creature, at most 64x64)
  frames()    {'move': [a, b]}  the 16x16 / 16x24 field sprite, two frames used both to idle and to move
and group() draws the whole bestiary as one NES encounter screen with each field sprite underneath.
"""
from PIL import Image

import nes
import nes_beasts_art as A
from variants import Variant

BEASTS = list(A.PORTRAITS)


def pic(cid):
    bg, spr, slots, pals, sslots, spals, (w, h) = A.PORTRAITS[cid]
    p = nes.Pic(nes.parse(bg, w, h, cid), slots, pals, sprite=nes.parse(spr, w, h, cid + ' sprite'),
                sprite_slots=sslots, sprite_palettes=spals, name=cid, transparent=True)
    p.check()            # raises if a Famicom rule is broken
    return p


def portrait(cid):
    return pic(cid).image()


def frames(cid):
    d = A.SPRITES[cid]
    return {'move': [nes.sprite_image(r, d['pal']) for r in d['move']]}


class BeastVariant(Variant):
    style = 'nes'
    primary = True
    fps = {'move': 3}
    notes = {'move': 'two frames, used both to idle and to move; faces the viewer'}

    def __init__(self, cid):
        self.cid = cid
        h = len(A.SPRITES[cid]['move'][0])
        self.anchor = (8, h - 1)

    def portrait(self):
        return portrait(self.cid)

    def frames(self):
        return frames(self.cid)


def group(members=None, cols=None):
    """An NES encounter screen: the battle pictures in a row on black, each one's field sprite on a dark strip below.
    cols=None puts them all in one row; otherwise they wrap."""
    members = members or BEASTS
    cols = cols or len(members)
    pics = [portrait(c) for c in members]
    cw = max(p.width for p in pics)
    chh = max(p.height for p in pics)
    gap, pad, road = 4, 6, 28
    rows = (len(pics) + cols - 1) // cols
    cell_h = chh + 4 + road
    W = pad * 2 + cols * cw + (cols - 1) * gap
    H = pad * 2 + rows * cell_h + (rows - 1) * gap
    out = Image.new('RGBA', (W, H), nes.rgba(0x0F))
    for i, (c, p) in enumerate(zip(members, pics)):
        col, row = i % cols, i // cols
        x, y = pad + col * (cw + gap), pad + row * (cell_h + gap)
        out.alpha_composite(p, (x + (cw - p.width) // 2, y + chh - p.height))
        if col == 0:
            out.alpha_composite(Image.new('RGBA', (W - pad * 2, road), nes.rgba(0x08)), (pad, y + chh + 4))
        spr = frames(c)['move'][0]
        out.alpha_composite(spr, (x + (cw - 16) // 2, y + chh + 4 + road - 2 - spr.height))
    return out
