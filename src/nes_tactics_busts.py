"""Portraits for 龍門戰記 (Longmen Tactics): 奕長風, 蕭無影 and the job figures (src/nes_tactics.py).
霸王之路 bust style, made exactly like nes_sects_busts.py: mondraw shapes for chests and props, the shared hand-typed
heads, hand pixels for faces; foe_busts.autofit() + mondraw.famicom() split each picture into the background layer and
a sprite overlay.

Slots: a b d robe   e f g second material (hats, bands)   h hair   S s skin   n o props   w white   r y accents   k black
"""
from foe_busts import Canvas, Mat, flat, put, head, body, shade_rows, centre_fix
from foe_busts_people import face, cross_collar, sash, HAND, WOOD, BODY, BEARD
from nes_longmen4_busts import BUN, LONGHAIR, GAUZE, CAP_ROUND, BEARD_FULL
from nes_sects_busts import soldier, finish_soldier, saber, darts, TOPKNOT, BANDKNOT, HOOD, HOOD_SIDES, WINGS, METAL

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


# ---------------------------------------------------------------- props
def gourd(c, x=40):
    top = c.new_part()
    c.ellipse(x, 38, 2.8, 2.6, Mat('n', 'n', 'o'), top)
    band = c.new_part()
    c.rect(x - 2, 40, x + 2, 41, flat('r'), band)
    bot = c.new_part()
    c.ellipse(x, 47, 4.8, 4.6, Mat('n', 'n', 'o'), bot)
    plug = c.new_part()
    c.rect(x - 1, 34, x + 1, 35, flat('o'), plug)


def qin(c):
    board = c.new_part()
    c.poly([(1, 45), (47, 41), (47, 47), (1, 52)], Mat('n', 'n', 'o'), board)
    return board


def qin_strings(c, board):
    for y in (45, 47):
        for x in range(4, 45):
            yy = y + round((44 - x) * 0.09) - 1
            if 0 <= yy < H and c.tone[yy][x] in ('n', 'o'):
                c.paint(x, yy, 'w', part=board)


def featherfan(c, x=40):
    fan = c.new_part()
    c.ellipse(x, 24, 6.5, 8.5, Mat('w', 'w', 'e'), fan)
    rib = c.new_part()
    c.rect(x, 18, x, 32, flat('e'), rib)
    handle = c.new_part()
    c.rect(x, 32, x + 1, 44, flat('n'), handle)
    fist = c.new_part()
    c.ellipse(x + 0.5, 45, 3.4, 3.0, HAND, fist)


def foldfan(c, x=39):
    fan = c.new_part()
    c.poly([(x - 9, 26), (x - 4, 18), (x + 4, 17), (x + 9, 24), (x + 1, 40)], Mat('r', 'r', 'y'), fan)
    fist = c.new_part()
    c.ellipse(x + 1, 42, 3.4, 3.0, HAND, fist)


def brush(c, x=41):
    shaft = c.new_part()
    c.rect(x, 8, x + 1, 50, flat('n'), shaft)
    tip = c.new_part()
    c.poly([(x - 2, 9), (x + 0.5, 0), (x + 3, 9)], flat('o'), tip)
    fist = c.new_part()
    c.ellipse(x + 0.5, 46, 3.4, 3.0, HAND, fist)


def dagger(c, x=40):
    knife = c.new_part()
    c.poly([(x - 2, 47), (x, 36), (x + 2, 47)], METAL, knife)
    fist = c.new_part()
    c.ellipse(x, 49, 3.4, 3.0, HAND, fist)


def peachsword(c, x=40):
    blade = c.new_part()
    c.rect(x, 8, x + 2, 42, Mat('n', 'n', 'o'), blade)
    talisman = c.new_part()
    c.rect(x - 1, 14, x + 3, 24, flat('y'), talisman)
    guard = c.new_part()
    c.rect(x - 3, 42, x + 5, 44, flat('r'), guard)
    fist = c.new_part()
    c.ellipse(x + 1, 48, 3.6, 3.2, HAND, fist)


