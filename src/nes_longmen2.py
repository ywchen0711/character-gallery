"""龍門武林 (Longmen Wulin), second group: the Black Wind Fort bandits and the master of the Netherworld Sect.

Same rules and helpers as nes_longmen.py (48x56 portraits, 16x24 field sprites, 2C02 colours, checked by nes.Pic.check()).
nes_longmen.py merges PORTRAITS, SPRITES and HEIGHTS from here.
"""

# ---------------------------------------------------------------- 黑熊 Hei Xiong, Black Bear
# chief of the Black Wind Fort: wild black hair, a full black beard, a bear-fur mantle over his right
# shoulder, a grey jerkin with a black belt and iron buckle, the spiked club (狼牙棒) held upright
HEIXIONG = '''
.......i........................................|
.......i.............k....k....k................|
......kwk...........khk..khk..khk..k............|
....kkwddk........k.khhkkhhhkkhhhkkhk...........|
...iiwddddk.......khkhhhhhhhhhhhhhhhhkk.........|
...kwdddiddk.....khhhhhhhhhhhhhhhhhhhhhk........|
...kwddddddii...khhhhhhhhhhhhhhhhhhhhhhhk.......|
..kwdiddddddk..khhhhhkhhhhhhhhhhhkhhhhhhk.......|
.iiwddddddddk..khhhhkhhhhhhhhhhhhhkhhhhhk.......|
..kwddddidddk..khhhkhhhhhhhhhhhhhhhkhhhhk.......|
..kwddddddddii.khhhkSSSSSSSSSSSSSSSkhhhhk.......|
..kwdiddddddk..khhkSSSSSSSSSSSSSSSSSkhhhk.......|
.iiwddddddddk..khhSSSSSSSSSSSSSSSSSSsshhk.......|
..kwddddidddk..khhSkkkkkSSSSSSkkkkksshhhk.......|
..kwddddddddii.khhSSSkkkkSSSSkkkkSsssshhk.......|
..kwdiddddddk..kSSSSSSSSSSSSSSSSSSSsssssk.......|
.iiwddddddddk..kSsSSSSkkSSSSSSkkSSSsssssk.......|
..kwddddidddk..kSsSSSSkkSSSSSSkkSSSsssssk.......|
..kwddddddddii.kSSSSSSSSSSssSSSSSSSsssssk.......|
..kwdiddddddk..kSSSSSSSSsSSsSSSSSSssssk.........|
..iiwddddddk....kSSSSSkkkkkkkkkkksssk...........|
...kwddddddk...khkhhkkhhhhhhhhhhhkhkhhkhk.......|
....kwddddii...kkhhkkhhhkkkkkkhhhhkhhkhhk.......|
.....kwddk.....kkhhkhhkhkSSSSkhkhhkhhkhhk.......|
.....kwdk......khhkhhkhhkhhkhhkhhkhhkhhkk.......|
.....kwdk......khhkhhkhhkhhkhhkhhkhhkhhkk.......|
.....kiik......khkhhkhhkhhkhhkhhkhhkhhkhk.......|
.....kwdk.......kkhhkhhkhhkhhkhhkhhkhhkk........|
.....kiik.......khhkhhkhhkhhkhhkhhkhhkhk........|
.....kwdk........khkhhkhhkhhkhhkhhkhhkk.........|
.....kwdk........kkhhkhhkhhkhhkhhkhhkhk.........|
.....kwkkk.k......khhkhhkhhkhhkhhkhhkk..........|
.....kwkkkkkk.....khkhhkhhkhhkhhkhhkhk..........|
....kkdddkdddkd....kkhhkhhkhhkhhkhhkk...........|
..kddwdddwdddwdd..kSkhkhhkhhkhhkhhkk............|
.kdkwddkwddkwddk.kGkSkkhhkhhkhhkhhkk............|
ddkkdddkdddkdddkkGGGkSSkkhhkhhkhkGGGkkkk........|
dddwdddwdddwdddwkGGGGkSSSkhkhhkGGGGGGGGGkkk.....|
dkwddkwddkwddkwdkGGGGGkSSSSkSkGGGGGGGGGGGGGkk...|
dkkddkdddkdddkddkGGGGGGkSSSSkGGGGGGGGGGGGGGGGk..|
dwdddwdddwdddwddkGGGGGGGkSSkGGGGGGGGGGGGGGGGGGk.|
wkdkwddkwddkwddkkGGGGGGGGkkGGGGGGGGGGGGGGkGGGGGk|
ddkkdddkdddkdddkkGGGGGGGGkGGGGGGGGGGGGGGGkGGGGGG|
dddwdddwdddwdddwkGGGGGGGGkGGGGGGGGGGGGGGGkGGGGGG|
dkwddkwddkwddkwdkGGGGGGGkGGGGGGGGGGGGGGGGGkGGGGG|
dkkddkdddkdddkddkGGGGGGGkGGGGGGGGGGGGGGGGGkGGGGG|
dwdddwdddwdddwddkGGGGGGkGGGGGGGGGGGGGGGGGGkGGGGG|
wkdkwddkwddkwddkkGGGGGGkGGGGGGGGGGGGGGGGGGkGGGGG|
ddkkdddkdddkdddkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk|
dddwdddwdddwdddwhhhhhhhhhhhhkkkkkhhhhhhhhhhhhhhh|
dkwddkwddkwddkwdhhhhhhhhhhhkGGGGGkhhhhhhhhhhhhhh|
dkkddkdddkdddkddhhhhhhhhhhhkGkkkGkhhhhhhhhhhhhhh|
dwdddwdddwdddwddhhhhhhhhhhhkGGGGGkhhhhhhhhhhhhhh|
wkdkwddkwddkwddkhhhhhhhhhhhhkkkkkhhhhhhhhhhhhhhh|
ddkkdddkdddkdddkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk|
dddwdddwdddwdddwGGGGGGGGkGGGGGGGGGGGGGGGGGkGGGGG|
'''
HEIXIONG_SPR = '''
.
'''
HEIXIONG_SLOTS = {'S': 0x37, 's': 0x27, 'h': 0x0C, 'w': 0x18, 'd': 0x08, 'i': 0x10, 'G': 0x00}
HEIXIONG_PALETTES = [(0x37, 0x27, 0x0C), (0x18, 0x08, 0x10), (0x37, 0x0C, 0x00)]
HEIXIONG_SPR_SLOTS = {}
HEIXIONG_SPR_PALETTES = []

