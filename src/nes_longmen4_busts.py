"""Portraits of the new people of Longmen Quest II, in the 霸王之路 bust style (like the generals and the common foes).

Drawn with the foe_busts helpers (mondraw shapes for the chest and props, hand-typed left halves for hair and hats,
mirrored; hand pixels for faces and details), then foe_busts.autofit() + mondraw.famicom() split each picture into
the background layer and a sprite overlay, the way nes_foes_art.py does. COLOURS maps each slot to an NES colour.
nes_longmen4.py turns these into PORTRAITS entries (nes.Pic.check() proves the Famicom rules).

Slots: a b d main material   e f g second material   h hair   S s skin   n o props   r y accents   w white   k black
"""
import foe_busts as FB
from foe_busts import Canvas, Mat, flat, put, head, body, shade_rows, centre_fix, T
from foe_busts_people import face, vchest, cross_collar, sash, HAIR, SCARF, BALD, SKIN, HAND, WOOD, BODY

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


# ---------------------------------------------------------------- hair and hats (left halves, 24 wide, from y=0)
GAUZE = '''
........................
.............kkkkkkkkkkk
............keeeeeeeeeee
............keeeeeeeeeee
............keeeeeeeeeee
............keeeeeeeeeee
............keeeeeeeeeee
............keeeeeeeeeee
............keeeeeeeeeee
.........kkkkkkkkkkkkkkk
........kfffffffffffffff
........kkkkkkkkkkkkkkkk
.......khhhhhhhhhhhhhhhh
.......khhhhhhhhhhhhhhhh
.......khhhhhhhhhhhhhhhh
.......khkkkkkkkkkkkkkkk
'''

CAP_ROUND = '''
........................
........................
.....................kkk
...................kkyyy
................kkkkeeee
.............kkkeeeeeeee
...........kkeeeeeeeeeee
..........keeeeeeeeeeeee
.........keeeeeeeeeeeeee
........keeeeeeeeeeeeeee
........keeeeeeeeeeeeeee
.......kffffffffffffffff
.......kffffffffffffffff
.......kkkkkkkkkkkkkkkkk
.......khhhhhhhhhhhhhhhh
.......khhhhhkkkkkkkkkkk
'''

SCHOLAR = '''
........................
........................
........kkkkkkkkkkkkkkkk
........keeeeeeeeeeeeeee
........keeeeeeeeeeeeeee
........keeeeeeeeeeeeeee
........keeeeeeeeeeeeeee
........keeeeeeeeeeeeeee
....kk..keeeeeeeeeeeeeee
...kwwk.keeeeeeeeeeeeeee
...kwwkkkfffffffffffffff
....kwwkkkkkkkkkkkkkkkkk
.....kwwkhhhhhhhhhhhhhhh
......kkkhhhhhhhhhhhhhhh
.......khhhhhhhhhhhhhhhh
.......khhhhhhhkkkkkkkkk
'''

BUN = '''
....................kkkk
...................khhhh
..................khhhhh
.................kyyhhhh
................kyyhhhhh
..............kkhhhhhhhh
............kkhhhhhhhhhh
..........kkhhhhhhhhhhhh
.........khhhhhhhhhhhhhh
........khhhhhhhhhhhhhhh
........khhhhhhhhhhhhhhh
.......khhhhhhhhhhhhhhhh
.......khhhhhhhhhhhhhhhh
.......khhhhhhhhhhhhhhhh
.......khhhhhhhhhhhkkkkk
.......khhhhhhhkkkkSSSSS
'''

PONY = '''
........................
........................
....................kkkk
..................kkhhhh
...............kkkhhhhhh
.............kkhhhhhhhhh
...........kkhhhhhhhhhhh
..........khhhhhhhhhhhhh
.........khhhhhhhhhhhhhh
........khhhhhhhhhhhhhhh
........khhhhhhhhhhhhhhh
.......khhhhhhhhhhhhhhhh
.......kwwwwwwwwwwwwwwww
.......kwwwwwwwwwwwwwwww
.......khhhhhhhhhhhhhhhh
.......khhhhhhkkkkkkkkkk
'''

LONGHAIR = '''
........................
........................
..................kkkkkk
...............kkkhhhhhh
.............kkhhhhhhhhh
...........kkhhhhhhhhhhh
..........khhhhhhhhhhhhh
.........khhhhhhhhhhhhhh
........khhhhghhhhhhhhhh
........khhhhghhhhhhhhhh
.......khhhhghhhhhhhhhhh
.......khhhhghhhhhhhhhhh
......khhhhghhhhhhhhhhhh
......khhhhghhhhhhhhhhhh
......khhhhhhhhhhhhhkkkk
......khhhhhhhhhkkkkSSSS
'''

