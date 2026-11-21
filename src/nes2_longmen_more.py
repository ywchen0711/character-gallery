"""nes2 portraits, part 2: 奕碩, 柳寒煙, 白先生, 苦禪, 冷笑天 (see nes2_longmen.py)."""
from nes2_longmen import *  # noqa: F401,F403
from nes2_longmen import bust, robe, neck, collar, robe_folds, face, skin_shade, backdrop_sky, EYES  # noqa: F401


# ================================================================ 奕碩 Yi Shuo
# the little brother: spiky hair over a red headband with long flying ties, an orange jacket with a dark-red
# collar, a black sash, a mole on his cheek, his football under his arm
YISHUO_HAIR = """
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
......kkkkkkkkkkkkkkkkkk
......kmmmmmmmmmmmmmmmmm
......knnnnnnnnnnnnnnnnn
......kkkkkkkkkkkkkkkkkk
........kiikkkiiikkkiiik
"""


@bust('yishuo', dict(S=0x37, s=0x27, t=0x35, h=0x1C, i=0x0C, a=0x27, b=0x17, d=0x07, m=0x16, n=0x06,
                     w=0x30, v=0x10, z=0x0C),
      near={'h': 'i', 't': 'S', 'v': 'w'}, backdrop=backdrop_sky(solid_to=6, check_to=26, fade=10))
def yishuo(c):
    neck(c, 20, 27, 30, 42)
    body = robe(c, Mat('a', 'b', 'd'), top=40, wide=1)
    ball = c.new_part()
    c.ellipse(7.5, 49.5, 6.6, 6.6, Mat('w', 'w', 'v'), ball)
    c.finish()
    # the ball's black patches
    put(c, """
...kkk...
..kkkkk..
...kkk...
.........
k.......k
kk.....kk
k...k...k
...kkk...
""", 3, 45)
    collar(c, body, top=40, band='mn', inner='S', inner2='S', slope=0.9)
    robe_folds(c, body)
    for x in range(14, 48):              # the black sash
        for y in (54, 55):
            if c.part[y][x] == body and c.tone[y][x] != 'k':
                c.tone[y][x] = 'k' if y == 54 else 'd'
    half(c, YISHUO_HAIR)
    face(c, 'i', 'bright', mouth='flat')
    put(c, ['k......k', '.kkkkkk.'], 20, 30)
    put(c, """
....kiik.kiik.kiik
.....kk...kk...kk.
""", 6, 16)
    put(c, """
....kiik.kiik.kiik
.....kk...kk...kk.
""", 24, 16)
    put(c, 'tt', 14, 27)
    put(c, 'tt', 32, 27)
    put(c, 'k', 31, 29)                   # the mole
    # headband ties streaming out to our right
    put(c, """
kkkk.......
mmmmkkk....
nnnmmmmkkk.
knnnnnnmmmk
.kkkkknnnnk
......kkkk.
""", 36, 11)
    skin_shade(c)
    shade_right(c, {'i': 'k', 'h': 'i', 'm': 'n'}, band=2, x0=24, y0=0, y1=16)
    return c


# ================================================================ 柳寒煙 Liu Hanyan
# Mistress of the Cold River Pavilion: a high bun with a jade pin, long hair down past her shoulders, white over
# pale blue, a slim sword; a cold moon behind her
LIU_HAIR = """
....................kkkk
..................kkiiii
.................kiihiii
.................kihiiii
.................kiiiiii
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


@bust('liuhanyan', dict(S=0x37, s=0x27, h=0x1C, i=0x0C, a=0x30, b=0x31, d=0x21, e=0x30, f=0x10, g=0x2A, G=0x1A,
                        r=0x26, v=0x10, w=0x30, z=0x0C, Z=0x31),
      spr='r', near={'h': 'i', 'G': 'g', 'f': 'b', 'Z': 'b'},
      backdrop=backdrop_sky(solid_to=4, check_to=24, fade=10, moon=(39.5, 9.5, 6.5)))
def liuhanyan(c):
    hair_back = c.new_part()
    c.poly2([(14, 10), (8, 14), (5, 22), (4, 36), (3, 48), (2, 56), (15, 56), (16, 46), (14, 36), (12, 26), (12, 16)],
            Mat('h', 'i', 'i'), hair_back)
    sword = c.new_part()
    c.capsule(43.5, 56, 43.5, 30, 1.0, Mat('w', 'v', 'v'), sword)
    neck(c, 20, 27, 30, 42)
    body = robe(c, Mat('a', 'b', 'd'), top=40)
    hair_front = c.new_part()
    c.poly2([(12, 26), (9, 34), (8, 44), (10, 53), (14, 45), (15, 36)], Mat('h', 'i', 'i'), hair_front)
    hilt = c.new_part()
    c.rect(42, 24, 45, 29, Mat('g', 'g', 'G'), hilt)
    c.finish()
    collar(c, body, top=40, band='ebb', inner='S', inner2='e', slope=0.8)
    # strands in the long hair
    for x0 in (6, 9, 39, 42):
        for y in range(20, 54, 1):
            x = x0 + (y - 20) // 12 * (-1 if x0 < 24 else 1)
            if c.tone[y][x] == 'i' and (y // 3) % 3 != 0:
                c.tone[y][x] = 'k' if (x0 in (9, 39)) else 'h'
    half(c, LIU_HAIR)
    face(c, 'i', 'cool', mouth='firm')
    put(c, '.rrrr.', 21, 30)
    # lashes, a little longer at the outer corner
    put(c, 'k', 14, 22, mirror=True)
    # the jade pin through the bun, a tassel hanging on our right
    put(c, """
