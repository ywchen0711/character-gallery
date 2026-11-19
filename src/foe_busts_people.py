"""Foe busts, part 1: the people and the undead (head-and-shoulders, like the 霸王之路 generals). See foe_busts.py."""
from foe_busts import *  # noqa: F401,F403

SKIN = Mat('S', 'S', 's', hi=2)
HAND = Mat('S', 'S', 's', hi=2)
WOOD = Mat('n', 'n', 'o')     # props on the sprite layer: n mid, o dark, w glint
BODY = Mat('a', 'b', 'd')
BODY2 = Mat('e', 'f', 'f')

# a face, left half, rows y=16..35 ('h' = hair at the temple, replaced per foe)
FACE = T('''
........kkhkSSSSSSSSSSSS
.........khkSSSSSSSSSSSS
.........khkSSSSSSSSSSSS
.........khkSSSSSSSSSSSS
........kSSkSSSSSSSSSSSS
........kSkkSSSSSSSSSSSS
........kSsSSSSSSSSSSSSS
........kSSkSSSSSSSSSSSS
.........kkkSSSSSSSSSSSS
..........kSSSSSSSSSSSSS
..........kSSSSSSSSSSSSS
...........kSSSSSSSSSSSS
...........kSSSSSSSSSSSS
...........kSSSSSSSSSSSS
............kSSSSSSSSSSS
............kSSSSSSSSSSS
.............kSSSSSSSSSS
..............kSSSSSSSSS
...............kkSSSSSSS
.................kkkkkkk
''')

# brows + eyes, left half (x from 12), rows from y=18
EYES = {
    'stern': T('''
.kkkk.......
...kkkkk....
............
...kkkkkk...
...kkwkk....
'''),
    'glare': T('''
kkk.........
.kkkkk......
....kkkk....
..kkkkkkk...
..kkwkkk....
'''),
    'calm': T('''
..kkkkkk....
............
............
..kkkkkk....
...kkkk.....
'''),
    'sly': T('''
..kk........
....kkkk....
............
..kkkkkkk...
....kkk.....
'''),
    'shut': T('''
.kkkk.......
...kkkkk....
............
............
..kkkkkkk...
'''),
}


def face(c, hair='k', eyes='stern', y0=16, nose=True, mouth='flat'):
    rows_ = [r.replace('h', hair) for r in FACE]
    head(c, '\n'.join(rows_), y0)
    put(c, '\n'.join(EYES[eyes]), 12, y0 + 2, mirror=True)
    if nose:
        put(c, '''
.ss.
kssk
''', 22, y0 + 8)
    M = {'flat': '''
.kkkkkk.
''', 'grin': '''
kkkkkkkk
.kwwwwk.
..kkkk..
''', 'frown': '''
..kkkk..
.k....k.
''', 'snarl': '''
kkkkkkkk
kwkwwkwk
.kkkkkk.
'''}[mouth]
    put(c, M, 20, y0 + 13)


def vchest(c, part, y0=38, slope=0.55, slot='S', line='k', width=1.5):
    """An open neckline: skin in a V under the chin, edged with a black line."""
    for y in range(y0, c.h):
        hw = width + (y - y0) * slope
        for x in range(c.w):
            if c.part[y][x] != part or c.tone[y][x] == 'k':
                continue
            u = abs(x + 0.5 - 24)
            if u < hw:
                c.tone[y][x] = slot
            elif u < hw + 1:
                c.tone[y][x] = line


def cross_collar(c, part, slot, y0=38, slope=0.9, w=1.6):
    """A crossed collar (right over left) as a band of `slot` on the robe."""
    for y in range(y0, c.h):
        for x in range(c.w):
            if c.part[y][x] == part and c.tone[y][x] != 'k':
                u = x - 23.5
                if (abs(u + (y - y0) * slope) < w and u < 3) or (abs(u - (y - y0) * slope) < w and u > -3):
                    c.tone[y][x] = slot


def sash(c, part, y, a, b):
    for x in range(c.w):
        if c.part[y][x] == part and c.tone[y][x] != 'k':
            c.tone[y][x] = a
        if y + 1 < c.h and c.part[y + 1][x] == part and c.tone[y + 1][x] != 'k':
            c.tone[y + 1][x] = b


def stubble(c, y0=26, y1=34):
    for y in range(y0, y1):
        for x in range(c.w):
            if c.tone[y][x] == 'S' and (x + y) % 3 == 0 and y % 2 == 0 and abs(x - 23.5) > 3.5:
                c.tone[y][x] = 's'