def finish_plain(c, P, hair, hair_slot='h', eyes='calm', mouth='flat', collar='e', sash_slot=None):
    c.finish()
    if collar:
        cross_collar(c, P['torso'], collar, y0=39, slope=0.85, w=1.3)
    if sash_slot:
        sash(c, P['torso'], 53, sash_slot, sash_slot)
    head(c, hair)
    face(c, hair_slot, eyes, mouth=mouth)


# ================================================================ the two people of the story
@design('yichangfeng', 'nowy')
def yichangfeng(c):
    saber(c)
    ring = c.new_part()
    c.ellipse(40.5, 53, 2.6, 2.2, flat('y'), ring)
    P = soldier(c, TOPKNOT)
    finish_plain(c, P, TOPKNOT, eyes='stern', mouth='flat', collar='e', sash_slot='d')
    head(c, BEARD_FULL, 27)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=27)
    centre_fix(c)
    return c


@design('xiaowuying', 'nowr')
def xiaowuying(c):
    darts(c)
    P = soldier(c, GAUZE)
    finish_plain(c, P, GAUZE, hair_slot='k', eyes='sly', mouth='flat', collar='e', sash_slot='r')
    put(c, WINGS, 0, 9, mirror=True)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


# ================================================================ the job figures
@design('sx_physician', 'nowr')
def sx_physician(c):
    P = soldier(c, TOPKNOT)
    gourd(c)
    finish_soldier(c, P, TOPKNOT, eyes='calm', mouth='flat', collar='e', sash_slot='d')
    return c


@design('sx_physician_f', 'nowr')
def sx_physician_f(c):
    P = soldier(c, BUN)
    gourd(c)
    finish_plain(c, P, BUN, eyes='calm', mouth='flat', collar='e')
    put(c, 'rr', 14, 26, mirror=True)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


@design('sx_thief', 'nowy')
def sx_thief(c):
    P = soldier(c, BANDKNOT)
    dagger(c)
    finish_soldier(c, P, BANDKNOT, eyes='sly', mouth='grin', collar='d')
    return c


@design('sx_daoist', 'nowry')
def sx_daoist(c):
    peachsword(c)
    P = soldier(c, TOPKNOT)
    finish_plain(c, P, TOPKNOT, eyes='calm', mouth='flat', collar='d', sash_slot='r')
    put(c, 'kyy\nkyy', 21, 0, mirror=True)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


@design('sx_qin', 'nowy')
def sx_qin(c):
    P = soldier(c, LONGHAIR)
    bd = qin(c)
    finish_plain(c, P, LONGHAIR, eyes='calm', mouth='flat', collar='e', sash_slot='e')
    qin_strings(c, bd)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


@design('sx_qin_f', 'nowr')
def sx_qin_f(c):
    P = soldier(c, BUN)
    bd = qin(c)
    finish_plain(c, P, BUN, eyes='calm', mouth='flat', collar='e')
    put(c, 'rr', 14, 26, mirror=True)
    qin_strings(c, bd)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


@design('sx_poison', 'nowr')
def sx_poison(c):
    P = soldier(c, HOOD)
    gourd(c)
    c.finish()
    cross_collar(c, P['torso'], 'd', y0=39, slope=0.85, w=1.3)
    sash(c, P['torso'], 53, 'r', 'r')
    head(c, HOOD)
    face(c, 'e', 'sly', mouth='snarl')
    put(c, HOOD_SIDES, 6, 16, mirror=True)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


@design('sx_strategist', 'nowye')
def sx_strategist(c):
    featherfan(c)
    P = soldier(c, CAP_ROUND)
    finish_plain(c, P, CAP_ROUND, eyes='calm', mouth='flat', collar='e', sash_slot='d')
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


@design('sx_teller', 'nowyfe')
def sx_teller(c):
    foldfan(c)
    P = soldier(c, CAP_ROUND)
    finish_plain(c, P, CAP_ROUND, eyes='calm', mouth='grin', collar='e', sash_slot='d')
    head(c, BEARD, 27)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=27)
    centre_fix(c)
    return c


