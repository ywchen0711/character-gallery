"""Monster designs: more of the jianghu and the undead, 48x56, in the people-portrait idiom (see mon_h.py)."""
from mondraw import Mat, flat
from mon_designs import design
from mon_h import person, eyes, nose, HAND

# ================================================================ assassin 刺客 (straw hat, masked, reversed blade)
BLACK = Mat('a', 'b', 'd')


@design('assassin', 48, 56, mirrored=True)
def assassin(c):
    person(c, BLACK, pants=Mat('b', 'd', 'd'), arms='left')
    arm = c.new_part()
    c.capsule(34, 24, 37, 33, 3.3, BLACK, arm)
    blade = c.new_part()
    c.poly([(37, 34), (40, 34), (42.5, 47), (41, 47.5)], Mat('w', 'w', 'a'), blade)
    hand = c.new_part()
    c.ellipse(37.5, 34.5, 3.0, 2.8, HAND, hand)
    mask = c.new_part(sep=False)
    c.ellipse(24, 16.5, 8.6, 4.8, Mat('b', 'b', 'd'), mask, clip=lambda x, y: y >= 15)
    hat = c.new_part()
    c.poly2([(24, 0.5), (21, 1.5), (3, 10.5), (3.5, 12.5), (24, 12)], Mat('e', 'f', 'f'), hat)
    c.reshade(hat, 18, 4, 18, 9, Mat('e', 'f', 'f'), dw=1)
    c.finish()
    c.put2([(19, 4), (17, 6), (15, 8), (13, 9), (11, 10), (14, 5), (11, 7), (8, 9), (6, 10)], 'k')
    c.put2([(x, 13) for x in range(17, 22)], 'k')
    c.put2([(19, 14), (20, 14)], 'r')
    c.put2([(18, 14), (21, 14)], 'k')
    c.put([(x, y) for y in (34, 35) for x in range(13, 35)], 'e')
    c.put([(23, 33), (24, 33), (23, 36), (24, 36), (22, 34), (25, 35)], 'e')
    c.put2([(16, 26), (17, 27), (18, 28), (19, 29)], 'd')
    c.put([(x, 17) for x in range(20, 28)], 'd')
    return c


# ================================================================ rogue monk 野和尚 (beads, kasaya, ringed staff)
ROBEM = Mat('b', 'b', 'd')


@design('roguemonk', 48, 56, mirrored=True)
def roguemonk(c):
    person(c, ROBEM, pants=Mat('b', 'd', 'd'), arms='left', waist=42)
    arm = c.new_part()
    c.capsule(34, 24, 38, 31, 3.4, ROBEM, arm)
    staff = c.new_part()
    c.rect(39, 4, 40, 54, Mat('d', 'd', 'd'), staff, shade='flat')
    hand = c.new_part()
    c.ellipse(39, 31.5, 3.0, 2.8, HAND, hand)
    kas = c.new_part()
    c.poly([(15, 22), (19, 21.5), (35, 37), (35, 43), (30, 43), (14, 27)], Mat('e', 'e', 'd'), kas)
    c.finish()
    c.stamp(36, 0, """
..kkkk
.kyyyyk
kykkkkyk
kyk..kyk
kyk..kyk
kykkkkyk
.kyyyyk
..kkkk
""")
    c.put([(41, 9), (41, 10), (37, 9), (37, 10)], 'y')
    eyes(c, 13, 'bushy')
    nose(c, 15)
    c.stamp(20, 18, "kkkkkkkk")
    c.stamp(21, 17, "k......k")
    c.stamp(21, 19, ".wwwwww")
    c.stamp(21, 20, ".kkkkkk")
    for (x, y) in ((22, 5), (25, 5), (21, 7), (24, 7), (27, 7)):
        c.paint(x, y, 'k')
    c.put([(x, 22) for x in range(17, 31) if x % 2 == 0], 'k')
    c.put([(x, 23) for x in range(18, 30) if x % 2 == 1], 'k')
    c.put([(28, 27), (28, 28), (29, 27), (29, 28)], 'k')
    c.put([(21, 31), (24, 34), (27, 37)], 'd')
    return c