# ================================================================ 嘍囉 bandit lackey: headscarf, stubble, open vest, a club on the shoulder
SCARF = '''
........................
........................
........................
........................
........................
.................kkkkkkk
..............kkkeeeeeee
............kkeeeeeeeeee
..........kkeeeeeeeeeeee
.........keeeeeeeeeeeeee
........keeeeeeeeeeeeeee
........keeeeeeeeeeeeeee
.......keeeeeeeeeeeeeeee
.......keeeeeeeeeeeeeeee
.......kffffffffffffffff
.......kkkkkkkkkkkkkkkkk
'''


@bust('lackey')
def lackey(c):
    P = body(c, BODY, BODY, dots=None, robe=True, neck=(19, 28), finish=False)
    club = c.new_part()
    c.capsule(40.5, 46, 42.5, 6, 1.8, WOOD, club, r1=3.6)
    fist = c.new_part()
    c.ellipse(40, 45.5, 3.4, 3.0, HAND, fist)
    c.finish()
    vchest(c, P['torso'], y0=39, slope=0.4)
    sash(c, P['torso'], 52, 'f', 'f')
    head(c, SCARF)
    face(c, 'k', 'stern', mouth='flat')
    put(c, '''
..kkkkk..
.kfeeefk.
kfeeeeefk
kfeeeeefk
.kfffffk.
..kkfkkk.
.kfkkfk..
.kfk.kfk.
kfk..kfk.
kk....kk.
''', 3, 7)
    shade_rows(c, {'e': 'f'}, band=3, y0=5, y1=14)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


def lackey_spiked(c):
    lackey(c)
    # nails through the club, a patch over the left eye
    put(c, 'w\n\n\nw\n\n\nw', 44, 9)
    put(c, 'w\n\n\nw', 38, 12)
    put(c, '''
kkkkkkk
kkkkkkk
kkkkkk.
''', 27, 20)
    put(c, 'k', 34, 17)
    put(c, 'k', 35, 16)
    put(c, 'k', 26, 19)
    return c


BUSTS['lackey_spiked'] = dict(fn=lackey_spiked, mirrored=True, open_slots='')


# ================================================================ archer: leather headband over tied-back hair, keen eyes, a bow on his right, arrows over his shoulder
HAIR = '''
........................
........................
........................
........................
.................kkkkkkk
..............kkkkkkkkkk
............kkkkkkkkkkkk
..........kkkkkkkkkkkkkk
.........kkkkkkkkkkkkkkk
........kkkkkkkkkkkkkkkk
........kkkkkkkkkkkkkkkk
.......kkkkkkkkkkkkkkkkk
.......kkkkkkkkkkkkkkkkk
.......kkkkkkkkkkkkkkkkk
.......keeeeeeeeeeeeeeee
.......kffffffffffffffff
'''


@bust('archer', open_slots='w')
def archer(c):
    P = body(c, BODY, BODY, dots=None, robe=True, neck=(19, 28), finish=False)
    bow = c.new_part()
    c.tube([(9, 3), (4, 12), (2.5, 28), (4, 44), (9, 54)], 1.6, WOOD, bow)
    quiver = c.new_part()
    c.poly([(34, 30), (39, 28), (44, 41), (39, 43)], WOOD, quiver)
    c.finish()
    cross_collar(c, P['torso'], 'd', y0=39, slope=0.85, w=1.3)
    for y in range(38, 56):                     # the quiver strap across the chest
        x = int(34 - (y - 38) * 1.1)
        for xx in (x, x + 1):
            if 0 <= xx < 48 and c.part[y][xx] == P['torso']:
                c.tone[y][xx] = 'e'
    for y in range(4, 54):                      # the bowstring
        if c.tone[y][10] == '.':
            c.paint(10, y, 'w', part=bow)
    head(c, HAIR)
    face(c, 'k', 'sly', mouth='flat')
    put(c, '''
.w.w.w.
kwkwkwk
kwkwkwk
.knknk.
.knknk.
''', 35, 24)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    centre_fix(c)
    return c


def archer_nether(c):
    archer(c)
    put(c, 'rr', 16, 21)
    put(c, 'rr', 30, 21)
    return c


BUSTS['archer_nether'] = dict(fn=archer_nether, mirrored=True, open_slots='w')