FEATHER = '''
...........kk...........
..........krrk..........
..........krrk..........
.........krrk...........
.........krrk...........
........krrk............
'''

HORNS = '''
...kk...................
..kwwk..................
..kwwk..................
...kwwk.................
...kwwk.......kkkkkkkkkk
....kwwk...kkkwwwwwwwwww
....kwwkkkkwwwwwwwwwwwww
.....kwwnwnwnwnwnwnwnwnw
.....knwnwnwnwnwnwnwnwnw
......kwwwwwwwwwwwwwwwww
.......kyyryyryyryyryyry
.......kkkkkkkkkkkkkkkkk
.......khhhhhhhhhhhhhhhh
.......khhhhhhhhhhhhhhhh
.......khhhhhhhhhhhhhhhh
.......khhhhhhhkkkkkkkkk
'''


def glasses(c, dark=True):
    put(c, '''
..kkkkk....
.k.....k...
k.......kkk
k.......k..
.k.....k...
..kkkkk....
''' if not dark else '''
..kkkkk....
.kkkkkkk...
kkkkkkkkkkk
kkkkkkkkk..
.kkkkkkk...
..kkkkk....
''', 13, 17, mirror=True)


# ================================================================ 胡半仙: the gauze cap, dark round glasses, a thin moustache, a banner
@design('hubanxian', 'nowr')
def hubanxian(c):
    P = body(c, BODY, BODY, dots=None, robe=True, neck=(19, 28), finish=False)
    pole = c.new_part()
    c.rect(40, 0, 41, 55, WOOD, pole)
    flag = c.new_part()
    c.rect(33, 3, 39, 33, flat('w'), flag)
    c.finish()
    cross_collar(c, P['torso'], 'd', y0=39, slope=0.85, w=1.3)
    for y in (7, 13, 19, 25):
        put(c, 'rrrr\nr..r\nrrrr', 34, y)
    face(c, 'h', 'calm', mouth='flat')
    head(c, GAUZE)
    glasses(c, True)
    put(c, '''
kkkk..
....kk
.....k
.....k
''', 15, 29, mirror=True)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


# ================================================================ 賈八方: a round cap, a big grin, a pack frame behind, a coin string
@design('jiabafang', 'norwy')
def jiabafang(c):
    pack = c.new_part()
    c.rect(2, 20, 9, 55, Mat('n', 'n', 'o'), pack)
    c.rect(38, 20, 45, 55, Mat('n', 'n', 'o'), pack)
    P = body(c, BODY, BODY, dots=None, robe=True, neck=(19, 28), finish=False)
    c.finish()
    vchest(c, P['torso'], y0=39, slope=0.45)
    for (x, y) in [(14, 42), (17, 45), (20, 47), (24, 48), (28, 47), (31, 45), (34, 42)]:
        put(c, '.k.\nkyk\n.k.', x - 1, y - 1)
    head(c, CAP_ROUND)
    face(c, 'h', 'sly', mouth='grin')
    for y in (24, 32, 40):
        put(c, 'oooooooo', 2, y)
        put(c, 'oooooooo', 38, y)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


# ================================================================ 武大膽: a red head cloth, a great black beard, a sweat drop, bare arms
BEARD_FULL = '''
........kkkSSSSSSSSSSSSS
........khkSSSSSSSSSSSSS
........khhkSSSSSSSSSSSS
........khhhkSSSSSkkkkkk
........khhhhkkkkkhhhhhh
.........khhhhhhhhhhhhhh
.........khhhhhhhhhhhhhh
..........khhhhhhhhhhhhh
..........khhhhhhhhhhhhh
...........khhhhhhhhhhhh
............khhhhhhhhhhh
.............kkhhhhhhhhh
...............kkkkhhhhh
...................kkkkk
'''


@design('wudadan', 'now')
def wudadan(c):
    P = body(c, BODY, SKIN, dots=None, robe=False, neck=(18, 29), finish=False, wide=2)
    staff = c.new_part()
    c.rect(43, 2, 44, 55, Mat('n', 'n', 'o'), staff)
    c.finish()
    vchest(c, P['torso'], y0=39, slope=0.5, width=3)
    head(c, SCARF)
    face(c, 'h', 'shut', mouth='flat')
    head(c, BEARD_FULL, 26)
    put(c, '.w\nww\nww', 8, 18)
    put(c, 'w\nw', 38, 22)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=28)
    centre_fix(c)
    for y in range(32, 56):
        for x in range(48):
            if c.tone[y][x] == 's':
                c.tone[y][x] = 'S'
    return c


