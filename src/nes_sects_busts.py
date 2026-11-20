"""Portraits for 龍門江湖志 (Sects of Longmen): the troops, the sects' own fighters, the crews of carts, engines and
ships, two great people and the abbess of the Mercy Cloud Nunnery. 霸王之路 bust style, like nes_longmen4_busts.py:
mondraw shapes for chests and props, hand-typed left halves for hair, hoods and hats (mirrored), hand pixels for faces;
foe_busts.autofit() + mondraw.famicom() then split each picture into the background layer and a sprite overlay.

Slots: a b d robe   e f g second material (hats, armour, mounts)   h hair   S s skin   n o props   w white
       r y accents   k black
"""
import foe_busts as FB
from foe_busts import Canvas, Mat, flat, put, head, body, shade_rows, centre_fix, T
from foe_busts_people import face, vchest, cross_collar, sash, HAIR, BALD, SKIN, HAND, WOOD, BODY, HAT, SAGE, BEARD
from nes_longmen4_busts import BUN, LONGHAIR, GAUZE, CAP_ROUND, BEARD_FULL

W, H = 48, 56
DESIGNS = {}


def design(name, spr):
    def deco(fn):
        DESIGNS[name] = dict(fn=fn, spr=spr)
        return fn
    return deco


def build(name):
    c = Canvas(W, H)
    DESIGNS[name]['fn'](c)
    return c


BODY2 = Mat('e', 'f', 'g')
METAL = Mat('w', 'w', 'o')
STEEL = Mat('e', 'f', 'g')

# ---------------------------------------------------------------- heads (left halves, 24 wide, from y=0)
TOPKNOT = '''
........................
....................kkkk
...................khhhh
...................khhhh
....................kkkk
..................kkkkkk
..............kkkkhhhhhh
............kkhhhhhhhhhh
..........kkhhhhhhhhhhhh
.........khhhhhhhhhhhhhh
........khhhhhhhhhhhhhhh
........khhhhhhhhhhhhhhh
.......khhhhhhhhhhhhhhhh
.......khhhhhhhhhhhhhhhh
.......khhhhhhhhhhhhhhhh
.......khhhhhhhkkkkkkkkk
'''
BANDKNOT = '''
........................
....................kkkk
...................khhhh
...................khhhh
....................kkkk
..................kkkkkk
..............kkkkhhhhhh
............kkhhhhhhhhhh
..........kkhhhhhhhhhhhh
.........khhhhhhhhhhhhhh
........khhhhhhhhhhhhhhh
........khhhhhhhhhhhhhhh
.......khhhhhhhhhhhhhhhh
.......khhhhhhhhhhhhhhhh
.......keeeeeeeeeeeeeeee
.......kffffffffffffffff
'''
HOOD = '''
........................
................kkkkkkkk
.............kkkeeeeeeee
...........kkeeeeeeeeeee
.........kkeeeeeeeeeeeee
........keeeeeeeeeeeeeee
........keeeeeeeeeeeeeee
.......keeeeeeeeeeeeeeee
.......keeeeeeeeeeeeeeee
.......keeeeeeeeeeeeeeee
.......keeeeeeeeeeeeeeee
......keeeeeeeeeeeeeeeee
......keeeeeeeeeeeeeeeee
......keeeeeeeeeeeeeeeee
......keeeeeeeeekkkkkkkk
......keeeeeeekkSSSSSSSS
'''
# the hood's sides, framing the face (stamped after the face, mirrored)
HOOD_SIDES = '''
keeek
keeek
keeek
keeek
keeek
keeek
keeek
.keeek
.keeek
..keeek
..keeek
...keeek
....keeeek
'''
HELMET = '''
....................rrrr
...................krrrr
...................krrrr
....................kkkk
..................kkeeee
...............kkkeeeeee
.............kkeeeeeeeee
...........kkeeeeeeeeeee
..........keeeeeeeeeeeee
.........keeeeeeeeeeeeee
........keeeeeeeeeeeeeee
........keeeeeeeeeeeeeee
.......kffffffffffffffff
.......kffffffffffffffff
.......kkkkkkkkkkkkkkkkk
........kkkkkkkkkkkkkkkk
'''
NUNHOOD = '''
........................
................kkkkkkkk
.............kkkeeeeeeee
...........kkeeeeeeeeeee
.........kkeeeeeeeeeeeee
........keeeeeeeeeeeeeee
........keeeeeeeeeeeeeee
.......keeeeeeeeeeeeeeee
.......keeeeeeeeeeeeeeee
.......keeeeeeeeeeeeeeee
.......keeeeeeeeeeeeeeee
......keeeeeeeeeeeeeeeee
......kfffffffffffffffff
......kfffffffffffffffff
......keeeeeeeekkkkkkkkk
......keeeeeeekkSSSSSSSS
'''
SPIKY = '''
........k.....k.....k...
.......khk...khk...khk..
.......khhk.khhk..khhhk.
......khhhkkhhhkkkhhhhhk
......khhhhhhhhhhhhhhhhh
.....khhhhhhhhhhhhhhhhhh
.....khhhhhhhhhhhhhhhhhh
......khhhhhhhhhhhhhhhhh
......khhhhhhhhhhhhhhhhh
.....khhhhhhhhhhhhhhhhhh
......khhhhhhhhhhhhhhhhh
......khhhhhhhhhhhhhhhhh
.......khhhhhhhhhhhhhhhh
.......khhhhhhhhhhhhhhhh
.......khhhhhhhhhhhhhhhh
.......khhhkkkkkkkkkkkkk
'''
WINGS = '''
kkkkkkkk
keeeeeek
kkkkkkkk
'''