...........kk
.........kkgGk
.......kkggkk.
.....kkggkk...
...kkggkk.....
.kkggkk.......
kggkk.........
kkk...........
""", 15, 0)
    put(c, ['k', 'r', 'r', 'k'], 31, 6)
    skin_shade(c)
    shade_right(c, {'i': 'k', 'h': 'i'}, band=2, x0=24, y0=0, y1=16)
    return c


# ================================================================ 白先生 Mr Bai
# the storyteller: a square scholar's cap, thin moustache and goatee, grey robe, the clapper block in his hand
BAI_HAIR = """
................kkkkkkkk
...........kkkkkiiiiiiii
..........kiiiiikiiiiiii
..........khhhhhkiiiiiii
..........khiiiikiiiiiii
..........khiiiikiiiiiii
..........khiiiikiiiiiii
..........khiiiikiiiiiii
..........khiiiikiiiiiii
.........kkhiiiikiiiiiii
.........khhiiiikiiiiiii
.........kkkkkkkkkkkkkkk
.........kiiiiiiiiiiiiii
.........kkkkkkkkkkkkkkk
.........kvkSSSSSSSSSSSS
.........kvkSSSSSSSSSSSS
"""


@bust('baixian', dict(S=0x37, s=0x27, h=0x10, i=0x00, a=0x10, b=0x00, d=0x2D, e=0x30, f=0x10, p=0x17, q=0x07,
                      v=0x10, z=0x08),
      near={'p': 'q', 'e': 'f'}, backdrop=backdrop_sky(solid_to=6, check_to=26, fade=10))
def baixian(c):
    neck(c, 20, 27, 30, 42)
    body = robe(c, Mat('a', 'b', 'd'), top=40)
    hand = c.new_part()
    c.ellipse(39.5, 49.5, 4.2, 3.6, Mat('S', 'S', 's'), hand)
    block = c.new_part()
    c.rect(35, 43, 44, 46, Mat('p', 'p', 'q'), block)
    c.finish()
    collar(c, body, top=40, band='eaa', inner='S', inner2='e', slope=0.8)
    robe_folds(c, body)
    half(c, BAI_HAIR)
    face(c, 'v', 'shut', mouth='flat', top=None)
    # moustache and goatee
    put(c, """
..kkkkkkkk..
.kk......kk.
k..........k
""", 18, 29)
    put(c, """
kvvk
kvvk
kvvk
.kk.
""", 22, 31)
    skin_shade(c)
    shade_right(c, {'i': 'k', 'h': 'i'}, band=2, x0=24, y0=0, y1=14)
    return c


# ================================================================ 苦禪 Kuchan
# abbot of the Thousand Buddhas: bald, long white brows and beard, saffron robe, red kasaya with gold seams,
# prayer beads, a ringed staff; a golden halo behind him
KUCHAN_HEAD = """
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


@bust('kuchan', dict(S=0x37, s=0x27, a=0x38, b=0x27, d=0x17, m=0x16, n=0x06, g=0x28, w=0x30, v=0x10, p=0x07,
                     q=0x17, y=0x28, z=0x07, Z=0x08),
      near={'g': 'a', 'y': 'a', 'v': 'w', 'p': 'n'},
      backdrop=backdrop_sky(solid_to=0, check_to=0, fade=0, moon=(24, 22, 23)))