@design('sx_scholar', 'nowy')
def sx_scholar(c):
    brush(c)
    P = soldier(c, BANDKNOT)
    finish_soldier(c, P, BANDKNOT, eyes='calm', mouth='flat', collar='e')
    return c


@design('sx_phantom', 'nowr')
def sx_phantom(c):
    darts(c)
    P = soldier(c, HOOD)
    c.finish()
    cross_collar(c, P['torso'], 'd', y0=39, slope=0.85, w=1.3)
    sash(c, P['torso'], 53, 'r', 'r')
    head(c, HOOD)
    face(c, 'e', 'glare', mouth='flat', nose=False)
    put(c, HOOD_SIDES, 6, 16, mirror=True)
    # a black cloth over the lower face, eyes only
    put(c, '''
kkkkkkkkkkk
kkkkkkkkkkk
.kkkkkkkkkk
..kkkkkkkkk
''', 13, 27, mirror=True)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=27)
    centre_fix(c)
    return c


SKN = dict(S=0x37, s=0x27)
TAN = dict(S=0x27, s=0x17)
COLOURS = {
    'yichangfeng': dict(SKN, h=0x00, a=0x12, b=0x02, d=0x0C, e=0x30, w=0x30, n=0x17, o=0x07, y=0x28),
    'xiaowuying': dict(SKN, h=0x0C, a=0x14, b=0x04, d=0x0C, e=0x00, f=0x0C, w=0x30, n=0x17, o=0x07, r=0x16),
    'sx_physician': dict(SKN, h=0x0C, a=0x2A, b=0x1A, d=0x0A, e=0x30, w=0x30, n=0x27, o=0x17, r=0x16),
    'sx_physician_f': dict(SKN, h=0x0C, a=0x2C, b=0x1C, d=0x0C, e=0x30, w=0x30, n=0x27, o=0x17, r=0x15, y=0x30),
    'sx_thief': dict(TAN, h=0x0C, a=0x10, b=0x00, d=0x0C, e=0x16, f=0x06, w=0x30, n=0x17, o=0x07, y=0x28),
    'sx_daoist': dict(SKN, h=0x0C, a=0x38, b=0x28, d=0x18, e=0x30, w=0x30, n=0x27, o=0x17, y=0x28, r=0x16),
    'sx_qin': dict(SKN, h=0x0C, a=0x21, b=0x11, d=0x01, e=0x30, w=0x30, n=0x17, o=0x07, y=0x28),
    'sx_qin_f': dict(SKN, h=0x0C, a=0x35, b=0x25, d=0x15, e=0x30, w=0x30, n=0x17, o=0x07, r=0x16, y=0x28),
    'sx_poison': dict(SKN, h=0x0C, a=0x14, b=0x04, d=0x0C, e=0x04, w=0x30, n=0x1A, o=0x0A, r=0x1A),
    'sx_strategist': dict(SKN, h=0x0C, a=0x10, b=0x00, d=0x0C, e=0x00, f=0x21, w=0x30, n=0x17, o=0x07, y=0x28),
    'sx_teller': dict(SKN, h=0x0C, a=0x27, b=0x17, d=0x07, e=0x0C, f=0x07, w=0x30, n=0x17, o=0x07, y=0x28, r=0x16),
    'sx_scholar': dict(SKN, h=0x0C, a=0x2B, b=0x1B, d=0x0B, e=0x30, f=0x10, w=0x30, n=0x27, o=0x0C, y=0x28),
    'sx_phantom': dict(TAN, h=0x0C, a=0x10, b=0x00, d=0x0C, e=0x00, w=0x30, n=0x17, o=0x07, r=0x16),
}
# every slot a shared head or prop may use gets a colour (darkest shades fall back to near-black)
for _c in COLOURS.values():
    for _k, _v in dict(f=_c.get('e', 0x00), g=0x0C, r=0x16, y=0x28, n=0x17, o=0x07).items():
        _c.setdefault(_k, _v)