# ---------------------------------------------------------------- 刀疤 Dao Ba, Scar
# the fort's second: shaved sides and a topknot, a long scar across his face (pink sprite
# overlay), a rust jacket open at the chest, the broad dao (大刀) held upright in his left hand
DAOBA = '''
................................................|
...................................k............|
...................................kk...........|
...................................kGk..........|
................kkkk...............kGWk.........|
...............khhhhk..............kGWWk........|
...............khhkhk..............kGGWWk.......|
................kkkk...............kGGWWWk......|
..............kkkhhkkk.............kGGGWWWk.....|
............kkhhhhhhhhkk...........kGGGGWWWk....|
...........khhhhhhhhhhhhk..........kGkGGGWWk....|
..........kShhhhhhhhhhhhsk.........kGkGGGWWk....|
.........kShShhhhhhhhhhshsk........kGkGGGWWk....|
........kShSShkhhhhhhkhshsk........kGkGGGWWk....|
........kSSSSSkkkkkkkkSSsssk.......kGkGGGWWk....|
........kSSSSSSSSSSSSSSSsssk.......kGkGGGWWk....|
........kSkkkkSSSSSSkkkkSssk.......kGkGGGWWk....|
........kSSkkSSSSSSSSkkSSssk.......kGkGGGWWk....|
.......kSSSSkkSSSSSSkkSSssssk......kGkGGGWWk....|
.......kSSSSkkSSSSSSkkSSssssk......kGkGGGWWk....|
.......kSSSSSSSSSsSSSSSSssssk......kGkGGGWWk....|
........kSSSSSSSSsSSSSSsssk........kGkGGGWWk....|
........kSSSSSSSssSSSSSsssk........kGkGGGWWk....|
........kSSSSSSkssskSSSsssk........kGGGGGWWk....|
........kSSSSSSSSSSSSSSsssk........kGGGGGWWk....|
........kSSSSSkkkkkkSSSsssk........kGGGGGWWk....|
........kSSSSSSSSSSSSSssssk........kGGGGGWWk....|
.........kSSSSSSSSSSSSsssk.........kGGGGGWWk....|
..........kSSSSSSSSSSsssk..........kGGGGGWWk....|
...........kkSSSSSSsskksk..........kkkkkkkkk....|
.............kkkkkkkksssk.........kWWWWWWWWWk...|
.............kSSSSSSsssskk........kkkkkkkkkkk...|
.......kkkkkkkSSSSSSwwwkdwkkkk......kwdwk.......|
....kkkdwwwwkkSSSSSSwwwkdddwwwkk....kdwdk.......|
...kSSkddwwkdkkSSSSwwwkddddddwwkk...kwdwk.......|
..kSSSkdddwkddkkSSSwwkddddddddwSSk..kdwdk.......|
.kSSSSkdddwkdddkkSSwkdddddddddwSSSk.kdwdk.......|
.kSSSSkddddkddddkkSkddddddddddwkSSSkkwdwk.......|
kSSSSSkddddkdddddkkkddddddddddwkkSSSkdwdk.......|
kSSSSSkddddkddddddkkdddddddddwk..kSSkwdwk.......|
kSSSSSkddddkddddddkddddddddddwk..kkkkkkkkk......|
kSSSSkddddkdddddddkddddddddddwk..SSSSSSSSSk.....|
kSSSSkddddkdddddddkddddddddddwk..SSkSSkSSkSk....|
kSSSSkddddkdddddddkdddddddddwk...SSSSSSSSSSk....|
kSSSSkddddkdddddddkdddddddddwk...kSSSSSSSSk.....|
kSSSSkddddkkkkkkkkkkkkkkkkkkwk....kkkkkkkk......|
kSSSSkdddkwwwwwwwwwwwwwwwwwwwk......kwdwk.......|
kSSSSkdddkkkkkkkkkkkkkkkkkkkkk......kdwdk.......|
kSSSSkddddkdddddddkddddddddwk.......kwdwk.......|
kSSSSkddddkdddddddkddddddddwk.......kkkkk.......|
kSSSSkddddkdddddddkddddddddwk.......kwwwk.......|
kSSSSkddddkdddddddkddddddddwk........kkk........|
kSSSSkddddkdddddddkddddddddwk...................|
kSSSSkddddkdddddddkddddddddwk...................|
kSSSSkddddkdddddddkddddddddwk...................|
kSSSSkddddkdddddddkddddddddwk...................|
'''
DAOBA_SPR = '''
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
9:rr
10:r
11:rr
.
.
14:r
15:rr
16:r
17:rr
18:r
19:rr
20:r
.
22:r
23:rr
'''
DAOBA_SLOTS = {'S': 0x37, 's': 0x27, 'h': 0x0C, 'w': 0x17, 'd': 0x07, 'G': 0x10, 'W': 0x30}
DAOBA_PALETTES = [(0x37, 0x27, 0x0C), (0x30, 0x10, 0x00), (0x37, 0x17, 0x07)]
DAOBA_SPR_SLOTS = {'r': 0x26}
DAOBA_SPR_PALETTES = [(0x26,)]

