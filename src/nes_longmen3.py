"""龍門武林 (Longmen Wulin), third group: more of the cast from the Longmen stories in the 8-bit `nes` style.

Hand-typed 48x56 portraits and 16x24 field sprites with the same rules and helpers as nes_longmen.py
(2C02 colours, nes.Pic.check() proves the Famicom rules). Every sprite also carries `legs`: the bottom rows of
walk frame 2 (front: the other foot forward; side: the passing pose), so the body never moves between frames
(see nes_walk.py). nes_longmen.py merges PORTRAITS, SPRITES and HEIGHTS from here.
"""

# ---------------------------------------------------------------- Tie Wusi, Master of the Law Hall
# iron-faced deputy of the Martial Alliance: a black official cap with long side wings, heavy slanting brows,
# a drooping black moustache, a charcoal round-collared robe trimmed in red with a rank badge, a gold belt,
# and the iron chain (his Iron Lock Chain) hanging over his shoulder
TIEWUSI = '''
................................................|
..................kkkkkkkkkkkk..................|
................kkhhhhhhhhhhhhkk................|
...............khhhhhhhhhhhhhhhhk...............|
...............khhhhhhhhhhhhhhhhk...............|
..............kkkkkkkkkkkkkkkkkkkk..............|
.............khhhhhhhhhhhhhhhhhhhhk.............|
............khhhhhhhhhhhhhhhhhhhhhhk............|
.kkkkkkkkkkkkhhhhhhhhhhhhhhhhhhhhhhkkkkkkkkkkkk.|
.khhhhhhhhhhkhhhhhhhhhhhhhhhhhhhhhhkhhhhhhhhhhk.|
.kkkkkkkkkkkkhhhhhhhhhhhhhhhhhhhhhhkkkkkkkkkkkk.|
............khhhhhhhhhhhhhhhhhhhhhhk............|
...........kkkkkkkkkkkkkkkkkkkkkkkkkk...........|
...........kkhhhhSSSSSSSSSSSSSShhhhkk...........|
............khhSSSSSSSSSSSSSSSSSShsk............|
............khSSSSSSSSSSSSSSSSSSSSsk............|
............kSkkkkSSSSSSSSSSSSkkkkSk............|
............kSSkkkkkkSSSSSSkkkkkkSSk............|
............kSSSSSkkkkSSSSkkkkSSSSSk............|
............kSSkkkkSSSSSSSSSSkkkkSsk............|
............kSSSkkSSSSSSSSSSSSkkSSsk............|
...........kSSSSkkSSSSSSSSSSSSkkSSsSk...........|
...........kSsSSSSSSSSSSSSSSSSSSSSsSk...........|
...........kSsSSSSSSSSSSSSSSSSSSSSsSk...........|
............kSSSSSSSSSSssSSSSSSSSSsk............|
............kSSSSSSSSSssssSSSSSSSSsk............|
............kSSSSSSSSkSSSSkSSSSSSSsk............|
............kSSSSkkkkkkkkkkkkkkSSssk............|
............kSSSkkkkkkkkkkkkkkkkSssk............|
............kSSkkkSSSSSSSSSSSSkksssk............|
............kSSkSSSSkkkkkkkkSSSSsssk............|
.............kSSSSSSSSSSSSSSSSSssSk.............|
...............kSSSSSSSSSSSSSSSSk...............|
...............kkSSSSSSSSSSSSSSkk...............|
.................kkkkkkkkkkkkkk.................|
..................kSSSSSSSSSSk..................|
..................kSSSSSSSSSSk..................|
...............kkkrrrkSSSSkrrrkkk...............|
......kWWk.kkkkGGkrrrkkkkkkrrrkGGkkkk...........|
....kWkkWkkGGGGGGGkrrrrrrrrrrkGGGGGGGkkk........|
...kWkkkGGGGGGGGGGGkkkkkkkkkkGGGGGGGGGGGkk......|
..kWkWkGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGkk....|
..kWkWkGGGGGGGGGGGGkkkkkkkkkkGGGGGGGGGGGGGGGk...|
..kkWkGGGGGGGGGGGGGkrrrGGrrrkGGGGGGGGGGGGGGGGk..|
.kGkWkGGGGGGGGGGGGGkrrGGGGrrkGGGGGGGGGGGGGGGGGk.|
kGkWkWkkGGGGGGGGGGGkrrGGGGrrkGGGGGGGGGGGkGGGGGGk|
GGkWkWkkGGGGGGGGGGGkrrrGGrrrkGGGGGGGGGGGkGGGGGGG|
GGGkWkGkGGGGGGGGGGGkkkkkkkkkkGGGGGGGGGGGkGGGGGGG|
kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk|
yyykyyykyyykyyykyyykyyykkyyykyyykyyykyyykyyykyyy|
kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk|
GGGGGGkGGGGGGGGGGGGGGGGkkGGGGGGGGGGGGGGGGkGGGGGG|
GGGGGGkGGGGGGGGGGGGGGGGkkGGGGGGGGGGGGGGGGkGGGGGG|
GGGGGkGGGGGGGGGGGGGGGGGkkGGGGGGGGGGGGGGGGGkGGGGG|
GGGGGkGGGGGGGGGGGGGGGGGkkGGGGGGGGGGGGGGGGGkGGGGG|
GGGGGkGGGGGGGGGGGGGGGGGkkGGGGGGGGGGGGGGGGGkGGGGG|
'''
TIEWUSI_SPR = '''
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
15:W..W..........W..W
'''
TIEWUSI_SLOTS = {'S': 0x37, 's': 0x27, 'h': 0x0C, 'G': 0x00, 'r': 0x16, 'y': 0x28, 'W': 0x10}
TIEWUSI_PALETTES = [(0x37, 0x27, 0x0C), (0x00, 0x16, 0x28), (0x00, 0x10, 0x16), (0x37, 0x16, 0x00)]
TIEWUSI_SPR_SLOTS = {'W': 0x30}
TIEWUSI_SPR_PALETTES = [(0x30,)]