# ================================================================ 文對仗: a scholar's cap with ribbons, a pale robe, the great brush raised
@design('wenduizhang', 'now')
def wenduizhang(c):
    P = body(c, BODY, BODY, dots=None, robe=True, neck=(19, 28), finish=False)
    brush = c.new_part()
    c.tube([(37, 52), (40, 30), (43, 8)], 1.4, Mat('n', 'n', 'o'), brush)
    tip = c.new_part()
    c.ellipse(43.5, 6, 2.2, 3.8, flat('k'), tip)
    fist = c.new_part()
    c.ellipse(38.5, 44, 3.4, 3.0, HAND, fist)
    c.finish()
    cross_collar(c, P['torso'], 'w', y0=39, slope=0.85, w=1.3)
    sash(c, P['torso'], 53, 'd', 'd')
    head(c, SCHOLAR)
    face(c, 'h', 'calm', mouth='flat')
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


# ================================================================ 蘇小婉: a high bun with a jade pin, pale as moonlight, a teacup
@design('suxiaowan', 'wry')
def suxiaowan(c):
    P = body(c, BODY, BODY, dots=None, robe=True, neck=(20, 27), finish=False)
    cup = c.new_part()
    c.rect(32, 44, 39, 49, flat('w'), cup)
    hand = c.new_part()
    c.ellipse(35.5, 51, 4, 2.4, HAND, hand)
    c.finish()
    cross_collar(c, P['torso'], 'e', y0=39, slope=0.8, w=1.2)
    put(c, 'rrrrrr', 33, 46)
    head(c, BUN)
    face(c, 'h', 'calm', mouth='flat')
    put(c, '''
.kk.
k..k
''', 21, 29)
    put(c, 'rr', 14, 26, mirror=True)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


# ================================================================ 楚天闊: a ponytail and white headband, a teal robe, a sword over the shoulder
@design('chutiankuo', 'nowy')
def chutiankuo(c):
    tail = c.new_part()
    c.tube([(30, 2), (36, 6), (40, 14), (41, 24)], 2.2, flat('h'), tail)
    sword = c.new_part()
    c.tube([(6, 4), (10, 20), (13, 38)], 1.2, Mat('w', 'w', 'n'), sword)
    P = body(c, BODY, BODY, dots=None, robe=True, neck=(19, 28), finish=False)
    c.finish()
    cross_collar(c, P['torso'], 'e', y0=39, slope=0.85, w=1.3)
    put(c, 'yyy\nyoy\nyyy', 7, 5)
    head(c, PONY)
    face(c, 'h', 'glare', mouth='grin')
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


# ================================================================ 牛飽飽: bald and round, stuffed cheeks, a steamed bun at his mouth, an apron
@design('niubaobao', 'wo')
def niubaobao(c):
    P = body(c, BODY, BODY, dots=None, robe=True, neck=(16, 31), finish=False, wide=3)
    bun = c.new_part()
    c.ellipse(34, 34, 5.5, 4.6, Mat('w', 'w', 'o'), bun)
    hand = c.new_part()
    c.ellipse(34, 40, 4.4, 3, HAND, hand)
    c.finish()
    for y in range(42, 56):
        for x in range(13, 35):
            if c.part[y][x] == P['torso'] and c.tone[y][x] != 'k':
                c.tone[y][x] = 'e'
    head(c, BALD)
    face(c, 'S', 'shut', mouth='grin')
    put(c, 'kk\nkk', 23, 0)
    put(c, 'r..\nrr.', 10, 27, mirror=True)
    put(c, 'o.o\n.o.', 32, 32)
    shade_rows(c, {'S': 's'}, band=2, y0=5, y1=35)
    centre_fix(c)
    return c


# ================================================================ 莫記得: a greying bun, little round spectacles, a goatee, a medicine box
@design('mojide', 'nowy')
def mojide(c):
    box = c.new_part()
    c.rect(33, 14, 46, 40, Mat('n', 'n', 'o'), box)
    P = body(c, BODY, BODY, dots=None, robe=True, neck=(19, 28), finish=False)
    c.finish()
    put(c, 'yyyyyyyyyy\nyoooooooyy', 35, 20)
    put(c, 'yyyyyyyyyy\nyoooooooyy', 35, 30)
    cross_collar(c, P['torso'], 'e', y0=39, slope=0.85, w=1.3)
    head(c, BUN.replace('yy', 'gg'))
    face(c, 'h', 'sly', mouth='flat')
    glasses(c, False)
    put(c, '''
..kk..
..kk..
...k..
''', 21, 31)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


