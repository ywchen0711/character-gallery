"""Common foes (小怪): 50 small regular monsters in the 8-bit `nes` style, built from 26 base designs with
NES-style palette swaps (灰狼 -> 血狼 -> 霜狼 ...).

The battle pictures are drawn by src/mon_designs.py (shapes rasterised on a clean grid, mirrored fronts, one light
from the top-left, a traced 1-px outline; checked by tools/lint.py). mondraw.famicom() splits each picture into
the background layer and a small sprite overlay (eyes, glints) and finds the sub-palettes, in slot letters, that
keep every 16x16 attribute area and 8x8 sprite tile legal. A foe = a base + one NES colour per slot.

BASES[name] = (picture rows, sprite-overlay rows, (field frame 1, field frame 2))   picture: '.' transparent, 'k' black
FOES[id] = dict(base, slots, palettes, spr_slots, spr_palettes, pal)   pal: the 16x16 field sprite colours
nes_foes.py turns these into gallery variants; nes.Pic.check() proves the Famicom rules for every foe.
"""
import mon_designs
import mondraw
from nes_foes_fields import FRAME, MODE, FIELD_PAL
from nes_walk_mon import field_frames

# the slots each base puts on the sprite layer
SPRITE_SLOTS = dict(wolf='r', boar='rw', snake='yr', bat='rw', crab='w', monkey='', hornet='', centipede='y',
                    scorpion='r', wisp='', paperghost='r', treesprite='y', mushroom='y', inkblot='', windsprite='',
                    stonetoad='wy', dummy='r', skeleton='e', drowned='e', littlejiangshi='yr', bronze='e',
                    lackey='', archer='w', assassin='ewS', roguemonk='S', sorcerer='yra')

