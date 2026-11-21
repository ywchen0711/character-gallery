"""The nes2 kit: shared, hand-typed parts so the whole Longmen cast can be drawn to the round-1 bar
(src/nes2_longmen.py) from a short spec per character.

Portrait spec (person(cid, spec)):
  colours   slot -> NES colour (see nes2.py for the slot letters)
  hair      a key of HAIR (top of the head, rows 0..15, a mirrored left half) - or a list of 16 rows
  hair_slot the slot used in the temple / sideburn pixels of the face ('i', 'k', 'S' for bald ...)
  face      'adult' | 'kid' | 'wide';   eyes: a key of EYES;   mouth: a key of MOUTHS;   mouth_y
  body      'robe' | 'armour' | 'vest' | 'gown' | 'fur'      collar: band slots (e.g. 'eaa'), inner, inner2
  beard     None | 'moustache' | 'goatee' | 'full' | 'long' | 'stubble' | 'thin'  (beard_slot, beard_shade)
  mask      None | 'cloth' | 'half' | 'ghost' | 'glasses' | 'patch' | 'scar'
  behind    parts drawn behind the body (props, capes, long hair):  list of (name, kwargs)
  front     parts drawn in front of the body before the outline:     list of (name, kwargs)
  after     hand pixels after the face: list of (rows, x, y, mirror)
  backdrop  kwargs for nes2_longmen.backdrop_sky
  spr, near passed to nes2.fit()
Every face uses the soft nose (one skin-shadow side stroke, no nostrils) and tiny dark eyes without whites.

Sprite spec (sprite(cid, ...)): a head from SHEADS (front / side / back, 14 rows each) or typed rows, a body
template from nes2_longmen_sprites (ROBE, GOWN, BOY) or this kit (ARMOUR, VEST), letters swapped per character,
props as overlays per view.
"""
import nes2_longmen as L
import nes2_longmen_sprites as SP
from nes2 import Mat, put, half, shade_right, T  # noqa: F401
from nes2_longmen import face, skin_shade, robe, neck, collar, robe_folds, backdrop_sky

# ================================================================ heads (portrait): rows 0..15, left halves
HAIR = {}

HAIR['topknot'] = """
........................
....................kkkk
...................khhii
...................kiiii
...................kkkkk
...............kkkkkiiii
............kkkiiiiikkkk
..........kkiiiiihiiiiii
.........kiiihiiiiiiiiii
........kiihiiiiiiiiiiii
........kihiiiiiiiiiiiii
.......kiihiiiiiiiiiiiii
.......kihiiiiiiiiiiiiii
.......kiiiiiiiiiiiiiiii
.......kiikkkkkkkkkkkkkk
.......kikSSSSSSSSSSSSSS
"""

HAIR['band'] = """
........................
....................kkkk
...................khhii
...................kiiii
...................kkkkk
...............kkkkkiiii
............kkkiiiiikkkk
..........kkiiiiihiiiiii
.........kiiihiiiiiiiiii
........kiihiiiiiiiiiiii
........kihiiiiiiiiiiiii
.......kkkkkkkkkkkkkkkkk
.......kmmmmmmmmmmmmmmmm
.......knnnnnnnnnnnnnnnn
.......kkkkkkkkkkkkkkkkk
.......kikSSSSSSSSSSSSSS
"""

HAIR['shaved'] = """
....................kkkk
...................khhii
...................kiiii
...................kkkkk
.................kkkkkkk
..............kkkiiiiiii
............kkSSSkiiiiii
..........kkSSSSSkiiiiii
.........kSSSSSSSkiiiiii
........kSSSSSSSSkiiiiii
........kSSSSSSSSkiiiiii
.......kSSSSSSSSSkiiiiii
.......kSSSSSSSSSSkkkkkk
.......kSSSSSSSSSSSSSSSS
.......kSSSSSSSSSSSSSSSS
.......kSkSSSSSSSSSSSSSS
"""

HAIR['wild'] = """
.........k....k.........
........kik..kik...k...k
.....k.kiiikkiiik.kik.ki
....kikiiiiiiiiiikiiikii
...kiiiihiiiiihiiiiiiiii
..kiiiihiiiiihiiiiiiihii
..kiiihiiiiihiiiiiiihiii
.kiiihiiiiihiiiiiiihiiii
.kiihiiiiiiiiiiiiiiiiiii
kiiiiiiiiiiiiiiiiiiiiiii
kiiiiiiiiiiiiiiiiiiiiiii
.kiiiiiiiiiiiiiiiiiiiiii
.kiiiiiikkiiiiikkiiiiiii
..kiiiikSSkiiikSSkiiiiik
..kiiiikSSSkkkSSSSkkkkkS
...kkkkkkSSSSSSSSSSSSSSS
"""

HAIR['spiky'] = """
...........k......k.....
..........kik....kik...k
.........kiik...kiik..ki
......k..kiiik.kiiik.kii
......kkkiiiiikiiiiikiii
.......kiiihiiiiihiiiiii
.....kkiiihiiiiihiiiiiii
....kiiiihiiiiihiiiiiiii
.....kiiihiiiiihiiiiiiii
....kiiiiiiiiiiiiiiiiiii
.....kiiiiiiiiiiiiiiiiii
......kiiiiiiiiiiiiiiiii
.......kiiiiiiiiiiiiiiii
.......kiiikkkiiikkkiiik
.......kiikSSkiikSSkiikS
.......kikSSSSkkSSSSkkSS
"""

HAIR['long'] = """
........................
................kkkkkkkk
.............kkkiiiiiiii
...........kkiiiiiiiiiik
..........kiiihiiiiiiiik
.........kiiihiiiiiiiiik
........kiiihiiiiiiiiiki
........kiihiiiiiiiiikii
.......kiihiiiiiiiiikiii
.......kiihiiiiiiikkSiii
.......kihiiiiiikkSSSkii
.......kihiiiikkSSSSSSkk
......kiiiiikkSSSSSSSSSS
......kiiikkSSSSSSSSSSSS
......kiikSSSSSSSSSSSSSS
......kikSSSSSSSSSSSSSSS
"""