# ================================================================ sorcerer 妖道 (talisman raised, long beard)
ROBES = Mat('a', 'b', 'd')


@design('sorcerer', 48, 56, mirrored=True)
def sorcerer(c):
    person(c, ROBES, waist=42, arms='left')
    skirt = c.new_part()
    c.poly2([(24, 38), (13, 38), (10, 54), (24, 54)], ROBES, skirt)
    c.reshade(skirt, 20, 40, 14, 14, ROBES, dw=2, hi=2)
    arm = c.new_part()
    c.capsule(34, 24, 38, 13, 3.4, ROBES, arm)
    hand = c.new_part()
    c.ellipse(38.5, 11, 3.0, 2.8, HAND, hand)
    trim = c.new_part(sep=False)
    c.rect(22, 22, 25, 54, flat('e'), trim, shade='flat')
    beard = c.new_part()
    c.poly2([(24, 15), (17.5, 15), (18, 21), (21, 27), (24, 31)], Mat('e', 'e', 'f'), beard)
    hat = c.new_part()
    c.ellipse(24, 5, 6.5, 3.5, Mat('f', 'f', 'f'), hat)
    c.rect(19, 4, 28, 5, flat('f'), hat, shade='flat')
    c.finish()
    c.stamp(35, 0, """
kkkkkkk
kyyyyyk
kyrrryk
kyyryyk
kyrrryk
kyyryyk
kyrrryk
kyyyyyk
kkkkkkk
""")
    c.put([(23, 2), (24, 2)], 'y')
    eyes(c, 12, 'sly')
    nose(c, 14)
    c.stamp(21, 16, "kkkkkk")
    c.put([(21, 20), (23, 22), (22, 25), (26, 20), (25, 23), (24, 27)], 'f')
    c.put([(x, 40) for x in range(14, 34)], 'k')
    c.put([(x, 41) for x in range(14, 34)], 'y')
    c.put2([(15, 46), (16, 47), (14, 50)], 'd')
    return c


# ================================================================ bronze man 銅人 (a living temple statue)
METAL = Mat('a', 'b', 'd')


@design('bronze', 48, 56, mirrored=True)
def bronze(c):
    lg = c.new_part()
    c.capsule2(19, 38, 14, 51, 3.8, METAL, lg)
    c.ellipse2(13, 53, 5, 2.2, METAL, lg)
    shorts = c.new_part()
    c.poly2([(24, 34), (15, 34), (13, 43), (20.5, 44), (24, 40)], Mat('e', 'f', 'f'), shorts)
    arm = c.new_part()
    c.capsule2(13, 22, 6, 30, 3.8, METAL, arm)
    c.capsule2(6, 30, 9, 17, 3.4, METAL, arm)
    c.ellipse2(9.5, 14, 4, 3.6, METAL, arm)
    torso = c.new_part()
    c.poly2([(24, 18), (14, 18.5), (10, 22.5), (14.5, 35), (24, 35)], METAL, torso)
    c.reshade(torso, 20, 23, 12, 14, METAL, dw=2)
    head = c.new_part()
    c.ellipse(24, 10.5, 7, 8, METAL, head)
    c.reshade(head, 21, 8, 9, 9, METAL, dw=1)
    c.finish()
    c.put2([(18, 24), (19, 25), (20, 25), (21, 25), (22, 24)], 'd')
    c.put([(23, 23), (23, 24), (24, 23), (24, 24)], 'd')
    c.put2([(20, 28), (21, 28), (20, 31), (21, 31)], 'd')
    c.put([(23, 27), (23, 28), (23, 30), (23, 31), (24, 27), (24, 28), (24, 30), (24, 31)], 'd')
    c.put2([(16, 21), (17, 20)], 'a')
    c.stamp(19, 8, "kkk", mirror=True)
    c.stamp(19, 9, "krk", mirror=True)
    c.put([(23, 12), (24, 12)], 'd')
    c.stamp(21, 15, "dddddd")
    c.put2([(11, 13), (12, 12), (7, 25), (16, 44)], 'a')
    c.put2([(17, 37), (18, 37)], 'y')
    return c