def soldier(c, hair, hair_slot='h', eyes='stern', mouth='flat', collar='e', robe=True, wide=0, cape=None, nose=True):
    P = body(c, BODY, BODY if robe else BODY2, dots=None, robe=robe, neck=(19, 28), finish=False, wide=wide, cape=cape)
    return P


def finish_soldier(c, P, hair, hair_slot='h', eyes='stern', mouth='flat', collar='e', sash_row=53, sash_slot='d', armour=False):
    c.finish()
    if collar:
        cross_collar(c, P['torso'], collar, y0=39, slope=0.85, w=1.3)
    if sash_row:
        sash(c, P['torso'], sash_row, sash_slot, sash_slot)
    head(c, hair)
    face(c, hair_slot, eyes, mouth=mouth)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)


# ---------------------------------------------------------------- props
def saber(c, x=40):
    blade = c.new_part()
    c.poly([(x - 2, 44), (x - 1, 20), (x + 2, 12), (x + 4, 16), (x + 3, 44)], METAL, blade)
    grip = c.new_part()
    c.rect(x - 3, 44, x + 4, 46, flat('o'), grip)
    fist = c.new_part()
    c.ellipse(x + 0.5, 49.5, 3.6, 3.2, HAND, fist)


def sword(c, x=40):
    blade = c.new_part()
    c.rect(x, 8, x + 2, 42, METAL, blade)
    guard = c.new_part()
    c.rect(x - 3, 42, x + 5, 44, flat('y'), guard)
    fist = c.new_part()
    c.ellipse(x + 1, 48, 3.6, 3.2, HAND, fist)


def spear(c, x=41):
    shaft = c.new_part()
    c.rect(x, 10, x + 1, 55, flat('n'), shaft)
    tip = c.new_part()
    c.poly([(x - 2, 10), (x + 0.5, 0), (x + 3, 10)], METAL, tip)
    tassel = c.new_part()
    c.ellipse(x + 0.5, 13, 3, 2.4, flat('r'), tassel)
    fist = c.new_part()
    c.ellipse(x + 0.5, 46, 3.4, 3.0, HAND, fist)


def staff(c, x=41, rings='y'):
    shaft = c.new_part()
    c.rect(x, 6, x + 1, 55, flat('n'), shaft)
    top = c.new_part()
    c.ellipse(x + 0.5, 5, 4, 3.6, flat(rings), top)
    fist = c.new_part()
    c.ellipse(x + 0.5, 46, 3.4, 3.0, HAND, fist)


def bow(c):
    b = c.new_part()
    c.tube([(9, 3), (4, 12), (2.5, 28), (4, 44), (9, 54)], 1.6, WOOD, b)
    return b


def darts(c):
    for k, x in enumerate((37, 40, 43)):
        d = c.new_part()
        c.poly([(x - 1, 46), (x, 36 - k % 2 * 2), (x + 1, 46)], METAL, d)
    fist = c.new_part()
    c.ellipse(40, 48.5, 4, 3.2, HAND, fist)


def palms(c):
    for x in (8, 40):
        g = c.new_part()
        c.ellipse(x, 47, 5, 5, Mat('w', 'y', 'y'), g)


def bundle(c):
    b = c.new_part()
    c.ellipse(9, 34, 7, 6, Mat('w', 'w', 'n'), b)
    knot = c.new_part()
    c.ellipse(14, 38, 2, 2, flat('r'), knot)


