"""Monsters & beasts (怪物與野獸) in the 8-bit `nes` style: original wuxia / Chinese-folklore creatures.

Each one has a big front-view battle picture like an NES RPG enemy (hand-typed rows, size per creature, at most
64x64; '.' is the transparent backdrop) and a 16x16 or 16x24 field sprite with a two-frame idle/move cycle.
Same colour rules as the people: 2C02 colours only, one 3-colour sub-palette per 16x16 area (max 4), sprite
overlays 3 colours per 8x8 tile; a field sprite is one sprite sub-palette (3 colours + transparent).
nes_beasts.py turns these into gallery variants.
"""

# ---------------------------------------------------------------- White Ape of the Broken Cliff
APE = '''
........................................................|
........................................................|
.........................kkkkkk.........................|
.......................kkWWWWWWkk.......................|
.....................kkWWWWWWWWWWkk.....................|
....................kWWWWWWWWWWWWWWk....................|
...................kWWWWWWWWWWWWWWWWk...................|
...................kWWWWWWWWWWWWWWWWk...................|
..................kWWWWWWWWWWWWWWWWWWk..................|
..................kWWWWWWWWWWWWWWWWWWk..................|
.................kWLWWkkkkkkkkkkkkWWLWk.................|
.................kWWWkkGGGGGGGGGGkkWWWk.................|
.................kWWWWGkkkGGGGkkkGWWWWk.................|
.................kWWWWGGkkGGGGkkGGWWWWk.................|
.................kLWWGGGGGGGGGGGGGGWWLk.................|
............kk...kWWWGGGGGkGGkGGGGGWWWk...kk............|
........kkkkWWk...kWWGGGGGGGGGGGGGGWWk...kWWkkkk........|
......kkWWWWWWkkkkWWWGGGkkkkkkkkGGGWWWkkkkWWWWWWkk......|
.....kWWWWWWWWkkWWWLWWGGGkWGGWkGGGWWLWWWkkWWWWWWWWk.....|
.....kWWWWWWWWWkWLLLLWGGGGGGGGGGGGWLLLLWkWWWWWWWWWk.....|
....kWWWWWWWWWWkLLLLLLWGGGGGGGGGGWLLLLLLkWWWWWWWWWWk....|
....kWWWWWWWWWWkLLLLLLLWGGGGGGGGWLLLLkLLkWWWWWWWWWWk....|
....kWWWWWkWWWWkLkLLLLLWWWWWWWWWWLLLLLkLkWWWWWWWWWWk....|
....kWWWWWWkWWWkLLkLLLWWWWWWWWWWWWLLLLLLkWWWWWWWWWWk....|
...kWWWWWWWWWWWWkLLLLGGGGGGGGGGGGGGLLLLkkWWWWWWWWWWWk...|
...kWWWWWWWWWWWWkWWWWGGGGGGGGGGGGGGWWWWkWkWWWWWWWWWWk...|
...kWWWWWWWWWWWWkWWWGGGGGGGGkGGGGGGGWWWkWWWWWWWWWWWWk...|
...kWWWWWWWWWWWWkWWWGGGGGGGGkGGGGGGGWWWkWWWWWWWWWWWWk...|
..kWWWWWWWWWWWWWkWWWGGGGGGGGkGGGGGGGWWWkWWWWWWWWWWWWWk..|
..kWWWWWWWWWWWWWkWWWGGGGGGGGkGGGGGGGWWWkWWWWWWWWWWWWWk..|
..kWWWWWkWWWWWWWkWWWGGGGGGGGkGGGGGGGWWWkWWWWWkWWWWWWWk..|
..kWWWWWWkWWWWWWkWWGGGGGGGGGkGGGGGGGGWWkWWWWWWkWWWWWWk..|
..kWWWLLWWWWWWWWkWWGGGkkkkGGkGkkkkGGGWWkWWWWWWWWLLWWWk..|
..kWWLLLLWWWWWWkWWWGGGGGGGGGkGGGGGGGGWWWkWWWWWWLLLLWWk..|
..kWLLLLLLWWWWWkWLLGGGGGGGGGkGGGGGGGGLLWkWWWWWLLLLLLWk..|
...kLLLLLLWWWWWkLLLLGGGGGGGGkGGGGGGGLLLLkWWWWWLLLLLLk...|
...kLLLLLLLWWLLkLLLLGGGGGGGGkGGGGGGGLLLLkLLWWLLLLLLLk...|
...kLLLLLLLWLLLkLLLLLGGGGGGGkGGGGGGLLLLLkLLLWLLLLLLLk...|
...kLLLLLLLkLLkkLLLLLGGGGGGGkGGGGGGLLLLLkkkLLLLLLLLLk...|
...kLLLLLLLLkLkLLLLLLLGGGGGGGGGGGGLLLLLLLkLkLLLLLLLLk...|
...kLLLLLLLLLLkLLLLLLLGGGGGGGGGGGGLLLLLLLkLLLLLLLLLLk...|
...kLLLLLLLLLLkLLLLLLLLGGGGGGGGGGLLLLLLLLkLLLLLLLLLLk...|
...kLLLLLLLWLLkLLLLLLLLLLLLLLLLLLLLLLLLLLkLLWLLLLLLLk...|
...kLLLLLLLWWLkLLLLLLLLLLLLLLLLLLLLLLLLLLkLWWLLLLLLLk...|
....kLLLLLWWWkLkLLLLLLLLLLLLLLLLLLLLLLLLkLkWWWLLLLLk....|
....kLLLLLWWWkLLkLLLLLLLLLLLLLLLLLLLLLLLLkkWWWLLLLLk....|
....kLGGGGGWWkLLLLLLLLLLLLLLLLLLLLLLLLLLLLkWWGGGGGLk....|
...kGGGGGGGGGLLLLLLLLLLLLLkkkkLLLLLLLLLLLLLGGGGGGGGGk...|
..kGGGGGGGGGGGLLLLLLLLLLLLk..kLLLLLLLLLLLLGGGGGGGGGGGk..|
..kGGGGGGGGGGGLLLLLLLLLLLLk..kLLLLLLLLLLLLGGGGGGGGGGGk..|
..kGGGGGGGGGGGLLLLLLLLLLLk....kLLLLLLLLLLLGGGGGGGGGGGk..|
..kGGGGGGGGGGGGGGGGGGLLLk......kLLLGGGGGGGGGGGGGGGGGGk..|
...kGkGGkGGkGGGGGGGGGGLk........kLGGGGGGGGGGkGGkGGkGk...|
....kkGGkGGkGGGGGGGGGGk..........kGGGGGGGGGGkGGkGGkk....|
......kk.kkGGGkGGkGGGk............kGGGkGGkGGGkk.kk......|
...........kkk.kk.kkk..............kkk.kk.kkk...........|
'''
APE_SPR = '''
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
45:g
44:krrk
43:rrrrr
43:rerrr
43:rrrrr
44:rrr
'''
APE_SLOTS = {'W': 0x30, 'L': 0x10, 'G': 0x00}
APE_PALETTES = [(0x30, 0x10, 0x00)]
APE_SPR_SLOTS = {'r': 0x16, 'e': 0x36, 'g': 0x1A, 'k': 0x16}
APE_SPR_PALETTES = [(0x16, 0x36, 0x1A)]
APE_SIZE = (56, 56)