# ---------------------------------------------------------------- 瘦猴 Shou Hou, Skinny Monkey
# the lackey: thin, spiky hair, sly eyes and a buck-toothed grin (teeth are
# sprites), patched brown clothes, a short knife held up by his chest (knife blade is sprites)
SHOUHOU = '''
................................................|
................................................|
................................................|
.....................k...k......................|
.................k..khk.khk..k..................|
.................kk.khhkhhk.kk..................|
.................khkkhhhhhhkhk.k................|
................kkhhhhhhhhhhhhkhk...............|
................khhhhhhhhhhhhhhhk...............|
...............khhhhhhkhhhhhkhhhhk..............|
...............khhhkhhhkhhhkhhhhhk..............|
...............khhkSShhkkhhhSkhhhk..............|
...............khkSSSSShhkSSSSkhhk..............|
..............kkhkSSSSSSSSSSSSskhk..............|
..............kSkSSSSSSSSSSSSSsskk..............|
..............kSkSkkkSSSSSSkkksSkSk.............|
..............kSSSSSSkSSSSkSSSsSsk..............|
..............kSkSSkkkkSSkkkkSssk...............|
...............kkSSSSkkSSSSSkksk................|
................kSSSSSSSSSSSSssk................|
................kSSSSSSSsSSSSssk................|
................kSSSSSSSsSSSSssk................|
................kSSSSSSksskSSssk................|
................kSkSSSSSSSSSSSsk................|
................kSSkkkkkkkkkkSsk................|
................kSSSSSkSSkSSSssk................|
.................kSSSSSSSSSSssk.................|
.................kSSSSSSSSSssk..................|
..................kSSSSSSSssk...................|
...................kkSSSSskk....................|
.....................kkkkk......................|
.....................kSSSSsk....................|
.....................kSSSSck....................|
.....................kSSSScd....................|
..................kkkkSSSScckkk.................|
...............kkkcdddkSSSckcddkk...............|
.............kkcdddddddkSckcdddddkk.............|
...........kkcddddddddddkkcdddddddddkk..........|
..........kcdddddddddddddkcddddddddddddk........|
........kkkkkkkdddddddddkkcddddddddddddddk......|
........kGGGGGkdddddddddkcddddkkkkkkdddddk......|
........kGGGGGkcddddddkcdddddkSSSSSSkcdddk......|
.......kkGGGGGkcdddddkcddddddkkkkkSSkcddddk.....|
.......kkGGGGGkcddddkcdddddddkSSSSSSkcddddk.....|
.......kkkkkkkkcddddkcdddddddkkkkkSSkkcdddk.....|
......kcdddddkcdddddkcdddddddkSSSSSkdkcddddk....|
......kcdddddkcdddddkcddddddddkkkkkddkcddddk....|
......kcdddddkcdddddkcddddddddddddddddkcdddk....|
......kcdddddkcdddddkkkkkkkkkkkkkkkkkkkcdddk....|
......kcdddddkcdddddkcdddddddddddddddddkcddk....|
......kcdddddkcddddkcddddddddddddkkkkkkkcddk....|
......kcdddddkcddddkcddddddddddddkGGGGGkcddk....|
......kcdddddkcddddkcddddddddddddkGGGGGkcddk....|
......kcdddddkcddddkcddddddddddddkGGGGGkcddk....|
.................................kGGGGGk........|
.................................kkkkkkk........|
'''
SHOUHOU_SPR = '''
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
22:WW.WW
.
.
.
.
.
.
32:W
31:WG
31:WG
31:WG
31:WG
31:WG
31:WG
'''
SHOUHOU_SLOTS = {'S': 0x37, 's': 0x27, 'h': 0x0C, 'c': 0x18, 'd': 0x08, 'G': 0x00}
SHOUHOU_PALETTES = [(0x37, 0x27, 0x0C), (0x18, 0x08, 0x00), (0x37, 0x18, 0x08)]
SHOUHOU_SPR_SLOTS = {'W': 0x30, 'G': 0x10}
SHOUHOU_SPR_PALETTES = [(0x30, 0x10)]