# ================================================================ assassin: a wide bamboo hat, a black mask over the lower face, a dagger raised
HAT = '''
........................
.....................kkk
...................kkeee
.................kkeefee
...............kkeeefeee
.............kkeeeefeeee
...........kkeeeeefeeeee
.........kkeeeeeefeeeeee
.......kkeeeeeeefeeeeeee
.....kkeeeeeeeefeeeeeeee
...kkeeeeeeeeefeeeeeeeee
..keeeeeeeeeefeeeeeeeeee
.kffffffffffffffffffffff
..kkkkkkkkkkkkkkkkkkkkkk
........kkkkkkkkkkkkkkkk
........kkkkkkkkkkkkkkkk
'''

MASK = '''
.........kkkkkkkkkkkkkkk
..........kbbbbbbbbbbbbb
..........kbbbbbbbbbbbbb
...........kbbbbbbbbbbbb
...........kbbbbbbbbbbbb
...........kbbbbbbbbbbbb
............kbbbbbbbbbbb
............kbbbbbbbbbbb
.............kbbbbbbbbbb
..............kbbbbbbbbb
...............kkbbbbbbb
.................kkkkkkk
'''


@bust('assassin')
def assassin(c):
    P = body(c, BODY, BODY, dots=None, robe=True, neck=(19, 28), finish=False)
    blade = c.new_part()
    c.poly([(38, 44), (40, 22), (42, 18), (43, 22), (42, 44)], Mat('w', 'w', 'o'), blade)
    grip = c.new_part()
    c.rect(37, 44, 43, 45, flat('o'), grip)
    fist = c.new_part()
    c.ellipse(40, 48.5, 3.6, 3.2, HAND, fist)
    c.finish()
    cross_collar(c, P['torso'], 'd', y0=39, slope=0.85, w=1.3)
    sash(c, P['torso'], 53, 'd', 'd')
    face(c, 'k', 'glare', mouth='flat', nose=False)
    head(c, MASK, 24)
    head(c, HAT)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=24)
    shade_rows(c, {'b': 'd'}, band=2, y0=24, y1=36)
    centre_fix(c)
    return c


# ================================================================ rogue monk: shaved head, heavy brows, big prayer beads, a red kasaya, a ringed staff
BALD = '''
........................
........................
........................
........................
........................
................kkkkkkkk
.............kkkSSSSSSSS
...........kkSSSSSSSSSSS
.........kkSSSSSSSSSSSSS
........kSSSSSSSSSSSSSSS
........kSSSSSSSSSSSSSSS
.......kSSSSSSSSSSSSSSSS
.......kSSSSSSSSSSSSSSSS
.......kSSSSSSSSSSSSSSSS
.......kSSSSSSSSSSSSSSSS
........kSSSSSSSSSSSSSSS
'''


@bust('roguemonk')
def roguemonk(c):
    P = body(c, BODY, BODY, dots=None, robe=True, neck=(19, 28), finish=False)
    staff = c.new_part()
    c.rect(41, 6, 42, 55, Mat('n', 'n', 'o'), staff)
    c.finish()
    cross_collar(c, P['torso'], 'd', y0=39, slope=0.85, w=1.3)
    for y in range(38, 56):                     # the kasaya over the left shoulder
        for x in range(48):
            if c.part[y][x] == P['torso'] and c.tone[y][x] != 'k':
                u = x - (2 + (y - 38) * 0.75)
                if 0 <= u < 6:
                    c.tone[y][x] = 'e' if 0 < u < 5 else 'k'
    head(c, BALD)
    face(c, 'S', 'glare', mouth='frown')
    for (x, y) in [(12, 40), (15, 43), (18, 45), (21, 46), (24, 46), (27, 45), (30, 43), (33, 40)]:
        put(c, '''
.kk.
kyyk
kyyk
.kk.
''', x - 2, y - 2)
    put(c, '''
.kkkk.
kyyyyk
kykkyk
kyyyyk
.kyyk.
..kk..
''', 39, 1)
    shade_rows(c, {'S': 's'}, band=2, y0=5, y1=35)
    put(c, 'w\nw', 18, 8)
    centre_fix(c)
    return c


def monk_iron(c):
    roguemonk(c)
    put(c, '''
kkk
kyk
kyk
kkk
''', 6, 21, mirror=True)
    return c


BUSTS['monk_iron'] = dict(fn=monk_iron, mirrored=True, open_slots='')