# ---------------------------------------------------------------- White-Browed Mountain Tiger
TIGER = '''
........................................................|
........................................................|
........kkkkkk............................kkkkkk........|
.......kooooook..........................kooooook.......|
......kooooooook........................kooooooook......|
.....kooooooooook....kk..........kk....kooooooooook.....|
.....koooooOooook.kkkookkkkkkkkkkookkk.kooooOoooook.....|
.....koooOOOOOookkoooooooookkoooooooookkooOOOOOoook.....|
.....koooOOOOOoooooooooooookkoooooooooooooOOOOOoook.....|
.....koooOOOOOooooooooookkkkkkkkooooooooooOOOOOoook.....|
.....koooOOOOOoooooooooooookkoooooooooooooOOOOOoook.....|
......kooooOoooooooooooooookkoooooooooooooooOooook......|
.......koooooooooooooookkkkkkkkkkoooooooooooooook.......|
........kkooooooooooooooooooooooooooooooooooookk........|
.........koooooWWWWWWWWooooooooooWWWWWWWWoooook.........|
........koookkWWWWWWWWWWooooooooWWWWWWWWWWkkoook........|
........kooookkkkWWWWWWooooooooooWWWWWWkkkkooook........|
........kkkoookWWWkkkooooooooooooookkkWWWkkkkoook.......|
.......kookkkokWWWkWWkkooooooooookkWWkWWWkkoooook.......|
......kooooooookkWkWWWkooooooooookWWWkWkkooooooook......|
......koooooooooookkkkkooooooooookkkkkoooooooooook......|
......kooooooooooooooooooooooooooooooooooooooooook......|
.......kkkkooooooooooooooooooooooooooooooookkkkook......|
......koOOkkOoooooooooooooooooooooooooooookkOOOOok......|
......kOOOOOOOooooooooooooooooooooooooooooOOOOOOOk......|
.....kOOOOOOOOOooooooooooooooooooooooooooOOOOOOOOOk.....|
.....kOOOOOOOOOoooooWWWkkkkkkkkkkWWWoooooOOOOOOOOOk.....|
....kOOkkOOOOOOOooWWWWWkWWWWWWWWkWWWWWooOOOOOOOkkOOk....|
.....kkOkkkOOOOOoWWWWWWWkWWWWWWkWWWWWWWoOOOOOkkkOkk.....|
....kOkkOOOOOOOOWWWWWWWWWkkWWkkWWWWWWWWWOOOOOOOOkkOk....|
....kOOOOOOOOOOOWWkWWWWWWWWkkWWWWWWWWkWWOOOOOOOOOOOk....|
.....kOOOOOOOOOoWWWWWWWWWWWkkWWWWWWWWWWWoOOOOOOOOOk.....|
.....kOOOOOOOOOoWWWWkkWWkkkWWkkkkkkkWWWWoOOOOOOOOOk.....|
......kOOOOOOOoookWWWkkkkkkkkkkkkkWWWWkoooOOOOOOOk......|
.......kOOOOOoooooWWWkWWkkkkkkkWWkWWWWoooooOOOOOk.......|
........kkkkkoooooooWWkWkkrrrkkWkWWWoooooookkkkk........|
..........kkooooooooookWkrrrrrkWkWooooooooookk..........|
........kkooooooooooooWkkkkkkkkkWWooooooooooookk........|
.......koooooooooooooooWWWWWWWWWWoooooooooooooook.......|
......koooooooooooooooooWWWWWWWWoooooooooooooooook......|
.....koookkoooooooooooooooooooooooooooooooooookkook.....|
....koooookkoooooooooooooooooooooooooooooooookkooook....|
...koooooookooooooookooooooooooooookoooooooookooooook...|
...kooooooooooooooookooooooooooooookooooooooooooooook...|
...kooooooooooooooookooooooooooooookooooooooooooooook...|
...koooookkkooooooookooooooooooooookooooooookkkoooook...|
....kooooookooooooookooooooooooooookooooooookooooook....|
.....kooooooooooooookooooooooooooookooooooooooooook.....|
......koOOOOOOOOOOookooooooooooooookooOOOOOOOOOOok......|
......kOOOOOOOOOOOOokooooooooooooookoOOOOOOOOOOOOk......|
.....kOOOOOOOOOOOOOOooooooooooooooooOOOOOOOOOOOOOOk.....|
....kOOOOOOOOOOOOOOOOooooooooooooooOOOOOOOOOOOOOOOOk....|
.....kOOOOkOOkOOkOOOooooooooooooooooOOOkOOkOOkOOOOk.....|
......kOOOkOOkOOkOOkkooooooooooooookkOOkOOkOOkOOOk......|
.......kOOOOOOOOOOk..kkkkkkkkkkkkkk..kOOOOOOOOOOk.......|
........kkkkkkkkkk....................kkkkkkkkkk........|
'''
TIGER_SPR = '''
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
..............yyyyyyyyy..........yyyyyyyyy..............
.................yyyyyy..........yyyyyy.................
...............yyy....................yyy...............
...............yyy.yy..............yy.yyy...............
.................y.yyy............yyy.y.................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................pppppppp........................
.......................p.pppppp.p.......................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
........................................................
'''
TIGER_SLOTS = {'o': 0x17, 'O': 0x27, 'W': 0x30, 'r': 0x16}
TIGER_PALETTES = [(0x27, 0x17, 0x30), (0x17, 0x16, 0x30)]
TIGER_SPR_SLOTS = {'y': 0x28, 'p': 0x25}
TIGER_SPR_PALETTES = [(0x28, 0x25)]
TIGER_SIZE = (56, 56)

