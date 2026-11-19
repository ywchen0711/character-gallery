"""Stronger-kin variants: a palette swap of a base plus a detail or two, so the higher tiers feel like tougher
relatives (a scar, a spiked club, ice, a forehead jewel, glowing eyes) and not only recolours.

Each variant is registered as its own design ('wolf_scar' ...) built from the base design, then marked by hand.
"""
from mon_designs import DESIGNS, design


def variant(name, base):
    d = DESIGNS[base]

    def deco(fn):
        def build(c):
            d['fn'](c)
            fn(c)
            return c
        DESIGNS[name] = dict(fn=build, w=d['w'], h=d['h'], mirrored=d['mirrored'], open_slots=d['open_slots'])
        return fn
    return deco


@variant('wolf_scar', 'wolf')                 # 血狼: a scar across the eye, a longer fang
def _(c):
    c.put([(5, 11), (6, 12), (8, 14), (9, 15), (10, 16), (11, 17)], 'k')
    c.put([(6, 21), (6, 22)], 'w')


@variant('wolf_frost', 'wolf')                # 霜狼: frost on the ruff and the tail tip
def _(c):
    c.put([(16, 15), (21, 16), (25, 17), (43, 6), (42, 9), (12, 33), (16, 34), (20, 32)], 'w')


@variant('boar_iron', 'boar')                 # 鐵甲野豬: riveted plates on the flank
def _(c):
    for x in range(20, 40, 5):
        c.put([(x, y) for y in range(21, 33) if c.tone[y][x] not in '.k'], 'd')
        c.put([(x + 1, 23), (x + 1, 29)], 'w')


@variant('skeleton_black', 'skeleton')        # 黑骨: a cracked skull and burning eyes
def _(c):
    c.put([(26, 3), (27, 4), (27, 5), (28, 6), (29, 7)], 'k')
    c.put([(19, 10), (28, 10), (19, 11), (28, 11)], 'e')


@variant('lackey_spiked', 'lackey')           # 打手 / 血手: nails through the club, an eye patch
def _(c):
    c.put([(38, 9), (43, 12), (39, 15), (44, 7)], 'w')
    c.put([(28, 12), (29, 12), (30, 12), (28, 13), (29, 13), (30, 13), (31, 11), (32, 10), (17, 11), (16, 10)], 'k')


@variant('bronze_jewel', 'bronze')            # 金剛護法: a jewel on the brow
def _(c):
    c.put([(23, 5), (24, 5), (23, 6), (24, 6)], 'y')


@variant('monk_iron', 'roguemonk')            # 鐵頭僧: heavy earrings
def _(c):
    c.put2([(14, 17), (14, 18), (13, 18)], 'y')


@variant('dummy_iron', 'dummy')               # 鐵木人: iron spikes on the arms
def _(c):
    c.put2([(7, 8), (10, 10), (7, 31), (10, 31)], 'w')
    c.put2([(7, 9), (10, 11), (7, 32), (10, 32)], 'k')


@variant('drowned_ice', 'drowned')            # 寒潭鬼: ice in the hair and on the hem
def _(c):
    c.put([(16, 14), (31, 18), (17, 26), (30, 30), (13, 48), (34, 49), (22, 51)], 'w')


@variant('wisp_nether', 'wisp')               # 幽冥火: angry brows
def _(c):
    c.put2([(16, 28), (17, 29), (18, 29), (19, 30)], 'k')


@variant('archer_nether', 'archer')           # 幽冥弓手: glowing eyes
def _(c):
    c.put([(18, 14), (19, 14), (28, 14), (29, 14)], 'r')


@variant('daoist_black', 'sorcerer')          # 黑袍妖道: a skull rosary
def _(c):
    for x in range(15, 33, 3):
        c.put([(x, 40), (x + 1, 40)], 'w')


@variant('hornet_ghost', 'hornet')            # 鬼面胡蜂: a skull face on the thorax
def _(c):
    c.put2([(22, 21), (21, 22)], 'w')


@variant('jiangshi_bronze', 'littlejiangshi')  # 銅甲小殭屍: a second talisman on the chest
def _(c):
    c.stamp(28, 39, """
kkkk
kyrk
kyyk
kyrk
kkkk
""")