# ---------------------------------------------------------------- 屠千秋 Tu Qianqiu
# master of the Netherworld Sect: gaunt and pale, long black hair with a white streak
# (sprites), a silver ghost half-mask, dark violet robe with a bone-bead necklace, the bone fan (白骨扇)
TUQIANQIU = '''
................................................|
................................................|
................................................|
....................kkkkkkkk....................|
.................kkkhhhhhhhhkkk.................|
...............kkhhhhhhhhkhhhhhhkk..............|
..............khhhhhhhhhhkhhhhhhhhk.............|
.............khhhhhhhhhhkkhhhhhhhhhk............|
............khhhhhhhhhhkSSkhhhhhhhhhk...........|
............khhhhhhhhhkSSSSkhhhhhhhhk...........|
...........khhhhhhhhhkSSSSSSkhhhhhhhhk..........|
...........khhhhhhhhkSSSSSSSSkhhhhhhhk..........|
...........khhhhhhhkSSSSkkkkkkkhhhhhhk..........|
...........khhhhhhkSSSSSkGGGGGkkhhhhhk..........|
...........khhhhhkSSSSSSkGGGGGGGkhhhhk..........|
...........khhhhkSkkSSSSkGGGGGGGGkhhhk..........|
...........khhhhkSSSkkkSkGkkkkGGGkhhhk..........|
...........khhhhkSSSSSSSkGGGGGGGGkhhhk..........|
...........khhhhkSSSSkkSkGGkkkGGGkhhhk..........|
...........khhhhkSSSSkkSkGGkkkGGGkhhhk..........|
...........khhhhkSSSSSSSkGGGGGGGGkhhhk..........|
...........khhhhkGSSSSSSkGGGGGGGGkhhhk..........|
...........khhhhkGSSSSSSkGGGGGGGkkhhhk..........|
...........khhhhkSGSSSSSkGGGGGGkSkhhhkkkkkkk....|
...........khhhhhkGSSSSSkGGGGGkGkhkkkGGGSGGGkkk.|
...........khhhhhkSSSSSkkGGGGkSSkkGSSGGGSGGGSSGk|
...........khhhhhhkSSSSSSkkkkSSkGGGSShhhShhhSSGG|
...........khhhhhhhkSSSSSSSSSSkSGGGhShhhShhhShGG|
...........khhhhhhhhkSSSSSSSSkhkShhhSShhShhSShhh|
...........khhhhhhhhhkkkkkkkkhhhkShhSShhShhSShhS|
...........khhhhhhhhhkGSSSSSkhhhhkShhShhShhShhSk|
...........khhhhhhhhkkGSSSSSkkhhhhSShSShShSShSS.|
...........khhhhhhhkkSSSSSSkkhhhhhhShhShShShhS..|
...........khhhhhhkSSSSSSSSSkkhhhhhhShShShShS...|
......kkkkkhhhhhkkkSSSSSSSSkkkhhhhhhkkkkkkSS....|
....kkddddkhhhhhkdkkSSSSSSkkdkhhhhhkSSSSSSk.....|
..kkddddddkhhhhhSkdkkSSSSkkddkhSkhhkSkSkSSkkk...|
.kddddddddkhhhhhkdddkkSSkkdddkhhhhhkSSSSSSkdkk..|
kdddddddddkhhhhhSkdddkkkkddddkhSkhhkkSSSSkdddk..|
kddddddddkhhhhhkdSkSkkkkkdddSkSkhhhhkkddkkdddddk|
kcdddddddkhhhhhkddddSkSkSSkSkdkhhhhhkddddddddddd|
kcdddddddkhhhhkcddddddkSSddddddkhhhhkddddddddddd|
kcdddddddkhhhhkcddddddkSSddddddkhhhhkddddddddddd|
kcdddddddkhhhhkcddddddkkkddddddkhhhhkddddddddddd|
kcddddddkhhhhkcdddddddkkddddddddkhhhhkdddddddddd|
kcddddddkhhhhkcdddddddkkddddddddkhhhhkdddddddddd|
kcddddddkhhhkcddddddddkkdddddddddkhhhkdddddddddd|
kcddddddkhhhkcddddddddkkdddddddddkhhhkdddddddddd|
kcddddddkhhkcdddddddddkkcdddddddddkhhkcddddddddd|
kcddddddkhhkcdddddddddkkcdddddddddkhhkcddddddddd|
kcddddddkkkcddddddddddkkcddddddddddkkkcddddddddd|
kcdddddddddddddddddddkkkkcdddddddddddddddddddddd|
kcdddddddddddddddddddkkkkcdddddddddddddddddddddd|
................................................|
................................................|
................................................|
'''
TUQIANQIU_SPR = '''
.
.
.
.
.
.
16:W
16:W
14:W
14:W
14:W
14:W
13:W
13:W............WWW
13:W............W
13:W
13:W..................W
13:W.................W
13:W
13:W
13:W
13:W
13:W
13:W
13:W
13:W
13:W
13:W
13:W
13:W
12:W
12:W
12:W
12:W
12:W
12:W
12:W
12:W
12:W
12:W
12:W
12:W
12:W
12:W
12:W
12:W
'''
TUQIANQIU_SLOTS = {'S': 0x36, 'G': 0x10, 'h': 0x0C, 'd': 0x04, 'c': 0x13}
TUQIANQIU_PALETTES = [(0x36, 0x10, 0x0C), (0x36, 0x04, 0x0C), (0x04, 0x13, 0x0C), (0x36, 0x04, 0x13)]
TUQIANQIU_SPR_SLOTS = {'W': 0x30}
TUQIANQIU_SPR_PALETTES = [(0x30,)]