# ---------------------------------------------------------------- Stone Guardian Lion
LION = '''
............kLLLLLLLLLkkLLLkkLLLkkLLLLLLLLLk............|
...........kLLLLLLLLLLGLkLLGGLLkLGLLLLLLLLLLk...........|
...........kLLLkkLLLLLLkkLLGGLLkkLLLLLLkkLLLk...........|
........kkkkLLLGLkLLLLLLLLLGGLLLLLLLLLkLGLLLkkkk........|
.......kLLLLLLLLkkLLLLLLLLGGGGLLLLLLLLkkLLLLLLLLk.......|
......kLLLLLLLLLLLLLGLLLLGGGGGGLLLLGLLLLLLLLLLLLLk......|
.....kLLLLLLLLLLLLLGGGGGGGGGGGGGGGGGGLLLLLLLLLLLLLk.....|
.....kLLLkkLLLGLLGGGGGGGGGGGGGGGGGGGGGGLLGLLLkkLLLk.....|
.....kLLLGLkLLGGGGGGGGGGLLLLLLLLGGGGGGGGGGLLkLGLLLk.....|
.....kLLLLkkLLGGGGGGGLLLLLLLLLLLLLLGGGGGGGLLkkLLLLk.....|
....kkGLLLLLLGGGGGGLLLLLLLLLLLLLLLLLLGGGGGGLLLLLLGkk....|
...kLLLLLLLLGGGGGGLLLLLLLLLLLLLLLLLLLLGGGGGGLLLLLLLLk...|
..kLLLLLLGGGGGGGGLLLLLLLLLLLLLLLLLLLLLLGGGGGGGGLLLLLLk..|
.kLLLLLLLLGGGGGGLLLLLLLLLLLLLLLLLLLLLLLLGGGGGGLLLLLLLLk.|
.kLLLkkLLLGGGGGLLkkkkkkkkLLLLLLkkkkkkkkLLGGGGGLLLkkLLLk.|
.kLLLGLkLLGGGGGLkGGGGGGGGkLLLLkGGGGGGGGkLGGGGGLLkLGLLLk.|
.kLLLLkkLLGGGGLLLLLkkkkLLLLLLLLLLkkkkLLLLLGGGGLLkkLLLLk.|
..kLLLLLLGGGGGLLLLkWWWWkLLLLLLLLkWWWWkLLLLGGGGGLLLLLLk..|
..kGLLLLGGGGGLLLLkWWkkWWkLLLLLLkWWkkWWkLLLLGGGGGLLLLGk..|
..kLLLLGGGGGGLLLLkWWkkWWkLLLLLLkWWkkWWkLLLLGGGGGGLLLLk..|
.kLLLLLLGGGGGLLLLLkWWWWkLLLLLLLLkWWWWkLLLLLGGGGGLLLLLLk.|
kLLLLLLLLGGGGLLLLLLkkkkLLLLLLLLLLkkkkLLLLLLGGGGLLLLLLLLk|
kLLLkkLLLGGGGLLLLLLLLLLkkkkkkkkkkLLLLLLLLLLGGGGLLLkkLLLk|
kLLLGLkLLGGGGLLLLLLLLLkGGGGGGGGGGkLLLLLLLLLGGGGLLkLGLLLk|
kLLLLkkLLGGGGLLLLLLLLkGGWGGGGGGWGGkLLLLLLLLGGGGLLkkLLLLk|
.kLLLLLLGGGGGLLLLLLLLkGkkGGGGGGkkGkLLLLLLLLGGGGGLLLLLLk.|
..kLLLLGGGGGGGLLLLLLLLkkkkGGGGkkkkLLLLLLLLGGGGGGGLLLLk..|
...kkLLLLGGGGGLLLLLLLLLLLLLLLLLLLLLLLLLLLLGGGGGLLLLkk...|
...kLLLLLLGGGGGLLLLkkkkkkkkkkkkkkkkkkLLLLGGGGGLLLLLLk...|
..kLLLLLLLLGGGGLLLkWWkWWkWWkkWWkWWkWWkLLLGGGGLLLLLLLLk..|
..kLLLkkLLLGGGGGLLkWkkkkkkkkkkkkkkkkWkLLGGGGGLLLkkLLLk..|
..kLLLGLkLLGGGGGGLkWkkkkkLLLLLLkkkkkWkLGGGGGGLLkLGLLLk..|
..kLLLLkkLLLLLGGGGkkkkkkLLWLLLLLkkkkkkGGGGLLLLLkkLLLLk..|
...kLLLLLLLLLLLGGGGkkkkkLLLLLLLGLkkkkGGGGLLLLLLLLLLLk...|
....kLLLLLLLLLLLGGGGkkkkkLLLLLGLkkkkGGGGLLLLLLLLLLLk....|
.....kkkLLLkkLLLGGGGGkkkkkkkkkkkkkkGGGGGLLLkkLLLkkk.....|
.......kLLLGLkLLGGGGGGGGGGGGGGGGGGGGGGGGLLkLGLLLk.......|
.......kLLLLkkLkkkGGGGGGGGGGGGGGGGGGGGGkkLkkLLLLk.......|
........kLLLLLLLLkkkkkkkkkkkkkkkkkkkkkkLLLLLLLLk........|
.........kLLLLLLLLLLGkLLLLkkkkkLLLkGLLLLLLLLLLk.........|
..........kkLLLLLLLLGkLLLkWWLLLkLLkGLLLLLLLLkk..........|
...........kLLLLLLLLGkLLLkWLLLGkLLkGLLLLLLLLk...........|
...........kLLLLLLLLGkLLLkkkGkkkLLkGLLLLLLLLk...........|
............kLLLLLLLGkLLLLkkkkkLLLkGLLLLLLLk............|
............kLLLLLLLGkLLLLLLLLLLLLkGLLLLLLLk............|
...........kLLLLLLLLGkLLLLLLLLLLLLkGLLLLLLLLk...........|
..........kLLLLLLLLLGkLLLLLLLLLLLLkGLLLLLLLLLk..........|
..........kLLLLLLLLLGkLLLLLLLLLLLLkGLLLLLLLLLk..........|
.....kkkkkkLLLkLkLkLLLLLLLLLLLLLLLLLLkLkLkLLLkkkkkk.....|
....kLLLLLLLLLkLkLkLLLLLLLLLLLLLLLLLLkLkLkLLLLLLLLLk....|
....kGmmGGGGmGGGLGGGGGGLLLLLLLmmLGGGGGGLGGGGGGGmmGGk....|
....kGGmkkkkkkkkkkkkkkGGGGGGGGGmGkkkkkkkkkkkkkGGmGGk....|
....kGmGkGGGGGGGGGGGGkGGGGGGGGGGGkGGGGGGGGGGGkGGGmGk....|
....kGGGkGGGGGGGGGGGGkGGGGGGGGGGGkGGGGGGGGGGGkGGGmGk....|
....kGGGkkkkkkkkkkkkkkGGGGmGGGGGGkkkkkkkkkkkkkGGGGGk....|
....kGGGGGGGGGGGGGGGGGGGGmmGGGGGGGGGGGGGGGGGGGGGGGGk....|
'''
LION_SPR = '''
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
20:rr..........rr
20:re..........re
'''
LION_SLOTS = {'L': 0x10, 'G': 0x00, 'W': 0x30, 'm': 0x1A}
LION_PALETTES = [(0x10, 0x00, 0x30), (0x10, 0x00, 0x1A)]
LION_SPR_SLOTS = {'r': 0x16, 'e': 0x26}
LION_SPR_PALETTES = [(0x16, 0x26)]
LION_SIZE = (56, 56)

# ---------------------------------------------------------------- Talisman Jiangshi
JIANGSHI = '''
........................................................|
........................kkkkkkkk........................|
......................kkppppppppkk......................|
....................kkppppppppppppkk....................|
...................kppppppppppppppppk...................|
..................kppppppppppppppppppk..................|
..................kppppppppppppppppppk..................|
.................kppppppppppppppppppppk.................|
.................kppppppppppppppppppppk.................|
.................kppppppppppppppppppppk.................|
...............kkkkkkkkkkkkkkkkkkkkkkkkkk...............|
..............kppppppppppppppppppppppppppk..............|
..............kppppppppppppppppppppppppppk..............|
..............kkkkkkkkkkkkkkkkkkkkkkkkkkkk..............|
...................kSSpkYYYYYYYYkpSSk...................|
..................kSSSSkYYYYYYYYkSSSSk..................|
..................kSSSSkYYYYYYYYkSSSSk..................|
..................kkkkkkYYYYYYYYkkkkkk..................|
..................kYYYkkYYYYYYYYkkYYYk..................|
.................kSkkkSkYYYYYYYYkSkkkSk.................|
.................kSSSSSkYYYYYYYYkSSSSSk.................|
.................kSSSSSkYYYYYYYYkSSSSSk.................|
.................kSSSSSkYYYYYYYYkSSSSSk.................|
.................kSSSSSkYYYYYYYYkSSSSSk.................|
.................kSSSSSkYYYYYYYYkSSSSSk.................|
.................kSSSSSkYYYYYYYYkSSSSSk.................|
...............kkkSSkWkkYYYYYYYYkkWkSSkkk...............|
..............kppppppSSkYYYYYYYYkSSppppppk..............|
.............kkppppppppkYYYYYYYYkppppppppkk.............|
........kkkkkppppppppppkkkkkkkkkkppppppppppkkkkk........|
kkkk.kkkppppppppppppppkyykppppppkyykppppppppppppkkk.kkkk|
SSSSkPPppppppppppppppppkyykppppkyykppppppppppppppPPkSSSS|
SSSSkPPpppppppppppppppppkyykkkkyykpppppppppppppppPPkSSSS|
kkSSkPPppppppppppppppppppppppppppppppppppppppppppPPkSSkk|
SSSSkPPPppppppppppppppppppppppppppppppppppppppppPPPkSSSS|
kkSSkPPppppppppppppppppppppppppppppppppppppppppppPPkSSkk|
SSSSkPPppppppppppppppppppppppppppppppppppppppppppPPkSSSS|
kkSSkPPppppppppppppppkkkkkkkkkkkkkkppppppppppppppPPkSSkk|
SSSSkkkkkppppppppppppkyyyyyyyyyyyykppppppppppppkkkkkSSSS|
kkkk.....kkkkkpppppppkykkkkkkkkkkykpppppppkkkkk.....kkkk|
.............kpppppppkykPPkPPkPPkykpppppppk.............|
.............kpppppppkykkPPPPPPkkykpppppppk.............|
.............kpppppppkykPPkPPkPPkykpppppppk.............|
.............kpppppppkykkkkkkkkkkykpppppppk.............|
.............kpppppppkyyyyyyyyyyyykpppppppk.............|
............kppppppppkkkkkkkkkkkkkkppppppppk............|
............kppppppppppppppppppppppppppppppk............|
............kppppppppppppppkkppppppppppppppk............|
............kppppppppppppppkkppppppppppppppk............|
............kppppppppppppppkkppppppppppppppk............|
............kppppppppppppppkkppppppppppppppk............|
............kppppppppppppppkkppppppppppppppk............|
...........kpppppppppppppppkkpppppppppppppppk...........|
...........kyyyyyyyyyyyyyyykyyyyyyyyyyyyyyyyk...........|
...........kpppppppppppppppkkpppppppppppppppk...........|
...........kpppppppppppppppkkpppppppppppppppk...........|
'''
JIANGSHI_SPR = '''
.
.
27:rr
26:rrrr
27:rr
.
.
.
.
.
.
.
.
.
.
.
25:rrrrrr
27:rr
25:rrrrrr
26:r..r
25:rrrrrr
27:rr
26:r..r
25:rr..rr
27:rr
'''
JIANGSHI_SLOTS = {'S': 0x3A, 'Y': 0x38, 'W': 0x38, 'p': 0x03, 'P': 0x13, 'y': 0x38}
JIANGSHI_PALETTES = [(0x3A, 0x38, 0x03), (0x3A, 0x13, 0x03), (0x03, 0x13, 0x38)]
JIANGSHI_SPR_SLOTS = {'r': 0x16}
JIANGSHI_SPR_PALETTES = [(0x16,)]
JIANGSHI_SIZE = (56, 56)