def banner(c, cloth='r', mark='y'):
    pole = c.new_part()
    c.rect(41, 2, 42, 55, flat('n'), pole)
    flag = c.new_part()
    c.rect(30, 3, 40, 17, flat(cloth), flag)
    fist = c.new_part()
    c.ellipse(41.5, 46, 3.4, 3.0, HAND, fist)
    return flag


# ================================================================ the troops
@design('sx_founder', 'nowr')
def sx_founder(c):
    bundle(c)
    stick = c.new_part()
    c.rect(41, 14, 42, 55, flat('n'), stick)
    fist = c.new_part()
    c.ellipse(41.5, 46, 3.4, 3.0, HAND, fist)
    P = soldier(c, TOPKNOT)
    finish_soldier(c, P, TOPKNOT, eyes='calm', mouth='grin')
    return c


@design('sx_scout', 'nowy')
def sx_scout(c):
    P = soldier(c, HAT)
    knife = c.new_part()
    c.poly([(38, 47), (40, 38), (42, 47)], METAL, knife)
    fist = c.new_part()
    c.ellipse(40, 49, 3.4, 3.0, HAND, fist)
    c.finish()
    cross_collar(c, P['torso'], 'd', y0=39, slope=0.85, w=1.3)
    sash(c, P['torso'], 53, 'd', 'd')
    face(c, 'k', 'sly', mouth='flat')
    head(c, HAT)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


@design('sx_disciple', 'nowy')
def sx_disciple(c):
    staff(c, rings='n')
    P = soldier(c, BANDKNOT)
    finish_soldier(c, P, BANDKNOT, eyes='stern', mouth='flat', collar='d')
    return c


@design('sx_archer', 'nowr')
def sx_archer(c):
    b = bow(c)
    P = soldier(c, BANDKNOT)
    quiver = c.new_part()
    c.poly([(34, 30), (39, 28), (44, 41), (39, 43)], WOOD, quiver)
    c.finish()
    cross_collar(c, P['torso'], 'd', y0=39, slope=0.85, w=1.3)
    for y in range(4, 54):
        if c.tone[y][10] == '.':
            c.paint(10, y, 'w', part=b)
    head(c, BANDKNOT)
    face(c, 'h', 'sly', mouth='flat')
    put(c, '''
.w.w.w.
kwkwkwk
.knknk.
''', 35, 25)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


@design('sx_saber', 'nowy')
def sx_saber(c):
    saber(c)
    P = soldier(c, TOPKNOT)
    finish_soldier(c, P, TOPKNOT, eyes='glare', mouth='flat', collar='d')
    return c


@design('sx_sword', 'nowy')
def sx_sword(c):
    sword(c)
    P = soldier(c, BANDKNOT)
    finish_soldier(c, P, BANDKNOT, eyes='stern', mouth='flat', collar='e')
    return c


@design('sx_hidden', 'nowr')
def sx_hidden(c):
    darts(c)
    P = soldier(c, HOOD)
    c.finish()
    cross_collar(c, P['torso'], 'd', y0=39, slope=0.85, w=1.3)
    sash(c, P['torso'], 53, 'r', 'r')
    head(c, HOOD)
    face(c, 'e', 'glare', mouth='flat')
    put(c, HOOD_SIDES, 6, 16, mirror=True)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


@design('sx_spear', 'nowr')
def sx_spear(c):
    spear(c)
    P = body(c, BODY, BODY, dots=None, robe=False, neck=(19, 28), finish=False)
    finish_soldier(c, P, HELMET, hair_slot='k', eyes='stern', mouth='flat', collar=None, sash_row=50, sash_slot='d')
    return c


@design('sx_inner', 'wy')
def sx_inner(c):
    palms(c)
    P = soldier(c, LONGHAIR)
    finish_soldier(c, P, LONGHAIR, eyes='calm', mouth='flat', collar='e', sash_slot='e')
    return c


@design('sx_swordform', 'nowyr')
def sx_swordform(c):
    blade = c.new_part()
    c.rect(40, 0, 42, 34, METAL, blade)
    guard = c.new_part()
    c.rect(37, 34, 45, 36, flat('y'), guard)
    fist = c.new_part()
    c.ellipse(41, 40, 3.6, 3.2, HAND, fist)
    P = body(c, BODY, BODY, dots=None, robe=False, neck=(19, 28), finish=False)
    finish_soldier(c, P, HELMET, hair_slot='k', eyes='glare', mouth='flat', collar=None, sash_row=50, sash_slot='d')
    return c