PORTRAITS = {
    'heixiong': (HEIXIONG, HEIXIONG_SPR, HEIXIONG_SLOTS, HEIXIONG_PALETTES, HEIXIONG_SPR_SLOTS, HEIXIONG_SPR_PALETTES),
    'daoba': (DAOBA, DAOBA_SPR, DAOBA_SLOTS, DAOBA_PALETTES, DAOBA_SPR_SLOTS, DAOBA_SPR_PALETTES),
    'shouhou': (SHOUHOU, SHOUHOU_SPR, SHOUHOU_SLOTS, SHOUHOU_PALETTES, SHOUHOU_SPR_SLOTS, SHOUHOU_SPR_PALETTES),
    'tuqianqiu': (TUQIANQIU, TUQIANQIU_SPR, TUQIANQIU_SLOTS, TUQIANQIU_PALETTES, TUQIANQIU_SPR_SLOTS, TUQIANQIU_SPR_PALETTES),
}


# ---------------------------------------------------------------- field sprites (16x24; see nes_sprites.py)
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
# 黑熊: wild black hair and a full black beard, bear fur over his right shoulder, the spiked club in his fist
SPRITES['heixiong'] = dict(pal=dict(k=0x0F, S=0x37, c=0x18), front=G('''
.kk.............
kcck...k.kk.k...
kcck..kkkkkkkk..
kcck.kkkkkkkkkk.
.kk..kSSSSSSSSk.
.ck..kSkkSSkkSk.
.ck..kSSkSSkSSk.
.ck..kSSSSSSSSk.
.ck..kkSkkkkSkk.
.ck..kkkkSSkkkk.
.ck.kkkkkkkkkkkk
.ck.kckckkkkkcck
.ckkckckckkkcccc
kSSkkckckcckcccc
kSSkckckkcckcccc
.ckkkckckcckccSS
.ck.kkkkckkkkcSS
.ck.kkkkkkkkkkk.
.ck..kcccckccck.
.ck..kcccckccck.
.ck..kcccckccck.
.kk..kkkkk.kkkk.
.....kkkkk.kkkk.
.....kkkkk.kkkkk
'''), side=G('''
...........kk...
..........kcck..
....k.kk..kcck..
...kkkkkkkkcck..
..kkkkkkkkkkk...
..kkkkkSSSSSk...
..kkkkSkkkSSk...
..kkkkSSSkSSSk..
..kkkkSSSSSSk...
..kkkkkkkkSSk...
..kkkkkkkkkkk...
..ckckkkkkkkk...
.ckckckkkkck....
.kckckcccckSSk..
.ckckcccccckSSk.
.kckcccckcckck..
.ckkkkkkkkkk.k..
..kkcccccck..k..
...kcccccccck...
...kcccckccccck.
..kkkkkk..kkkkk.
.kkkkkk....kkkk.
.kkkkk.....kkkk.
................
'''), side2=G('''
................
...........kk...
..........kcck..
....k.kk..kcck..
...kkkkkkkkcck..
..kkkkkkkkkkk...
..kkkkkSSSSSk...
..kkkkSkkkSSk...
..kkkkSSSkSSSk..
..kkkkSSSSSSk...
..kkkkkkkkSSk...
..kkkkkkkkkkk...
..ckckkkkkkkk...
.ckckckkkkck....
.kckckcccckSSk..
.ckckcccccckSSk.
.kckcccckcckck..
.ckkkkkkkkkk.k..
..kkcccccck..k..
...kcccccck.....
...kcccccck.....
....kkkkkkk.....
....kkkkkkk.....
................
'''))

