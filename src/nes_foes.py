"""Common foes (小怪) as gallery variants in the `nes` style: 50 small regular monsters (art in nes_foes_art.py).

A foe variant gives the battle picture (transparent backdrop, 48x48, people-like foes 48x56) and a 16x16 field sprite with one
two-frame animation `move` (used to idle and to move). group() draws them all as one roster, ordered by tier.
"""
from PIL import Image

import nes
import nes_foes_art as A
from variants import Variant

FOES = list(A.FOES)


def _rows(t):
    return [r for r in t.strip('\n').split('\n')]


def pic(fid):
    f = A.FOES[fid]
    bg, spr, _frames = A.BASES[f['base']]
    rows = _rows(bg)
    w, h = len(rows[0]), len(rows)
    p = nes.Pic(rows, f['slots'], f['palettes'], sprite=_rows(spr), sprite_slots=f['spr_slots'],
                sprite_palettes=f['spr_palettes'], name=fid, transparent=True)
    p.check()            # raises if a Famicom rule is broken
    return p


def portrait(fid):
    return pic(fid).image()


def frames(fid):
    f = A.FOES[fid]
    fr = A.BASES[f['base']][2]
    return {'move': [nes.sprite_image(_rows(t), f['pal']) for t in fr]}


class FoeVariant(Variant):
    style = 'nes'
    primary = True
    fps = {'move': 3}
    anchor = (8, 15)
    notes = {'move': 'two frames, used both to idle and to move'}

    def __init__(self, fid):
        self.cid = fid

    def portrait(self):
        return portrait(self.cid)

    def frames(self):
        return frames(self.cid)


def group(members, cols=10):
    """All the given foes on black: battle pictures bottom-aligned in equal cells, each field sprite on a strip below."""
    pics = {fid: portrait(fid) for fid in members}
    cw = max(p.width for p in pics.values())
    chh = max(p.height for p in pics.values())
    road, gap, pad = 20, 4, 6
    rows = (len(members) + cols - 1) // cols
    cell_h = chh + 2 + road
    W = pad * 2 + cols * cw + (cols - 1) * gap
    H = pad * 2 + rows * cell_h + (rows - 1) * gap
    out = Image.new('RGBA', (W, H), nes.rgba(0x0F))
    for i, fid in enumerate(members):
        col, row = i % cols, i // cols
        x, y = pad + col * (cw + gap), pad + row * (cell_h + gap)
        p = pics[fid]
        out.alpha_composite(p, (x + (cw - p.width) // 2, y + chh - p.height))
        if col == 0:
            out.alpha_composite(Image.new('RGBA', (W - pad * 2, road), nes.rgba(0x08)), (pad, y + chh + 2))
        s = frames(fid)['move'][0]
        out.alpha_composite(s, (x + (cw - 16) // 2, y + chh + 2 + 2))
    return out