@design('sx_crossbow', 'nowy')
def sx_crossbow(c):
    stock = c.new_part()
    c.poly([(26, 46), (44, 42), (45, 45), (27, 49)], WOOD, stock)
    arms = c.new_part()
    c.tube([(40, 33), (43, 43), (41, 53)], 1.2, flat('w'), arms)
    fist = c.new_part()
    c.ellipse(30, 49, 3.4, 3.0, HAND, fist)
    P = body(c, BODY, BODY, dots=None, robe=False, neck=(19, 28), finish=False)
    finish_soldier(c, P, BANDKNOT, eyes='sly', mouth='flat', collar=None, sash_row=50, sash_slot='d')
    return c


@design('sx_master', 'nowy')
def sx_master(c):
    hilt = c.new_part()
    c.tube([(7, 4), (10, 14), (13, 30)], 1.3, Mat('y', 'y', 'o'), hilt)
    P = soldier(c, LONGHAIR)
    finish_soldier(c, P, LONGHAIR, eyes='stern', mouth='flat', collar='y', sash_slot='y')
    return c


@design('sx_starbow', 'nowy')
def sx_starbow(c):
    b = c.new_part()
    c.tube([(10, 0), (4, 12), (2.5, 28), (4, 44), (10, 55)], 2.0, Mat('y', 'y', 'o'), b)
    P = body(c, BODY, BODY, dots=None, robe=False, neck=(19, 28), finish=False)
    c.finish()
    for y in range(1, 55):
        if c.tone[y][11] == '.':
            c.paint(11, y, 'w', part=b)
    sash(c, P['torso'], 50, 'd', 'd')
    head(c, BANDKNOT)
    face(c, 'h', 'glare', mouth='flat')
    put(c, '''
..r..
.rrr.
rrwrr
''', 34, 4)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


# ================================================================ the sects' own fighters
@design('sx_lm_saber', 'nowy')
def sx_lm_saber(c):
    saber(c)
    ring = c.new_part()
    c.ellipse(40.5, 53, 2.6, 2.2, flat('y'), ring)
    P = soldier(c, BANDKNOT)
    finish_soldier(c, P, BANDKNOT, eyes='stern', mouth='flat', collar='e')
    return c


@design('sx_hj_sword', 'nowy')
def sx_hj_sword(c):
    sword(c)
    P = soldier(c, BUN)
    c.finish()
    cross_collar(c, P['torso'], 'd', y0=39, slope=0.8, w=1.2)
    head(c, BUN)
    face(c, 'h', 'calm', mouth='flat')
    put(c, 'rr', 14, 26, mirror=True)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


@design('sx_qf_monk', 'noy')
def sx_qf_monk(c):
    staff(c)
    P = soldier(c, BALD)
    beads = c.new_part()
    for k in range(9):
        c.ellipse(16 + k * 2, 40 + abs(k - 4) * -0.6 + 2, 1.4, 1.4, flat('o'), beads)
    finish_soldier(c, P, BALD, hair_slot='S', eyes='shut', mouth='grin', collar='e', sash_row=None)
    return c


@design('sx_bl_palm', 'wy')
def sx_bl_palm(c):
    P = body(c, SKIN, SKIN, dots=None, robe=False, neck=(18, 29), finish=False, wide=2)
    c.finish()
    vchest(c, P['torso'], y0=40, slope=0.6, width=3)
    sash(c, P['torso'], 52, 'b', 'd')
    head(c, SPIKY)
    face(c, 'h', 'glare', mouth='snarl')
    put(c, 'yyyy\nyyyy', 3, 47, mirror=True)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=56)
    centre_fix(c, light_map={})
    return c


@design('sx_ym_assassin', 'nowr')
def sx_ym_assassin(c):
    darts(c)
    P = soldier(c, HOOD)
    c.finish()
    cross_collar(c, P['torso'], 'd', y0=39, slope=0.85, w=1.3)
    sash(c, P['torso'], 53, 'r', 'r')
    head(c, HOOD)
    face(c, 'e', 'glare', mouth='flat', nose=False)
    put(c, HOOD_SIDES, 6, 16, mirror=True)
    # the white bone half-mask
    put(c, '''
wwwwwwwwwww
wwwwwwwwwww
.wwwwwwwwww
.wwwwwwwwww
..wwwwwwwww
...wwwwwwww
''', 13, 25, mirror=True)
    put(c, 'rr', 18, 21, mirror=True)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


@design('sx_hf_club', 'nowr')
def sx_hf_club(c):
    club = c.new_part()
    c.capsule(40.5, 46, 42.5, 6, 1.8, WOOD, club, r1=3.8)
    fist = c.new_part()
    c.ellipse(40, 45.5, 3.4, 3.0, HAND, fist)
    P = body(c, BODY, BODY, dots=None, robe=False, neck=(18, 29), finish=False, wide=2)
    c.finish()
    vchest(c, P['torso'], y0=39, slope=0.6, width=3)
    head(c, SPIKY)
    face(c, 'h', 'glare', mouth='grin')
    head(c, BEARD_FULL, 27)
    put(c, 'w\n\n\nw\n\n\nw', 44, 8)
    put(c, 'w\n\n\nw', 38, 11)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