# ---------------------------------------------------------------- Shanxiao, the One-Footed Mountain Imp
SHANXIAO = '''
...............kggggk..............kggggk...............|
..............kggggggk..kkkkkkkk..kggggggk..............|
..........kkkkkggggggkkkggggggggkkkggggggkkkkk..........|
.........kggggkggggggggggggggggggggggggggkggggk.........|
........kggggggggggggggggggggggggggggggggggggggk........|
........kggggggkggggggggggggggggggggggggkggggggk........|
........kggggggkggggggggggggggggggggggggkggggggk........|
........kggggggggggggggggBBBBBBggggggggggggggggk........|
.........kggggggggggggBBBBBBBBBBBBggggggggggggk.........|
.......kkkkkkggggggggBBBBBBBBBBBBBBggggggggkkkkkk.......|
......kggggkkgggggggBBBBBBBBBBBBBBBBgggggggkkggggk......|
.....kgggggggggggggkkkkkkkkkkkkkkkkkkgggggggggggggk.....|
.....kggggggggggggBBkggkkkrrrrkkkggkBBggggggggggggk.....|
.....kggggggggggggBBkggkkBrrrrBkkggkBBggggggggggggk.....|
.....kggggggggggggBBBkkBBBrrrrBBBkkBBBggggggggggggk.....|
......kggggggggggBBBBBBBBBrrrrBBBBBBBBBggggggggggk......|
.......kkkkggggggBBBBBBBBBrrrrBBBBBBBBBggggggkkkk.......|
......kkkkkggggggBkkkBBBBBrrrrBBBBBkkkBggggggkkkkk......|
.....kggggkggggggBBBBBBBBBrrrrBBBBBBBBBggggggkggggk.....|
....kggggggggggggBBBBBBBBBrrrrBBBBBBBBBggggggggggggk....|
....kggggggggggggBkkkBBBBBrrrrBBBBBkkkBggggggggggggk....|
....kggggggkgggggBBBBBBBBBrrrrBBBBBBBBBgggggkggggggk....|
....kggggggkgggggBBBBBBBBBrrrrBBBBBBBBBgggggkggggggk....|
.....kggggk.kggggBkkkBBBBBrrrrBBBBBkkkBggggk.kggggk.....|
......kkkkkkkgggggBBBBBBBBrrrrBBBBBBBBgggggkkkkkkk......|
........kggggkggggBBBBBBrrrrrrrBBBBBBBggggkggggk........|
.......kggggggkggggBBBBBrkrrrrkBBBBBBggggkggggggk.......|
.......kggggggkkggggggBBrrrrrrrBBBggggggkkggggggk.......|
.......kggggggk.kgggggggrrrrrrrggggggggk.kggggggk.......|
.......kggggggk..kkggggggggrgggggggggkk..kggggggk.......|
........kggggk.....kkgkkkkkkkkkkkkgkk.....kggggk........|
.........kkkkkkk.....k.kgkkkkkkgk.k.....kkkkkkk.........|
.........kkkooook..kkkkokkkkkkkkokkkk..kooookkk.........|
........koooooookkkooooooooooooooooookkkoooooook........|
.......kooooooooookooooooooooooooooookooooooooook.......|
.......kooooooooooooooooooooooooooooooooooooooook.......|
......koooooooooooooookooooooooookoooooooooooooook......|
......koooooooooooooookooooooooookoooooooooooooook......|
.....kokooooooooooooddddddddddddddddooooooooooookok.....|
.....kokooooooooooddddddddddddddddddddooooooooookok.....|
.....kooooooookooddddddddddddddddddddddookooooooook.....|
....kooooooookkooddddddddddddddddddddddookkooooooook....|
....kooooooook.kkoddddddddddddddddddddokk.kooooooook....|
...koooooooook...kkoddddddddddddddddokk...koooooooook...|
...kooooooook......kkkooooooooooookkk......kooooooook...|
...kooooooook.........kddddddddddk.........kooooooook...|
...kooooooook.........kddddddddddk.........kooooooook...|
....koddddook.........kddkddddkddk.........kooddddok....|
...kddddddddk.........kddkddddkddk.........kddddddddk...|
...kddddddddk......kkkddddddddddddkkk......kddddddddk...|
...kddddddddk....kkddddddddddddddddddkk....kddddddddk...|
...kddddddddk...kddddddddddddddddddddddk...kddddddddk...|
....kkddkdkk....kddddddddddddddddddddddk....kkdkddkk....|
......kk.k......kddkdddkdddkdddkdddkdddk......k.kk......|
.................kkddddddddddddddddddkk.................|
...................kkkddddddddddddkkk...................|
'''
SHANXIAO_SPR = '''
.
'''
SHANXIAO_SLOTS = {'o': 0x17, 'd': 0x07, 'g': 0x28, 'r': 0x16, 'B': 0x21}
SHANXIAO_PALETTES = [(0x17, 0x07, 0x28), (0x16, 0x21, 0x28), (0x17, 0x16, 0x21)]
SHANXIAO_SPR_SLOTS = {'y': 0x38}
SHANXIAO_SPR_PALETTES = [(0x38,)]
SHANXIAO_SIZE = (56, 56)