# foe id -> (base, {slot: NES colour})
COLOURS = {
    'greywolf': ('wolf', dict(a=0x30, b=0x10, d=0x00, r=0x16)),
    'bloodwolf': ('wolf', dict(a=0x26, b=0x16, d=0x06, r=0x28)),
    'frostwolf': ('wolf', dict(a=0x30, b=0x31, d=0x11, r=0x21)),
    'wildboar': ('boar', dict(a=0x27, b=0x17, d=0x07, w=0x30, r=0x16)),
    'ironboar': ('boar', dict(a=0x30, b=0x10, d=0x00, w=0x38, r=0x16)),
    'bambooviper': ('snake', dict(a=0x3A, b=0x2A, d=0x1A, y=0x28, r=0x16)),
    'redsnake': ('snake', dict(a=0x37, b=0x16, d=0x06, y=0x28, r=0x30)),
    'cavebat': ('bat', dict(a=0x23, b=0x13, d=0x03, r=0x16, w=0x30)),
    'bloodbat': ('bat', dict(a=0x25, b=0x15, d=0x05, r=0x28, w=0x30)),
    'rivercrab': ('crab', dict(a=0x27, b=0x16, d=0x06, w=0x30)),
    'ironcrab': ('crab', dict(a=0x10, b=0x00, d=0x0C, w=0x30)),
    'mountainmonkey': ('monkey', dict(a=0x37, b=0x18, d=0x08)),
    'goldmonkey': ('monkey', dict(a=0x38, b=0x28, d=0x18)),
    'tigerhornet': ('hornet', dict(a=0x30, b=0x28, d=0x07)),
    'ghosthornet': ('hornet', dict(a=0x32, b=0x14, d=0x04)),
    'centipede': ('centipede', dict(a=0x27, b=0x16, d=0x07, y=0x28)),
    'goldcentipede': ('centipede', dict(a=0x38, b=0x28, d=0x08, y=0x16)),
    'sandscorpion': ('scorpion', dict(a=0x38, b=0x27, d=0x17, r=0x16)),
    'inkscorpion': ('scorpion', dict(a=0x12, b=0x02, d=0x0C, r=0x21)),
    'wisp': ('wisp', dict(a=0x31, b=0x21, w=0x30)),
    'netherflame': ('wisp', dict(a=0x34, b=0x14, w=0x30)),
    'papereffigy': ('paperghost', dict(a=0x30, b=0x16, d=0x10, r=0x25)),
    'treesprite': ('treesprite', dict(e=0x2A, f=0x1A, b=0x18, d=0x08, y=0x28)),
    'deadwood': ('treesprite', dict(e=0x18, f=0x08, b=0x00, d=0x0C, y=0x16)),
    'toadstool': ('mushroom', dict(a=0x24, b=0x14, d=0x04, e=0x37, f=0x27, y=0x2A)),
    'inkspirit': ('inkblot', dict(b=0x12, d=0x02, w=0x30)),
    'skeleton': ('skeleton', dict(w=0x30, a=0x10, r=0x16, d=0x07, e=0x16)),
    'blackbone': ('skeleton', dict(w=0x10, a=0x00, r=0x04, d=0x0C, e=0x24)),
    'drowned': ('drowned', dict(a=0x3B, b=0x1C, w=0x30, e=0x21)),
    'coldpool': ('drowned', dict(a=0x31, b=0x12, w=0x30, e=0x30)),
    'littlejiangshi': ('littlejiangshi', dict(b=0x12, d=0x02, S=0x3A, y=0x38, r=0x16)),
    'bronzejiangshi': ('littlejiangshi', dict(b=0x18, d=0x08, S=0x2A, y=0x28, r=0x16)),
    'windsprite': ('windsprite', dict(w=0x30, a=0x31, b=0x21)),
    'thundersprite': ('windsprite', dict(w=0x30, a=0x38, b=0x28)),
    'stonetoad': ('stonetoad', dict(a=0x10, b=0x00, d=0x0C, w=0x30, y=0x28)),
    'dummy': ('dummy', dict(a=0x27, b=0x17, d=0x07, r=0x16)),
    'irondummy': ('dummy', dict(a=0x10, b=0x00, d=0x0C, r=0x21)),
    'bronzeman': ('bronze', dict(a=0x38, b=0x27, d=0x07, e=0x30)),
    'vajraguardian': ('bronze', dict(a=0x30, b=0x28, d=0x18, e=0x16)),
    'lackey': ('lackey', dict(S=0x37, a=0x18, b=0x00, d=0x08)),
    'cudgeler': ('lackey', dict(S=0x27, a=0x17, b=0x07, d=0x0C)),
    'bloodthug': ('lackey', dict(S=0x37, a=0x16, b=0x06, d=0x07)),
    'archer': ('archer', dict(S=0x37, b=0x18, d=0x08, w=0x30)),
    'netherarcher': ('archer', dict(S=0x36, b=0x04, d=0x0C, w=0x10)),
    'assassin': ('assassin', dict(S=0x37, a=0x10, b=0x00, d=0x18, w=0x30, e=0x16)),
    'netherassassin': ('assassin', dict(S=0x36, a=0x14, b=0x0C, d=0x04, w=0x30, e=0x16)),
    'roguemonk': ('roguemonk', dict(S=0x37, b=0x27, a=0x16, d=0x07)),
    'ironmonk': ('roguemonk', dict(S=0x10, b=0x00, a=0x30, d=0x0C)),
    'daoist': ('sorcerer', dict(S=0x37, b=0x12, d=0x02, a=0x30, y=0x38, r=0x16)),
    'blackdaoist': ('sorcerer', dict(S=0x36, b=0x04, d=0x0C, a=0x10, y=0x28, r=0x16)),
}

BASES = {}
GROUPS = {}
for _name in sorted({b for b, _ in COLOURS.values()}):
    _c = mon_designs.build(_name)
    _bg, _sp, _g, _sg = mondraw.famicom(_c.rows(), SPRITE_SLOTS[_name])
    _f1, _f2 = field_frames(FRAME[_name].strip('\n').split('\n'), MODE[_name])
    BASES[_name] = ('\n'.join(_bg), '\n'.join(_sp), ('\n'.join(_f1), '\n'.join(_f2)))
    GROUPS[_name] = (_g, _sg)

FOES = {}
for _fid, (_base, _cols) in COLOURS.items():
    _g, _sg = GROUPS[_base]
    _spr = SPRITE_SLOTS[_base]
    FOES[_fid] = dict(base=_base,
                      slots={k: v for k, v in _cols.items() if k not in _spr},
                      palettes=[tuple(_cols[s] for s in g) for g in _g],
                      spr_slots={k: v for k, v in _cols.items() if k in _spr},
                      spr_palettes=[tuple(_cols[s] for s in g) for g in _sg],
                      pal=FIELD_PAL[_fid])