@design('sx_xd_blood', 'nowy')
def sx_xd_blood(c):
    blade = c.new_part()
    c.poly([(38, 44), (39, 20), (42, 10), (45, 13), (43, 44)], Mat('r', 'r', 'o'), blade)
    grip = c.new_part()
    c.rect(37, 44, 44, 46, flat('o'), grip)
    fist = c.new_part()
    c.ellipse(40.5, 49.5, 3.6, 3.2, HAND, fist)
    P = soldier(c, TOPKNOT)
    finish_soldier(c, P, TOPKNOT, eyes='glare', mouth='frown', collar='d')
    return c


@design('sx_zf_chain', 'nowy')
def sx_zf_chain(c):
    chain = c.new_part()
    for k in range(7):
        c.ellipse(38 + (k % 2) * 3, 30 + k * 3.6, 2.2, 1.8, Mat('w', 'w', 'o'), chain)
    fist = c.new_part()
    c.ellipse(40, 28, 3.4, 3.0, HAND, fist)
    P = soldier(c, GAUZE)
    c.finish()
    cross_collar(c, P['torso'], 'e', y0=39, slope=0.85, w=1.3)
    sash(c, P['torso'], 53, 'd', 'd')
    head(c, GAUZE)
    face(c, 'k', 'stern', mouth='frown')
    put(c, WINGS, 0, 9, mirror=True)
    put(c, '''
..kkkkkkk.
kkkkkkkkkk
''', 15, 28, mirror=True)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


@design('sx_cy_nun', 'nowy')
def sx_cy_nun(c):
    sword(c)
    P = soldier(c, NUNHOOD)
    c.finish()
    cross_collar(c, P['torso'], 'e', y0=39, slope=0.8, w=1.2)
    head(c, NUNHOOD)
    face(c, 'e', 'calm', mouth='flat')
    put(c, HOOD_SIDES, 6, 16, mirror=True)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


@design('jingci', 'nowr')
def jingci(c):
    whisk = c.new_part()
    c.rect(41, 26, 42, 50, flat('n'), whisk)
    tuft = c.new_part()
    c.tube([(41.5, 26), (40, 16), (38, 6)], 2.4, Mat('w', 'w', 'w'), tuft, r1=1.0)
    fist = c.new_part()
    c.ellipse(41.5, 46, 3.4, 3.0, HAND, fist)
    P = soldier(c, NUNHOOD)
    beads = c.new_part()
    for k in range(9):
        c.ellipse(16 + k * 2, 42 - abs(k - 4) * 0.5, 1.4, 1.4, flat('r'), beads)
    c.finish()
    cross_collar(c, P['torso'], 'e', y0=39, slope=0.8, w=1.2)
    head(c, NUNHOOD)
    face(c, 'e', 'shut', mouth='flat')
    put(c, HOOD_SIDES, 6, 16, mirror=True)
    # age lines and white brows
    put(c, 'eeee', 13, 17, mirror=True)
    put(c, 's', 14, 27, mirror=True)
    put(c, 's', 15, 28, mirror=True)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


@design('sx_grandmaster', 'nowy')
def sx_grandmaster(c):
    staff(c, rings='y')
    P = soldier(c, SAGE)
    c.finish()
    cross_collar(c, P['torso'], 'e', y0=39, slope=0.85, w=1.3)
    sash(c, P['torso'], 53, 'd', 'd')
    head(c, SAGE)
    face(c, 'e', 'shut', mouth='flat')
    head(c, BEARD, 26)
    put(c, 'eeee', 13, 17, mirror=True)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=26)
    centre_fix(c)
    return c


@design('sx_smith', 'nowr')
def sx_smith(c):
    handle = c.new_part()
    c.rect(41, 24, 42, 50, flat('n'), handle)
    hd = c.new_part()
    c.rect(36, 18, 47, 25, Mat('w', 'o', 'o'), hd)
    fist = c.new_part()
    c.ellipse(41.5, 46, 3.4, 3.0, HAND, fist)
    P = body(c, SKIN, SKIN, dots=None, robe=False, neck=(18, 29), finish=False, wide=2)
    apron = c.new_part()
    c.rect(14, 42, 33, 56, BODY, apron)
    c.finish()
    head(c, TOPKNOT)
    face(c, 'h', 'stern', mouth='grin')
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=56)
    centre_fix(c, light_map={})
    return c