def kuchan(c):
    staff = c.new_part()
    c.capsule(4.5, 56, 4.5, 12, 1.1, Mat('y', 'y', 'p'), staff)
    ring = c.new_part()
    c.ellipse(4.5, 7.5, 3.6, 4.6, Mat('y', 'y', 'y'), ring)
    neck(c, 20, 27, 30, 42)
    body = robe(c, Mat('a', 'b', 'd'), top=40)
    kasaya = c.new_part()
    c.poly([(28, 40), (36, 41), (44, 45), (48, 50), (48, 56), (14, 56)], Mat('m', 'm', 'n'), kasaya)
    beard = c.new_part()
    c.poly2([(24, 30), (16, 30), (15, 36), (18, 44), (21, 49), (24, 51)], Mat('w', 'w', 'v'), beard)
    c.finish()
    put(c, ['kk', 'kk'], 4, 7)
    put(c, ['.kk.', 'kkkk', '.kk.'], 3, 6)
    # gold seams on the kasaya (a patchwork grid)
    for (x, y) in c.cells(kasaya):
        if c.tone[y][x] in 'mn' and ((x + (56 - y)) % 7 == 0 or y in (47, 53)):
            c.tone[y][x] = 'g'
    # prayer beads across the robe
    for i, (x, y) in enumerate([(13, 44), (15, 45), (17, 46), (34, 46), (36, 45), (38, 44)]):
        put(c, ['kpk', 'pqp', 'kpk'][0:3] if False else ['pq', 'qp'], x, y)
    half(c, KUCHAN_HEAD)
    face(c, 'S', 'shut', mouth='flat', nose=True)
    # long white brows drooping past the eyes
    put(c, """
...........kkkkkk.......
..........kwwwwwwk......
.........kwwvvvk........
.........kwvk...........
..........kk............
""", 0, 18, mirror=True)
    # moustache over the beard
    put(c, """
...kkkkkk...
..kwwwwwwk..
.kwwvvvvwwk.
kwvk....kvwk
""", 18, 28)
    skin_shade(c)
    shade_right(c, {'S': 's'}, band=2, x0=30, y0=2, y1=16)
    return c


# ================================================================ 冷笑天 Leng Xiaotian
# the Tyrant Dragon: swept silver hair, gold dragon horns, black robe with gold trim and dots, a crimson cape
# with a high collar; red eyes
XT_HAIR = """
........................
........................
...............kkkkkkkkk
............kkkhhhhhhhhh
..........kkhhhhhhhhhhhh
.........khHHhhhiihhhhhh
........khHhhhiihhhhHHhh
.......khHhhiihhhhHHhhhh
......khHhhihhhhHHhhhhhh
......khHhihhhhHhhhhhhhh
.....khhhihhhhHhhhhhhhhh
.....khhhhhhhhhhhhhhhhhh
.....khhhhkkkkkkkkkkkkkk
.....khhhkygyyyyyyyyyyyy
....khhhhkkkkkkkkkkkkkkk
....khhhhkhhhkSSSSSSSSSS
"""


@bust('xiaotian', dict(S=0x37, s=0x27, h=0x10, H=0x30, i=0x00, j=0x00, a=0x00, b=0x0F, d=0x0F, g=0x28, y=0x28, Y=0x38,
                       m=0x16, n=0x06, r=0x16, z=0x00),
      spr='yYr', near={'Y': 'y', 'H': 'h'}, backdrop=backdrop_sky(solid_to=6, check_to=26, fade=10))
def xiaotian(c):
    cape = c.new_part()
    c.poly2([(24, 34), (14, 32), (10, 38), (2, 42), (0, 46), (0, 56), (24, 56)], Mat('m', 'm', 'n'), cape)
    hair_back = c.new_part()
    c.poly2([(14, 12), (6, 16), (3, 26), (5, 34), (10, 38), (14, 30)], Mat('H', 'h', 'i'), hair_back)
    neck(c, 20, 27, 30, 42)
    body = robe(c, Mat('a', 'b', 'b'), top=41, wide=-2)
    c.finish()
    collar(c, body, top=41, band='gk', inner='S', inner2='k', slope=0.8)
    for (x, y) in c.cells(body):         # gold dots on the black robe
        if c.tone[y][x] == 'b' and (x % 4 == 1 and y % 4 == 1 or x % 4 == 3 and y % 4 == 3) and 44 < y < 55 and 0 < x < 47:
            if all(c.part[y + dy][x + dx] == body for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                c.tone[y][x] = 'g'
    half(c, XT_HAIR)
    face(c, 'h', 'proud', mouth='smirk')
    put(c, 'rr', 16, 23)
    put(c, 'rr', 30, 23)
    # the dragon horns rising from the diadem, curving outward
    put(c, """
.kk.......
kYyk......
kYyk......
.kYyk.....
.kYyk.....
..kYyk....
..kYyyk...
...kYyyk..
....kYyk..
.....kyk..
""", 6, 3, mirror=True)
    skin_shade(c)
    shade_right(c, {'h': 'i', 'i': 'j'}, band=2, x0=24, y0=0, y1=40)
    return c