# ================================================================ little jiangshi 小殭屍 (Qing hat, talisman)
ROBEJ = Mat('a', 'b', 'd')
SKINJ = flat('S')


@design('littlejiangshi', 48, 56, mirrored=True)
def littlejiangshi(c):
    lg = c.new_part()
    c.capsule2(21, 44, 21, 51, 2.8, Mat('d', 'd', 'd'), lg)
    c.ellipse2(20.5, 53, 4, 2.0, Mat('d', 'd', 'd'), lg)
    robe = c.new_part()
    c.poly2([(24, 21), (15, 21.5), (12.5, 46), (24, 46)], ROBEJ, robe)
    c.reshade(robe, 20, 28, 12, 18, ROBEJ, dw=2, hi=0.9)
    sleeve = c.new_part()
    c.capsule2(15, 24, 5, 25, 3.6, ROBEJ, sleeve)
    hand = c.new_part()
    c.poly2([(1.5, 24), (6, 24), (5.5, 31), (2, 31)], flat('H'), hand)
    badge = c.new_part()
    c.rect(18, 29, 29, 38, flat('y'), badge, shade='flat')
    head = c.new_part()
    c.ellipse(24, 14, 8.5, 7.5, SKINJ, head)
    c.reshade(head, 21, 12, 10, 9, SKINJ, dw=1, hi=2)
    brim = c.new_part()
    c.ellipse(24, 8, 14, 3.2, Mat('d', 'd', 'd'), brim)
    hat = c.new_part()
    c.ellipse(24, 5, 8.5, 4.5, Mat('b', 'd', 'd'), hat)
    c.finish()
    c.stamp(21, 9, """
kkkkkk
kyyyyk
kyrryk
kyyyyk
kyrryk
kyyyyk
kyrryk
kyyyyk
kkkkkk
""")
    c.stamp(23, 0, "kk")
    c.stamp(22, 1, "krrk")
    c.stamp(16, 13, "kkk", mirror=True)
    c.stamp(16, 14, "kek", mirror=True)
    c.stamp(16, 15, ".k.", mirror=True)
    c.stamp(20, 19, "kk", mirror=True)
    c.put([(19, 20), (28, 20)], 'y')
    c.stamp(20, 31, "dddddddd")
    c.stamp(20, 33, "dd....dd")
    c.stamp(20, 35, "dddddddd")
    c.stamp(1, 31, "k.k.k", mirror=True)
    c.put2([(16, 40), (17, 41), (18, 42)], 'd')
    return c


# ================================================================ skeleton 骷髏兵 (rusty sabre, red headband)
BONE = Mat('w', 'w', 'a')