# ---------------------------------------------------------------- Nine-Tailed Fox Spirit
FOX = '''
.............k.............kk.............k.............|
............kgk...........kWWk...........kgk............|
...........kgWWkk........kWWWWk........kkWWgk...........|
...........kWWWWWkk.....kWWWWWWk.....kkWWWWWk...........|
...........kWWWWWWgk...kgWWWWWWgk...kgWWWWWWk...........|
..........kWWWWWWWggk..kgWWWWWWgk..kggWWWWWWWk..........|
..........kWWWWWWWgk...kggWWWWggk..kgkWWWWWWWk..........|
..........kgWWWWWggkk.kggggggggggkkgkkgWWWWWgk..........|
..........kgggWggkYkk.kggggggggggkkYkkgggWgggk..........|
..........kgggggggkYYkkggggggggggkgkYYkggggggk..........|
..........kgggggggkYYkkggggggggggkkkYYkggggggk..........|
...kkkk...kgggggggkWYYYkgggggggggkYYWYkggggggk...kkkk...|
..kWWWWkkkkgggggggkWWYYkgggggggggkYWWYkggggggkkkkWWWWk..|
..kWWWWWWggggggggkkWWWYYkgggggggkYWWWYkkgggggggWWWWWWk..|
..kWWWWWWggggggggkYYWWWYkggggggYkWWWYYYkgggggggWWWWWWk..|
..kWWWWWWgggkggggkYYWWYYYkYYYYYkYYWWYYYkggkggggWWWWWWk..|
.kWWWWWWWggggkgggkYYWYYYYYYYYYYYYYYWYYYkgggkgggWWWWWWWk.|
.kgWWWWWgggggggggkYYYYYYYYYYYYYYYYYYYYYkggggggggWWWWWgk.|
.kggWWWgggggggggkYYYYYYYYYYYYYYYYYYYYYYYkggggggggWWWggk.|
.kggggggggggggggkYYYkkkYYYYYYYYYYkkkYYYYkgggggggggggggk.|
..kgggggggggggggkYYYYkkkkYYYYYYkkkkYYYYYkggggggggggggk..|
..kggggggggggggkgkYYYYYkkYYYYYYkkYYYYYYkgkgggggggggggk..|
...kggggggkggggggkYYYYYYYYWWWWYYYYYYYYYkggggkgggggggk...|
...kgggggggkgggggWkWWYYWWWWWWWWWWYYWWWkggggggkggggggk...|
....kgggggggggggWWkWWWWWWWWWWWWWWWWWWWkWgggggggggggk....|
....kggggggggggWWWWkWWWWWWWWWWWWWWWWWkWWWggggggggggk....|
.....kgggggggggWWWWWkWWWWWWWWWWWWWWWkWWWWgggggggggk.....|
....kkggggggggggWWWWkWYWWWWkkWWWWYWWkWWWggggggggggkk....|
..kkWWgggggggggggWWWWkYYWWWWWWWWYYYkWWWgggggggggggWWkk..|
.kWWWWWggggggggggggggkYYWWWWWWWWYYgkgggggggggggggWWWWWk.|
kWWWWWWgggggggggggggggkkYkWWWWkYYkkggggggggggggggWWWWWWk|
kWWWWWWgggggggggggggggYYkkkkkkYkkYgggggggggggggggWWWWWWk|
kWWWWWWgggggggggggggYYYYWkkWWWkkYYYYgggggggggggggWWWWWWk|
.kWWWWWkgggggggggggYYYYWWWWkkkWWWYYYYggggggggggkgWWWWWk.|
.kWWWgggkgggggggggYYYYYWWWWWkWWWWYYYYYggggggggggkggWWWk.|
.kgggggggggggggggYYYYYYWWWWWkWWWWYYYYYYgggggggggggggggk.|
..kgggggggggggggYYYYYYWWWWWWkWWWWWYYYYYYgggggggggggggk..|
...kggggggggggggYYYYYYWWWWWWkWWWWWYYYYYYggggggggggggk...|
....kgggggggggggYYYYYYWWWWWWkWWWWWYYYYYYgggggggggggk....|
.....kgggggggggYYYYYYYWWWWWWkWWWWWYYYYYYYgggggggggk.....|
......kkgggggggYYYYYYYWWWWWWkWWWWWYYYYYYYgggggggkk......|
........kkgggggYYYYYYYWWWWWWkWWWWWYYYYYYYgggggkk........|
..........kkkggYYYYYYYYYYYWWWWWYYYYYYYYYYggkkk..........|
.............kkYYYYYYYYYYYWWWWWYYYYYYYYYYkk.............|
..............kYYYYYYYYYYYWWWWWYYYYYYYYYYk..............|
...............kYYYYYYYYYYkWWWkYYYYYYYYYk...............|
...............kYYYYYYYYYYkWWWkYYYYYYYYYk...............|
...............kYYYYYYYYYYkWWWkYYYYYYYYYk...............|
................kYYYYYYYYYkWWWkYYYYYYYYk................|
.................kYYYYYYYYkWWWkYYYYYYYk.................|
..................kYYYYYYYkWWWkYYYYYYk..................|
...................kYWWWWYkYYYkWWWWYk...................|
...................kWWWWWWkYYYkWWWWWk...................|
...................kWWWWWWkYYYkWWWWWk...................|
....................kWWWWk.kkkkWWWWk....................|
.....................kkkk......kkkk.....................|
'''
FOX_SPR = '''
.
....b.............................................b.....
...bb............................................bb.....
...bbb...........................................bbb....
....b.............................................b.....
.
.
.
.
.
.
...................p................p...................
...................pp..............pp...................
...................ppp............ppp...................
....................ppp..........ppp....................
....................pp............pp....................
....................p..............p....................
.
.
.b...................................................b..
bb...................rr..........rr.................bb..
bbb.................................................bbb.
.b...................................................b..
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
'''
FOX_SLOTS = {'Y': 0x38, 'g': 0x28, 'W': 0x30, 'p': 0x35}
FOX_PALETTES = [(0x30, 0x38, 0x28)]
FOX_SPR_SLOTS = {'b': 0x21, 'r': 0x16, 'p': 0x35}
FOX_SPR_PALETTES = [(0x21,), (0x16, 0x35)]
FOX_SIZE = (56, 56)

# ---------------------------------------------------------------- River Jiao
JIAO = '''
..........................k..........k..........................|
.........................kTk...kk...kTk.........................|
........................kTkk..kTTk..kkTk........................|
...................kk...kTkTkkTkkTkkTkTk...kk...................|
..................kYYk..kTkTkkTkkTkkTkTk..kYYk..................|
...................kYYk.kTTkTTTkkTTTkTTk.kYYk...................|
....................kYYkTTTkTTTkkTTTkTTTkYYk....................|
.....................kYkTTTkTTTkkTTTkTTTkYk.....................|
......................kTTTTTTttttttTTTTTTk......................|
.....................kTTTTTTTTttttTTTTTTTTk.....................|
.....................kTTTTTTTTttttTTTTTTTTk.....................|
....................ktTTTTTTTTttttTTTTTTTTtk....................|
....................kkTTTTTTTTttttTTTTTTTTkk....................|
...................ktkkkkkTTTttttttTTTkkkkktk...................|
..................ktttkYYYYkttttttttkYYYYktttk..................|
..................ktttkYYkkkttttttttkkkYYktttk..................|
..................ktttkYYkkkttttttttkkkYYktttk..................|
..................kttttkkkkttttttttttkkkkttttk..................|
..................kttttttttttttttttttttttttttk..................|
..................kttttttttkkttttttkkttttttttk..................|
...................kttttttttttttttttttttttttk...................|
...................ktttttkkkkkkkkkkkkkktttttk...................|
.................kkWWttttkWkWkkkkkkWkWkttttWWkk.................|
...............kkWWkkkttttkWkkkkkkkkWkttttkkkWWkk...............|
............kkkWWWk...kttttkkkkkkkkkkttttk...kWWWkkk............|
..........kkWWWkkk.....kttttttttttttttttk.....kkkWWWkk..........|
.........kWWkkk.......kttttttttttttttttttk.......kkkWWk.........|
..........kk..........kttttttttttttttttttk..........kk..........|
......................kttttYttttttttYttttk......................|
......................kttttkkkkkkkkkkttttk......................|
......................kttttYYYYYYYYYYttttk......................|
........kkkk..........ktktkYYYYYYYYYYtktk...........kkkk........|
......kkttttkk........kttktkkkkkkkkkkttktk........kkttttkk......|
.....kTtttttttk.......kttttYYYYYYYYYYttttk.......ktttttttTk.....|
....kTtttttttttk......kttttYYYYYYYYYYttttk......ktttttttttTk....|
...kTTttktktttttk.....kttttkkkkkkkkkkttttk.....kttttttttttTTk...|
..kTTttttktttttttk....kttttYYYYYYYYYYttttk....kttttttktktttTTk..|
..kTTttttkkttktktk....ktktkYYYYYYYYYYtktk.....ktttktk.kttttTTk..|
.kTTtktkk..kttktttk...kttktkkkkkkkkkkttktk...ktttttk...kktktTTk.|
.kTTttk.....ktttttk...kttttYYYYYYYYYYttttk...ktttttk.....kttTTk.|
.kTTtttk....ktttttk...kttttYYYYYYYYYYttttk...ktttttk....ktttTTk.|
kTTTttk......kttktk...kttttkkkkkkkkkkttttk..kTtktkk......kttTTTk|
kTTTttk......ktttkTk..kttttYYYYYYYYYYttttk..kTttktk......kttTTTk|
kTTTttk......kttttTk..kttttYYYYYYYYYYttttk..kTttttk......kttTTTk|
kTTTktk......kttttTk..kttttkkkkkkkkkkttttk..kTttttk.......ktkTTk|
kTTTtk.......kttttTk..kttttYYYYYYYYYYttttk..kTttttk......ktkTTTk|
kTTTttk......kttttTk..kttttYYYYYYYYYYttttk..kTttttk......kttTTTk|
kTTTttkkkkkkkkttttTkkkkkkkkkkkkkkkkkkkkkkkkkkTttttkkkkkkkkttTTTk|
bbbbWWWbbbbbbbbbWWWbbbbbbbbbWWWbbbbbbbbbWWWbbbbbbbbbWWWbbbbbbbbb|
bbWWbbbWbbbbbbWWbbbWbbbbbbWWbbbWbbbbbbWWbbbWbbbbbbWWbbbWbbbbbbWW|
bWbbBBbbWbbWbWbbBBbbWbbWbWbbBBbbWbbWbWbbBBbbWbbWbWbbBBbbWbbWbWbb|
WbbBBBBbbWWbWbbBBBBbbWWbWbbBBBBbbWWbWbbBBBBbbWWbWbbBBBBbbWWbWbbB|
bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb|
bbbbbbbbWWbbbbbbbbbbWWbbbbbbbbbbWWbbbbbbbbbbWWbbbbbbbbbbWWbbbbbb|
bbbbbbbWbbWbbbbbbbbWbbWbbbbbbbbWbbWbbbbbbbbWbbWbbbbbbbbWbbWbbbbb|
bbbbbbWbBBbWbbbbbbWbBBbWbbbbbbWbBBbWbbbbbbWbBBbWbbbbbbWbBBbWbbbb|
'''
JIAO_SPR = '''
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
29:rrrrrr
'''
JIAO_SLOTS = {'t': 0x1C, 'T': 0x2C, 'Y': 0x38, 'F': 0x0C, 'W': 0x30, 'b': 0x11, 'B': 0x21}
JIAO_PALETTES = [(0x2C, 0x1C, 0x38), (0x21, 0x11, 0x30), (0x1C, 0x38, 0x30)]
JIAO_SPR_SLOTS = {'r': 0x16}
JIAO_SPR_PALETTES = [(0x16,)]
JIAO_SIZE = (64, 56)

