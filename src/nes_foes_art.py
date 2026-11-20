"""Common foes (小怪): 50 small regular monsters in the 8-bit `nes` style, built from 26 base designs with
NES-style palette swaps (灰狼 -> 血狼 -> 霜狼 ...); 14 of the stronger kin add a detail (a scar, nails in the club, ice).

The battle pictures are 霸王之路-style busts drawn by src/foe_busts.py (48x56 on the black NES panel, like the
generals; checked by tools/lint.py). foe_busts.autofit() makes every 16x16 area fit the Famicom palette rule at
slot level, then mondraw.famicom() splits each picture into the background layer and a small sprite overlay
(props, eyes, glints) and finds the sub-palettes, in slot letters. A foe = a base + one NES colour per slot.

BASES[name] = (picture rows, sprite-overlay rows, (field frame 1, field frame 2))   picture: '.' = the black panel
FOES[id] = dict(base, slots, palettes, spr_slots, spr_palettes, pal, pal2)   pal / pal2: the two field sprite layers
nes_foes.py turns these into gallery variants; nes.Pic.check() proves the Famicom rules for every foe.
"""
import foe_busts
import mondraw
from nes_foes_fields import FRAME, MODE, field_pals
from nes_walk_mon import field_frames

# the slots each base puts on the sprite layer
SPRITE_SLOTS = {'archer': 'nowr', 'archer_nether': 'nowr', 'assassin': 'ow', 'bat': 'rw', 'boar': 'rw', 'boar_iron': 'rw', 'bronze': 'yr', 'bronze_jewel': 'yr', 'centipede': 'yw', 'crab': 'w', 'daoist_black': 'yrw', 'drowned': 'e', 'drowned_ice': 'e', 'dummy': 'rw', 'dummy_iron': 'rw', 'hornet': 'w', 'hornet_ghost': 'w', 'inkblot': '', 'jiangshi_bronze': 'yrw', 'lackey': 'now', 'lackey_spiked': 'now', 'littlejiangshi': 'yrw', 'monk_iron': 'noyw', 'monkey': 'w', 'mushroom': 'y', 'paperghost': 'r', 'roguemonk': 'noyw', 'scorpion': 'rw', 'skeleton': 'nor', 'skeleton_black': 'nore', 'snake': 'yrw', 'sorcerer': 'yr', 'greatbell': 'erw', 'stonetoad': 'wy', 'treesprite': 'y', 'windsprite': '', 'wisp': '', 'wisp_nether': '', 'wolf': 'rw', 'wolf_frost': 'rw', 'wolf_scar': 'rw'}