# 刀疤: shaved sides and a topknot, a scar, a rust jacket open on the chest, the broad dao held upright
SPRITES['daoba'] = dict(pal=dict(k=0x0F, S=0x37, c=0x17), front=G('''
......kk.....k..
.....kkkk...kSk.
......kk....kSk.
....kkkkkk..kSk.
...kSkkkkSk.kSk.
...kSSSSSSk.kSk.
...kSkkSkkk.kSk.
...kSSkSSkk.kSk.
...kSSSkSSk.kSk.
...kSSkkkSk.kSk.
....kSSSSk..kSk.
.....kSSk...kkk.
..kkkcSSckkkcck.
.kcccckSkcckSSk.
.kcccccckcckSSk.
.kSSkcccckcckk..
.kSSkcccckcck...
..kkkkkkkkkkk...
...kcccckcccck..
...kcccckcccck..
...kcccckcccck..
...kkkkk.kkkkk..
...kkkkk..kkk...
.........kkkk...
'''), side=G('''
......kk.....k..
.....kkkk...kSk.
......kk....kSk.
....kkkkkkk.kSk.
...kkkkSSSSkkSk.
...kkkSSSSSkkSk.
...kkkSkkSkkkSk.
...kkkkSSkSSkSk.
...kkkSSSSSkkSk.
...kkkSSkkSkkSk.
....kkSSSSk.kSk.
.....kkSSk..kkk.
....kcccSck.kSk.
...kccccckckSk..
...kcccccckSSk..
...kccccckkSSk..
...kkkkkkkkkk...
...kcccccck.....
...kcccccck.....
....kccccccck...
...kccccccccck..
..kkkkk..kkkkk..
.kkkkk....kkkkk.
................
'''), side2=G('''
.............k..
......kk....kSk.
.....kkkk...kSk.
......kk....kSk.
....kkkkkkk.kSk.
...kkkkSSSSkkSk.
...kkkSSSSSkkSk.
...kkkSkkSkkkSk.
...kkkkSSkSSkSk.
...kkkSSSSSkkSk.
...kkkSSkkSkkSk.
....kkSSSSk.kSk.
.....kkSSk..kkk.
....kcccSck.kSk.
...kcccckckkSk..
...kcccccckSSk..
...kccccckkSSk..
...kkkkkkkkkk...
...kcccccck.....
....kccccck.....
....kcccccck....
.....kkkkkk.....
.....kkkkkk.....
................
'''))