HAIR['bun_f'] = """
....................kkkk
..................kkmmmm
.................kmmnmmm
.................kmnmmmm
.................kmmmmmm
..................kkkkkk
..............kkkkiiiiik
............kkiiiiiiiiik
..........kkiiihiiiiiiik
.........kiiihiiiiiiiikS
........kiiihiiiiiiiikSS
........kiihiiiiiiikkSSS
.......kiihiiiiiikkSSSSS
.......kiihiiiikkSSSSSSS
.......kihiiikkSSSSSSSSS
.......kihikkSSSSSSSSSSS
"""

HAIR['twinbuns'] = """
..kkkk..................
.kiiiik.................
kiihiiik................
kihiiiik......kkkkkkkkkk
kiiiiiikk..kkkiiiiiiiiii
.kiiiikmmkkiiiiiiiiiiiii
..kkkkmmkiiihiiiiiiiiiii
.....kkkiihiiiiiiiiiiiii
.......kihiiiiiiiiiiiiii
.......kiiiiiiiiiiiiiiii
.......kiiiiiiiiiiiiiiii
.......kiiiiikiiiiiiikii
.......kiiiikSkiiiiikSki
.......kiiikSSSkkkkkSSSk
.......kiikSSSSSSSSSSSSS
.......kikSSSSSSSSSSSSSS
"""

HAIR['bald'] = """
........................
........................
................kkkkkkkk
.............kkkSSSSSSSS
...........kkSSSSSSSSSSS
..........kSSSwSSSSSSSSS
.........kSSSwwSSSSSSSSS
.........kSSSSSSSSSSSSSS
........kSSSSSSSSSSSSSSS
........kSSSSSSSSSSSSSSS
........kSSSSSSSSSSSSSSS
........kSSSSSSSSSSSSSSS
........kSSSSSSSSSSSSSSS
........kSSSSSSSSSSSSSSS
.........kSSSSSSSSSSSSSS
.........kSSSSSSSSSSSSSS
"""

HAIR['official'] = """
........................
................kkkkkkkk
..............kkmmmmmmmm
.............kmmmmmmmmmm
.............kmnmmmmmmmm
............kmmnmmmmmmmm
............kmmmmmmmmmmm
kkkkkkkk...kkkkkkkkkkkkk
kmmmmmmmkkkkmmmmmmmmmmmm
kmnnnnnmmmmkmmmmmmmmmmmm
kkkkkkkkkkkkmmmmmmmmmmmm
.........kkkkkkkkkkkkkkk
.........kiikkkkkkkkkkkk
.........kiikSSSSSSSSSSS
.........kiikSSSSSSSSSSS
.........kikSSSSSSSSSSSS
"""

HAIR['melon'] = """
......................kk
.....................kyy
.....................kyy
................kkkkkkkk
.............kkkmmmmkmmm
...........kkmmmmmmkmmmm
..........kmmnmmmmkmmmmm
.........kmmnmmmmkmmmmmm
.........kmnmmmmkmmmmmmm
.........kmmmmmmkmmmmmmm
.........kkkkkkkkkkkkkkk
.........knnnnnnnnnnnnnn
.........kkkkkkkkkkkkkkk
.........kiikSSSSSSSSSSS
.........kiikSSSSSSSSSSS
.........kikSSSSSSSSSSSS
"""

HAIR['scholar'] = """
................kkkkkkkk
...........kkkkkmmmmmmmm
..........kmmmmmkmmmmmmm
..........knnnnnkmmmmmmm
..........knmmmmkmmmmmmm
..........knmmmmkmmmmmmm
..........knmmmmkmmmmmmm
..........knmmmmkmmmmmmm
..........knmmmmkmmmmmmm
.........kknmmmmkmmmmmmm
.........knnmmmmkmmmmmmm
.........kkkkkkkkkkkkkkk
.........kmmmmmmmmmmmmmm
.........kkkkkkkkkkkkkkk
.........kikSSSSSSSSSSSS
.........kikSSSSSSSSSSSS
"""

HAIR['straw'] = """
........................
....................kkkk
.................kkkmmmm
...............kkmmmmmmm
.............kkmmmnmmmmm
...........kkmmmnmmmmmmm
.........kkmmmnmmmmmmmmm
.......kkmmmnmmmmmmmmmmm
.....kkmmmnmmmmmmmmmmmmm
...kkmmmnmmmmmmmmmmmmmmm
.kknnnnnnnnnnnnnnnnnnnnn
kkkkkkkkkkkkkkkkkkkkkkkk
.........kiikSSSSSSSSSSS
.........kiikSSSSSSSSSSS
.........kiikSSSSSSSSSSS
.........kikSSSSSSSSSSSS
"""

HAIR['hood'] = """
........................
................kkkkkkkk
.............kkkmmmmmmmm
...........kkmmmmmmmmmmm
..........kmmmmmmmmmmmmm
.........kmmmmmmmmmmmmmm
........kmmmmmmmmmmmmmmm
........kmmmmmmmmmmmmmmm
.......kmmmmmmmmmmmmmmmm
.......kmmmmmmmmmmmmmmmm
.......kmmmmmmmmmmmmmmmm
.......kmmmmkkkkkkkkkkkk
.......kmmmkSSSSSSSSSSSS
.......kmmkSSSSSSSSSSSSS
.......kmmkSSSSSSSSSSSSS
.......kmmkSSSSSSSSSSSSS
"""

HAIR['helmet'] = """
......................kk
.....................kyy
.....................kyy
................kkkkkkkk
.............kkkmmmmmmmm
...........kkmmmmmmmmmmm
..........kmmmmmmmmmmmmm
.........kmmmmmmmmmmmmmm
.........kmmnmmmmmmmmmmm
........kmmnmmmmmmmmmmmm
........kmnmmmmmmmmmmmmm
.......kkkkkkkkkkkkkkkkk
.......knnnnnnnnnnnnnnnn
.......kkkkkkkkkkkkkkkkk
.........kiikSSSSSSSSSSS
.........kikSSSSSSSSSSSS
"""