# ---------------------------------------------------------------- Qian Wanli, the Golden Abacus
# treasurer of the Martial Alliance: round and well fed, a maroon melon-skin cap with a red knob, a thin
# moustache over a pleased little smile, a maroon robe trimmed in gold, and the gold-beaded abacus
QIANWANLI = '''
................................................|
......................kkkk......................|
.....................khhhhk.....................|
.................kkkkkkkkkkkkkk.................|
..............kkkhhhhkhhhhkhhhhkkk..............|
.............khhhhhhkhhhhhhkhhhhhhk.............|
............khhhhhhkhhhhhhhhkhhhhhhk............|
...........khhhhhhkhhhhhhhhhhkhhhhhhk...........|
...........khhhhhhkhhhhhhhhhhkhhhhhhk...........|
..........khhhhhhkhhhhhhhhhhhhkhhhhhhk..........|
..........khhhhhhkhhhhhhhhhhhhkhhhhhhk..........|
..........kkkkkkkkkkkkkkkkkkkkkkkkkkkk..........|
..........kyyyyyyyyyyyyyyyyyyyyyyyyyyk..........|
..........kkkkkkkkkkkkkkkkkkkkkkkkkkkk..........|
.........kkSSSSSSSSSSSSSSSSSSSSSSSSSSkk.........|
.........kSSSSSSSSSSSSSSSSSSSSSSSSSSSSk.........|
........kSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSk........|
........kSSSkkkkSSSSSSSSSSSSSSSSkkkkSSSk........|
........kSSkSSSSkSSSSSSSSSSSSSSkSSSSkSSk........|
........kSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSk........|
........kSSSSkkkSSSSSSSSSSSSSSSSkkkSSSSk........|
.......kSSSSSkSkSSSSSSSSSSSSSSSSkSkSSSSSk.......|
.......kSsSSSSSSSSSSSSSSSSSSSSSSSSSSSSsSk.......|
.......kSsSSSSSSSSSSSSSssSSSSSSSSSSSSSsSk.......|
.......kSSSSSSSSSSSSSSssssSSSSSSSSSSSSSSk.......|
.......kSSSSSSSSSSSSSkSSSSkSSSSSSSSSSSSSk.......|
.......kSSsSSSSSSSSSSSSSSSSSSSSSSSSSSsSSk.......|
.......kSSSsSSSSSSSkkkkSSkkkkSSSSSSSsSSSk.......|
.......kSSSSSSSSSkkSSSSSSSSSSkkSSSSSSSSSk.......|
........kSSSSSSSSSSSkSSSSSSkSSSSSSSSSSSk........|
........kSSSSSSSSSSSSkkkkkkSSSSSSSSSSSSk........|
........kSSSsSSSSSSSSSSSSSSSSSSSSSSsSSSk........|
.........kSSSSSSSSSSSSSSSSSSSSSSSSSSSSk.........|
.........kSSSSSSSSSSSSSSSSSSSSSSSSSSSSk.........|
..........kSSSSSSSSSSSSSSSSSSSSSSSSSSk..........|
...........kkSSSSSSSSSSSSSSSSSSSSSSkk...........|
.............kkkkkkkkkkkkkkkkkkkkkk.............|
.........kkkkkyhhhhhkSSSSSSkhhhhhykkkkk.........|
......kkkhhhhkyhhhhhhkkkkkkhhhhhhykhhhhkkk......|
....kkhhhhhhhkyhhhhhhhhyyhhhhhhhhykhhhhhhhkk....|
...khhhhhhhhhkyhhhhhhhyhhyhhhhhhhykhhhhhhhhhk...|
..khhhhhhhhhkyhhhhhhhyhhhhyhhhhhhhykhhhhhhhhhk..|
.khhhhhhhhhhkyhhhhhhyhhhhhhyhhhhhhykhhhhhhhhhhk.|
khhhhhhhhhhkyhhhhhhyhhhhhhhhyhhhhhhykhhhhhhhhhhk|
hhhhhhhhhhhkkkkkkkkkkkkkkkkkkkkkkkkkkhhhhhhhhhhh|
hhhhhhhhhhkSSkkyykkyykkyykkyykkyykkSSkhhhhhhhhhh|
hhhhhhhhhhkSSSkkkkkkkkkkkkkkkkkkkkSSSkhhhhhhhhhh|
hhhhhhhhhkkSSkkyykkyykkyykkyykkyykkSSkkhhhhhhhhh|
hhhhhhhhhkSSSSkkkkkkkkkkkkkkkkkkkkSSSSkhhhhhhhhh|
hhhhhhhhhkSSSkkyykkyykkyykkyykkyykkSSSkhhhhhhhhh|
hhhhhhhhhkkSSkkkkkkkkkkkkkkkkkkkkkkSSkkhhhhhhhhh|
hhhhhhhhhhkkkkkkkkkkkkkkkkkkkkkkkkkkkkhhhhhhhhhh|
hhhhhhhhhhkhhhhyhhhhhhhhhhhhhhhhyhhhhkhhhhhhhhhh|
hhhhhhhhhhkhhhhyhhhhhhhhhhhhhhhhyhhhhkhhhhhhhhhh|
hhhhhhhhhhkhhhhyhhhhhhhhhhhhhhhhyhhhhkhhhhhhhhhh|
hhhhhhhhhhkhhhhyhhhhhhhhhhhhhhhhyhhhhkhhhhhhhhhh|
'''
QIANWANLI_SPR = '''
.
22:rrrr
22:rrrr
'''
QIANWANLI_SLOTS = {'S': 0x37, 's': 0x27, 'h': 0x05, 'R': 0x15, 'y': 0x28}
QIANWANLI_PALETTES = [(0x37, 0x27, 0x05), (0x15, 0x05, 0x28), (0x37, 0x05, 0x28), (0x37, 0x27, 0x28)]
QIANWANLI_SPR_SLOTS = {'W': 0x30, 'r': 0x16}
QIANWANLI_SPR_PALETTES = [(0x30, 0x16)]

# ---------------------------------------------------------------- Wen Ruyu, clerk of the Alliance treasury
# a soft-spoken young scholar: hair in a bun wrapped in dark green cloth, a gentle face with thin brows and
# a polite little smile, a pale green gown with dark green trim and a spot of ink on the collar, the ledger at his chest
WENRUYU = '''
..................................S.............|
....................kkkkkkkk....SS..............|
...................kggggggggk.SS................|
..................kgggggggggkS..................|
..................kggkggggkkgk..................|
..................kkgggkkkggkk..................|
.................kkkkkkkkkkkkkk.................|
..............kkkhhhhhhhhhhhhhhkkk..............|
............kkhhhhhhhhhhhhhhhhhhhhkk............|
...........khhhhhhhhhhhhhhhhhhhhhhhhk...........|
...........khhhhhhhhhhhhhhhhhhhhhhhhk...........|
..........khhhhhhhhhhhhhhhhhhhhhhhhhhk..........|
..........khhhhhhhhhhhhkkhhhhhhhhhhhhk..........|
..........khhhhkkkkkkkkSSkkkkkkkkhhhhk..........|
..........khhkkSSSSSSSSSSSSSSSSSSkkhhk..........|
..........khhkSSSSSSSSSSSSSSSSSSSSkhhk..........|
..........khkSSSSSSSSSSSSSSSSSSSSSSkhk..........|
..........khkSSSSSSSSSSSSSSSSSSSSSSkhk..........|
..........khkSSSkkkkSSSSSSSSkkkkSSSkhk..........|
..........khkSSkSSSSSSSSSSSSSSSSkSSkhk..........|
..........kSSSSSSSSSSSSSSSSSSSSSSSSSSk..........|
..........kSSSSkkkkkSSSSSSSSkkkkkSSSSk..........|
.........kSsSSSSkkkSSSSSSSSSSSkkkSSSsSk.........|
.........kSsSSSSSSSSSSSSSSSSSSSSSSSSsSk.........|
..........kSSSSSSSSSSSSssSSSSSSSSSSSSk..........|
..........kSSSSSSSSSSSSssSSSSSSSSSSSSk..........|
..........kSSSSSSSSSSSssssSSSSSSSSSSSk..........|
...........kSSSSSSSSSSkSSkSSSSSSSSSSk...........|
...........kSSSSSSSSSSSSSSSSSSSSSSSSk...........|
............kSSSSSSSSSSSSSSkSSSSSSSk............|
............kSSSSSSSkkkkkkkSSSSSSSSk............|
.............kSSSSSSSSSSSSSSSSSSSSk.............|
...............kSSSSSSSSSSSSSSSSk...............|
................kkSSSSSSSSSSSSkk................|
..................kkkkkkkkkkkk..................|
...................kSSSSSSSSk...................|
...................kSSSSSSSSk...................|
...............kkkkkgkSSSSkgkkkkk...............|
...........kkkkcccckggkSSkggkcccckkkk...........|
........kkkccccccccckggkkggkccccccccckkk........|
......kkccccccccccccckggggkccccckkkkkkkkkkkk....|
....kkccccccccccccccckkggkcccccckWWWWWWWWWWk....|
...kcccccccccccccccckkcccccccccckggggggggggkk...|
..kccccccccccccccccccccccccccccckgkkkkkkkkgkck..|
.kcccckccccccccccccccccccccccccckgkWWWWWWkgkcck.|
kccccckccccccccccccccccccccccccckgkWWWWWWkgkccck|
cccccckccccccccccccccccccccccccckgkkkkkkkkgkcccc|
cccccckcccccccccccccccccccckkkkkkggggggggggkcccc|
ccccckcccccccccccccccccccckSSSSkkggggggggggkcccc|
ccccckcccccccccccccccccccckSkSSkkggggggggggkcccc|
ccccckcccccccccccccccccccckSkSSkkggggggggggkcccc|
ccccckcccccccccccccccccccckSSSSkkggggggggggkcccc|
cccckcccccccccccccccccccccckkkkckWWWWWWWWWWkcccc|
cccckccccccccccccccccccccccccccckkkkkkkkkkkkcccc|
cccckcccccccccccccccccccccccccccccccccccccckcccc|
cccckcccccccccccccccccccccccccccccccccccccckcccc|
'''
WENRUYU_SPR = '''
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
17:W............W
'''
WENRUYU_SLOTS = {'S': 0x37, 's': 0x27, 'h': 0x0C, 'g': 0x0A, 'c': 0x3B, 'W': 0x30}
WENRUYU_PALETTES = [(0x37, 0x27, 0x0C), (0x37, 0x0C, 0x0A), (0x37, 0x3B, 0x0A), (0x30, 0x3B, 0x0A)]
WENRUYU_SPR_SLOTS = {'W': 0x30}
WENRUYU_SPR_PALETTES = [(0x30,)]