# ---------------------------------------------------------------- Three-Legged Fire Crow
CROW = '''
................................................................|
................................................................|
................................................................|
......kkk..............................................kkk......|
...kkkdddkk..........................................kkdddkkk...|
.kkddddddddkk......................................kkddddddddkk.|
kddddddddddddkk..............kkkkkk..............kkddddddddddddk|
kodddddddddddddkk...........kddddddk...........kkdddddddddddddok|
koddddkddddddddddkk........kddddddddk........kkdddddddddkkddddok|
oooddddkkddddddddddk......kddddddddddk......kdddddddddkkdddddooo|
ooordddddkkdddddddddk....kddddddddddddk....kddddddddkkddddddrooo|
ooordddddddkkddddddddk..kdkkkddddddkkkdk..kdddddddkkddddddddrooo|
kooorddddddddkkdddddddk.kddkYkddddkYkddk.kddddddkkdddddddddroook|
.koorddddddddddkdddddddkkdddkddddddkdddkkddddddkdddddddddddrook.|
..korrddddddddddkkddddddkddddddddddddddkdddddkkdddddddddddrrok..|
.koorrddddddddddddkkdddddddddYYYYYYddddddddkkdddddddddddddrrook.|
.kookkrdddddddddddddkkddddddddYYkYdddddddkkddddddddddddddrkkook.|
.kooorkkkkddddddddddddkkddddddYYkYdddddkkdddddddddddddkkkkroook.|
koooorrdddkkkdddddddddddkdkdddYYkYdddkkddddddddddddkkkdddrrooook|
.koooorrdddddkkkdddddddddddddddYkdddddddddddddddkkkdddddrrooook.|
..kkoorrddddddddkkkddddddkdddddYkdddddkddddddkkkddddddddrrookk..|
....koorrddddddddddkkkkdddddddddkddddddddkkkkddddddddddrrook....|
...koooorrdddddddddddddkkddddddddddddddkkdddddddddddddrrooook...|
..kooooorrrddddddddddddddddddddddddddddddddddddddddddrrroooook..|
..kookkkkkrrddddddddddddddddddddddddddddddddddddddddrrkkkkkook..|
.kooooooorkkkkkkkkkddddddddddddddddddddddddddkkkkkkkkkroooooook.|
..kkoooooorrrrdddddkkkkkdddddkddddkdddddkkkkkdddddrrrrooooookk..|
....kkkooorrrrrdddddddddddddddkkkkdddddddddddddddrrrrroookkk....|
.....koooorrrrrddddddddddddddddddddddddddddddddddrrrrrooook.....|
.....kooooorrrrrddddddddddddddddddddddddddddddddrrrrroooook.....|
.....kookkkkkkkkkkkkkkkddddddkddddkddddddkkkkkkkkkkkkkkkook.....|
....koook.krrrrrrddddddkddddddkkkkddddddkddddddrrrrrrk.koook....|
.....kkk..krrrrrrdddddk.kddddddddddddddk.kdddddrrrrrrk..kkk.....|
..........krrrrrkdddddk.kddddddddddddddk.kdddddkrrrrrk..........|
..........krrrkk.kdddk..kddddkddddkddddk..kdddk.kkrrrk..........|
..........krkk...kddk....kddddkkkkddddk....kddk...kkrk..........|
...........k......kk.....kddddddddddddk.....kk......k...........|
..........................kddddddddddk..........................|
...........................kddddddddk...........................|
...........................kkkdkkkkkkk..........................|
..........................kkkkkkkk.kkk..........................|
.........................krkkk.kkk.kkk..........................|
.........................krkkk.kkkkkkkk.........................|
........................krrkkkkkkkokkkrk........................|
........................krokkkokkkokkkrk........................|
.......................krrokkkokkkokkkrrk.......................|
.......................krrokkkokkkokkkrrk.......................|
......................krroroooooooooororrk......................|
......................krrrrooookkoooorrrrk......................|
.....................krrkrrooorkkrooorrkrrk.....................|
......................kkkrrrorrkkrrorrrkkk......................|
........................krrrrrrkkrrrrrrk........................|
.........................krrkkrkkrkkrrk.........................|
.........................krk..krrk..krk.........................|
..........................k....kk....k..........................|
................................................................|
'''
CROW_SPR = '''
.
.
.
.
.
.
.
.
.
.
.
.
.Y.........................W........W.........................Y.
.
.
.
.
.
.Y............................................................Y.
.
.
.
.
.
.
...Y........................................................Y...
.
.
.
.
.
......Y..................................................Y......
.
.
.
...........Y........................................Y...........
.................Y............................Y.................
.
.
............................Y...Y...Y...........................
............................Y...Y...Y...........................
............................Y...Y...Y...........................
............................Y...Y...Y...........................
............................Y...Y...Y...........................
............................Y...Y...Y...........................
...........................YYY.YYY.YYY..........................
.
.
.
.
.
.
.
.
..........................Y.....Y...............................
.
'''
CROW_SLOTS = {'d': 0x06, 'r': 0x16, 'o': 0x27, 'Y': 0x38}
CROW_PALETTES = [(0x06, 0x16, 0x27), (0x16, 0x27, 0x38), (0x06, 0x16, 0x38), (0x06, 0x27, 0x38)]
CROW_SPR_SLOTS = {'W': 0x30, 'Y': 0x38}
CROW_SPR_PALETTES = [(0x30, 0x38)]
CROW_SIZE = (64, 56)