HAIR['kerchief'] = """
........................
........................
................kkkkkkkk
.............kkkmmmmmmmm
...........kkmmmmmmmmmmm
..........kmmmmmmmmmmmmm
.........kmmmnmmmmmmmmmm
........kmmmnmmmmmmmmmmm
........kmmnmmmmmmmmmmmm
.......kmmnmmmmmmmmmmmmm
.......kmmmmmmmmmmmmmmmm
.......knnnnnnnnnnnnnnnn
.......kkkkkkkkkkkkkkkkk
.........kiikSSSSSSSSSSS
.........kiikSSSSSSSSSSS
.........kikSSSSSSSSSSSS
"""

HAIR['crown'] = """
.....................kyy
....................kyyy
...................kkkkk
..................kyyyyy
..................kykkyy
...............kkkkyyyyy
............kkkiiiikkkkk
..........kkiiiiihiiiiii
.........kiiihiiiiiiiiii
........kiihiiiiiiiiiiii
........kihiiiiiiiiiiiii
.......kiihiiiiiiiiiiiii
.......kihiiiiiiiiiiiiii
.......kiiiiiiiiiiiiiiii
.......kiikkkkkkkkkkkkkk
.......kikSSSSSSSSSSSSSS
"""

HAIR['flat'] = """
........................
........................
............kkkkkkkkkkkk
............kmmmmmmmmmmm
............kmmmmmmmmmmm
............knnnnnnnnnnn
............kmmmmmmmmmmm
............kmmmmmmmmmmm
.....kkkkkkkkkkkkkkkkkkk
.....kmmmmmmmmmmmmmmmmmm
.....kkkkkkkkkkkkkkkkkkk
.........kiiiiiiiiiiiiii
.........kiiikkkkkkkkkkk
.........kiikSSSSSSSSSSS
.........kiikSSSSSSSSSSS
.........kikSSSSSSSSSSSS
"""

HAIR['feather'] = """
...........k.k.k.k.k.k.k
..........kwkwkwkwkwkwkw
..........kwkwkwkwkwkwkw
..........kwkwkwkwkwkwkw
.......kkkkkkkkkkkkkkkkk
......kmmmmmmmmmmmmmmmmm
.....kmmnnmmnnmmnnmmnnmm
.....kmmmmmmmmmmmmmmmmmm
.....kkkkkkkkkkkkkkkkkkk
........kiiiiiiiiiiiiiii
........kiiiiiiiiiiiiiii
.......kiiiiiiiiiiiiiiii
.......kiiikkkkkkkkkkkkk
.......kiikSSSSSSSSSSSSS
.......kiikSSSSSSSSSSSSS
.......kikSSSSSSSSSSSSSS
"""

HAIR['tiger'] = """
...........kkk..........
..........kmmmk.........
..........kmnmk..kkkkkkk
...........kmmkkkmmmmmmm
...........kmmmmmmmmmmmm
..........kmmmmmmmmmmmmm
.........kmmmkmmmmmkmmmm
........kmmmmkmmmmmkmmmm
........kmmmmmmmmmmmmmmm
.......kmmmmmmmmmmmmmmmm
.......kmmmmmmkkkkkkkkkk
.......kmmmmkkSSSSSSSSSS
.......kmmmkSSSSSSSSSSSS
.......kmmkSSSSSSSSSSSSS
.......kmmkSSSSSSSSSSSSS
.......kmmkSSSSSSSSSSSSS
"""

# ================================================================ beards and masks (left halves unless noted)
def beard(c, kind, slot='i', shade='k'):
    if kind == 'moustache':
        put(c, ['...kkkkkk...', '.kkkkkkkkkk.', 'kkkkkkkkkkkk', 'kkk......kkk', 'k..........k'], 18, 27)
    elif kind == 'thin':
        put(c, ['.kkkkkkkkkk.', 'k..........k'], 18, 29)
    elif kind == 'goatee':
        put(c, ['..kkkkkkkk..', '.kk......kk.'], 18, 28)
        put(c, ['k' + slot * 2 + 'k', 'k' + slot * 2 + 'k', 'k' + slot * 2 + 'k', '.kk.'], 22, 31)
    elif kind in ('full', 'long'):
        # the beard covers the jaw below the cheeks and hangs below the chin (long: far down the chest)
        y0, n, w0, rate = (28, 6, 9, 1.2) if kind == 'full' else (29, 13, 8, 0.45)
        reg = set()
        for y in range(y0, 34):
            for x in range(c.w):
                if c.tone[y][x] in 'Ss' and 9 < x < 39:
                    reg.add((x, y))
        for y in range(34, 34 + n):
            w = w0 - (y - 34) * rate
            for x in range(c.w):
                if abs(x + 0.5 - 24) < w:
                    reg.add((x, y))
        for (x, y) in reg:
            c.paint(x, y, slot)
        for (x, y) in reg:
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                q = (x + dx, y + dy)
                if q not in reg and 0 <= q[0] < c.w and 0 <= q[1] < c.h and c.tone[q[1]][q[0]] not in 'Ssk':
                    c.paint(x, y, 'k')
                    break
        shade_right(c, {slot: shade}, band=2, x0=27, y0=y0, y1=34 + n)
        put(c, ['k' + slot * 8 + 'k', '..kkkk..'][0:1], 19, y0)
        put(c, ['.kkkk.'], 21, y0 + 3)
    elif kind == 'bushy':
        # a real beard: cheeks stay bare, the beard grows along the jaw from below the cheekbones, a drooping
        # moustache over a visible mouth, and a full beard hanging below the chin with a ragged edge and strands
        reg = set()
        for y in range(27, 34):
            for x in range(c.w):
                if c.tone[y][x] in 'Ss' and 9 < x < 39 and (abs(x + 0.5 - 24) > 8.5 - (y - 27) * 1.4 or y >= 31):
                    reg.add((x, y))
        rag = [0, 1, 0, 2, 1, 0, 1, 2, 0, 1, 0, 2, 1, 0, 1, 2, 0, 1, 0, 2, 1, 0, 1, 2]
        for y in range(34, 46):
            w = 11.5 - (y - 34) * 0.55
            for x in range(c.w):
                if abs(x + 0.5 - 24) < w and y < 46 - rag[abs(x - 24) % len(rag)]:
                    reg.add((x, y))
        for (x, y) in reg:
            c.paint(x, y, slot)
        for (x, y) in reg:
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                q = (x + dx, y + dy)
                if q not in reg and 0 <= q[0] < c.w and 0 <= q[1] < c.h and c.tone[q[1]][q[0]] not in 'Ssk':
                    c.paint(x, y, 'k')
                    break
        for (x, y) in reg:                       # strands
            if c.tone[y][x] == slot and y > 33 and (x * 2 + y) % 5 == 0:
                c.tone[y][x] = 'h'
        shade_right(c, {slot: shade}, band=2, x0=28, y0=27, y1=46)
        put(c, ['..kkkkkkkk..', '.k' + slot * 8 + 'k.', 'k' + slot * 3 + 'kkkk' + slot * 3 + 'k',
                'k' + slot * 2 + 'k....k' + slot * 2 + 'k'], 18, 28)
        put(c, ['.kkkk.', 'kSSSSk', '.kkkk.'], 21, 31)
    elif kind == 'stubble':
        for y in range(27, 34):
            for x in range(14, 34):
                if c.tone[y][x] in 'Ss' and (x + y) % 3 == 0 and y % 2 == 0 and abs(x - 23.5) > 3.5:
                    c.tone[y][x] = 's'