# ================================================================ daoist: a small gold crown on a white topknot, a long white beard, a blue robe, a talisman raised
SAGE = '''
........................
....................kkkk
...................kyyyy
..................kkyyyy
..................keeeee
.................keeeeee
..............kkkkeeeeee
............kkeeeeeeeeee
..........kkeeeeeeeeeeee
.........keeeeeeeeeeeeee
........keeeeeeeeeeeeeee
........keeeeeeeeeeeeeee
.......keeeeeeeeeeeeeeee
.......keeeeeeeeeeeeeeee
.......keeeeeeeeeeeeeeee
.......keeeeeekkkkkkkkkk
'''

BEARD = '''
..........keSSSSSSSSSSSS
...........keSSSSSSSSSSS
...........keeSSSSSSkkkk
...........keeeSSSkkeeee
............keeeekeeeeee
............keeeeeeeeeee
.............keeeeeeeeee
..............keeeeeeeee
...............keeeeeeee
................keeeeeee
.................keeeeee
..................keeeee
...................keeee
....................keee
.....................kke
.......................k
'''

TALISMAN = '''
.kkkkk.
.kyyyk.
.kyryk.
.kyyyk.
.kyrrk.
.kyyyk.
.kyryk.
.kyyyk.
.kyrrk.
.kyyyk.
kSSSSSk
kSSSSSk
kSSSSSk
.kSSSk.
'''


@bust('sorcerer')
def sorcerer(c):
    P = body(c, BODY, BODY, dots=None, robe=True, neck=(19, 28), finish=True)
    cross_collar(c, P['torso'], 'e', y0=39, slope=0.85, w=1.3)
    sash(c, P['torso'], 53, 'd', 'd')
    head(c, SAGE)
    face(c, 'e', 'calm', mouth='flat')
    head(c, BEARD, 26)
    put(c, TALISMAN, 37, 27)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=30)
    centre_fix(c)
    return c


def daoist_black(c):
    sorcerer(c)
    for x in range(13, 35, 4):
        put(c, '''
kk
ww
kk
''', x, 44)
    return c


BUSTS['daoist_black'] = dict(fn=daoist_black, mirrored=True, open_slots='')


# ================================================================ bronze man: a bald bronze head, glowing eyes, a broad bare chest
@bust('bronze')
def bronze(c):
    BR = Mat('a', 'b', 'd', hi=0.8, lo=0.3)
    chest = c.new_part()
    c.poly2([(24, 36), (12, 37), (3, 41), (0, 46), (0, 56), (24, 56)], BR, chest)
    c.reshade(chest, 14, 44, 18, 14, BR, dw=2, hi=0.85)
    sh = c.new_part()
    c.ellipse2(6, 46, 8, 7, BR, sh)
    neck = c.new_part()
    c.rect(18, 28, 29, 38, BR, neck)
    hd = c.new_part()
    c.ellipse(24, 19, 13, 16, BR, hd)
    c.reshade(hd, 19, 13, 16, 16, BR, dw=2, hi=0.8)
    ears = c.new_part()
    c.ellipse2(10.5, 21, 2.2, 3.4, BR, ears)
    c.finish()
    put(c, '''
..kkkkk
.k.....
k......
''', 12, 45, mirror=True)
    put(c, 'k\nk\nk\nk\nk\nk', 23, 47, mirror=True)
    sash(c, chest, 54, 'e', 'f')
    put(c, '''
.kkkkk.......
...kkkkkk....
.............
...kkkkkk....
...kyyyk.....
....kkk......
''', 12, 16, mirror=True)
    put(c, '''
.dd.
kddk
''', 22, 24)
    put(c, '''
kkkkkkkk
.k....k.
''', 20, 29)
    return c


def bronze_jewel(c):
    bronze(c)
    put(c, '''
.kk.
kyyk
kyyk
.kk.
''', 22, 9)
    return c


BUSTS['bronze_jewel'] = dict(fn=bronze_jewel, mirrored=True, open_slots='')


# ================================================================ little jiangshi: a Qing official cap with a red bead, a talisman over the face, green skin, fangs, arms held out
CAP = '''
........................
....................kkkk
...................kraar
...................kaaaa
..................kkkkkk
..............kkkkaaaaaa
............kkaaaaaaaaaa
..........kkaaaaaaaaaaaa
.........kaaaaaaaaaaaaaa
........kaaaaaaaaaaaaaaa
.......kaaaaaaaaaaaaaaaa
......kkkkkkkkkkkkkkkkkk
.....kbbbbbbbbbbbbbbbbbb
.....kdddddddddddddddddd
......kkkkkkkkkkkkkkkkkk
........kkkkkkkkkkkkkkkk
'''