# ================================================================ mounted troops: the rider with the mount's head beside
def mount_head(c, mat, ears='k', tiger=False):
    neck = c.new_part()
    c.poly2([(32, 56), (34, 40), (38, 32), (46, 36), (47, 56)], mat, neck) if False else c.poly([(32, 56), (35, 40), (39, 33), (47, 36), (47, 56)], mat, neck)
    hd = c.new_part()
    if tiger:
        c.ellipse(41, 30, 7, 6.5, mat, hd)
    else:
        c.poly([(36, 26), (40, 20), (46, 22), (47, 38), (43, 40)], mat, hd)
    return hd


@design('sx_rider', 'nowr')
def sx_rider(c):
    hd = mount_head(c, WOOD)
    P = body(c, BODY, BODY, dots=None, robe=True, neck=(19, 28), finish=False)
    c.finish()
    cross_collar(c, P['torso'], 'd', y0=39, slope=0.85, w=1.3)
    put(c, 'kk\nkk', 42, 25)
    put(c, 'w\nw\nw\nw', 45, 26)
    put(c, 'k.k\nkkk', 40, 18)
    head(c, HELMET)
    face(c, 'k', 'stern', mouth='flat')
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


@design('sx_ironcav', 'nowr')
def sx_ironcav(c):
    hd = mount_head(c, Mat('w', 'o', 'o'))
    P = body(c, BODY, BODY, dots=None, robe=False, neck=(19, 28), finish=False)
    c.finish()
    put(c, 'kk\nkk', 42, 25)
    put(c, 'k.k\nkkk', 40, 18)
    sash(c, P['torso'], 50, 'd', 'd')
    head(c, HELMET)
    face(c, 'k', 'glare', mouth='flat')
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


@design('sx_yy_tiger', 'nowr')
def sx_yy_tiger(c):
    hd = mount_head(c, WOOD, tiger=True)
    P = body(c, BODY, BODY, dots=None, robe=True, neck=(19, 28), finish=False)
    c.finish()
    cross_collar(c, P['torso'], 'd', y0=39, slope=0.85, w=1.3)
    put(c, '''
k.....k
kk...kk
.......
.kk.kk.
.wk.kw.
.......
..kkk..
.wkwkw.
''', 38, 23)
    put(c, 'k\nk\n.\nk\nk', 35, 30)
    put(c, 'k\nk\n.\nk\nk', 46, 30)
    head(c, HOOD)
    face(c, 'e', 'sly', mouth='flat')
    put(c, HOOD_SIDES, 6, 16, mirror=True)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


# ================================================================ crews of carts, engines and ships
@design('sx_caravan', 'nowry')
def sx_caravan(c):
    flag = banner(c)
    P = soldier(c, BANDKNOT)
    c.finish()
    put(c, '''
yyy
y.y
yyy
.y.
yyy
''', 34, 7)
    cross_collar(c, P['torso'], 'e', y0=39, slope=0.85, w=1.3)
    sash(c, P['torso'], 53, 'd', 'd')
    head(c, BANDKNOT)
    face(c, 'h', 'stern', mouth='grin')
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


@design('sx_qj_escort', 'nowry')
def sx_qj_escort(c):
    flag = banner(c, cloth='y', mark='r')
    P = soldier(c, CAP_ROUND)
    c.finish()
    put(c, '''
rrr
r.r
rrr
.r.
rrr
''', 34, 7)
    cross_collar(c, P['torso'], 'e', y0=39, slope=0.85, w=1.3)
    sash(c, P['torso'], 53, 'd', 'd')
    head(c, CAP_ROUND)
    face(c, 'h', 'calm', mouth='grin')
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


@design('sx_ram', 'nowy')
def sx_ram(c):
    log = c.new_part()
    c.capsule(2, 36, 46, 30, 3.6, WOOD, log)
    cap = c.new_part()
    c.ellipse(45, 30, 3.2, 4.2, Mat('w', 'w', 'o'), cap)
    P = body(c, SKIN, SKIN, dots=None, robe=False, neck=(18, 29), finish=False, wide=2)
    c.finish()
    sash(c, P['torso'], 52, 'b', 'd')
    head(c, BALD)
    face(c, 'S', 'glare', mouth='grin')
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=56)
    centre_fix(c, light_map={})
    return c