def mask(c, kind, slot='m', slot2='n'):
    if kind == 'cloth':                    # a cloth over the nose and mouth
        for y in range(24, 34):
            for x in range(c.w):
                if c.tone[y][x] in 'Ss' and c.part[y][x] != -1 and 10 < x < 38:
                    c.tone[y][x] = slot if x < 30 else slot2
        put(c, ['k' * 26], 11, 24)
    elif kind == 'half':                   # a silver ghost half-mask over our right half of the face
        for y in range(16, 33):
            for x in range(24, 38):
                if c.tone[y][x] in 'Ss':
                    c.tone[y][x] = 'v' if x < 33 else 'w'
        put(c, ['k'] * 17, 24, 16)
        put(c, ['kkk', 'krk', 'kkk'], 28, 21)
    elif kind == 'ghost':                  # a white fanged ghost mask filling the face
        for y in range(16, 34):
            for x in range(9, 39):
                if c.tone[y][x] in 'Ss':
                    c.tone[y][x] = 'w' if x < 31 else 'v'
        put(c, ['kkkkk', 'krrrk', '.kkk.'], 14, 21, True)
        put(c, ['kkkkkkkkkkkk', 'kwkwkwwkwkwk', 'kkkkkkkkkkkk'], 18, 28)
    elif kind == 'glasses':                # dark round lenses with a glint (the fortune teller)
        put(c, ['..kkkk..', '.k' + slot2 * 4 + 'k.', 'k' + slot2 + 'w' + slot2 * 3 + 'k', 'k' + slot2 * 5 + 'k',
                '.k' + slot2 * 4 + 'k.', '..kkkk..'], 13, 20, True)
        put(c, ['kkkk'], 21, 22)
    elif kind == 'roundglasses':
        put(c, ['.kkkk.', 'k....k', 'k....k', '.kkkk.'], 13, 21, True)
        put(c, ['kkkk'], 22, 22)
    elif kind == 'patch':
        put(c, ['kkkkkk', 'kkkkkk', '.kkkk.'], 28, 21)
        put(c, ['k'] * 1, 27, 20)
    elif kind == 'scar':
        for i in range(9):
            x, y = 15 + i * 2, 19 + i
            if c.tone[y][x] in 'Ss':
                c.tone[y][x] = 'r'


# ================================================================ bodies and props (mondraw shapes)
def body_robe(c, S):
    return robe(c, Mat('a', 'b', 'd'), top=S.get('top', 40), wide=S.get('wide', 0))


def body_armour(c, S):
    """Shoulder plates like the 霸王之路 generals: a torso plate with two layered round pauldrons."""
    top = S.get('top', 40)
    p = c.new_part()
    c.poly2([(24, top), (16, top), (8, top + 3), (4, top + 8), (3, 56), (24, 56)], Mat('a', 'b', 'd'), p)
    c.reshade(p, 16, top + 5, 14, 14, Mat('a', 'b', 'd'), dw=1, hi=0.9)
    pa2 = c.new_part()
    c.ellipse2(7.5, top + 11.5, 7.5, 5.5, Mat('e', 'f', 'g'), pa2)
    pa1 = c.new_part()
    c.ellipse2(8.5, top + 7, 8, 5.5, Mat('e', 'f', 'g'), pa1)
    S['_parts'] = [pa1, pa2]
    return p


def body_vest(c, S):
    """An open vest over a bare chest (brawlers, bandits)."""
    p = robe(c, Mat('a', 'b', 'd'), top=S.get('top', 40), wide=S.get('wide', 1))
    S['_vest'] = True
    return p


def body_fur(c, S):
    p = robe(c, Mat('a', 'b', 'd'), top=S.get('top', 40), wide=2)
    S['_fur'] = True
    return p


BODIES = {'robe': body_robe, 'armour': body_armour, 'vest': body_vest, 'fur': body_fur, 'gown': body_robe}