# 瘦猴: thin, spiky hair, a buck-toothed grin, patched brown clothes, a short knife
SPRITES['shouhou'] = dict(pal=dict(k=0x0F, S=0x37, c=0x08), front=G('''
....k.k.k.......
....kkkkkk......
...kkkkkkkk.....
...kkkkkkkk.....
..kSkSSSSkSk....
..kSkkSSkkSk....
...kkSSSSkk.....
...kSkkkkSk.....
...kSSkkSSk.....
....kSSSSk......
.....kSSk.......
....kckkck......
...kccckccck....
..kcckcckcck....
..kckkccckck.S..
..kSSkcccckSSk..
..kSSkckkkkSSk..
...kkckkkckkk...
....kcccccck....
....kcckccck....
....kcck.kcck...
....kkkk.kkkk...
....kkk...kkk...
...........kkk..
'''), side=G('''
....k.k.k.......
....kkkkkk......
...kkkkkkkk.....
...kkkkkSSSk....
...kkkkSkkSk....
...kkkkSSkSSk...
...kkkkSSSSk....
...kkkkkSkkk....
....kkkSSSk.....
.....kkSSk......
.....kckkck.....
....kccckcck....
....kckkcckk.S..
....kcccckkSSk..
....kcccckkSSk..
....kkcckkkkk...
....kkkkkkkk....
....kcccccck....
....kcckcccck...
...kcckkcccck...
..kkkkk..kkkkk..
.kkkkk....kkkkk.
................
................
'''), side2=G('''
................
....k.k.k.......
....kkkkkk......
...kkkkkkkk.....
...kkkkkSSSk....
...kkkkSkkSk....
...kkkkSSkSSk...
...kkkkSSSSk....
...kkkkkSkkk....
....kkkSSSk.....
.....kkSSk......
.....kckkck.....
....kccckcck....
....kckkcckk.S..
....kcccckkSSk..
....kcccckkSSk..
....kkcckkkkk...
....kkkkkkkk....
....kcccccck....
....kcckccck....
.....kcccck.....
.....kkkkkk.....
.....kkkkk......
................
'''))