@design('sx_catapult', 'nowy')
def sx_catapult(c):
    stone = c.new_part()
    c.ellipse(40, 44, 6, 5.5, Mat('w', 'o', 'o'), stone)
    fist = c.new_part()
    c.ellipse(36, 49, 3.4, 3.0, HAND, fist)
    P = soldier(c, CAP_ROUND)
    finish_soldier(c, P, CAP_ROUND, eyes='sly', mouth='flat', collar='e')
    return c


@design('sx_thunder', 'nowr')
def sx_thunder(c):
    bomb = c.new_part()
    c.ellipse(40, 44, 6, 6, Mat('o', 'o', 'o'), bomb)
    fuse = c.new_part()
    c.tube([(41, 38), (43, 33), (46, 31)], 0.8, flat('n'), fuse)
    fist = c.new_part()
    c.ellipse(35, 50, 3.4, 3.0, HAND, fist)
    P = soldier(c, BANDKNOT)
    c.finish()
    put(c, '.r.\nrwr\n.r.', 45, 28)
    cross_collar(c, P['torso'], 'e', y0=39, slope=0.85, w=1.3)
    sash(c, P['torso'], 53, 'd', 'd')
    head(c, BANDKNOT)
    face(c, 'h', 'glare', mouth='grin')
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


@design('sx_boat', 'nowy')
def sx_boat(c):
    oar = c.new_part()
    c.rect(41, 4, 42, 55, flat('n'), oar)
    blade = c.new_part()
    c.ellipse(41.5, 6, 3, 6, WOOD, blade)
    fist = c.new_part()
    c.ellipse(41.5, 44, 3.4, 3.0, HAND, fist)
    P = soldier(c, HAT)
    c.finish()
    cross_collar(c, P['torso'], 'd', y0=39, slope=0.85, w=1.3)
    face(c, 'k', 'calm', mouth='grin')
    head(c, HAT)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


@design('sx_warship', 'nowyr')
def sx_warship(c):
    flag = banner(c, cloth='y', mark='r')
    P = body(c, BODY, BODY, dots=None, robe=False, neck=(19, 28), finish=False)
    c.finish()
    put(c, '''
.r.
rrr
.r.
''', 34, 8)
    sash(c, P['torso'], 50, 'd', 'd')
    head(c, HELMET)
    face(c, 'k', 'stern', mouth='flat')
    put(c, '''
..kkkkk..
.kk...kk.
''', 16, 28, mirror=True)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