# ---------------------------------------------------------------- Xiaolian, the little apprentice of the Cold River Pavilion
# Liu Hanyan's young disciple and Yi Shuo's first friend: two round buns tied with red ribbons, a fringe,
# bright eyes and rosy cheeks, a pink robe with a white collar and sash
XIAOLIAN = '''
................................................|
................................................|
......kkkk............................kkkk......|
.....khhhhk..........................khhhhk.....|
....khhhhhhk........................khhhhhhk....|
....khhhhhhk......kkkkkkkkkkkk......khhhhhhk....|
....khhhhhhk...kkkhhhhhhhhhhhhkkk...khhhhhhk....|
.....khhhhk..kkhhhhhhhhhhhhhhhhhhkk..khhhhk.....|
......kkkkkkkhhhhhhhhhhhhhhhhhhhhhhkkkkkkk......|
...........khhhhhhhhhhhhhhhhhhhhhhhhk...........|
..........khhhhhhhhhhhhhhhhhhhhhhhhhhk..........|
.........khhhhhhhhhhhhhhhhhhhhhhhhhhhhk.........|
.........khhhhhhhhhhhhhhhhhhhhhhhhhhhhk.........|
........khhhhhhhhhhhhhhhhhhhhhhhhhhhhhhk........|
........khhhhhhhhhhhhhhhhhhhhhhhhhhhhhhk........|
........khhhSShhhhSShhhhhhhhSShhhhSShhhk........|
........khhSSSShhSSSShhSShhSSSShhSSSShhk........|
........khSSSSSSSSSSSSSSSSSSSSSSSSSSSShk........|
........khSSSSSSSSSSSSSSSSSSSSSSSSSSSShk........|
........khSSSSkkSSSSSSSSSSSSSSSSkkSSSShk........|
........kSSSSSkkSSSSSSSSSSSSSSSSkkSSSSSk........|
........kSSSSSkkSSSSSSSSSSSSSSSSkkSSSSSk........|
........kSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSk........|
........kSsSSSSSSSSSSSSSSSSSSSSSSSSSSsSk........|
........kSSSSSSSSSSSSSSssSSSSSSSSSSSSSSk........|
........kSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSk........|
.........kSSSSSSSSSSSkSSSSkSSSSSSSSSSSk.........|
.........kSSSSSSSSSSSSkkkkSSSSSSSSSSSSk.........|
.........kSSSSSSSSSSSSSSSSSSSSSSSSSSSSk.........|
..........kSSSSSSSSSSSSSSSSSSSSSSSSSSk..........|
...........kkSSSSSSSSSSSSSSSSSSSSSSkk...........|
.............kkkSSSSSSSSSSSSSSSSkkk.............|
................kkkkkkkkkkkkkkkk................|
....................kSSSSSSk....................|
..................kkWSSSSSSWkk..................|
...............kkppkWWSSSSWWkppkk...............|
............kkkpppppkWWSSWWkpppppkkk............|
..........kkpppppppppkWWWWkpppppppppkk..........|
........kkppppppppppppkWWkppppppppppppkk........|
.......kpppppppppppppppkkpppppppppppppppk.......|
......kppppppppppppppppppppppppppppppppppk......|
.....kpppPppppppppppppppppppppppppppppPpppk.....|
....kppppPppppppppppppppppppppppppppppPppppk....|
....kpppPppppppppppppppppppppppppppppppPpppk....|
...kppppPppppppppppppppppppppppppppppppPppppk...|
...kppppPppppppppppppppppppppppppppppppPppppk...|
...kpppPppppppppppppppppppppppppppppppppPpppk...|
...kpppPppppppppppppppppppppppppppppppppPpppk...|
...kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk...|
...kWWWWWWWWWWWWWWWWWWWWWWWWWWkWWkWWWWWWWWWWk...|
...kkkkkkkkkkkkkkkkkkkkkkkkkkkWWWWkkkkkkkkkkk...|
...kpppPppppppppppppppppppppppkWWkppppppPpppk...|
...kpppPppppppppppppppppppppppkWWkppppppPpppk...|
...kppPppppppppppppppppppppppppppppppppppPppk...|
...kppPppppppppppppppppppppppppppppppppppPppk...|
...kppPppppppppppppppppppppppppppppppppppPppk...|
'''
XIAOLIAN_SPR = '''
.
.
.
.
.
.
9:rrr........................rrr
9:r.r........................r.r
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
15:W................W
.
.
.
11:bbb....................bbb
'''
XIAOLIAN_SLOTS = {'S': 0x37, 's': 0x27, 'h': 0x0C, 'p': 0x35, 'P': 0x25, 'W': 0x30}
XIAOLIAN_PALETTES = [(0x37, 0x27, 0x0C), (0x35, 0x25, 0x30), (0x37, 0x35, 0x30)]
XIAOLIAN_SPR_SLOTS = {'W': 0x30, 'b': 0x35, 'r': 0x16}
XIAOLIAN_SPR_PALETTES = [(0x30, 0x35, 0x16)]

