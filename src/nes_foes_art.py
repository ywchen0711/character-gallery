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
SPRITE_SLOTS = dict(wolf='rw', boar='rw', snake='yrw', bat='rw', crab='w', monkey='w', hornet='w', centipede='yw',
                    scorpion='rw', wisp='', paperghost='r', treesprite='y', mushroom='y', inkblot='', windsprite='',
                    stonetoad='wy', dummy='rw', skeleton='er', drowned='e', littlejiangshi='yreH', bronze='ry',
                    lackey='SsHw', archer='SsHwyr', assassin='SsHwr', roguemonk='SsHwy', sorcerer='SsHwyr')

# the stronger-kin variants (mon_var.py) use their base's sprite slots
VARIANT_OF = dict(wolf_scar='wolf', wolf_frost='wolf', boar_iron='boar', skeleton_black='skeleton',
                  lackey_spiked='lackey', bronze_jewel='bronze', monk_iron='roguemonk', dummy_iron='dummy',
                  drowned_ice='drowned', wisp_nether='wisp', archer_nether='archer', daoist_black='sorcerer',
                  hornet_ghost='hornet', jiangshi_bronze='littlejiangshi')
for _v, _b in VARIANT_OF.items():
    SPRITE_SLOTS[_v] = SPRITE_SLOTS[_b]