def prop(c, name, x=42.5, y0=8, y1=56, **kw):
    """Props held upright at the side of the bust (x is the shaft centre). Slots p q (shaft light/dark),
    v w (metal), y (gold), r (accent)."""
    P = c.new_part()
    if name == 'staff':
        c.capsule(x, y1, x, y0, 1.1, Mat('p', 'p', 'q'), P)
    elif name == 'spear':
        c.capsule(x, y1, x, y0 + 8, 1.0, Mat('p', 'p', 'q'), P)
        c.poly([(x - 2.5, y0 + 9), (x, y0), (x + 2.5, y0 + 9)], Mat('w', 'v', 'v'), c.new_part())
        c.rect(int(x - 2), y0 + 9, int(x + 1), y0 + 10, Mat('r', 'r', 'r'), c.new_part())
    elif name == 'dao':
        c.poly([(x - 2.5, y0 + 4), (x - 1, y0), (x + 2.5, y0 + 2), (x + 2.5, y1 - 14), (x - 2.5, y1 - 14)],
               Mat('w', 'v', 'v'), P)
        c.rect(int(x - 3.5), y1 - 14, int(x + 3), y1 - 13, Mat('y', 'y', 'y'), c.new_part())
        c.capsule(x, y1 - 12, x, y1 - 4, 1.3, Mat('p', 'p', 'q'), c.new_part())
    elif name == 'jian':
        c.poly([(x - 1.2, y0 + 3), (x, y0), (x + 1.2, y0 + 3), (x + 1.2, y1 - 14), (x - 1.2, y1 - 14)],
               Mat('w', 'v', 'v'), P)
        c.rect(int(x - 3), y1 - 14, int(x + 2), y1 - 13, Mat('y', 'y', 'y'), c.new_part())
        c.capsule(x, y1 - 12, x, y1 - 5, 1.0, Mat('p', 'p', 'q'), c.new_part())
    elif name == 'club':
        c.capsule(x, y1, x, y0, 2.0, Mat('p', 'p', 'q'), P, r1=3.8)
    elif name == 'fan':                    # a folding fan held up, ribs fanned out
        c.ellipse(x, y0 + 7, 7, 6, Mat('w', 'v', 'v'), P, clip=lambda xx, yy: yy < y0 + 8)
        c.capsule(x, y0 + 7, x, y0 + 13, 1.2, Mat('p', 'p', 'q'), c.new_part())
    elif name == 'feather':
        c.ellipse(x, y0 + 6, 5, 7, Mat('w', 'w', 'v'), P)
        c.capsule(x, y0 + 12, x, y0 + 18, 1.0, Mat('p', 'p', 'q'), c.new_part())
    elif name == 'gourd':
        c.ellipse(x, y0 + 8.5, 4.5, 4.5, Mat('p', 'p', 'q'), P)
        c.ellipse(x, y0 + 2.5, 3, 3, Mat('p', 'p', 'q'), P)
        c.rect(int(x - 1), y0 + 5, int(x), y0 + 5, Mat('r', 'r', 'r'), c.new_part())
    elif name == 'book':
        c.rect(int(x - 5), y0, int(x + 4), y0 + 9, Mat('p', 'p', 'q'), P)
        c.rect(int(x - 3), y0 + 2, int(x + 2), y0 + 3, Mat('w', 'w', 'w'), c.new_part())
    elif name == 'abacus':
        c.rect(int(x - 9), y0, int(x + 8), y0 + 6, Mat('q', 'q', 'q'), P)
    elif name == 'brush':
        c.capsule(x, y1, x, y0 + 5, 0.9, Mat('p', 'p', 'q'), P)
        c.ellipse(x, y0 + 2.5, 1.6, 3, Mat('k', 'k', 'k'), c.new_part())
    elif name == 'whisk':
        c.capsule(x, y1, x, y0 + 12, 0.9, Mat('p', 'p', 'q'), P)
        c.ellipse(x + 1.5, y0 + 6, 2.5, 7, Mat('w', 'w', 'v'), c.new_part())
    elif name == 'chain':
        for i in range(y0, y1, 3):
            c.ellipse(x + (1 if (i // 3) % 2 else -1), i + 1.5, 1.6, 1.6, Mat('w', 'v', 'v'), P)
    elif name == 'bow':
        c.tube([(x + 3, y0), (x - 1, y0 + 12), (x - 2, (y0 + y1) / 2), (x - 1, y1 - 12), (x + 3, y1)], 1.2,
               Mat('p', 'p', 'q'), P)
    elif name == 'hammer':
        c.capsule(x, y1, x, y0 + 6, 1.2, Mat('p', 'p', 'q'), P)
        c.rect(int(x - 4), y0, int(x + 3), y0 + 6, Mat('w', 'v', 'v'), c.new_part())
    elif name == 'banner':
        c.capsule(x, y1, x, y0, 0.9, Mat('p', 'p', 'q'), P)
        c.poly([(x + 1, y0 + 1), (x - 9, y0 + 1), (x - 9, y0 + 13), (x + 1, y0 + 13)], Mat('r', 'r', 'r'), c.new_part())
    elif name == 'dagger':
        c.poly([(x - 1, y0 + 2), (x, y0), (x + 1, y0 + 2), (x + 1, y0 + 8), (x - 1, y0 + 8)], Mat('w', 'v', 'v'), P)
        c.rect(int(x - 2), y0 + 9, int(x + 1), y0 + 9, Mat('y', 'y', 'y'), c.new_part())
        c.capsule(x, y0 + 10, x, y0 + 13, 1.0, Mat('p', 'p', 'q'), c.new_part())
    elif name == 'ball':
        c.ellipse(x, y0 + 6.5, 6.6, 6.6, Mat('w', 'w', 'v'), P)
    elif name == 'qin':                     # a qin across the bottom of the bust
        c.poly([(4, 50), (46, 47), (47, 52), (5, 55)], Mat('p', 'p', 'q'), P)
    elif name == 'hand':                    # a fist / hand at the bust's lower edge
        c.ellipse(x, y0 + 3.5, 4.2, 3.6, Mat('S', 'S', 's'), P)
    elif name == 'cape':
        c.poly2([(24, 34), (14, 32), (10, 38), (2, 42), (0, 46), (0, 56), (24, 56)], Mat('m', 'm', 'n'), P)
    elif name == 'longhair':
        c.poly2([(14, 10), (9, 13), (6, 18), (5, 26), (4, 40), (3.5, 56), (15, 56), (16, 46), (14, 36), (12, 26), (12, 16)], Mat('h', 'i', 'i'), P)
    elif name == 'sidehair':                # locks falling in front of the shoulders
        c.poly2([(12, 26), (11, 29), (9.5, 34), (8.5, 40), (8, 46), (10, 53), (14, 45), (15, 36)], Mat('h', 'i', 'i'), P)
    elif name == 'hoodcape':                # the hood falling onto the shoulders
        c.poly2([(16, 14), (11, 18), (8, 23), (6, 30), (4, 38), (1, 46), (0, 56), (14, 56), (16, 44), (16, 30)],
                Mat('m', 'm', 'n'), P)
    elif name == 'redcape':                 # a cape on the shoulders with a high collar, in the pauldron colours
        c.poly2([(24, 33), (13, 31), (9, 36), (2, 41), (0, 45), (0, 56), (24, 56)], Mat('f', 'f', 'g'), P)
    elif name == 'log':                     # the ram's iron-capped log on his shoulder
        c.capsule(-2, 47, 30, 41, 3.6, Mat('p', 'p', 'q'), P)
        c.ellipse(30, 41, 3.8, 3.8, Mat('w', 'v', 'v'), c.new_part())
    elif name == 'pack':                    # a peddler's big pack behind the shoulders
        c.rect(2, 24, 45, 50, Mat('p', 'p', 'q'), P, dw=2)
    elif name == 'bell':                    # a staff with a gold bell hanging at the top
        c.capsule(x, y1, x, y0 + 4, 1.1, Mat('p', 'p', 'q'), P)
        c.ellipse(x, y0 + 8, 3.2, 3.6, Mat('y', 'y', 'q'), c.new_part())
    elif name == 'cup':
        c.rect(int(x - 3), y0, int(x + 2), y0 + 4, Mat('w', 'v', 'v'), P)
    else:
        raise KeyError(name)
    return P


# ================================================================ the portrait builder
def person(cid, spec):
    S = dict(spec)
    colours = S['colours']
    bd = S.get('backdrop', dict(solid_to=6, check_to=26, fade=10))

    def fn(c):
        for name, kw in S.get('behind', []):
            prop(c, name, **kw)
        neck(c, 20, 27, 30, 42)
        body = BODIES[S.get('body', 'robe')](c, S)
        for name, kw in S.get('front', []):
            prop(c, name, **kw)
        c.finish()
        if S.get('_vest'):
            collar(c, body, top=S.get('top', 40), x_over=29.5, x_under=18.0, slope=0.5, band='ef',
                   inner='S', inner2='S', skin_rows=20)
        elif S.get('collar', 'eaa'):
            collar(c, body, top=S.get('top', 40), band=S.get('collar', 'eaa'), inner='S',
                   inner2=S.get('inner2', 'e'), slope=S.get('slope', 0.8))
        if S.get('body', 'robe') in ('robe', 'gown', 'vest', 'fur'):
            robe_folds(c, body)
        if S.get('_fur'):
            for (x, y) in c.cells(body):
                if c.tone[y][x] in 'abd' and (x * 3 + y * 5) % 7 == 0:
                    c.tone[y][x] = 'd'
        if S.get('sash'):
            a, b = S['sash']
            for x in range(c.w):
                for y, t in ((53, a), (54, b)):
                    if c.part[y][x] == body and c.tone[y][x] != 'k':
                        c.tone[y][x] = t
        hair = S['hair']
        half(c, HAIR[hair] if isinstance(hair, str) else hair)
        face(c, S.get('hair_slot', 'i'), S.get('eyes', 'keen'), mouth=S.get('mouth', 'firm'),
             shape=S.get('face', 'adult'), mouth_y=S.get('mouth_y', 30 if S.get('face', 'adult') != 'kid' else 28))
        if S.get('beard'):
            beard(c, S['beard'], S.get('beard_slot', 'i'), S.get('beard_shade', 'k'))
        if S.get('mask'):
            mask(c, S['mask'], S.get('mask_slot', 'm'), S.get('mask_slot2', 'n'))
        for rows, x, y, mir in S.get('after', []):
            put(c, rows, x, y, mirror=mir)
        skin_shade(c)
        shade_right(c, S.get('hair_shade', {'i': 'k', 'h': 'i', 'm': 'n'}), band=2, x0=24, y0=0, y1=16)
        if S.get('neck'):                  # a hood or cloak hides the neck
            for y in range(33, 43):
                for x in range(18, 30):
                    if c.tone[y][x] in 'Ss':
                        c.tone[y][x] = S['neck']
        for fx in S.get('post', []):
            fx(c)
        return c

    L.BUSTS[cid] = dict(fn=fn, colours=colours, spr=S.get('spr', ''), backdrop=backdrop_sky(**bd),
                        near=S.get('near', {}))


# ================================================================ sprites: heads (front, side, back; 14 rows)
SHEADS = {}


def R(t):
    return SP.R(t)


# letters: h hair, k black, S skin, b headgear, x headgear accent / band
SHEADS['topknot'] = (R('''
......kkkk......
......khhk......
....kkkkkkkk....
...khhhhhhhhk...
..khhkhhhhkhhk..
..khhhhhhhhhhk..
..khhhhhhhhhhk..
..khSSSSSSSShk..
..kSkkSSSSkkSk..
.kkSSkSSSSkSSkk.
.kSkSkSSSSkSkSk.
..kkSSSSSSSSkk..
...kkSSkkSSkk...
....kkkSSkkk....
'''), R('''
.....kkkk.......
.....khhk.......
...kkkkkkkk.....
..khhhhhhhhk....
.khhhkhhhhhhk...
.khhhhhhhhhhhk..
.khhhhhhhhhhhk..
.khhhhhhhSSSSk..
.khhhhhhSSkkSk..
.khhhhhhSSSkSk..
.khhhhSkSSSkSSk.
..khhhhSSSSSSk..
...khhhSSSSkk...
.....kkSSSk.....
'''), R('''
......kkkk......
......khhk......
....kkkkkkkk....
...khhhhhhhhk...
..khhkhhhhkhhk..
..khhhhhhhhhhk..
..khhhhhhhhhhk..
..khhhhhhhhhhk..
..khhhkhhkhhhk..
.kkhhhhhhhhhhkk.
.kSkhhhhhhhhkSk.
..kkhhhhhhhhkk..
...kkhhhhhhkk...
....kkSSSSkk....
'''))

SHEADS['band'] = tuple(SP.over(v, [r], 0, 6) for v, r in zip(SHEADS['topknot'], (
    '..kbbbbbbbbbbkbk', 'bkbbbbbbbbbbbbk.', '.kbbbbbbbbbbbbk.')))

SHEADS['bald'] = (R('''
................
................
.....kkkkkk.....
...kkSSSSSSkk...
..kSSwSSSSSSSk..
..kSwSSSSSSSSk..
..kSSSSSSSSSSk..
..kSSSSSSSSSSk..
..kSkkSSSSkkSk..
.kkSSkSSSSkSSkk.
.kSkSkSSSSkSkSk.
..kkSSSSSSSSkk..
...kkSSkkSSkk...
....kkkSSkkk....
'''), R('''
................
................
.....kkkkkk.....
...kkSSSSSSkk...
..kSSwSSSSSSSk..
.kSSwSSSSSSSSk..
.kSSSSSSSSSSSk..
.kSSSSSSSSSSSk..
.kSSSSSSSSkkSk..
.kSSSSSSSSSkSk..
.kSSSSkSSSSSSSk.
..kSSSSSSSSSSk..
...kkSSSSSSkk...
.....kkSSSk.....
'''), R('''
................
................
.....kkkkkk.....
...kkSSSSSSkk...
..kSSwSSSSSSSk..
..kSwSSSSSSSSk..
..kSSSSSSSSSSk..
..kSSSSSSSSSSk..
..kSSSSSSSSSSk..
.kkSSSSSSSSSSkk.
.kSkSSSSSSSSkSk.
..kkSSSSSSSSkk..
...kkSSSSSSkk...
....kkSSSSkk....
'''))

SHEADS['long'] = (R('''
................
.....kkkkkk.....
....khhhhhhk....
...khhhhhhhhk...
..khhhhkkhhhhk..
..khhhkSSkhhhk..
..khhkSSSSkhhk..
..khkSSSSSSkhk..
.khkSkkSSkkSkhk.
.khkSSkSSkSSkhk.
.khkSSSSSSSSkhk.
.khhkSSSSSSkhhk.
.khhhkSSSSkhhhk.
.khhkkkSSkkkhhk.
'''), R('''
................
....kkkkkk......
...khhhhhhk.....
..khhhhhhhhk....
.khhhhhhhhhhk...
.khhhhhhhhkSk...
.khhhhhhhSSSSk..
khhhhhhhSSkkSk..
khhhhhhhSSSkSk..
khhhhhhSSSSSSSk.
khhhhhhkSSSSSk..
khhhhhhhkSSkk...
.khhhhhhhkk.....
.khhhhhhhk......
'''), R('''
................
.....kkkkkk.....
....khhhhhhk....
...khhhhhhhhk...
..khhhhhhhhhhk..
..khhhhhhhhhhk..
..khhhhhhhhhhk..
..khhhhhhhhhhk..
.khhhhhhhhhhhhk.
.khhhhhhhhhhhhk.
.khhhhhhhhhhhhk.
.khhhhhhhhhhhhk.
.khhhhhhhhhhhhk.
.khhhhhhhhhhhhk.
'''))

SHEADS['bun_f'] = tuple(SP.over(v, ['.....kbbk.......'[i:] if False else r for r in rows], 0, 0) for v, rows in zip(
    SHEADS['long'], ([
        '......kbbk......',
        '.....kkbbkk.....'], [
        '.....kbbk.......',
        '....kkbbkk......'], [
        '......kbbk......',
        '.....kkbbkk.....'])))

SHEADS['hood'] = (R('''
.....kkkkkk.....
....kbbbbbbk....
...kbbbbbbbbk...
..kbbbbbbbbbbk..
..kbbbbbbbbbbk..
..kbbkkkkkkbbk..
..kbkSSSSSSkbk..
..kbkSSSSSSkbk..
.kbkSkkSSkkSkbk.
.kbkSSkSSkSSkbk.
.kbkSSSSSSSSkbk.
.kbbkSSSSSSkbbk.
.kbbbkSSSSkbbbk.
.kbbbbkkkkbbbbk.
'''), R('''
....kkkkkk......
...kbbbbbbk.....
..kbbbbbbbbk....
.kbbbbbbbbbbk...
.kbbbbbbbbbbk...
.kbbbbbbbkkkbk..
.kbbbbbbkSSSkk..
.kbbbbbbkSSkSk..
.kbbbbbbkSSkSk..
.kbbbbbbkSSSSSk.
.kbbbbbbkSSSSk..
.kbbbbbbbkkkk...
.kbbbbbbbbbk....
.kbbbbbbbbbk....
'''), R('''
.....kkkkkk.....
....kbbbbbbk....
...kbbbbbbbbk...
..kbbbbbbbbbbk..
..kbbbbbbbbbbk..
..kbbbbbbbbbbk..
..kbbbbbbbbbbk..
..kbbbbbbbbbbk..
.kbbbbbbbbbbbbk.
.kbbbbbbbbbbbbk.
.kbbbbbbbbbbbbk.
.kbbbbbbbbbbbbk.
.kbbbbbbbbbbbbk.
.kbbbbbbbbbbbbk.
'''))

SHEADS['straw'] = tuple(SP.over(v, rows, 0, 0) for v, rows in zip(SHEADS['topknot'], ([
    '.......kk.......',
    '.....kkbbkk.....',
    '...kkbbbbbbkk...',
    '.kkbbbbbbbbbbkk.',
    'kxxxxxxxxxxxxxxk',
    'kkkkkkkkkkkkkkkk',
    '..khhhhhhhhhhk..'], [
    '......kk........',
    '....kkbbkk......',
    '..kkbbbbbbkk....',
    'kkbbbbbbbbbbkk..',
    'xxxxxxxxxxxxxxk.',
    'kkkkkkkkkkkkkkk.',
    '.khhhhhhhhhhhk..'], [
    '.......kk.......',
    '.....kkbbkk.....',
    '...kkbbbbbbkk...',
    '.kkbbbbbbbbbbkk.',
    'kxxxxxxxxxxxxxxk',
    'kkkkkkkkkkkkkkkk',
    '..khhhhhhhhhhk..'])))

SHEADS['cap'] = tuple(SP.over(v, rows, 0, 0) for v, rows in zip(SHEADS['topknot'], ([
    '................',
    '................',
    '.....kkkkkk.....',
    '...kkbbbbbbkk...',
    '..kbbbbbbbbbbk..',
    '..kbbbbbbbbbbk..',
    '..kxxxxxxxxxxk..'], [
    '................',
    '................',
    '....kkkkkk......',
    '..kkbbbbbbkk....',
    '.kbbbbbbbbbbk...',
    '.kbbbbbbbbbbbk..',
    '.kxxxxxxxxxxxk..'], [
    '................',
    '................',
    '.....kkkkkk.....',
    '...kkbbbbbbkk...',
    '..kbbbbbbbbbbk..',
    '..kbbbbbbbbbbk..',
    '..kxxxxxxxxxxk..'])))

SHEADS['helmet'] = tuple(SP.over(v, rows, 0, 0) for v, rows in zip(SHEADS['cap'], ([
    '.......kk.......',
    '.......kxk......'], [
    '......kk........',
    '......kxk.......'], [
    '.......kk.......',
    '.......kxk......'])))

SHEADS['official'] = tuple(SP.over(v, rows, 0, 0) for v, rows in zip(SHEADS['topknot'], ([
    '................',
    '.....kkkkkk.....',
    '....kbbbbbbk....',
    '....kbbbbbbk....',
    'kkkkkbbbbbbkkkkk',
    'kbbkkkkkkkkkkbbk',
    'kkkbbbbbbbbbbkkk'], [
    '................',
    '....kkkkkk......',
    '...kbbbbbbk.....',
    '...kbbbbbbk.....',
    'kkkkbbbbbbbkkkk.',
    'kbbkkkkkkkkkkbbk',
    '.kbbbbbbbbbbbkkk'], [
    '................',
    '.....kkkkkk.....',
    '....kbbbbbbk....',
    '....kbbbbbbk....',
    'kkkkkbbbbbbkkkkk',
    'kbbkkkkkkkkkkbbk',
    'kkkbbbbbbbbbbkkk'])))

SHEADS['spiky'] = tuple(SP.over(v, rows, 0, 0) for v, rows in zip(SHEADS['topknot'], ([
    '...k..k..k..k...',
    '..khkkhkkhkkhk..',
    '..khhhhhhhhhhk..',
    '..khhhhhhhhhhk..'], [
    '..k..k..k.......',
    '.khkkhkkhkk.....',
    '.khhhhhhhhhk....',
    '.khhhhhhhhhhk...'], [
    '...k..k..k..k...',
    '..khkkhkkhkkhk..',
    '..khhhhhhhhhhk..',
    '..khhhhhhhhhhk..'])))

SHEADS['twinbuns'] = tuple(SP.over(v, rows, 0, 0) for v, rows in zip(SHEADS['topknot'], ([
    'kkk..........kkk',
    'khhk.kkkkkk.khhk',
    'khhkkhhhhhhkkhhk',
    '.kxkhhhhhhhhkxk.'], [
    '...........kkk..',
    '...kkkkkk.khhk..',
    '..khhhhhhkkhhk..',
    '.khhhhhhhhkxk...'], [
    'kkk..........kkk',
    'khhk.kkkkkk.khhk',
    'khhkkhhhhhhkkhhk',
    '.kxkhhhhhhhhkxk.'])))


def sprite(cid, head, pal, pal2, body='robe', m=None, extra=None, px=None, short=False, hairfill=False, face=None):
    """Register a nes2 field sprite. head: a SHEADS key or a (front, side, back) tuple of 14-row grids.
    face: optional overlay rows for the front head (beards, masks), as (rows, x, y)."""
    heads = SHEADS[head] if isinstance(head, str) else head
    fr, sd, bk = [list(h) for h in heads]
    if face:
        for rows, x, y, view in face:
            if view == 'front':
                fr = SP.over(fr, rows, x, y)
            elif view == 'side':
                sd = SP.over(sd, rows, x, y)
            else:
                bk = SP.over(bk, rows, x, y)
    bodies = {'robe': SP.ROBE, 'gown': SP.GOWN, 'boy': SP.BOY}
    bd = bodies[body] if isinstance(body, str) else body
    if short:
        fr, sd, bk = fr[1:], sd[1:], bk[1:]
    SP.SPRITES[cid] = dict(pal=pal, pal2=pal2, body=bd, m=m or {}, front=fr, side=sd, back=bk,
                           extra=extra or dict(front=[], side=[], back=[]), px=px or {}, short=short,
                           hairfill=hairfill)


# common prop overlays for sprites (front view at the right hand, side view in front, back view over the shoulder)
def sp_staff(letter='p', top=None):
    return dict(front=[([letter] * 20, 14, 3)], side=[([letter] * 20, 12, 3)], back=[([letter] * 20, 1, 3)])


def sp_blade(letter='w', hilt='p'):
    col = [letter] * 7 + [hilt] * 3
    return dict(front=[(col, 14, 9)], side=[(col, 12, 9)], back=[([letter, letter, hilt], 13, 11)])