# the stronger-kin variants use their base's field sprite
VARIANT_OF = {'wolf_scar': 'wolf', 'wolf_frost': 'wolf', 'boar_iron': 'boar', 'skeleton_black': 'skeleton', 'lackey_spiked': 'lackey', 'bronze_jewel': 'bronze', 'monk_iron': 'roguemonk', 'dummy_iron': 'dummy', 'drowned_ice': 'drowned', 'wisp_nether': 'wisp', 'archer_nether': 'archer', 'daoist_black': 'sorcerer', 'hornet_ghost': 'hornet', 'jiangshi_bronze': 'littlejiangshi'}

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
    'skeleton': ('skeleton', dict(w=0x30, a=0x10, r=0x16, n=0x07, o=0x00, e=0x16)),
    'blackbone': ('skeleton_black', dict(w=0x10, a=0x00, r=0x04, n=0x0C, o=0x0C, e=0x24)),
    'drowned': ('drowned', dict(w=0x30, a=0x3B, b=0x1C, d=0x0C, e=0x21)),
    'coldpool': ('drowned_ice', dict(w=0x30, a=0x31, b=0x12, d=0x02, e=0x30)),
    'littlejiangshi': ('littlejiangshi', dict(S=0x3A, s=0x2A, a=0x21, b=0x12, d=0x02, y=0x38, r=0x16, e=0x16, w=0x30)),
    'bronzejiangshi': ('jiangshi_bronze', dict(S=0x2A, s=0x1A, a=0x28, b=0x18, d=0x08, y=0x38, r=0x16, e=0x16, w=0x30)),
    'windsprite': ('windsprite', dict(w=0x30, a=0x31, b=0x21)),
    'thundersprite': ('windsprite', dict(w=0x30, a=0x38, b=0x28)),
    'stonetoad': ('stonetoad', dict(a=0x10, b=0x00, d=0x0C, w=0x30, y=0x28)),
    'dummy': ('dummy', dict(w=0x30, a=0x27, b=0x17, d=0x07, r=0x16)),
    'irondummy': ('dummy_iron', dict(w=0x30, a=0x10, b=0x00, d=0x0C, r=0x21)),
    'bronzeman': ('bronze', dict(a=0x38, b=0x27, d=0x07, e=0x16, f=0x06, y=0x30, r=0x30)),
    'vajraguardian': ('bronze_jewel', dict(a=0x38, b=0x28, d=0x18, e=0x12, f=0x02, y=0x16, r=0x16)),
    'lackey': ('lackey', dict(S=0x37, s=0x27, H=0x37, w=0x30, a=0x28, b=0x18, d=0x08, e=0x10, f=0x00, n=0x18, o=0x08)),
    'cudgeler': ('lackey_spiked', dict(S=0x27, s=0x17, H=0x27, w=0x30, a=0x27, b=0x17, d=0x07, e=0x16, f=0x06, n=0x17, o=0x07)),
    'bloodthug': ('lackey_spiked', dict(S=0x37, s=0x27, H=0x37, w=0x30, a=0x26, b=0x16, d=0x06, e=0x00, f=0x0C, n=0x17, o=0x07)),
    'archer': ('archer', dict(S=0x37, s=0x27, w=0x30, y=0x38, a=0x2A, b=0x1A, d=0x0A, e=0x18, f=0x08, n=0x18, o=0x08, r=0x16)),
    'netherarcher': ('archer_nether', dict(r=0x2A, S=0x36, s=0x26, w=0x30, y=0x38, a=0x24, b=0x14, d=0x04, e=0x10, f=0x00, n=0x10, o=0x00)),
    'assassin': ('assassin', dict(S=0x37, s=0x27, w=0x30, r=0x16, a=0x10, b=0x00, d=0x0C, e=0x38, f=0x28, o=0x07)),
    'netherassassin': ('assassin', dict(S=0x36, s=0x26, w=0x30, r=0x2A, a=0x14, b=0x04, d=0x0C, e=0x10, f=0x00, o=0x0C)),
    'roguemonk': ('roguemonk', dict(S=0x37, s=0x27, w=0x30, y=0x28, a=0x27, b=0x17, d=0x07, e=0x16, f=0x06, n=0x18, o=0x08)),
    'ironmonk': ('monk_iron', dict(S=0x10, s=0x00, w=0x30, y=0x38, a=0x30, b=0x10, d=0x00, e=0x12, f=0x02, n=0x00, o=0x0C)),
    'daoist': ('sorcerer', dict(S=0x37, s=0x27, w=0x30, y=0x38, r=0x16, a=0x21, b=0x12, d=0x02, e=0x30, f=0x10)),
    'acolyte': ('sorcerer', dict(S=0x37, s=0x27, w=0x30, y=0x28, r=0x16, a=0x2A, b=0x1A, d=0x0A, e=0x10, f=0x00)),
    'pirate': ('lackey', dict(S=0x37, s=0x27, H=0x37, w=0x30, a=0x21, b=0x11, d=0x01, e=0x30, f=0x10, n=0x17, o=0x07)),
    'mudspirit': ('inkblot', dict(b=0x17, d=0x07, w=0x37)),
    'glowcap': ('mushroom', dict(a=0x2C, b=0x1C, d=0x0C, e=0x3B, f=0x2B, y=0x38)),
    'lotusghost': ('drowned', dict(w=0x30, a=0x35, b=0x25, d=0x15, e=0x2A)),
    'redpaper': ('paperghost', dict(h=0x0C, a=0x26, b=0x06, d=0x16, r=0x28)),
    'goldsnake': ('snake', dict(w=0x30, a=0x38, b=0x28, d=0x08, y=0x16, r=0x16)),
    'bamboosprite': ('treesprite', dict(e=0x2A, f=0x1A, b=0x28, d=0x18, y=0x16)),
    'firehornet': ('hornet', dict(w=0x30, a=0x38, b=0x16, d=0x06)),
    'lavacrab': ('crab', dict(a=0x26, b=0x16, d=0x00, w=0x30)),
    'lavawolf': ('wolf_scar', dict(w=0x30, a=0x27, b=0x07, d=0x08, r=0x38)),
    'lavascorpion': ('scorpion', dict(w=0x30, a=0x27, b=0x16, d=0x06, r=0x38)),
    'bellguard': ('assassin', dict(S=0x37, s=0x27, w=0x30, r=0x28, a=0x14, b=0x04, d=0x0C, e=0x28, f=0x18, o=0x07)),
    'icebat': ('bat', dict(a=0x31, b=0x21, d=0x11, r=0x16, w=0x30)),
    'snowmonkey': ('monkey', dict(w=0x30, a=0x30, b=0x10, d=0x00)),
    'snowsprite': ('windsprite', dict(w=0x30, a=0x30, b=0x31)),
    'iceboar': ('boar_iron', dict(a=0x30, b=0x31, d=0x21, w=0x10, r=0x16)),
    'icejiangshi': ('jiangshi_bronze', dict(S=0x31, s=0x21, a=0x30, b=0x10, d=0x00, y=0x31, r=0x16, e=0x11, w=0x30)),
    'bellfire': ('wisp_nether', dict(a=0x35, b=0x15, w=0x30)),
    'bellpuppet': ('dummy_iron', dict(w=0x30, a=0x28, b=0x18, d=0x08, r=0x16)),
    'goldbone': ('skeleton_black', dict(w=0x38, a=0x28, r=0x16, n=0x18, o=0x08, e=0x16)),
    'jadetoad': ('stonetoad', dict(a=0x2A, b=0x1A, d=0x0A, w=0x30, y=0x38)),
    'greatbell': ('greatbell', dict(a=0x38, b=0x28, d=0x18, e=0x21, r=0x16, w=0x30, y=0x27)),
    'blackdaoist': ('daoist_black', dict(S=0x36, s=0x26, w=0x30, y=0x28, r=0x16, a=0x14, b=0x04, d=0x0C, e=0x10, f=0x00)),
}