# 屠千秋: long black hair with a white streak, a pale face half under a silver mask, a violet robe, the bone fan
SPRITES['tuqianqiu'] = dict(pal=dict(k=0x0F, S=0x30, c=0x04), front=G('''
.....kkkkkk.....
....kkSkkkkk....
...kkSkkkkkkk...
...kSkkkkkkkkk..
..kkSkSSkkkkkk..
..kkSkSSSkSSkk..
..kkSkkkSkkSkk..
..kkSkSkSSkSkk..
..kkSkSSSSSSkk..
..kkSkSSkkSSkk..
..kkSkkSSSSkkk..
..kkSkkkSSkkkk.k
..kkSkcckkcckkSk
.kckSkcSSScckkSk
.kccSkckSkcckSSk
.kcckcckkkcckSk.
.kSSkccckcccckk.
..kkkccckccckk..
...kccccckccck..
...kcccckcccck..
..kcccccckccccck
..kccccckcccccck
..kkkkkkkkkkkkk.
...kkkk...kkkk..
'''), side=G('''
.....kkkkkk.....
....kkkkkkkk....
...kkkkkkkkkk...
..kkkkkkkSSSSk..
..kkkkkkSSSSSk..
..kkkkkkSkkSSk..
..kkkkkkSSkSSSk.
..kkkkkkSSSSSk..
..kkkkkkSSSSkk..
..kkkkkkkSkkk...
..kkkkkkkSSk....
..kkkkcccSck....
..kkkcccccck....
..kkkcccckckS...
...kkcccckSSk...
...kkcccccSSk...
...kkccccckk....
...kccccccck....
...kccccccck....
..kccccccccck...
..kkkkkkkkkkk...
....kkk..kkk....
................
................
'''), side2=G('''
................
.....kkkkkk.....
....kkkkkkkk....
...kkkkkkkkkk...
..kkkkkkkSSSSk..
..kkkkkkSSSSSk..
..kkkkkkSkkSSk..
..kkkkkkSSkSSSk.
..kkkkkkSSSSSk..
..kkkkkkSSSSkk..
..kkkkkkkSkkk...
..kkkkkkkSSk....
..kkkkcccSck....
..kkkcccccck....
..kkkcccckckS...
...kkccccSSk....
...kkccccSSk....
...kkcccckk.....
...kccccccck....
...kccccccck....
...kcccccccck...
...kkkkkkkkk....
.....kkkkk......
................
'''))
HEIGHTS = {'heixiong': 24, 'daoba': 24, 'shouhou': 23, 'tuqianqiu': 24}