# ---------------------------------------------------------------- Li Hanshan, the Soul-Severing Blade of the Blood Saber Sect
# tall and gaunt, white hair swept back and tied with a dark red band, cruel slanting brows and narrow eyes,
# a high-collared dark red robe trimmed in red, the long curved blood-red blade held upright (the blade is sprites)
LIHANSHAN = '''
................................................|
.....................kkkkkk.....................|
....................kwwwwwwk....................|
...................kkbbbbbbkk...................|
.................kkkkbbbbbbkkkk.................|
..............kkkwwwwwwwwwwwwwwkkk..............|
............kkwwwwkwwwwwwwwwwkwwwwkk............|
...........kwwwwkwwwwkwwwwkwwwwkwwwwk...........|
..........kwwwwkwwwwkwwwwwwkwwwwkwwwwk..........|
..........kwwwkwwwwkwwwwwwwwkwwwwkwwwk..........|
.........kwwwkwwwwkwwwwwwwwwwkwwwwkwwwk.........|
.........kwwkwwwwkwwwwwwwwwwwwkwwwwkwwk.........|
.........kwwkwwwkkkkkkkkkkkkkkkkwwwkwwk.........|
.........kwwkwkkSSSSSSSSSSSSSSSSkkwkwwk.........|
.........kwkwkSSSSSSSSSSSSSSSSSSSSkwkwk.........|
.........kwkwkSSSSSSSSSSSSSSSSSSSSkwkwk.........|
.........kwkwkSkkkSSSSSSSSSSSSkkkSkwkwk.........|
.........kwkwkSSSkkkkSSSSSSkkkkSSSkwkwk.........|
.........kwkwkSSSSSSkkSSSSkkSSSSSSkwkwk.........|
.........kwkwkSkkkkkSSSSSSSSkkkkkSkwkwk.........|
.........kwkwkSSwwkkSSSSSSSSkkwwSSkwkwk.........|
.........kwkwkSSSSSSSSSSSSSSSSSSSSkwkwk.........|
.........kwkwkSSSSSSSSSSSSSSSSSSSSkwkwk.........|
.........kwkwkSSSSSSSSSssSSSSSSSSSkwkwk.........|
.........kwkwwkSSSSSSSssssSSSSSSSkwwkwk.........|
.........kwkwwkSSSSSkSSSSSSkSSSSSkwwkwk.........|
.........kwkwwkSSSSSSSSSSSSSSSSSSkwwkwk.........|
........kwwkwwkSSSSSSSSSSSSSSSSSSkwwkwwk........|
........kwkwwwkSSSSkkkkkkkkkkSSSSkwwwkwk........|
........kwkwwwkSSSkSSSSSSSSSSkSSSkwwwkwk........|
........kwkwwwwkSSSSSSSSSSSSSSSSkwwwwkwk........|
.......kwwkwwwwkSSSSSSSSSSSSSSSSkwwwwkwwk.......|
.......kwkwwwwwwkSSSSSSSSSSSSSSkwwwwwwkwk.......|
.......kwkwwwwwk.kkSSSSSSSSSSkk.kwwwwwkwk.......|
......kwwkwwwwk....kkkkkkkkkk....kwwwwkwwk......|
......kwkwwwwwk....kSSSSSSSSk....kwwwwwkwk......|
.....kwwkwwwwk.....kSSSSSSSSk.....kwwwwkwwk.....|
.....kwkwwwwwk....krrkSSSSkrrk....kwwwwwkwk.....|
....kwkwwwwkkkkkkbrrkkkkkkkkrrbkkkkkkwwwwkwk....|
...kwwkwwwkbbbbbkbbbrrrrrrrrbbbkbbbbbkwwwkwwk...|
...kwkwwwkbbbbbbbkkbbkkkkkkbbkkbbbbbbbkwwwkwk...|
..kwwkwwkbbbbbbbbbbbbbkrrkbbbbbbbbbbbbbkwwkwwk..|
..kwkwwkbbbbbbbbbbbbbbkrrkbbbbbbbbbbbbbbkwwkwk..|
.kwwkwkbbbbbbbbbbbbbbbkrrkbbbbbbbbbbbbbbbkwkwwk.|
.kwkwwkbbbbbbbbbbbbbbbkrrkbbbbbbbbbbbbbbbkwwkwk.|
kwwkwkbbbbbbbbbbbbbbbbkrrkbbbbbbbbbbbbbbbbkwkwwk|
kwkwwkbbbbbbbbbbbbbbbbkrrkbbbbbbbbbbbbbbbbkwwkwk|
kkkkkbbbbbbbbbbbbbbbbbkrrkbbbbbbbbbbbbbbbbbkkkkk|
bkkkkkkkkbbbbbbbbbbbbbkrrkbbbbbbbbbbbbbbbbkbbbbb|
bkSSSSSSkbbbbbbbbbbbbbkrrkbbbbbbbbbbbbbbbbkbbbbb|
bkSkSkSkkbbbbbbbbbbbbbkrrkbbbbbbbbbbbbbbbbkbbbbb|
bkSSSSSSkbbbbbbbbbbbbbkrrkbbbbbbbbbbbbbbbbkbbbbb|
bkkkkkkkkbbbbbbbbbbbbbkrrkbbbbbbbbbbbbbbbbbkbbbb|
bbbbkbbbbbbbbbbbbbbbbbkrrkbbbbbbbbbbbbbbbbbkbbbb|
bbbbkbbbbbbbbbbbbbbbbbkrrkbbbbbbbbbbbbbbbbbkbbbb|
bbbbkbbbbbbbbbbbbbbbbbkrrkbbbbbbbbbbbbbbbbbkbbbb|
'''
LIHANSHAN_SPR = '''
.
.
.
7:W
6:Wr
6:Wrr
6:Wrr
6:Wrr
6:Wrr
6:Wrr
6:Wrr
6:Wrr
6:Wrr
6:Wrr
6:Wrr
6:Wrr
5:Wrr
5:Wrr
5:Wrr
5:Wrr
5:Wrr
5:Wrr
5:Wrr
5:Wrr
5:Wrr
5:Wrr
5:Wrr
5:Wrr
5:Wrr
5:Wrr
5:Wrr
4:Wrr
4:Wrr
4:Wrr
4:Wrr
4:Wrr
4:Wrr
4:Wrr
4:Wrr
4:Wrr
4:Wrr
4:Wrr
4:Wrr
4:Wrr
4:Wrr
4:Wrr
4:Wrr
2:ddddddd
5:d
.
.
.
.
5:d
5:d
4:ddd
'''
LIHANSHAN_SLOTS = {'S': 0x37, 's': 0x27, 'w': 0x30, 'g': 0x10, 'b': 0x06, 'r': 0x16}
LIHANSHAN_PALETTES = [(0x30, 0x37, 0x06), (0x37, 0x27, 0x30), (0x37, 0x06, 0x16), (0x06, 0x16, 0x30)]
LIHANSHAN_SPR_SLOTS = {'W': 0x30, 'r': 0x16, 'd': 0x06}
LIHANSHAN_SPR_PALETTES = [(0x30, 0x16, 0x06)]

# ---------------------------------------------------------------- the One-Armed Fisherman
# an old recluse of the river: a wide straw rain hat, long white brows and a long white beard, a weathered face,
# a patched grey robe with the empty left sleeve knotted at the shoulder, and his fishing rod over the other side
YUWENG = '''
................................................|
................................................|
..............................k.................|
.......................kk......ok...............|
......................kYYk......ok..............|
.....................kYyyYk......ok.............|
....................kYyYYyYk......ok............|
...................kYyYYYYyYk......ok...........|
.................kkYyYYYYYYyYkk.....ok..........|
...............kkYYyYYYYYYYYyYYkk....ok.........|
.............kkYYYyYYYYyyYYYYyYYYkk...ok........|
...........kkYYYYyYYYYyYYyYYYYyYYYYkk..ok.......|
.........kkYYYYYyYYYYyYYYYyYYYYyYYYYYkk.ok......|
.......kkYYYYYYyYYYYyYYYYYYyYYYYyYYYYYYkkok.....|
.....kkyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyykok....|
....kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk....|
............kSSSSSSSSSSSSSSSSSSSSSSk.......ok...|
............kSSSSSSSSSSSSSSSSSSSSSSk........ok..|
...........kSkkkSSSSSSSSSSSSSSSSkkkSk........ok.|
...........kSSSkkSSSSSSSSSSSSSSkkSSSk.........ok|
...........kWWWWSkSSSSSSSSSSSSkSWWWWk..........o|
...........kSSSSWWSSSSSSSSSSSSWWSSSSk...........|
...........kSSkkkkSSSSSSSSSSSSkkkkSSk...........|
...........kSSSkkSSSSSSSSSSSSSSkkSSSk...........|
..........kSSSSSSSSSSSSSSSSSSSSSSSSSSk..........|
..........kSSSSSSSSSSSSSSSSSSSSSSSSSSk..........|
...........kSSSSSSSSSSSSSSSSSSSSSSSSk...........|
...........kSSSSSSSSSkSSSSkSSSSSSSSSk...........|
...........kSSSSWWWWWWWWWWWWWWWWSSSSk...........|
...........kSSWWWWWWWWWWWWWWWWWWWWSSk...........|
...........kSWWWWWkkkkkkkkkkkkWWWWWSk...........|
...........kSWWWWWWWWWWWWWWWWWWWWWWSk...........|
............kWWWWWWWWWWWWWWWWWWWWWWk............|
............kWWWWWWWWWWWWWWWWWWWWWWk............|
.............kWWWWWWWWWWWWWWWWWWWWk.............|
.............kWWWWWWWWWWWWWWWWWWWWk.............|
...........kkkWWWWWWWWWWWWWWWWWWWWkkk...........|
........kkkGGGkWWWWWWWWWWWWWWWWWWkGGGkkk........|
......kkGGGGGGkWWWWWWWWWWWWWWWWWWkGGGGGGkk......|
....kkGGGGGGGGkWWWWWWWWWWWWWWWWWWkGGGkkkkkkk....|
...kGGGGGGGGGGGkWWWWWWWWWWWWWWWWkGGGGkGGGGGkk...|
..kGGGGGGGGGGGGkWWWWWWWWWWWWWWWWkGGGGkGGkGGkGk..|
.kGGGGGGGGGGGGGGkWWWWWWWWWWWWWWkGGGGGkGGkGGkGGk.|
kGGGGGGGGGGGGGGGkWWWWWWWWWWWWWWkGGGGGkGGkGGkGGGk|
GGGGGGkGGGGGGGGGGkWWWWWWWWWWWWkGGGGGGkGGkGGkGGGG|
GGGGGGkGGGGGGGGGGkWWWWWkkWWWWWkGGGGGGkoGkGGkGGGG|
GGGGGGkGGGGGGGGGGGkWWWkGGkWWWkGGGGGGGkooGkGkGGGG|
GGGGGkkkkkkkGGGGGGGkkkGGGGkkkGGGGGGGGkGGkGGkGGGG|
GGGGGkkoooookGGGGGGGkGGGGGGkGGGGGGGGGkGkkkGkGGGG|
GGGGGkkokoookGGGGGGGkGGGGGGkGGGGGGGGGkkkkkkkGGGG|
GGGGGkkoooookGGGGGGGkGGGGGGkGGGGGGGGGGGGGGkGGGGG|
GGGGkGkkkkkkGGGGGGGGkGGGGGGkGGGGGGGGGGGGGGGkGGGG|
GGGGkGGGGGGGGGGGGGGGkGGGGGGkGGGGGGGGGGGGGGGkGGGG|
GGGGkGGGGGGGGGGGGGGGkGGGGGGkGGGGGGGGGGGGGGGkGGGG|
GGGGkGGGGGGGGGGGGGGGkGGGGGGkGGGGGGGGGGGGGGGkGGGG|
GGGGkGGGGGGGGGGGGGGGkGGGGGGkGGGGGGGGGGGGGGGkGGGG|
'''
YUWENG_SPR = '''
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
47:W
47:W
47:W
47:W
47:W
47:W
47:W
47:W
47:W
47:W
'''
YUWENG_SLOTS = {'S': 0x37, 's': 0x27, 'Y': 0x38, 'y': 0x28, 'o': 0x18, 'W': 0x30, 'G': 0x00}
YUWENG_PALETTES = [(0x38, 0x28, 0x18), (0x37, 0x27, 0x30), (0x00, 0x18, 0x30), (0x37, 0x30, 0x18)]
YUWENG_SPR_SLOTS = {'W': 0x30}
YUWENG_SPR_PALETTES = [(0x30,)]