BASES = {}
GROUPS = {}
for _name in sorted({b for b, _ in COLOURS.values()}):
    _rows, _notes = foe_busts.autofit(foe_busts.build(_name).rows(), SPRITE_SLOTS[_name])
    _bg, _sp, _g, _sg = mondraw.famicom(_rows, SPRITE_SLOTS[_name])
    _fb = VARIANT_OF.get(_name, _name)
    _f1, _f2 = field_frames(FRAME[_fb].strip('\n').split('\n'), MODE[_fb])
    BASES[_name] = ('\n'.join(_bg), '\n'.join(_sp), ('\n'.join(_f1), '\n'.join(_f2)))
    GROUPS[_name] = (_g, _sg)

FOES = {}
for _fid, (_base, _cols) in COLOURS.items():
    _g, _sg = GROUPS[_base]
    _fb = VARIANT_OF.get(_base, _base)
    _p1, _p2 = field_pals(FRAME[_fb].strip('\n').split('\n'), _cols)
    FOES[_fid] = dict(base=_base,
                      slots=dict(_cols),
                      palettes=[tuple(_cols[s] for s in g) for g in _g],
                      spr_slots=dict(_cols),
                      spr_palettes=[tuple(_cols[s] for s in g) for g in _sg],
                      pal=_p1, pal2=_p2)