PAPER = '''
kkkkkkkk
kyyyyyyk
kyrrrryk
kyyryyyk
kyrrrryk
kyyryyyk
kyrryryk
kyyyyyyk
kyrrrryk
kyyyyyyk
.kyyyyk.
..kkkk..
'''


@bust('littlejiangshi')
def littlejiangshi(c):
    P = body(c, BODY, BODY, dots=None, robe=True, neck=(19, 28), finish=False)
    arms = c.new_part()
    c.capsule2(9, 44, 13, 50, 4.2, BODY, arms)
    hands = c.new_part()
    c.ellipse2(15.5, 53.5, 3.4, 2.8, flat('S'), hands)
    c.finish()
    cross_collar(c, P['torso'], 'd', y0=39, slope=0.85, w=1.3)
    head(c, CAP)
    face(c, 'k', 'shut', mouth='flat', nose=False)
    put(c, '''
kwk.....kwk
.k.......k.
''', 18, 30)
    put(c, '''
kkkkkkkkkk
''', 19, 29)
    put(c, PAPER, 20, 13)
    put(c, 'dd\nd.', 13, 23, mirror=True)
    shade_rows(c, {'S': 's'}, band=2, y0=16, y1=35)
    shade_rows(c, {'a': 'b'}, band=2, y0=5, y1=12)
    centre_fix(c, x0=0, x1=48)
    for y in range(48, 56):
        for x in range(48):
            if c.tone[y][x] in 'as':
                c.tone[y][x] = 'b' if c.tone[y][x] == 'a' else 'S'
    return c


def jiangshi_bronze(c):
    littlejiangshi(c)
    put(c, '''
kkkkk
kyryk
kyyyk
kyryk
kyyyk
kkkkk
''', 30, 40)
    return c


BUSTS['jiangshi_bronze'] = dict(fn=jiangshi_bronze, mirrored=True, open_slots='')


# ================================================================ skeleton: a grinning skull under a red headband, collarbones and ribs, a rusty sword raised
SKULL = '''
........................
........................
................kkkkkkkk
.............kkkwwwwwwww
...........kkwwwwwwwwwww
..........kwwwwwwwwwwwww
.........kwwwwwwwwwwwwww
........kwwwwwwwwwwwwwww
........kwwwwwwwwwwwwwww
.......kwwwwwwwwwwwwwwww
.......krrrrrrrrrrrrrrrr
.......krrrrrrrrrrrrrrrr
.......kwwwwwwwwwwwwwwww
.......kwwwwwwwwwwwwwwww
.......kwwwkkkkkkwwwwwww
.......kwwkkkkkkkkwwwwww
.......kwwkkkkkkkkkwwwww
.......kwwkkkkkkkkkwwwww
........kwwkkkkkkkkwwwww
........kwwwkkkkkkwwwwww
.........kwwwwwwwwwwwkww
.........kwwwwwwwwwwkkkw
..........kwwwwwwwwwkkkw
..........kwwwwwwwwwwwww
...........kkkkkkkkkkkkk
...........kwkwkwkwkwkwk
...........kwkwkwkwkwkwk
...........kkkkkkkkkkkkk
............kwkwkwkwkwkw
............kkkkkkkkkkkk
..............kkkkkkkkkk
'''

BONES = '''
........................
........................
.................kkkkkkk
.................kaaaaaa
.................kaaaaaa
.................kkkkkkk
...kkkkkkkkkkkk..kaaaaaa
.kkwwwwwwwwwwwwkkkaaaaaa
kwwwwwwwwwwwwwwwwkkkkkkk
kkkkkkkkkkkkkkkkkkaaaaaa
.........kkkkkkk.kaaaaaa
........kwwwwwwwkkkkkkkk
........kkkkkkkkk.kaaaak
.......kwwwwwwwwwkkkkkkk
.......kkkkkkkkkkk.kaak.
......kwwwwwwwwwwwkkkkk.
......kkkkkkkkkkkkk.....
.....kwwwwwwwwwwwwk.....
.....kkkkkkkkkkkkkk.....
'''