# ---------------------------------------------------------------- the Ghost-mask Warden of the Netherworld Sect
# a tall warden in a pointed blood-red hood and cloak, his face hidden behind a white ghost mask painted with
# slanting brows and a fanged grin, red light in the eye holes (sprites), a gold diamond emblem on the chest
GUIMIAN = '''
................................................|
.......................kk.......................|
......................krrk......................|
.....................krrrrk.....................|
....................krrrrrrk....................|
...................krrrrrrrrk...................|
.................kkrrrrrrrrrrkk.................|
...............kkrrrrrrrrrrrrrrkk...............|
.............kkrrrrrrrrrrrrrrrrrrkk.............|
............krrrrrrrrrrrrrrrrrrrrrrk............|
...........krrrrrrkkkkkkkkkkkkrrrrrrk...........|
..........krrrrrkkWWWWWWWWWWWWkkrrrrrk..........|
..........krrrrkWWWWWWWWWWWWWWWWkrrrrk..........|
.........krrrrkWWWWWWWWWWWWWWWWWWkrrrrk.........|
.........krrrkWWWWWWWWWWWWWWWWWWWWkrrrk.........|
.........krrrkWkkkWWWWWWWWWWWWkkkWkrrrk.........|
.........krrrkWWkkkkWWWWWWWWkkkkWWkrrrk.........|
........krrrkWWWWWkkkWWWWWWkkkWWWWWkrrrk........|
........krrrkWWkkkkkkWWWWWWkkkkkkWWkrrrk........|
........krrrkWWkkkkkkWWWWWWkkkkkkWWkrrrk........|
........krrrkWWWkkkkWWWWWWWWkkkkWWWkrrrk........|
........krrrkWWWWWWWWWWWWWWWWWWWWWWkrrrk........|
........krrrkWWWWWWWWWggggWWWWWWWWWkrrrk........|
........krrrkWWWWWWWWkggggkWWWWWWWWkrrrk........|
........krrrkWWWWWWWWWWWWWWWWWWWWWWkrrrk........|
........krrrkWWkkkkkkkkkkkkkkkkkkWWkrrrk........|
........krrrkWWkWkWkWkWkkWkWkWkWkWWkrrrk........|
........krrrkWWkkWkkkWkkkkWkkkWkkWWkrrrk........|
........krrrkWWWkkkkkkkkkkkkkkkkWWWkrrrk........|
.........krrrkWWWWWWWWWWWWWWWWWWWWkrrrk.........|
.........krrrkkWWWWWWWWWWWWWWWWWWkkrrrk.........|
..........krrrrkkkkkkkkkkkkkkkkkkrrrrk..........|
..........krrrrrrrrrrrrrrrrrrrrrrrrrrk..........|
.........krrrrrrrrrrrrrrrrrrrrrrrrrrrrk.........|
........krrrrrrrrrrrrrrrrrrrrrrrrrrrrrrk........|
.......krrrrdrrrrrrrrrrrrrrrrrrrrrrdrrrrk.......|
......krrrrrdrrrrrrrrrrrrrrrrrrrrrrdrrrrrk......|
.....krrrrrrdrrrrrrrrrrrrrrrrrrrrrrdrrrrrrk.....|
....krrrrrrrdrrrrrrrrrkkkkrrrrrrrrrdrrrrrrrk....|
...krrrrrrrrdrrrrrrrrkyyyykrrrrrrrrdrrrrrrrrk...|
..krrrrrrrrrdrrrrrrrkyykkyykrrrrrrrdrrrrrrrrrk..|
.krrrrrrrrrrdrrrrrrkyykddkyykrrrrrrdrrrrrrrrrrk.|
krrrrrrrrrrrdrrrrrkyykddddkyykrrrrrdrrrrrrrrrrrk|
rrrrrrrrrrrrdrrrrrrkyykddkyykrrrrrrdrrrrrrrrrrrr|
rrrrrrrrrrrrdrrrrrrrkyykkyykrrrrrrrdrrrrrrrrrrrr|
rrrrrrrrrrrrdrrrrrrrrkyyyykrrrrrrrrdrrrrrrrrrrrr|
rrrrrrrrrrrrdrrrrrrrrrkkkkrrrrrrrrrdrrrrrrrrrrrr|
rrrrrrrrrrrrdrrrrrrrrrrrrrrrrrrrrrrdrrrrrrrrrrrr|
rrrrrrrrrrrdrrrrrrrrrrrrrrrrrrrrrrrrdrrrrrrrrrrr|
rrrrrrrrrrrdrrrrrrrrrrrrrrrrrrrrrrrrdrrrrrrrrrrr|
rrrrrrrrrrrdrrrrrrrrrrrrrrrrrrrrrrrrdrrrrrrrrrrr|
rrrrrrrrrrrdrrrrrrrrrrrrrrrrrrrrrrrrdrrrrrrrrrrr|
rrrrrrrrrrdrrrrrrrrrrrrrrrrrrrrrrrrrrdrrrrrrrrrr|
rrrrrrrrrrdrrrrrrrrrrrrrrrrrrrrrrrrrrdrrrrrrrrrr|
rrrrrrrrrrdrrrrrrrrrrrrrrrrrrrrrrrrrrdrrrrrrrrrr|
rrrrrrrrrrdrrrrrrrrrrrrrrrrrrrrrrrrrrdrrrrrrrrrr|
'''
GUIMIAN_SPR = '''
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
17:ee..........ee
.
.
14:RR..................RR
14:RR..................RR
'''
GUIMIAN_SLOTS = {'r': 0x16, 'd': 0x06, 'W': 0x30, 'g': 0x10, 'y': 0x28}
GUIMIAN_PALETTES = [(0x16, 0x06, 0x30), (0x30, 0x10, 0x16), (0x16, 0x06, 0x28)]
GUIMIAN_SPR_SLOTS = {'e': 0x26, 'R': 0x16}
GUIMIAN_SPR_PALETTES = [(0x26, 0x16)]