# ---------------------------------------------------------------- Venom Toad of the Marsh
TOAD = '''
................................................................|
................................................................|
................................................................|
................................................................|
.............kkk...kkkk..................kkkk...kkk.............|
.............kkkkkkggggk................kggggkkkkkk.............|
...............kkkkkkkkgk..............kgkkkkkkkk...............|
..............kggookkkkkk..............kkkkkkooggk..............|
.............kggoookkookkkk..........kkkkookkoooggk.............|
............kgggoookkooogggk........kgggoookkooogggk............|
............kgggoookkooogggk........kgggoookkooogggk............|
............kgggoookkooogggk........kgggoookkooogggk............|
............kgggoookkooogggk........kgggoookkooogggk............|
............kgggoookkoooggk..........kggoookkooogggk............|
............kggggoooooogggkkkkkkkkkkkkgggooooooggggk............|
.............kggggggggggggggggggggggggggggggggggggk.............|
..............kggggggggggggggggggggggggggggggggggk..............|
...............kggggggggggggggggggggggggggggggggk...............|
.............kkgggggggggggLggggggggggLgggggggggggkk.............|
...........kkggggggggggggLgLggggggggLgLggggggggggggkk...........|
..........kgggLgggggggggggLggggggggggLgggggggggggLgggk..........|
.........kgggLgLgggggggggggkggggggggkgggggggggggLgLgggk.........|
........kgggggLggggggggggggggggggggggggggggggggggLgggggk........|
.......kggggggggggggggggggggggggggggggggggggggggggggggggk.......|
......kgggLggggggggggggggggggggggggggggggggggggggggggLgggk......|
.....kgggLkkggggggggggggggggggggggggggggggggggggggggkkLgggk.....|
.....kggggLgkkggggggggggggggggggggggggggggggggggggkkgLggggk.....|
....kgggggggggkkggggggggggggggggggggggggggggggggkkgggggggggk....|
....kgggggggggLkkggggggggggggggggggggggggggggggkkLgggggggggk....|
....kggggggggggLgkkggggggggYYYYYYYYYYggggggggkkgLggggggggggk....|
...kkgggLggggggggggkkkkkkkkkkkkkkkkkkkkkkkkkkggggggggggLgggkk...|
..kggggLgLgggggggggggggYYYYYYYYYYYYYYYYYYgggggggggggggLgLggggk..|
.kggggggLggggggggggggYYYYYYYYYYYYYYYYYYYYYYggggggggggggLggggggk.|
kgggggggggggggggggggYYYYYYYYYYYYYYYYYYYYYYYYgggggggggggggggggggk|
kgggggggggggggggggggYYYYYYYYYYYYYYYYYYYYYYYYgggggggggggggggggggk|
ggggLggggggggggggggYYYYYYddddddddddddddYYYYYYggggggggggggggLgggg|
gggLgLgggggggggggggYYYYYYYYYYYYYYYYYYYYYYYYYYgggggggggggggLgLggg|
ggggLggggggggggggggYYYYYYYYYYYYYYYYYYYYYYYYYYggggggggggggggLgggg|
gggggggggggggggggggYYYYYYYYYYYYYYYYYYYYYYYYYYggggggggggggggggggg|
ggggggggggggggggggggYYYYYddddddddddddddYYYYYgggggggggggggggggggg|
ggggggggggggggggggggYYYYYYYYYYYYYYYYYYYYYYYYgggggggggggggggggggg|
kggggggggggggkkggggggYYYYYYYYYYYYYYYYYYYYYYggggggkkggggggggggggk|
kggddddddddggk.kkggggggYYYYYYYYYYYYYYYYYYggggggkk.kggddddddddggk|
ddddddddddddddk.kgggggggYYYYYYYYYYYYYYYYgggggggk.kdddddddddddddd|
dddddddddddddddkddddddgkkggYYYYYYYYYYggkkgddddddkddddddddddddddd|
ddddddddddddddddddddddddkkkkkkkkkkkkkkkkdddddddddddddddddddddddd|
ddddddddddddddddddddddddk..............kdddddddddddddddddddddddd|
kkkdddkdddkkkkkkdddkddkk................kkddkdddkkkkkkdddkdddkkk|
'''
TOAD_SPR = '''
.
.
.
.
.
.
.
.
.
.
..................W.......................W.....................
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
......................p..................p......................
......................p..................p......................
......................p.................pp......................
.....................pp.........................................
.
.
.
.
.
.
.
.
.
.
.
.
.
'''
TOAD_SLOTS = {'g': 0x18, 'd': 0x08, 'L': 0x2B, 'Y': 0x37, 'o': 0x16}
TOAD_PALETTES = [(0x2B, 0x18, 0x08), (0x18, 0x08, 0x37), (0x2B, 0x18, 0x16), (0x2B, 0x18, 0x37)]
TOAD_SPR_SLOTS = {'p': 0x2B, 'W': 0x30}
TOAD_SPR_PALETTES = [(0x2B, 0x30)]
TOAD_SIZE = (64, 48)

PORTRAITS = {
    'ape': (APE, APE_SPR, APE_SLOTS, APE_PALETTES, APE_SPR_SLOTS, APE_SPR_PALETTES, APE_SIZE),
    'tiger': (TIGER, TIGER_SPR, TIGER_SLOTS, TIGER_PALETTES, TIGER_SPR_SLOTS, TIGER_SPR_PALETTES, TIGER_SIZE),
    'lion': (LION, LION_SPR, LION_SLOTS, LION_PALETTES, LION_SPR_SLOTS, LION_SPR_PALETTES, LION_SIZE),
    'jiangshi': (JIANGSHI, JIANGSHI_SPR, JIANGSHI_SLOTS, JIANGSHI_PALETTES, JIANGSHI_SPR_SLOTS, JIANGSHI_SPR_PALETTES, JIANGSHI_SIZE),
    'shanxiao': (SHANXIAO, SHANXIAO_SPR, SHANXIAO_SLOTS, SHANXIAO_PALETTES, SHANXIAO_SPR_SLOTS, SHANXIAO_SPR_PALETTES, SHANXIAO_SIZE),
    'fox': (FOX, FOX_SPR, FOX_SLOTS, FOX_PALETTES, FOX_SPR_SLOTS, FOX_SPR_PALETTES, FOX_SIZE),
    'jiao': (JIAO, JIAO_SPR, JIAO_SLOTS, JIAO_PALETTES, JIAO_SPR_SLOTS, JIAO_SPR_PALETTES, JIAO_SIZE),
    'crow': (CROW, CROW_SPR, CROW_SLOTS, CROW_PALETTES, CROW_SPR_SLOTS, CROW_SPR_PALETTES, CROW_SIZE),
    'toad': (TOAD, TOAD_SPR, TOAD_SLOTS, TOAD_PALETTES, TOAD_SPR_SLOTS, TOAD_SPR_PALETTES, TOAD_SIZE),
}


# ---------------------------------------------------------------- field sprites (16 wide; see nes_sprites.py)
def G(t, h=24):
    rows = [ln.strip() for ln in t.strip('\n').split('\n')]
    rows = ['.' * 16] * (h - len(rows)) + rows       # short figures stand on the bottom row
    for r in rows:
        if len(r) != 16:
            raise ValueError('sprite row is %d wide: %s' % (len(r), r))
    if len(rows) != h:
        raise ValueError('sprite has %d rows' % len(rows))
    return rows


SPRITES = {}

# White Ape of the Broken Cliff
SPRITES['ape'] = dict(pal=dict(k=0x0F, W=0x30, G=0x00), move=[G('''
.....kkkkkk.....
....kWWWWWWk....
...kWkGGGGkWk...
...kWGkGGkGWk...
..kkWGGGGGGWkk..
.kWWWkGkkGkWWWk.
kWWWkkGGGGkkWWWk
kWWkWWkkkkWWkWWk
kWWkWGGGGGGWkWWk
kWWkWGGGGGGWkWWk
kWWkWWGGGGWWkWWk
kGGkWWWWWWWWkGGk
kGGkWWWkkWWWkGGk
.kk.kWWk.kWWk.kk
....kGGk.kGGk...
.....kk...kk....
''', 16), G('''
................
.....kkkkkk.....
....kWWWWWWk....
...kWkGGGGkWk...
...kWGkGGkGWk...
.kkkWGGGGGGWkkk.
kWWWWkGkkGkWWWWk
kWWkkkGGGGkkkWWk
kWWkWWkkkkWWkWWk
kWWkWGGGGGGWkWWk
kWWkWGGGGGGWkWWk
kGGkWWGGGGWWkGGk
kGGkWWWWWWWWkGGk
.kk.kWWWkWWWk.kk
....kGGGkGGGk...
.....kkk.kkk....
''', 16)])

# White-Browed Mountain Tiger
SPRITES['tiger'] = dict(pal=dict(k=0x0F, O=0x27, c=0x17), move=[G('''
.kk.........kk..
kOOk.kkkkk.kOOk.
kOOkkcckcckkOOk.
.kcccckkccccck..
.kckkcccckkcck..
.kcOkkcckkOcck..
.kcOOOkkOOOcck..
..kcOkkkkOcck...
...kcOOOOccck...
..kcccccccccck..
.kcckcccccckcck.
.kccckcccckccck.
.kccccccccccccck
kOOkcckkkckcOOOk
kOOOkkk..kkkOOOk
.kkkk.....kkkkk.
''', 16), G('''
................
.kk.........kk..
kOOk.kkkkk.kOOk.
kOOkkcckcckkOOk.
.kcccckkccccck..
.kckkcccckkcck..
.kcOkkcckkOcck..
.kcOOOkkOOOcck..
..kcOkkkkOcck...
..kccOOOOcccck..
.kcckcccccckcck.
.kccckcccckccck.
kccccccccccccck.
kOOOkcckkkcOOOk.
kOOOkk....kkOOOk
.kkkk......kkkk.
''', 16)])