# foe id -> (base, {slot: NES colour})
COLOURS = {
    'greywolf': ('wolf', dict(w=0x30, a=0x30, b=0x10, d=0x00, r=0x16)),
    'bloodwolf': ('wolf_scar', dict(w=0x30, a=0x26, b=0x16, d=0x06, r=0x28)),
    'frostwolf': ('wolf_frost', dict(w=0x30, a=0x30, b=0x31, d=0x11, r=0x21)),
    'wildboar': ('boar', dict(a=0x27, b=0x17, d=0x07, w=0x30, r=0x16)),
    'ironboar': ('boar_iron', dict(a=0x30, b=0x10, d=0x00, w=0x38, r=0x16)),
    'bambooviper': ('snake', dict(w=0x30, a=0x3A, b=0x2A, d=0x1A, y=0x28, r=0x16)),
    'redsnake': ('snake', dict(w=0x30, a=0x37, b=0x16, d=0x06, y=0x28, r=0x30)),
    'cavebat': ('bat', dict(a=0x23, b=0x13, d=0x03, r=0x16, w=0x30)),
    'bloodbat': ('bat', dict(a=0x25, b=0x15, d=0x05, r=0x28, w=0x30)),
    'rivercrab': ('crab', dict(a=0x27, b=0x16, d=0x06, w=0x30)),
    'ironcrab': ('crab', dict(a=0x10, b=0x00, d=0x0C, w=0x30)),
    'mountainmonkey': ('monkey', dict(w=0x30, a=0x37, b=0x18, d=0x08)),
    'goldmonkey': ('monkey', dict(w=0x30, a=0x38, b=0x28, d=0x18)),
    'tigerhornet': ('hornet', dict(w=0x30, a=0x30, b=0x28, d=0x07)),
    'ghosthornet': ('hornet_ghost', dict(w=0x30, a=0x32, b=0x14, d=0x04)),
    'centipede': ('centipede', dict(w=0x30, a=0x27, b=0x16, d=0x07, y=0x28)),
    'goldcentipede': ('centipede', dict(w=0x30, a=0x38, b=0x28, d=0x08, y=0x16)),
    'sandscorpion': ('scorpion', dict(w=0x30, a=0x38, b=0x27, d=0x17, r=0x16)),
    'inkscorpion': ('scorpion', dict(w=0x30, a=0x12, b=0x02, d=0x0C, r=0x21)),
    'wisp': ('wisp', dict(a=0x31, b=0x21, w=0x30)),
    'netherflame': ('wisp_nether', dict(a=0x34, b=0x14, w=0x30)),
    'papereffigy': ('paperghost', dict(h=0x0C, a=0x30, b=0x16, d=0x10, r=0x25)),
    'treesprite': ('treesprite', dict(e=0x2A, f=0x1A, b=0x18, d=0x08, y=0x28)),
    'deadwood': ('treesprite', dict(e=0x18, f=0x08, b=0x00, d=0x0C, y=0x16)),
    'toadstool': ('mushroom', dict(a=0x24, b=0x14, d=0x04, e=0x37, f=0x27, y=0x2A)),
    'inkspirit': ('inkblot', dict(b=0x12, d=0x02, w=0x30)),
    'skeleton': ('skeleton', dict(w=0x30, a=0x10, r=0x16, d=0x07, e=0x16)),
    'blackbone': ('skeleton_black', dict(w=0x10, a=0x00, r=0x04, d=0x0C, e=0x24)),
    'drowned': ('drowned', dict(w=0x30, a=0x3B, b=0x1C, d=0x0C, e=0x21)),
    'coldpool': ('drowned_ice', dict(w=0x30, a=0x31, b=0x12, d=0x02, e=0x30)),
    'littlejiangshi': ('littlejiangshi', dict(S=0x3A, s=0x2A, H=0x3A, a=0x21, b=0x12, d=0x02, y=0x38, r=0x16, e=0x16, w=0x30)),
    'bronzejiangshi': ('jiangshi_bronze', dict(S=0x2A, s=0x1A, H=0x2A, a=0x28, b=0x18, d=0x08, y=0x38, r=0x16, e=0x16, w=0x30)),
    'windsprite': ('windsprite', dict(w=0x30, a=0x31, b=0x21)),
    'thundersprite': ('windsprite', dict(w=0x30, a=0x38, b=0x28)),
    'stonetoad': ('stonetoad', dict(a=0x10, b=0x00, d=0x0C, w=0x30, y=0x28)),
    'dummy': ('dummy', dict(w=0x30, a=0x27, b=0x17, d=0x07, r=0x16)),
    'irondummy': ('dummy_iron', dict(w=0x30, a=0x10, b=0x00, d=0x0C, r=0x21)),
    'bronzeman': ('bronze', dict(a=0x38, b=0x27, d=0x07, e=0x16, f=0x06, y=0x30, r=0x30)),
    'vajraguardian': ('bronze_jewel', dict(a=0x38, b=0x28, d=0x18, e=0x12, f=0x02, y=0x16, r=0x16)),
    'lackey': ('lackey', dict(S=0x37, s=0x27, H=0x37, w=0x30, a=0x28, b=0x18, d=0x08, e=0x10, f=0x00)),
    'cudgeler': ('lackey_spiked', dict(S=0x27, s=0x17, H=0x27, w=0x30, a=0x27, b=0x17, d=0x07, e=0x16, f=0x06)),
    'bloodthug': ('lackey_spiked', dict(S=0x37, s=0x27, H=0x37, w=0x30, a=0x26, b=0x16, d=0x06, e=0x00, f=0x0C)),
    'archer': ('archer', dict(S=0x37, s=0x27, H=0x37, w=0x30, y=0x38, a=0x2A, b=0x1A, d=0x0A, e=0x18, f=0x08)),
    'netherarcher': ('archer_nether', dict(r=0x2A, S=0x36, s=0x26, H=0x36, w=0x30, y=0x38, a=0x24, b=0x14, d=0x04, e=0x10, f=0x00)),
    'assassin': ('assassin', dict(S=0x37, s=0x27, H=0x37, w=0x30, r=0x16, a=0x10, b=0x00, d=0x0C, e=0x38, f=0x28)),
    'netherassassin': ('assassin', dict(S=0x36, s=0x26, H=0x36, w=0x30, r=0x2A, a=0x14, b=0x04, d=0x0C, e=0x10, f=0x00)),
    'roguemonk': ('roguemonk', dict(S=0x37, s=0x27, H=0x37, w=0x30, y=0x28, a=0x27, b=0x17, d=0x07, e=0x16, f=0x06)),
    'ironmonk': ('monk_iron', dict(S=0x10, s=0x00, H=0x10, w=0x30, y=0x38, a=0x30, b=0x10, d=0x00, e=0x12, f=0x02)),
    'daoist': ('sorcerer', dict(S=0x37, s=0x27, H=0x37, w=0x30, y=0x38, r=0x16, a=0x21, b=0x12, d=0x02, e=0x30, f=0x10)),
    'blackdaoist': ('daoist_black', dict(S=0x36, s=0x26, H=0x36, w=0x30, y=0x28, r=0x16, a=0x14, b=0x04, d=0x0C, e=0x10, f=0x00)),
}

BASES = {}
GROUPS = {}
for _name in sorted({b for b, _ in COLOURS.values()}):
    _c = mon_designs.build(_name)
    _bg, _sp, _g, _sg = mondraw.famicom(_c.rows(), SPRITE_SLOTS[_name])
    _fb = VARIANT_OF.get(_name, _name)
    _f1, _f2 = field_frames(FRAME[_fb].strip('\n').split('\n'), MODE[_fb])
    BASES[_name] = ('\n'.join(_bg), '\n'.join(_sp), ('\n'.join(_f1), '\n'.join(_f2)))
    GROUPS[_name] = (_g, _sg)

FOES = {}
for _fid, (_base, _cols) in COLOURS.items():
    _g, _sg = GROUPS[_base]
    _spr = SPRITE_SLOTS[_base]
    FOES[_fid] = dict(base=_base,
                      slots=dict(_cols),
                      palettes=[tuple(_cols[s] for s in g) for g in _g],
                      spr_slots=dict(_cols),
                      spr_palettes=[tuple(_cols[s] for s in g) for g in _sg],
                      pal=FIELD_PAL[_fid])
