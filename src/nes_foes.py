"""Common foes (小怪) as gallery variants in the `nes` style: 50 small regular monsters (art in nes_foes_art.py).

A foe variant gives the battle picture - a 霸王之路-style bust, 48x56 on the black NES panel like the generals'
portraits - and a 16x16 field sprite (two stacked sprite layers) with one two-frame animation `move` (used to idle
and to move). group() draws them all as one roster in NES window frames, ordered by tier.
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
                sprite_palettes=f['spr_palettes'], name=fid)
    p.check()            # raises if a Famicom rule is broken
    return p


def portrait(fid):
    return pic(fid).image()


def frames(fid):
    f = A.FOES[fid]
    fr = A.BASES[f['base']][2]
    return {'move': [nes.sprite_image(_rows(t), f['pal'], f['pal2']) for t in fr]}


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
    """All the given foes as one roster: each bust in an NES window frame, its field sprite on a strip below."""
    from nes_variant import window
    wins = {fid: window(portrait(fid)) for fid in members}
    ww, wh = next(iter(wins.values())).size
    road, gap, pad = 20, 4, 6
    rows = (len(members) + cols - 1) // cols
    cell_h = wh + 2 + road
    W = pad * 2 + cols * ww + (cols - 1) * gap
    H = pad * 2 + rows * cell_h + (rows - 1) * gap
    out = Image.new('RGBA', (W, H), nes.rgba(0x0F))
    for i, fid in enumerate(members):
        col, row = i % cols, i // cols
        x, y = pad + col * (ww + gap), pad + row * (cell_h + gap)
        out.alpha_composite(wins[fid], (x, y))
        if col == 0:
            out.alpha_composite(Image.new('RGBA', (W - pad * 2, road), nes.rgba(0x08)), (pad, y + wh + 2))
        s = frames(fid)['move'][0]
        out.alpha_composite(s, (x + (ww - 16) // 2, y + wh + 2 + 2))
    return out