SKN = dict(S=0x37, s=0x27)
TAN = dict(S=0x27, s=0x17)
COLOURS = {
    'sx_founder': dict(SKN, h=0x0C, a=0x27, b=0x17, d=0x07, e=0x30, w=0x30, n=0x17, o=0x07, r=0x16),
    'sx_scout': dict(SKN, h=0x0C, a=0x2A, b=0x1A, d=0x0A, e=0x38, f=0x28, w=0x30, n=0x17, o=0x07, y=0x28),
    'sx_disciple': dict(SKN, h=0x0C, a=0x10, b=0x00, d=0x0C, e=0x30, f=0x10, w=0x30, n=0x17, o=0x07, y=0x28),
    'sx_archer': dict(SKN, h=0x0C, a=0x2A, b=0x0A, d=0x0C, e=0x16, f=0x06, w=0x30, n=0x17, o=0x07, r=0x16),
    'sx_saber': dict(SKN, h=0x0C, a=0x27, b=0x17, d=0x07, e=0x10, w=0x30, n=0x17, o=0x07, y=0x28),
    'sx_sword': dict(SKN, h=0x0C, a=0x31, b=0x21, d=0x11, e=0x30, f=0x10, w=0x30, n=0x17, o=0x07, y=0x28),
    'sx_hidden': dict(SKN, h=0x0C, a=0x13, b=0x03, d=0x0C, e=0x00, w=0x30, n=0x17, o=0x07, r=0x16),
    'sx_spear': dict(SKN, h=0x0C, a=0x26, b=0x16, d=0x06, e=0x10, f=0x00, g=0x0C, w=0x30, n=0x17, o=0x07, r=0x16),
    'sx_inner': dict(SKN, h=0x0C, g=0x00, a=0x30, b=0x10, d=0x00, e=0x21, w=0x30, y=0x31),
    'sx_swordform': dict(SKN, h=0x0C, a=0x22, b=0x12, d=0x02, e=0x10, f=0x00, g=0x0C, w=0x30, n=0x17, o=0x07, y=0x28, r=0x30),
    'sx_crossbow': dict(SKN, h=0x0C, a=0x2C, b=0x1C, d=0x0C, e=0x10, f=0x00, g=0x0C, w=0x30, n=0x17, o=0x07, y=0x28),
    'sx_master': dict(SKN, h=0x30, g=0x10, a=0x10, b=0x00, d=0x0C, e=0x28, w=0x30, n=0x17, o=0x07, y=0x28),
    'sx_starbow': dict(SKN, h=0x0C, a=0x26, b=0x16, d=0x06, e=0x28, f=0x18, g=0x08, w=0x30, n=0x17, o=0x07, y=0x28, r=0x16),
    'sx_lm_saber': dict(SKN, h=0x0C, a=0x22, b=0x12, d=0x02, e=0x21, f=0x11, w=0x30, n=0x17, o=0x07, y=0x28),
    'sx_hj_sword': dict(SKN, h=0x0C, a=0x31, b=0x21, d=0x11, e=0x30, w=0x30, n=0x17, o=0x07, y=0x30, r=0x15),
    'sx_qf_monk': dict(SKN, h=0x0C, a=0x38, b=0x28, d=0x17, e=0x16, n=0x17, o=0x07, y=0x28, w=0x30),
    'sx_bl_palm': dict(TAN, h=0x0C, b=0x16, d=0x06, w=0x30, y=0x28),
    'sx_ym_assassin': dict(SKN, h=0x0C, a=0x14, b=0x04, d=0x0C, e=0x04, w=0x30, n=0x17, o=0x07, r=0x16),
    'sx_hf_club': dict(TAN, h=0x0F, a=0x17, b=0x07, d=0x0C, w=0x30, n=0x17, o=0x07, r=0x16),
    'sx_xd_blood': dict(SKN, h=0x0C, a=0x16, b=0x06, d=0x0C, w=0x30, n=0x17, o=0x07, r=0x16, y=0x28),
    'sx_zf_chain': dict(SKN, h=0x0C, a=0x10, b=0x00, d=0x0C, e=0x0F, f=0x00, w=0x30, n=0x17, o=0x07, y=0x28),
    'sx_cy_nun': dict(SKN, h=0x0C, a=0x35, b=0x25, d=0x15, e=0x30, f=0x25, w=0x30, n=0x17, o=0x07, y=0x28),
    'jingci': dict(SKN, h=0x0C, a=0x10, b=0x00, d=0x0C, e=0x30, f=0x15, w=0x30, n=0x17, o=0x07, r=0x16),
    'sx_grandmaster': dict(SKN, h=0x0C, a=0x21, b=0x11, d=0x01, e=0x30, w=0x30, n=0x17, o=0x07, y=0x28),
    'sx_smith': dict(TAN, h=0x0C, a=0x17, b=0x07, d=0x0C, e=0x16, f=0x06, w=0x30, n=0x17, o=0x00, r=0x16),
    'sx_rider': dict(SKN, h=0x0C, a=0x26, b=0x16, d=0x06, e=0x10, f=0x00, g=0x0C, w=0x30, n=0x17, o=0x07, r=0x16),
    'sx_ironcav': dict(SKN, h=0x0C, a=0x22, b=0x12, d=0x02, e=0x10, f=0x00, g=0x0C, w=0x10, n=0x17, o=0x00, r=0x30),
    'sx_yy_tiger': dict(SKN, h=0x0C, a=0x2A, b=0x1A, d=0x0A, e=0x0A, f=0x0A, w=0x30, n=0x27, o=0x07, r=0x16),
    'sx_caravan': dict(SKN, h=0x0C, a=0x27, b=0x17, d=0x07, e=0x16, f=0x06, w=0x30, n=0x17, o=0x07, r=0x16, y=0x28),
    'sx_qj_escort': dict(SKN, h=0x0C, a=0x38, b=0x28, d=0x18, e=0x16, f=0x06, w=0x30, n=0x17, o=0x07, r=0x16, y=0x28),
    'sx_ram': dict(TAN, h=0x0C, b=0x07, d=0x0C, w=0x10, n=0x17, o=0x07, y=0x28),
    'sx_catapult': dict(SKN, h=0x0C, a=0x2A, b=0x1A, d=0x0A, e=0x17, f=0x07, w=0x10, n=0x17, o=0x00, y=0x28),
    'sx_thunder': dict(SKN, h=0x0C, a=0x26, b=0x16, d=0x06, e=0x28, f=0x18, w=0x30, n=0x17, o=0x00, r=0x27),
    'sx_boat': dict(SKN, h=0x0C, a=0x21, b=0x11, d=0x01, e=0x38, f=0x28, w=0x30, n=0x17, o=0x07, y=0x28),
    'sx_warship': dict(SKN, h=0x0C, a=0x22, b=0x12, d=0x02, e=0x10, f=0x00, g=0x0C, w=0x30, n=0x17, o=0x07, y=0x28, r=0x16),
}