# Stone Guardian Lion
SPRITES['lion'] = dict(pal=dict(k=0x0F, S=0x10, c=0x00), move=[G('''
....kk.kk.kk....
..kkSSkSSkSSkk..
.kSSkkkkkkkkSSk.
.kSkSSSSSSSSkSk.
kSkSkkSSSSkkSkSk
kSkSSSSccSSSSkSk
kSkSkkkkkkkkSkSk
.kSkkSkSSkSkkSk.
.kSSkkkkkkkkSSk.
..kkSSSSSSSSkk..
..kSSkSSSSkSSk..
..kSSkSSSSkSSk..
.kSSSkSSSSkSSSk.
.kkkkkkkkkkkkkk.
.kcccccccccccck.
.kkkkkkkkkkkkkk.
''', 16), G('''
....kk.kk.kk....
..kkSSkSSkSSkk..
.kSSkkkkkkkkSSk.
.kSkSSSSSSSSkSk.
kSkSkkSSSSkkSkSk
kSkSSSSccSSSSkSk
kSkSkkkkkkkkSkSk
.kSkkkkkkkkkkSk.
.kSSkSkSSkSkSSk.
..kkSSSSSSSSkk..
..kSSkSSSSkSSk..
..kSSkSSSSkSSk..
.kSSSkSSSSkSSSk.
.kkkkkkkkkkkkkk.
.kcccccccccccck.
.kkkkkkkkkkkkkk.
''', 16)])

# Talisman Jiangshi
SPRITES['jiangshi'] = dict(pal=dict(k=0x0F, S=0x3A, c=0x03), move=[G('''
................
.......kk.......
.....kkkkkk.....
....kcccccck....
..kkkkkkkkkkkk..
...kSSkSSkSSk...
...kSkkSSkkSk...
...kSSkSkkSSk...
...kSSkSSkSSk...
...kSSkkkkSSk...
....kSkSSkSk....
.....kkkkkk.....
kkkkkkcSSckkkkkk
SSccccccccccccSS
kkkkkkcccckkkkkk
.....kcccck.....
....kcSSSSck....
....kcSkkSck....
....kcSSSSck....
....kcccccck....
....kcccccck....
....kccckcck....
....kkkkkkkk....
....kkk..kkk....
''', 24), G('''
....kcccccck....
..kkkkkkkkkkkk..
...kSSkSSkSSk...
...kSkkSSkkSk...
...kSSkSkkSSk...
...kSSkSSkSSk...
...kSSkkkkSSk...
....kSkSSkSk....
.....kkkkkk.....
kkkkkkcSSckkkkkk
SSccccccccccccSS
kkkkkkcccckkkkkk
.....kcccck.....
....kcSSSSck....
....kcSkkSck....
....kcSSSSck....
....kcccccck....
....kcccccck....
....kccckcck....
....kkkkkkkk....
....kkk..kkk....
................
................
................
''', 24)])

# Shanxiao, the One-Footed Mountain Imp
SPRITES['shanxiao'] = dict(pal=dict(k=0x0F, g=0x28, c=0x17), move=[G('''
...kgggggggk....
..kgkkkkkkkgk...
.kgkcckkccckgk..
.kgkkgkkgkkkgk..
.kgkcckkcckkgk..
..kgkckkckkgk...
...kkkkkkkkk....
..kcccccccccck..
.kcckcccccckcck.
kcck.kcccck.kcck
kcck.kcccck.kcck
.kk..kkcckk..kk.
......kcck......
.....kccccck....
....kkkkkkkkk...
................
''', 16), G('''
................
...kgggggggk....
..kgkkkkkkkgk...
.kgkcckkccckgk..
.kgkkgkkgkkkgk..
.kgkcckkcckkgk..
..kgkckkckkgk...
...kkkkkkkkk....
..kcccccccccck..
.kcckcccccckcck.
kcck.kcccck.kcck
kcck.kcccck.kcck
.kk..kkcckk..kk.
.....kccccck....
....kkkkkkkkk...
................
''', 16)])

# Nine-Tailed Fox Spirit
SPRITES['fox'] = dict(pal=dict(k=0x0F, W=0x30, c=0x28), move=[G('''
.k.......k......
kck.....kck...kk
kcckkkkkcck..kWk
kccccccccck.kWck
kckWcccWckk.kcck
kcckcccckck.kcck
.kccWWWcck..kck.
..kkWkWkk..kcck.
...kWWWk..kcck..
..kcWWWck.kck...
..kcWWWcckcck...
..kcWWWccccck...
..kckWkckcck....
..kckWkckkk.....
..kWkkkWk.......
...k...k........
''', 16), G('''
.k.......k......
kck.....kck.....
kcckkkkkcck..kk.
kccccccccck.kWck
kckWcccWckk.kcck
kcckcccckck.kcck
.kccWWWcck..kck.
..kkWkWkk..kcck.
...kWWWk...kck..
..kcWWWck.kcck..
..kcWWWcckcck...
..kcWWWccccck...
..kckWkckcck....
..kckWkckkk.....
..kWkkkWk.......
...k...k........
''', 16)])

# River Jiao
SPRITES['jiao'] = dict(pal=dict(k=0x0F, T=0x2C, c=0x1C), move=[G('''
.....k....k.....
....kTk..kTk....
....kkkkkkkk....
...kcccccccck...
..kcTkccccTkck..
..kcckccccckck..
...kcccccccck...
....kckkkkck....
.....kcTTck.....
.kk..kcTTck..kk.
kcck.kcTTck.kcck
kcck.kcTTck.kcck
kTTTTTTTTTTTTTTk
TcTTTcTTTTcTTTcT
.TTTTTTTTTTTTTT.
................
''', 16), G('''
................
.....k....k.....
....kTk..kTk....
....kkkkkkkk....
...kcccccccck...
..kcTkccccTkck..
..kcckccccckck..
...kcccccccck...
....kckkkkck....
.kk..kcTTck..kk.
kcck.kcTTck.kcck
kcck.kcTTck.kcck
TTTTTTTTTTTTTTTT
cTTTcTTTTcTTTcTT
.TTTTTTTTTTTTTT.
................
''', 16)])

# Three-Legged Fire Crow
SPRITES['crow'] = dict(pal=dict(k=0x0F, d=0x06, o=0x27), move=[G('''
oo............oo
odo..........odo
oddo..kkkk..oddo
odddokddddkoddd.
.oddddkookdddd..
..ooddddddddo...
...oddkddkddo...
....odddddddo...
.....kddddk.....
.....kddddk.....
......kddk......
.....ooddoo.....
....o.oooo.o....
......k.kk......
.....k..k.k.....
................
''', 16), G('''
................
................
......kkkk......
.....kddddk.....
.....kookdk.....
..oooddddddooo..
oodddkddkdddddoo
odddddddddddddo.
oddddkddddkdddo.
.oo..kddddk..oo.
......kddk......
.....ooddoo.....
....o.oooo.o....
......k.kk......
.....k..k.k.....
................
''', 16)])

# Venom Toad of the Marsh
SPRITES['toad'] = dict(pal=dict(k=0x0F, L=0x2B, c=0x18), move=[G('''
................
................
................
..kkk......kkk..
.kLkLk....kLkLk.
.kLLLkkkkkkLLLk.
kcccLcccccLccck.
kcccccccccccccck
kckkkkkkkkkkkkck
kcccLLLLLLLLccck
kccLLLLLLLLLLcck
.kccLLLLLLLLcck.
kcckkcccccckkcck
kcck.kkkkkk.kcck
.kk..........kk.
................
''', 16), G('''
................
................
................
................
..kkk......kkk..
.kLkLk....kLkLk.
.kLLLkkkkkkLLLk.
kcccLcccccLccck.
kcccccccccccccck
kckkkkkkkkkkkkck
kccLLLLLLLLLLcck
.kccLLLLLLLLcck.
kcckkcccccckkcck
kcck.kkkkkk.kcck
.kk..........kk.
................
''', 16)])