# ---------------------------------------------------------------- the Masked Man of the Stratagem Pavilion
# nobody has seen his face: a deep purple hood piped in gold, a violet veil over everything but the eyes and the sword brows,
# a purple robe edged in gold with a gold belt; a violet glow gathers in his hands (sprites)
MASKED = '''
.......................kk.......................|
......................kppk......................|
...................kkkppppkkk...................|
................kkkppppppppppkkk................|
..............kkppppppppppppppppkk..............|
.............kppppppppppppppppppppk.............|
............kppyppppppppppppppppyppk............|
...........kppyppppppppppppppppppyppk...........|
...........kpyppppppppppppppppppppypk...........|
..........kppyppppppppppppppppppppyppk..........|
..........kpyppppppppppppppppppppppypk..........|
..........kpypppppykkkkkkkkkkypppppypk..........|
.........kppyppykkkkkkkkkkkkkkkkyppyppk.........|
.........kpyppykkkkkkkkkkkkkkkkkkyppypk.........|
.........kpypykkkkkkkkkkkkkkkkkkkkypypk.........|
.........kpyykkkkkkkkkkkkkkkkkkkkkkyypk.........|
.........kpkpkkkkkkkkkkkkkkkkkkkkkkpkpk.........|
.........kpkpkkkSSSSSSSSSSSSSSSSkkkpkpk.........|
.........kpkpkSkkkkSSSSSSSSSSkkkkSkpkpk.........|
.........kpkpkSSSSSSSSSSSSSSSSSSSSkpkpk.........|
.........kpkpkSkkkkSSSSSSSSSSkkkkSkpkpk.........|
.........kpkpkSSkkSSSSSSSSSSSSkkSSkpkpk.........|
.........kpkpkkkkkkkkkkkkkkkkkkkkkkpkpk.........|
.........kpkpkPPPPPPPPPPPPPPPPPPPPkpkpk.........|
.........kpkpkPkPPPPPPPPPPPPPPPPkPkpkpk.........|
.........kpkpkPPkPPPPPPPPPPPPPPkPPkpkpk.........|
.........kpkpkPPPkPPPPPPPPPPPPkPPPkpkpk.........|
.........kpkpkPPPPkPPPPPPPPPPkPPPPkpkpk.........|
..........kpkpkPPPPkPPPPPPPPkPPPPkpkpk..........|
..........kpkpkPPPPPkPPPPPPkPPPPPkpkpk..........|
...........kpkpkPPPPPPPPPPPPPPPPkpkpk...........|
............kpkpkkkkkkkkkkkkkkkkpkpk............|
...........kpppppkkkkkkkkkkkkkkpppppk...........|
..........kpppkyyppppppppppppppyykpppk..........|
.........kpppppkyyppppppppppppyykpppppk.........|
........kppppppkyyppppppppppppyykppppppk........|
.......kppppppppkyyppppppppppyykppppppppk.......|
......kpppppppppkyyppppppppppyykpppppppppk......|
.....kpppppppppppkyyppppppppyykpppppppppppk.....|
....kppppppppppppkyyppppppppyykppppppppppppk....|
...kppppppppppppppkyyppppppyykppppppppppppppk...|
..kpppppppppppppppkyyppppppyykpppppppppppppppk..|
.kpppppppppppppppppkyyppppyykpppppppppppppppppk.|
pppppppkpppppppppppkyyppppyykpppppppppppkppppppp|
pppppppkppppppppppppkyyppyykppppppppppppkppppppp|
pppppppkppppppppppppkyyppyykppppppppppppkppppppp|
pppppppkpppppppppppppkyyyykpppppppppppppkppppppp|
pppppppkpppppppppppppkyyyykpppppppppppppkppppppp|
kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk|
yyyyyyyyyyyyyyyyyyyykkkkkkkkyyyyyyyyyyyyyyyyyyyy|
kkkkkkkkkkkkkkkkkkkkkPPkkPPkkkkkkkkkkkkkkkkkkkkk|
pppppppkppppppppppppppppppppppppppppppppkppppppp|
pppppppkppppppppppppppppppppppppppppppppkppppppp|
pppppppkppppppppppppppppppppppppppppppppkppppppp|
pppppppkppppppppppppppppppppppppppppppppkppppppp|
pppppppkppppppppppppppppppppppppppppppppkppppppp|
'''
MASKED_SPR = '''
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
18:W..........W
'''
MASKED_SLOTS = {'S': 0x37, 'p': 0x04, 'P': 0x14, 'G': 0x00, 'y': 0x28}
MASKED_PALETTES = [(0x37, 0x14, 0x04), (0x04, 0x28, 0x00), (0x04, 0x14, 0x28)]
MASKED_SPR_SLOTS = {'W': 0x30, 'v': 0x24}
MASKED_SPR_PALETTES = [(0x30, 0x24)]

