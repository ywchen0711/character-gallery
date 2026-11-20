"""Foe busts for Longmen Quest II: the Bell of Ten Thousand Beasts itself (see foe_busts.py)."""
from foe_busts import *  # noqa: F401,F403


@bust('greatbell', open_slots='erw')
def greatbell(c):
    BR = Mat('a', 'b', 'd', hi=0.8, lo=0.3)
    loop = c.new_part()
    c.ellipse2(20.5, 6, 3, 3.5, BR, loop)
    top = c.new_part()
    c.rect(14, 9, 33, 12, BR, top)
    bell = c.new_part()
    c.poly2([(24, 11), (14, 13), (11, 21), (10, 34), (7, 44), (3, 49), (24, 49)], BR, bell)
    c.reshade(bell, 17, 24, 16, 24, BR, dw=2, hi=0.85)
    rim = c.new_part()
    c.rect(2, 48, 45, 52, BR, rim)
    c.finish()
    for y in (22, 23, 41, 42):
        for x in range(48):
            if c.part[y][x] == bell and c.tone[y][x] != 'k':
                c.tone[y][x] = 'd'
    put(c, '''
.kkk.
keeek
keewk
keeek
.kkk.
''', 13, 28)
    put(c, '''
.kkk.
krrrk
krwrk
krrrk
.kkk.
''', 21, 26)
    put(c, '''
.kkk.
kwwwk
kwwwk
kwwwk
.kkk.
''', 29, 28)
    put(c, 'kkkkk', 10, 36, mirror=True)
    for x in range(6, 42, 4):
        put(c, 'y', x, 50)
    return c