@design('skeleton', 48, 56, mirrored=True)
def skeleton(c):
    lg = c.new_part()
    c.capsule2(20, 38, 19, 45, 1.6, BONE, lg)
    c.capsule2(19, 45, 18.5, 51, 1.5, BONE, lg)
    c.ellipse2(19, 45, 2.2, 1.9, BONE, lg)
    c.ellipse2(17.5, 53, 4, 1.9, BONE, lg)
    arm = c.new_part()
    c.capsule(15, 22, 11, 29, 1.5, BONE, arm)
    c.capsule(11, 29, 12, 36, 1.4, BONE, arm)
    c.ellipse(11, 29, 2.0, 1.8, BONE, arm)
    c.ellipse(12, 38, 2.6, 2.4, BONE, arm)
    c.capsule(33, 22, 37, 28, 1.5, BONE, arm)
    c.capsule(37, 28, 38, 21, 1.4, BONE, arm)
    blade = c.new_part()
    c.poly([(37, 19), (39.5, 2.5), (42.5, 1.5), (40, 19)], Mat('w', 'w', 'a'), blade)
    guard = c.new_part()
    c.rect(35, 19, 42, 20, flat('d'), guard, shade='flat')
    fist = c.new_part()
    c.ellipse(38.5, 21.5, 2.4, 2.2, BONE, fist)
    spine = c.new_part()
    c.rect(23, 19, 24, 35, BONE, spine, shade='flat')
    ribs = c.new_part()
    for y in (22, 25, 28):
        c.capsule2(24, y, 16.5, y + 1.8, 1.1, BONE, ribs)
    sh = c.new_part()
    c.capsule2(24, 20, 15, 21, 1.5, BONE, sh)
    pelvis = c.new_part()
    c.ellipse(24, 36, 6.5, 3, BONE, pelvis)
    cloth = c.new_part()
    c.poly2([(24, 35), (16.5, 35), (16, 42), (18.5, 40.5), (21, 43), (24, 41)], Mat('d', 'd', 'd'), cloth)
    skull = c.new_part()
    c.ellipse(24, 10, 8.5, 8, BONE, skull)
    c.rect(19, 15, 28, 18, BONE, skull)
    band = c.new_part(sep=False)
    c.rect(16, 5, 31, 6, flat('r'), band, shade='flat')
    c.finish()
    c.stamp(18, 9, "kkk", mirror=True)
    c.stamp(18, 10, "kek", mirror=True)
    c.stamp(18, 11, "kkk", mirror=True)
    c.stamp(23, 13, "kk")
    c.stamp(20, 16, "kwkwkwkw")
    c.stamp(20, 17, "kkkkkkkk")
    c.put([(15, 6), (14, 7), (15, 8)], 'r')
    c.put([(25, 3), (27, 4)], 'a')
    return c


# ================================================================ the drowned 水鬼 (long wet hair, one eye showing)
ROBE = Mat('w', 'a', 'a')
HAIR = Mat('b', 'b', 'd')


@design('drowned', 48, 56, mirrored=True)
def drowned(c):
    robe = c.new_part()
    c.poly2([(24, 18), (14, 21), (9, 46), (11, 54), (14.5, 50), (18, 54), (21.5, 50), (24, 54)], ROBE, robe)
    c.reshade(robe, 20, 28, 13, 22, ROBE, dw=0, hi=0.9)
    arms = c.new_part()
    c.capsule2(14, 23, 10, 34, 2.8, ROBE, arms)
    hands = c.new_part()
    c.capsule2(10, 35, 9.5, 40, 1.7, flat('a'), hands)
    hair = c.new_part()
    c.ellipse(24, 11, 10, 9, HAIR, hair)
    c.poly2([(24, 7), (14.5, 10), (12.5, 36), (16, 39), (18, 35), (21, 38), (24, 34)], HAIR, hair)
    face = c.new_part(sep=False)
    c.poly([(21.5, 10), (26.5, 10), (27, 24), (21, 24)], Mat('a', 'a', 'a'), face, shade='flat')
    c.finish()
    for x in (15, 18, 29, 32):
        for y in range(13, 34):
            if c.part[y][x] == hair and c.tone[y][x] in 'bd' and (y + x) % 4 != 0:
                c.paint(x, y, 'k')
    c.put([(24, 15), (25, 15)], 'k')
    c.put([(24, 16)], 'e')
    c.put([(25, 16)], 'k')
    c.put([(22, 21), (23, 21), (24, 21)], 'k')
    c.put([(23, 22)], 'k')
    c.put([(10, 44), (37, 46), (12, 41)], 'w')
    c.put2([(10, 41), (10, 42)], 'k')
    return c