PORTRAITS = {
    'tiewusi': (TIEWUSI, TIEWUSI_SPR, TIEWUSI_SLOTS, TIEWUSI_PALETTES, TIEWUSI_SPR_SLOTS, TIEWUSI_SPR_PALETTES),
    'qianwanli': (QIANWANLI, QIANWANLI_SPR, QIANWANLI_SLOTS, QIANWANLI_PALETTES, QIANWANLI_SPR_SLOTS, QIANWANLI_SPR_PALETTES),
    'wenruyu': (WENRUYU, WENRUYU_SPR, WENRUYU_SLOTS, WENRUYU_PALETTES, WENRUYU_SPR_SLOTS, WENRUYU_SPR_PALETTES),
    'xiaolian': (XIAOLIAN, XIAOLIAN_SPR, XIAOLIAN_SLOTS, XIAOLIAN_PALETTES, XIAOLIAN_SPR_SLOTS, XIAOLIAN_SPR_PALETTES),
    'lihanshan': (LIHANSHAN, LIHANSHAN_SPR, LIHANSHAN_SLOTS, LIHANSHAN_PALETTES, LIHANSHAN_SPR_SLOTS, LIHANSHAN_SPR_PALETTES),
    'yuweng': (YUWENG, YUWENG_SPR, YUWENG_SLOTS, YUWENG_PALETTES, YUWENG_SPR_SLOTS, YUWENG_SPR_PALETTES),
    'guimian': (GUIMIAN, GUIMIAN_SPR, GUIMIAN_SLOTS, GUIMIAN_PALETTES, GUIMIAN_SPR_SLOTS, GUIMIAN_SPR_PALETTES),
    'masked': (MASKED, MASKED_SPR, MASKED_SLOTS, MASKED_PALETTES, MASKED_SPR_SLOTS, MASKED_SPR_PALETTES),
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

# Tie Wusi, Master of the Law Hall
SPRITES['tiewusi'] = dict(pal=dict(k=0x0F, S=0x37, c=0x00), front=G('''
......kkkk......
.....kkkkkk.....
kkkk.kkkkkk.kkkk
.kkkkkkkkkkkkkk.
....kkkkkkkk....
...kSSSSSSSSk...
...kkkkSSkkkk...
...kSkkSSkkSk...
...kSSSSSSSSk...
...kSkkkkkkSk...
...kSkSSSSkSk...
....kSSSSSSk....
.....kkSSkk.....
..kkkccSSccckk..
.kccccckkccccck.
.kcckcccccckcck.
.kcckcccccckcck.
.kSSkcccccckSSk.
..kkkkkkkkkkkkk.
...kcccccccck.c.
...kccccckccckk.
...kkkkkk.kkkkc.
...kkkkk..kkk.k.
.........kkkk...
'''), side=G('''
................
.....kkkkk......
....kkkkkkk.....
....kkkkkkk.....
kkkkkkkkkkkkkkkk
...kkkkkkkkk....
..kkkkkkkkkSk...
..kkkkkkkSSSSk..
..kkkkkSkkkkSk..
..kkkkkSSSSkSSk.
..kkkkkkSSSSSSk.
...kkkkSSkkkkk..
....kkkSSkSSk...
.....kkkSSkk....
....kcccSSk.....
...kcccccckk....
...kcccccckck...
...kcccccckSSk..
...kkkkkkkkkkk..
..kcccccccccck..
..kccck..kcccck.
.kccck....kccck.
.kkkkk.....kkkkk
kkkkk......kkkkk
'''), side2=G('''
................
.....kkkkk......
....kkkkkkk.....
....kkkkkkk.....
kkkkkkkkkkkkkkkk
...kkkkkkkkk....
..kkkkkkkkkSk...
..kkkkkkkSSSSk..
..kkkkkSkkkkSk..
..kkkkkSSSSkSSk.
..kkkkkkSSSSSSk.
...kkkkSSkkkkk..
....kkkSSkSSk...
.....kkkSSkk....
....kcccSSk.....
...kcccccckk....
...kcccccckck...
...kcccccckSSk..
...kkkkkkkkkkk..
...kccccccck....
....kcccccck....
....kccccck.....
....kkkkkkkk....
....kkkkkkkk....
'''), legs=dict(front=['...kkkkkk.kkkkc.', '....kkk..kkkk.k.', '...kkkk.........']))

# Qian Wanli, the Golden Abacus
SPRITES['qianwanli'] = dict(pal=dict(k=0x0F, S=0x37, c=0x05), front=G('''
................
.......kk.......
.....kkkkkk.....
....kckcckck....
...kcckcckcck...
...kkkkkkkkkk...
..kSSSSSSSSSSk..
..kSkkSSSSkkSk..
..kSSSSSSSSSSk..
..kSSkkSSkkSSk..
..kSSSkkkkSSSk..
..kSSSSSSSSSSk..
...kkSSSSSSkk...
.kkcckkkkkkcckk.
kcccccckkcccccck
kcckcccccccckcck
kcckkkkkkkkkkcck
kSSkSkSkSkSkkSSk
kcckkkkkkkkkkcck
.kkcccccccccckk.
..kcccccccccck..
..kccccccckccck.
..kkkkkkkkkkkkk.
...kkkk...kkkk..
'''), side=G('''
......kk........
....kkkkkk......
...kckcckck.....
..kcckcckcck....
..kkkkkkkkkk....
..kkkSSSSSSSk...
.kkkSSSSSSSSSk..
.kkSSSSSSkSSSk..
.kkSkSSSSkSSSSk.
.kkSSSSSSSSSSSk.
.kkSSSSSSkkkk...
..kSSSSSSSSSk...
...kkSSSSSSkk...
..kccckkkkkcck..
.kcccccccccck...
.kccccccckkkkkk.
.kcccccckSkSkSk.
.kcccccckkkkkkk.
.kccccccccSSk...
.kcccccccckk....
.kccccccccck....
.kccccccccccck..
.kkkkkkkkkkkkk..
..kkkk...kkkk...
'''), side2=G('''
......kk........
....kkkkkk......
...kckcckck.....
..kcckcckcck....
..kkkkkkkkkk....
..kkkSSSSSSSk...
.kkkSSSSSSSSSk..
.kkSSSSSSkSSSk..
.kkSkSSSSkSSSSk.
.kkSSSSSSSSSSSk.
.kkSSSSSSkkkk...
..kSSSSSSSSSk...
...kkSSSSSSkk...
..kccckkkkkcck..
.kcccccccccck...
.kccccccckkkkkk.
.kcccccckSkSkSk.
.kcccccckkkkkkk.
.kccccccccSSk...
.kcccccccckk....
.kcccccccck.....
.kkkkkkkkkk.....
...kkkkkk.......
...kkkkkk.......
'''), legs=dict(front=['...kkkkk...kkk..']))

# Wen Ruyu, clerk of the Alliance treasury
SPRITES['wenruyu'] = dict(pal=dict(k=0x0F, S=0x37, c=0x3B), front=G('''
.......kk.......
......kkkk......
.....kkkkkk.....
....kkkkkkkk....
...kkkkkkkkkk...
...kkkSSSSkkk...
...kkSSSSSSkk...
...kSSSSSSSSk...
...kSkkSSkkSk...
...kSSSSSSSSk...
...kSSSkkSSSk...
....kSSSSSSk....
.....kkSSkk.....
..kkkccSSccckk..
.kccccckSccccck.
.kcckccckkkkkk..
.kcckccckSSSSk..
.kSSkccckkkkkk..
..kkkcccckSSk...
...kcccccckk....
...kccccckcccck.
..kcccckccccccck
..kkkkkkkkkkkkk.
....kkk...kk....
'''), side=G('''
.....kk.........
....kkkk........
...kkkkkk.......
..kkkkkkkkk.....
..kkkkkkkkkk....
..kkkkkkkkkSk...
..kkkkkkkSSSSk..
..kkkkkSkSSkSk..
..kkkkkSSSSkSSk.
..kkkkkkSSSSSSk.
...kkkkSSSSkkk..
....kkkSSSSSk...
.....kkkSSkk....
....kcccSSk.....
...kcccccckkkk..
...kccccckkSSk..
...kccccckSkkk..
...kcccccckk....
...kccccccck....
..kcccccccccck..
..kccccccccccck.
.kcccccccccccck.
.kkkkkkkkkkkkkk.
.kkk.......kkkk.
'''), side2=G('''
.....kk.........
....kkkk........
...kkkkkk.......
..kkkkkkkkk.....
..kkkkkkkkkk....
..kkkkkkkkkSk...
..kkkkkkkSSSSk..
..kkkkkSkSSkSk..
..kkkkkSSSSkSSk.
..kkkkkkSSSSSSk.
...kkkkSSSSkkk..
....kkkSSSSSk...
.....kkkSSkk....
....kcccSSk.....
...kcccccckkkk..
...kccccckkSSk..
...kccccckSkkk..
...kcccccckk....
...kccccccck....
...kcccccccck...
...kcccccccck...
...kcccccccck...
...kkkkkkkkkk...
.....kkkkkk.....
'''), legs=dict(front=['....kk...kkk....']))

# Xiaolian, the little apprentice of the Cold River Pavilion
SPRITES['xiaolian'] = dict(pal=dict(k=0x0F, S=0x37, c=0x25), front=G('''
..kk........kk..
.kkkk.kkkk.kkkk.
.kkkkkkkkkkkkkk.
..kkkkkkkkkkkk..
..kkSkkSSkkSkk..
..kSSSSSSSSSSk..
..kSkkSSSSkkSk..
..kSkkSSSSkkSk..
..kSSSSSSSSSSk..
...kSSSkkSSSk...
....kkkkkkkk....
...kkcckcckk....
..kccckSkccck...
..kSkkSSSkkSk...
...kcccckccck...
...kccckccccck..
...kkkkkkkkkkk..
....kkk...kk....
'''), side=G('''
..kk..kk........
.kkkkkkkk.......
.kkkkkkkkkk.....
.kkkkkkkkSSk....
.kkkkkkSSSSk....
.kkkkkkSSkSk....
.kkkkkkSSkSSk...
..kkkkkSSSSk....
...kkkkSSSk.....
....kkkSSk......
...kccSSScck....
...kcccccSSk....
...kccccckk.....
..kccccccck.....
..kcccccccck....
.kcccccccccck...
.kkkkkkkkkkk....
'''), side2=G('''
..kk..kk........
.kkkkkkkk.......
.kkkkkkkkkk.....
.kkkkkkkkSSk....
.kkkkkkSSSSk....
.kkkkkkSSkSk....
.kkkkkkSSkSSk...
..kkkkkSSSSk....
...kkkkSSSk.....
....kkkSSk......
...kccSSScck....
...kcccccSSk....
...kccccckk.....
..kccccccck.....
..kcccccccck....
.kcccccccccck...
.kkkkkkkkkkk....
'''), legs=dict(front=['......kk...kkk..']))

# Li Hanshan, the Soul-Severing Blade of the Blood Saber Sect
SPRITES['lihanshan'] = dict(pal=dict(k=0x0F, S=0x30, c=0x16), front=G('''
.......kk.....k.
......kcck...kSk
.....kkkkkk..kck
....kSSSSSSk.kck
...kSSkSSkSSkkck
...kSkkkkkkSkkck
..kSkSSSSSSkSkck
..kSkkkSSkkkSkck
..kSkSkSSkSkSkck
..kSkSSSSSSkSkck
..kSkSkkkkSkSkck
..kSkkSSSSkkSkck
.kSSk.kkkk.kSSkk
.kSkkcckkcckkkSk
.kSkcccckcccckSk
.kkkcccckccccckk
.kSSkccckccckkk.
..kkkkkkkkkkkk..
...kcccckcccck..
...kcccckcccck..
...kcccckcccck..
...kkkkk.kkkkk..
...kkkkk..kkk...
.........kkkk...
'''), side=G('''
................
.....kkkkk......
...kkSSSSSkk....
..kSSSSSSSSSk...
..kSSSSSSSSSSk..
.kSSSSSSkkkkkk..
.kSSSkSkSSSSSk..
.kSSSkSkSSSkSk..
.kSSkSSkSSSkSSk.
.kSSkSSkSSSSSSk.
.kSSkSSkSSSkkk..
.kSSSkSkkSSSk...
.kSSSkSSkkkk....
.kSSkSkcccck....
.kSSkkccccckk...
..kSkcccccckk...
...kcccccckSSk..
...kccccccckSkk.
...kkkkkkkkkkSk.
..kcccccccccckSk
..kccck..kcccckS
.kccck....kccck.
.kkkkk.....kkkkk
kkkkk......kkkkk
'''), side2=G('''
................
.....kkkkk......
...kkSSSSSkk....
..kSSSSSSSSSk...
..kSSSSSSSSSSk..
.kSSSSSSkkkkkk..
.kSSSkSkSSSSSk..
.kSSSkSkSSSkSk..
.kSSkSSkSSSkSSk.
.kSSkSSkSSSSSSk.
.kSSkSSkSSSkkk..
.kSSSkSkkSSSk...
.kSSSkSSkkkk....
.kSSkSkcccck....
.kSSkkccccckk...
..kSkcccccckk...
...kcccccckSSk..
...kccccccckSkk.
...kkkkkkkkkkSk.
...kccccccck.kSk
....kcccccck..kS
....kccccck.....
....kkkkkkkk....
....kkkkkkkk....
'''), legs=dict(front=['...kkkkkk.kkkk..', '....kkk..kkkkk..', '...kkkk.........']))

# the One-Armed Fisherman
SPRITES['yuweng'] = dict(pal=dict(k=0x0F, S=0x37, c=0x18), front=G('''
.......kk.....c.
......kcck....c.
.....kcccck...c.
....kcccccck..c.
..kccccccccck.c.
.kkkkkkkkkkkkkc.
...kSSSSSSSSk.c.
...kSkkSSkkSk.c.
...kSkkSSkkSk.c.
...kSSSSSSSSk.c.
...kSSkkkkSSk.c.
....kSSSSSSk..c.
...kkkSSSSkkkkc.
..kcccckSSkcckSk
..kccccckkcccSSk
..kcckcccccckkk.
..kkkkcccccck...
..kcckcccccck...
..kcckkkkkkkk...
...kkcccccck....
...kccccckcck...
...kkkkkk.kkkk..
...kkkkk..kkk...
.........kkkk...
'''), side=G('''
..............kc
.............kc.
......kk....kc..
.....kcck..kc...
....kcccck.c....
...kcccccckc....
.kcccccccccck...
kkkkkkkkkkkkkk..
...kkkkkSSSSk...
...kkkkSkSSkSk..
...kkkkSSSkkSSk.
...kkkkSSSSSSSk.
....kkkSSkkkkk..
....kkkSSSSSk...
.....kkSSSSSk...
....kcckSSSk....
...kcccckSkck...
...kccccckSSk...
...kkkkkkkkk....
..kcccccccccck..
..kccck..kcccck.
.kccck....kccck.
.kkkkk.....kkkkk
kkkkk......kkkkk
'''), side2=G('''
..............kc
.............kc.
......kk....kc..
.....kcck..kc...
....kcccck.c....
...kcccccckc....
.kcccccccccck...
kkkkkkkkkkkkkk..
...kkkkkSSSSk...
...kkkkSkSSkSk..
...kkkkSSSkkSSk.
...kkkkSSSSSSSk.
....kkkSSkkkkk..
....kkkSSSSSk...
.....kkSSSSSk...
....kcckSSSk....
...kcccckSkck...
...kccccckSSk...
...kkkkkkkkk....
...kccccccck....
....kcccccck....
....kccccck.....
....kkkkkkkk....
....kkkkkkkk....
'''), legs=dict(front=['...kkkkkk.kkkk..', '....kkk..kkkkk..', '...kkkk.........']))

# the Ghost-mask Warden of the Netherworld Sect
SPRITES['guimian'] = dict(pal=dict(k=0x0F, S=0x30, c=0x16), front=G('''
.......kk.......
......kcck......
.....kcccck.....
....kcckkcck....
...kcckSSkcck...
...kckSSSSkck...
..kcckSSSSkcck..
..kckkkSSkkkck..
..kckSSSSSSkck..
..kckSkkkkSkck..
..kckkSkkSkkck..
..kcckkSSkkcck..
.kccckkkkkkccck.
.kcccccccccccck.
kccccccSScccccck
kcccccSkkScccccc
kccccccSScccccck
kSSkcccccccckSSk
.kkccccccccccck.
..kccccckcccck..
..kccccckcccck..
..kcccckccccck..
..kkkkkkkkkkkkk.
...kkk....kkk...
'''), side=G('''
......kk........
.....kcck.......
....kcccck......
...kccccccck....
..kccccccccck...
..kcccccckSSk...
.kcccccckSSSSk..
.kccccccSkkSkk..
.kcccccckSSSSk..
.kccccccSSkkkk..
.kcccccckSkSk...
.kccccccckkkk...
.kccccccccck....
.kcccccccccck...
.kccccccckcck...
.kcccccccckck...
.kcccccccckSSk..
.kcccccccckkk...
.kccccccccck....
.kcccccccccck...
.kccccccccccck..
kcccccccccccck..
kkkkkkkkkkkkkk..
..kkk.....kkkk..
'''), side2=G('''
......kk........
.....kcck.......
....kcccck......
...kccccccck....
..kccccccccck...
..kcccccckSSk...
.kcccccckSSSSk..
.kccccccSkkSkk..
.kcccccckSSSSk..
.kccccccSSkkkk..
.kcccccckSkSk...
.kccccccckkkk...
.kccccccccck....
.kcccccccccck...
.kccccccckcck...
.kcccccccckck...
.kcccccccckSSk..
.kcccccccckkk...
.kccccccccck....
.kccccccccck....
.kccccccccck....
.kccccccccck....
.kkkkkkkkkkk....
...kkkkkkk......
'''), legs=dict(front=['....kkk....kkk..']))

# the Masked Man of the Stratagem Pavilion
SPRITES['masked'] = dict(pal=dict(k=0x0F, S=0x37, c=0x04), front=G('''
......kkkk......
....kkcccckk....
...kcccccccck...
..kcckcccckcck..
..kckcccccckck..
..kckSkkkkSkck..
..kckSSSSSSkck..
..kckSkkkkSkck..
..kckcccccckck..
..kckcccccckck..
..kcckcccckcck..
.kccccckkccccck.
.kccccSkkSccccck
.kcckccSSccckcck
.kcckcccccckkcck
.kSSkcccccckSSk.
..kkkkkkkkkkkk..
...kSSSSSSSSk...
...kkkkkkkkkk...
...kcccccccck...
...kccccckccck..
...kkkkkk.kkkk..
...kkkkk..kkk...
.........kkkk...
'''), side=G('''
................
.....kkkkkk.....
...kkcccccck....
..kcccccccccck..
..kcccccccccck..
.kcccccckkkkck..
.kccccckkSSSkk..
.kccccckSSkSSk..
.kccccckcccccck.
.kccccckccccck..
.kccccckcccck...
..kccccckkkk....
..kcccccckk.....
..kcccccccck....
...kcccccckk....
...kccccckcck...
...kcccccckck...
...kcccccckSSk..
...kkkkkkkkkk...
..kcccccccccck..
..kccck..kcccck.
.kccck....kccck.
.kkkkk.....kkkkk
kkkkk......kkkkk
'''), side2=G('''
................
.....kkkkkk.....
...kkcccccck....
..kcccccccccck..
..kcccccccccck..
.kcccccckkkkck..
.kccccckkSSSkk..
.kccccckSSkSSk..
.kccccckcccccck.
.kccccckccccck..
.kccccckcccck...
..kccccckkkk....
..kcccccckk.....
..kcccccccck....
...kcccccckk....
...kccccckcck...
...kcccccckck...
...kcccccckSSk..
...kkkkkkkkkk...
...kccccccck....
....kcccccck....
....kccccck.....
....kkkkkkkk....
....kkkkkkkk....
'''), legs=dict(front=['...kkkkkk.kkkk..', '....kkk..kkkkk..', '...kkkk.........']))
HEIGHTS = {'tiewusi': 24, 'qianwanli': 24, 'wenruyu': 24, 'xiaolian': 17, 'lihanshan': 24, 'yuweng': 24, 'guimian': 24, 'masked': 24}