# ================================================================ 霍天下: a gold band with a red feather, a big grin, a red cape, bare chest
@design('huotianxia', 'rwy')
def huotianxia(c):
    P = body(c, SKIN, Mat('e', 'f', 'f'), dots=None, robe=False, neck=(18, 29), finish=False, wide=1,
             cape=Mat('e', 'f', 'f'))
    c.finish()
    vchest(c, P['torso'], y0=37, slope=1.2, width=4)
    head(c, HAIR.replace('eeeeeeeeeeeeeeee', 'yyyyyyyyyyyyyyyy').replace('ffffffffffffffff', 'yyyyyyyyyyyyyyyy'))
    face(c, 'h', 'glare', mouth='grin')
    put(c, FEATHER, 25, 0)
    put(c, '''
..k..k..
.k....k.
k..kk..k
''', 13, 46, mirror=True)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


# ================================================================ 墨無涯: long black hair with a grey streak, an ink robe edged in white, the bell staff
@design('mowuya', 'nowy')
def mowuya(c):
    staff = c.new_part()
    c.rect(41, 8, 42, 55, Mat('n', 'n', 'o'), staff)
    bell = c.new_part()
    c.poly([(37, 9), (46, 9), (47, 3), (36, 3)], Mat('y', 'y', 'o'), bell)
    P = body(c, BODY, BODY, dots=None, robe=True, neck=(19, 28), finish=False)
    c.finish()
    cross_collar(c, P['torso'], 'w', y0=39, slope=0.9, w=1.4)
    head(c, LONGHAIR)
    face(c, 'h', 'stern', mouth='frown')
    for y in range(16, 50):
        for x in (6, 7, 40, 41):
            if c.tone[y][x] in '.':
                pass
    put(c, 'kk\nyy\nkk', 40, 10)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


# ================================================================ 阿蠻: a horned silver Miao headdress, a wolf-fur shawl, bright eyes
@design('aman', 'nwy')
def aman(c):
    P = body(c, BODY, Mat('e', 'f', 'f'), dots=None, robe=False, neck=(20, 27), finish=False)
    c.finish()
    for y in range(38, 47):
        for x in range(48):
            if c.part[y][x] in (P['torso'], P.get('pa1'), P.get('pa2')) and c.tone[y][x] != 'k' and (x + y) % 3 == 0:
                c.tone[y][x] = 'f'
    for x in range(14, 34, 3):
        put(c, 'w\nn', x, 49)
    head(c, HORNS)
    face(c, 'h', 'sly', mouth='flat')
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


# ---------------------------------------------------------------- colours (slot -> NES)
COLOURS = {
    'hubanxian': dict(S=0x37, s=0x27, h=0x0C, a=0x10, b=0x00, d=0x0C, e=0x00, f=0x10, w=0x30, r=0x16, n=0x17, o=0x07),
    'jiabafang': dict(S=0x37, s=0x27, h=0x0C, a=0x27, b=0x17, d=0x07, e=0x16, f=0x06, y=0x28, n=0x18, o=0x08, r=0x16, w=0x30),
    'wudadan': dict(S=0x27, s=0x17, h=0x0F, a=0x16, b=0x06, d=0x07, e=0x16, f=0x06, n=0x17, o=0x07, w=0x30),
    'wenduizhang': dict(S=0x37, s=0x27, h=0x0C, a=0x31, b=0x21, d=0x11, e=0x00, f=0x10, w=0x30, n=0x17, o=0x07),
    'suxiaowan': dict(S=0x30, s=0x31, h=0x0C, a=0x3A, b=0x2A, d=0x1A, e=0x30, y=0x2A, w=0x30, r=0x15),
    'chutiankuo': dict(S=0x37, s=0x27, h=0x0C, a=0x2C, b=0x1C, d=0x0C, e=0x30, w=0x30, n=0x10, o=0x00, y=0x28),
    'niubaobao': dict(S=0x37, s=0x27, h=0x0F, a=0x27, b=0x17, d=0x07, e=0x30, w=0x30, o=0x10, r=0x26),
    'mojide': dict(S=0x37, s=0x27, h=0x00, g=0x10, a=0x2A, b=0x1A, d=0x0A, e=0x30, n=0x17, o=0x07, y=0x28, w=0x30),
    'huotianxia': dict(S=0x27, s=0x17, h=0x0C, e=0x16, f=0x06, y=0x28, r=0x16, w=0x30),
    'mowuya': dict(S=0x36, s=0x26, h=0x0C, g=0x10, a=0x13, b=0x03, d=0x0F, w=0x30, n=0x17, o=0x07, y=0x28),
    'aman': dict(S=0x27, s=0x17, h=0x0C, a=0x12, b=0x02, d=0x0C, e=0x10, f=0x00, w=0x30, n=0x10, y=0x28, r=0x16),
}