@bust('skeleton')
def skeleton(c):
    blade = c.new_part()
    c.poly([(39, 50), (39, 12), (41, 7), (43, 12), (43, 50)], Mat('w', 'w', 'o'), blade)
    guard = c.new_part()
    c.rect(36, 49, 45, 50, flat('n'), guard)
    grip = c.new_part()
    c.rect(40, 51, 42, 55, flat('o'), grip)
    c.finish()
    head(c, BONES, 37)
    head(c, SKULL, 1)
    put(c, '''
..kk
.krrk
krrkrk
krkkrk
.k..kk
''', 2, 9)
    shade_rows(c, {'w': 'a'}, band=2, y0=2, y1=36)
    return c


def skeleton_black(c):
    skeleton(c)
    put(c, 'k\n.k\n.k\n..k\n...k', 27, 3)
    put(c, '''
....
.ee.
.ee.
''', 13, 14, mirror=True)
    return c


BUSTS['skeleton_black'] = dict(fn=skeleton_black, mirrored=True, open_slots='')


# ================================================================ drowned: long wet hair hiding most of a pale face, one eye showing, a white burial robe
WET = '''
........................
........................
.................kkkkkkk
..............kkkbbbbbbb
............kkbbbbbbbbbb
..........kkbbbbbbbbbbbb
.........kbbbbbbbbbbbbbb
........kbbbbbbbbbbbbbbb
.......kbbbbbbbbbbbbbbbb
.......kbbbbbbbbbbbbbbbb
......kbbbbbbbbbbbbbbbbb
......kbbbbbbbbbbbbbbbkk
......kbbbbbbbbbbbbbbkww
.....kbbbbbbbbbbbbbbkwww
.....kbbbbbbbbbbbbbbkwww
.....kbbbbbbbbbbbbbkwwww
.....kbbbbbbbbbbbbbkwwww
.....kbbbbbbbbbbbbbkwwww
.....kbbbbbbbbbbbbbkwwww
.....kbbbbbbbbbbbbbkwwww
....kbbbbbbbbbbbbbbkwwww
....kbbbbbbbbbbbbbbkwwww
....kbbbbbbbbbbbbbbbkwww
....kbbbbbbbbbbbbbbbkwww
....kbbbbbbbbbbbbbbbbkww
....kbbbbbbbbbbbbbbbbkww
...kbbbbbbbbbbbbbbbbbbkk
...kbbbbbbbbbbbbbbbbbbbb
...kbbbbbbbbbbbbbbbbbbbb
...kbbbbbbbbbbbbbbbbbbbb
...kbbbbbbbbbbbbbbbbbbbb
..kbbbbbbbbbbbbbbbbbbbbb
..kbbbbbbbbbbbbbbbbbbbbb
..kbbbbbbbbbbbbbbbbbbbbb
..kbbbbbbbbbbbbbbbbbbbbb
...kkkkkkkkkkkkkkkkkkkkk
'''


@bust('drowned', mirrored=False)
def drowned(c):
    P = body(c, Mat('w', 'a', 'a'), Mat('w', 'a', 'a'), dots=None, robe=True, neck=(19, 28), finish=True, neck_slot='a')
    cross_collar(c, P['torso'], 'a', y0=39, slope=0.85, w=1.3)
    head(c, WET, 2)
    # wet strands: darker lines down the hair
    for x in (9, 13, 17, 30, 34, 38):
        for y in range(8, 40):
            if c.tone[y][x] == 'b' and (y + x) % 7 < 5:
                c.tone[y][x] = 'd'
    # the part shows one eye (her left), a dark mouth
    put(c, '''
kkkk
keek
.kk.
''', 25, 20)
    put(c, '''
.kk.
kkkk
.kk.
''', 22, 29)
    for y in range(40, 56):                  # hair falling over the robe
        for x in list(range(4, 13)) + list(range(35, 44)):
            if c.part[y][x] >= 0 and c.tone[y][x] != 'k' and y < 40 + (6 - abs(x - 8 if x < 24 else x - 39)) * 2:
                c.tone[y][x] = 'b' if (x % 4) else 'd'
    return c


def drowned_ice(c):
    drowned(c)
    put(c, 'w', 10, 14)
    put(c, 'w', 36, 18)
    put(c, 'w', 15, 27)
    put(c, 'w', 33, 31)
    put(c, 'w', 8, 36)
    return c


BUSTS['drowned_ice'] = dict(fn=drowned_ice, mirrored=False, open_slots='')
