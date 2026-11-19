"""Hand-typed 48x56 portraits for the `nes` style (三國志 霸王の大陸-like Famicom look).

Every row is exactly 48 pixels and ends with '|'. One character = one pixel:
  '.' backdrop (black, NES $0F)   'k' a black line (also $0F)
  BG slots (per portrait below): skin, hair sheen, cloth, props ...
The sprite layer (*_SPR) holds the few overlay pixels real games put in sprites:
eye whites, lip colour, a hairpin, the headband, cheek blush.

Colours are indexes into the standard 2C02 palette (src/nes.py). nes.Pic.check() proves the
Famicom rules: backdrop + one 3-colour sub-palette per 16x16 attribute area (max 4),
sprites 3 colours per 8x8 tile (max 4 sprite sub-palettes, max 8 tiles per scanline).
"""
import nes

W, H = 48, 56

# ---------------------------------------------------------------- jeff
JEFF = '''
.....................hhhhhh.....................|
....................hhkhhhhh....................|
....................hkhhhhkh....................|
.....................khhhkk.....................|
.....................ssssss.....................|
................khhkhhkhhkhhkhhk................|
..............khhkhhhkhhhhkhhhkhhk..............|
.............khhkhhhkhhhhhhkhhhkhhk.............|
............khhkhhhkhhhhhhhhkhhhkhhk............|
...........khhkhhhkhhhhhhhhhhkhhhkhhk...........|
...........khkhhhkhhhhhhhhhhhhkhhhkhk...........|
..........khkhhhkhhhhhhhhhhhhhhkhhhkhk..........|
..........khhkhkhkSSSSSSSSSSSSkhkkhkkk..........|
..........khhkhSSSSSSSSSSSSSSSssskhkkk..........|
..........khhkSSSSSSSSSSSSSSSSSssskkhk..........|
..........khhkSSSSSSSSSSSSSSSSSssskkhk..........|
..........khhkSkkkkSSSSSSSSSSkkkkskhkk..........|
..........khkkSSSkkkkkSSSSkkkkkSSskkhk..........|
..........kkkkSSkkkkSSSSSSSSkkkkSskkkk..........|
...........SSSSkSSSSkSSSSSSkSSSSkSsSS...........|
..........SSsSkSSkkSSkkkkkkSSkkSSkssSS..........|
..........SsSSkSSkkSSkSSSskSSkkSSksSsS..........|
..........SsSSkSSSSSSkSSSskSSSSSSksSsS..........|
..........SSsSSkSSSSkSSSSsSkSSSSkSssSS..........|
...........SSSSSkkkkSSSSSsSSkkkkSSsSS...........|
............SSSSSSSSSSSSsSSSSSssssS.............|
.............SSSSSSSSSkSSkSSSSSssss.............|
..............SSSSSSSSssssSSSSSsss..............|
..............SSSSSSSSSSSSSSSSSsss..............|
..............SSSSSSSSSSSSSSSSSsss..............|
..............SSSSSSSkkkkkkSSSSsss..............|
...............SSSSSSSssssSSSSsss...............|
................SSSSSSSSSSSSSsss.........kk.kk..|
................SSSSSSSSSSSSSsss........kwwkwwk.|
.................SSSSSSSSSSSsss.........kwwwwwk.|
...................SSSSSSSsss............kwwwk..|
...................kkkkkkkkkk............kwwk...|
...................ssssssssss...........kwwk....|
.............CCCckSSkSSSSsskSSkcccc.....kwwk....|
..........CCCccccckSSkSSsskSSkccccddcc.kwwk.....|
.......CCCccccccccckSSkSskSSkcccccdddddkwwk.....|
.....CCCcccccccccccckSSkkSSkccccccddddkwwkc.....|
...CCCcccccccccccccccckSSkccccccccddddkwwkddc...|
..CCcccccccccccccccccckSSkcccccccccddkwwkdddddc.|
.CccccccccccccccccccckSSkcccccccccdddkwwkdddddc.|
CccccccccccccccccccckSSkccccccccccddkwwkdddddddc|
cccccccccccccccccccckSSkccccccccccddkwwkdddddddc|
ccccccccccccccccccckSSkcccccccccccdkwwkddddddddc|
ccccccccccccccccccckSSkcccccccccccdkwwkddddddddc|
cccccccccccccccccckSSkcccccccccccckwwkdddddddddc|
cccccccccccccccccckSSkcccccccccccckwwkdddddddddc|
ccccccccccccccccckSSkcccccccccccckwwkddddddddddc|
ccccccccccccccccckSSkcccccccccccckwwkddddddddddc|
cccccccccccccccckSSkcccccccccccckwwkdddddddddddc|
cccccccccccccccckSSkcccccccccccckwwkdddddddddddc|
cccccccccccccccckSSkccccccccccckwwkddddddddddddc|
'''
JEFF_SPR = '''
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
'''
JEFF_SLOTS = {'S': 0x37, 's': 0x27, 'h': 0x0C, 'C': 0x38, 'c': 0x18, 'd': 0x08, 'w': 0x10}
JEFF_PALETTES = [(0x37, 0x27, 0x0C), (0x38, 0x18, 0x08), (0x37, 0x27, 0x18), (0x18, 0x08, 0x10)]
JEFF_SPR_SLOTS = {'W': 0x30}
JEFF_SPR_PALETTES = [(0x30,)]

# ---------------------------------------------------------------- erin
ERIN = '''
................................................|
................................................|
................................................|
...................hhhhkhhhhh...................|
................hhhkhhhShhhhkhhh................|
..............hhhkhhhhkShkhhhhkhhh..............|
.............hhkhhhhhkhSShkhhhhhkhh.............|
............hhkhhhhhkhhSShhkhhhhhkhh............|
...........hhkhhhhhkhhhSShhhkhhhhhkhh...........|
..........hhkhhhhhkhhhhSShhhhkhhhhhkhh..........|
..........hhkhhhhkhhhSSSSSShhhkhhhhkhh..........|
..........hkhhhhkhhSSSSSSSSSShhkhhhhkh..........|
..........hkhhhkhSSSSSSSSSSSSsshkhhhkh..........|
.........hhkhhkhSSSSSSSSSSSSSSsshkhhkkh.........|
.........hhkhhkhSSSSSSSSSSSSSSsshkhhkkh.........|
.........hhkhhkhSSSkkkSSSSkkkSsshkhhkkh.........|
.........hhkhhkhSSkSSSSSSSSSSksshkhhkkh.........|
.........hhkhhkhSkSSSSSSSSSSSSkshkhhkkh.........|
.........hhkhhkhSSkkkkSSSSkkkksshkhhkkh.........|
.........hhkhhkhSSSkkSSSSSSkkSsshkhhkkh.........|
.........hhkhhkhSSSkkSSSSSSkkSsshkhhkkh.........|
.........hhkhhkhSSSSSSSSsSSSSSsshkhhkkh.........|
.........hhkhhkhSSSSSSSSsSSSSSsshkhhkkh.........|
.........hhkhhkhSSSSSSSssSSSSSsshkhhkkh.........|
.........hhkhhkhSSSSSSSSSSSSSSsshkhhkkh.........|
.........hhkhhkkSSSSSSkkkkSSSSsskkhhkkh.........|
.........hhkhhkkkSSSSSSSSSSSSsskkkhhkkh.........|
.........hhkhhkkkkSSSSSSSSSSsskkkkhhkkh.........|
.........hhkhhkkkkkSSSSSSSSsskkkkkhhkkh.........|
.........hhkhhkkkkkkSSSSSSsskkkkkkhhkkh.........|
.........hhkhhkkkkkkkSSSSsskkkkkkkhhkkh.........|
.........hhkhhkkkkkkkkkkkkkkkkkkkkhhkkh.........|
.........hhkhhkhkkkksssssssskkkkhkhhkkh.........|
.........hhkhhkhkkkkSSSSSSsskkkkhkhhkkh.........|
.........hhkhhkhkkkkSSSSSSsskkkkhkhhkkh.........|
.........hhkhhkhkkkkSSSSSSsskkkkhkhhkkh.........|
........hhkhhkhkkkkkSSSSSSsskkkkkhkhhkkh........|
........hhkhhkhkckSSkSSSSsskSSkckhkhhkkh........|
........hhkhhkhkcckSSkSSsskSSkcckhkhhkkh........|
........hhkhhkhkccckSSkSskSSkccckhkhhkkh........|
.....CCchhkhhkhkcccckSSkSSkccccckhkhhkkhcdd.....|
...CCccchhkhhkhkcccccckSSkcccccckhkhhkkhcccdd...|
..CCcccchhkhhkhkcccccckSSkcccccckhkhhkkhccccdd..|
.CCccccchhkhhkhkccccckSSkccccccckhkhhkkhcccccdd.|
CccccccchhkhhkhkccccckSSkccccccckhkhhkkhccdddddd|
CccccccchhkhhkhkcccckSSkcccccccckhkhhkkhccdddddd|
CccccccchhkhhkhkcccckSSkcccccccckhkhhkkhccdddddd|
CccccccchhkhhkhkccckSSkccccccccckhkhhkkhccdddddd|
cccccccchhkhhkhkccckSSkccccccccckhkhhkkhccdddddd|
cccccccchhkhhkhkcckSSkcccccccccckhkhhkkhccdddddd|
ccccccccchhkhhkhcckSSkcccccccccchkhhkhhdccdddddd|
cccccccccchhkhhhckSSkccccccccccchhhkhhddccdddddd|
ccccccccccccccccckSSkcccccccccccccccddddccdddddd|
cccccccccccccccckSSkccccccccccccccccddddccdddddd|
cccccccccccccccckSSkccccccccccccccccddddccdddddd|
cccccccccccccccckSSkccccccccccccccccddddccdddddd|
'''
ERIN_SPR = '''
................................................|
................................................|
................................................|
................................................|
................................................|
.................................GG.............|
................................GGG.............|
...............................YyG..............|
..............................Yy................|
.............................Yy.................|
............................Y...................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
..................W..W....W..W..................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
.......................rr.......................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
'''
ERIN_SLOTS = {'S': 0x37, 's': 0x27, 'h': 0x0C, 'C': 0x2C, 'c': 0x1C, 'd': 0x0C}
ERIN_PALETTES = [(0x37, 0x27, 0x0C), (0x2C, 0x1C, 0x0C), (0x37, 0x27, 0x1C)]
ERIN_SPR_SLOTS = {'W': 0x30, 'r': 0x26, 'Y': 0x28, 'y': 0x18, 'G': 0x2A, 'g': 0x1A}
ERIN_SPR_PALETTES = [(0x30, 0x26, 0x16), (0x28, 0x18, 0x2A)]

# ---------------------------------------------------------------- josh
JOSH = '''
.....................hhhhhh.....................|
....................hhkhhhhh....................|
....................hkhhhhkh....................|
....................hkhhhkhh....................|
.....................khhkhk.....................|
................khhkhhkkkkhhkhhk................|
..............khhhkhhhkhhkhhhkhhhk..............|
.............khhhkhhhkhhhhkhhhkhhhk.............|
............khhhkhhhkhhhhhhkhhhkhhhk............|
...........khhhkhhhkhhhhhhhhkhhhkhhhk...........|
...........khhkhhhkhhhhhhhhhhkhhhkhhk...........|
..........khhkhhhkhhhhhhhhhhhhkhhhkhhk..........|
..........khkhhhkhhhhhhhhhhhhhhkhhhkhk..........|
..........khkShhhShhhhShhhShhhhShhskhk..........|
..........hhkSShSSShhSSShSSShhSShsskhh..........|
..........hhSSSSSSSSSSSSSSSSSSSSSssshh..........|
..........hkSSSkkkkSSSSSSSSSSkkkkssskh..........|
..........hhSSSSSSkkSSSSSSSSkkSSSssshh..........|
..........hhSSSSSSSSSSSSSSSSSSSSSssshh..........|
..........SSSSSSkkkkSSSSSSSSkkkkSsssSS..........|
.........SSsSSSSSkkSSSSSSSSSSkkSSssssSS.........|
.........SsSSSSSSkkSSSSSSSSSSkkSSsssSsS.........|
.........SsSSSSSSkkSSSSSSSSSSkkSSsssSsS.........|
.........SSsSSSSSSSSSSSSSSSSSSSSSssssSS.........|
..........SSSSSSSSSSSSSSsSSSSSSSSsssSS..........|
............SSSSSSSSSSSssSSSSSSSSsss............|
.............SSSSSSSSSSSSSSSSSSSsss.............|
..............SSSSSSSkSSSSkSSSSsss..............|
...............SSSSSSSkkkkSSSSsss...............|
................SSSSSSSSSSSSSsss................|
..................SSSSSSSSSsss..................|
...................kkkkkkkkkk...................|
....................ssssssss....................|
....................SSSSSSss....................|
....................SSSSSSss....................|
....................SSSSSSss....................|
..............ccckSSkSSSSsskSSkcdd..............|
...........ccccccckSSkSSsskSSkccddddd...........|
.........cccccccccckSSkSskSSkcccccddddd.........|
.......ccccccccccccckSSkSSkcccccccccddddd.......|
.....ccccccccccccccccckSSkccccccccccccddddd.....|
....cccccccccccccccccckSSkcccccccccccccddddd....|
kkkkccccccccccccccccckSSkcccccccccccccccddddd...|
kYYYYkkcccccccccccccckSSkccccccccccccccccddddd..|
YYwwwYYYkccccccccccckSSkccccccccccccccccccddddd.|
wwwkwwwYYkcccccccccckSSkcccccccccccccccccccddddd|
wwwkwwwwwYkcccccccckSSkccccccccccccccccccccddddd|
wwkwwwwkwwYkccccccckSSkccccccccccccccccccccddddd|
wwkwwwwkwwwYkccccckSSkcccccccccccccccccccccddddd|
wwkwwwwkwwwwYkcccckSSkcccccccccccccccccccccddddd|
wkwwwwwkwwwwYkccckSSkccccccccccccccccccccccddddd|
wkwwwwkwwwwwwYkcckSSkccccccccccccccccccccccddddd|
wkwwwwkwwwwwwYkckSSkcccccccccccccccccccccccddddd|
kwwwwwkwwwwwwwYkkSSkcccccccccccccccccccccccddddd|
kwwwwwkwwwwwwwYkkSSkcccccccccccccccccccccccddddd|
kwwwwkwwwwwwwwYkkSSkcccccccccccccccccccccccddddd|
'''
JOSH_SPR = '''
................................................|
................................................|
................................................|
................................................|
................................................|
......................YYYY......................|
................................................|
................................................|
................................................|
................................................|
................................................|
..........YYYYYYYYYYYYYYYYYYYYYYYYYYYY..........|
..........yyyyyyyyyyyyyyyyyyyyyyyyyyyyYy........|
......................................yY........|
.......................................Y........|
.......................................y........|
................................................|
................................................|
................................................|
................................................|
................W..W........W..W................|
................................................|
................................................|
................................................|
..............pp................pp..............|
..............pp................pp..............|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
'''
JOSH_SLOTS = {'S': 0x37, 's': 0x27, 'h': 0x0C, 'C': 0x26, 'c': 0x16, 'd': 0x06, 'Y': 0x28, 'w': 0x18}
JOSH_PALETTES = [(0x37, 0x27, 0x0C), (0x26, 0x16, 0x06), (0x37, 0x27, 0x16), (0x16, 0x18, 0x28)]
JOSH_SPR_SLOTS = {'W': 0x30, 'p': 0x35, 'Y': 0x38, 'y': 0x28}
JOSH_SPR_PALETTES = [(0x30, 0x35, 0x26), (0x38, 0x28, 0x18)]

# ---------------------------------------------------------------- jasper
JASPER = '''
................................................|
................................................|
................................................|
.............hhh................hhh.............|
............hkhhh..............hkhhh............|
...........hkhhkhh............hkhhkhh...........|
...........hkhhhkh............hkhhhkh...........|
...........hhkkhkh............hhkkhkh...........|
............hhhkh.hhhhhkkhhhhh.hhhkh............|
.............hhhkhhhkhhkkhhkhhhkhhh.............|
...............khhhkhhkhhkhhkhhhk...............|
..............khhhkhhkhhhhkhhkhhhk..............|
.............khhhkhhkhhhhhhkhhkhhhk.............|
.............khhkhhkhhhhhhhhkhhkhhk.............|
............khhhhhhhhhhhhhhhhhhhhhhk............|
............khhhkhhhhkhhhhkhhhhkhhhh............|
............hkShhShhhShhShhhShhshskh............|
............hSSShSShSSShSShSSShSsssh............|
............hSSSkkSSSSSSSSSSSSkksssh............|
............hSSSSSkkSSSSSSSSkkSSsssh............|
...........SSSSSkkkkSSSSSSSSkkkksssSS...........|
..........SSsSSSSkkSSSSSSSSSSkkSssssSS..........|
..........SsSSSSSkkSSSSSSSSSSkkSsssSsS..........|
..........SsSSSSSSSSSSSSSSSSSSSSsssSsS..........|
..........SSsSSSSSSSSSSSSSSSSSSSssssSS..........|
...........SSSSSSSSSSSSSsSSSSSSSsssSS.kk...kk...|
.............SSSSSSSSSSssSSSSSSSsss..ksSk.ksSk..|
..............SSSSSSSSSSSSSSSSSsss...ksSk.ksSk..|
...............SSSSSSSSSSSkSSSsss....ksSk.ksSk..|
................SSSSSSkkkkSSSsss......ksSkSsk...|
.................SSSSSSSSSSSsss.......kssSssk...|
...................SSSSSSSsss..........ksSsk....|
...................kkkkkkkkkk..........ksssk....|
....................ssssssss...........ksssk....|
....................SSSSSSss...........ksssk....|
....................SSSSSSss...........ksssk....|
....................SSSSSSss...........ksssk....|
....................SSSSSSss...........ksssk....|
..............CCckSSkSSSSsskSSkcdd.....ksssk....|
...........CCCcccckSSkSSsskSSkccddddd..ksssk....|
.........CCCccccccckSSkSskSSkcccccdddddksssk....|
.......CCCcccccccccckSSkSSkcccccccccdddddssk....|
......CCCccccccccccccckSSkcccccccccccdddddsk....|
.....CCCcccccccccccccckSSkccccccccccccddddd.....|
....CCCcccccccccccccckSSkccccccccccccccddddd....|
...CCCccccccccccccccckSSkcccccccccccccccddddd...|
..CCCccccccccccccccckSSkcccccccccccccccccddddd..|
.ccccccccccccccccccckSSkccccccccccccccccccddddd.|
ccccccccccccccccccckSSkccccccccccccccccccccddddd|
ccccccccccccccccccckSSkccccccccccccccccccccddddd|
cccccccccccccccccckSSkcccccccccccccccccccccddddd|
cccccccccccccccccckSSkcccccccccccccccccccccddddd|
ccccccccccccccccckSSkccccccccccccccccccccccddddd|
ccccccccccccccccckSSkccccccccccccccccccccccddddd|
cccccccccccccccckSSkcccccccccccccccccccccccddddd|
cccccccccccccccckSSkcccccccccccccccccccccccddddd|
'''
JASPER_SPR = '''
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................W..W........W..W................|
................................................|
................................................|
................................................|
...............pp..............pp...............|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
'''
JASPER_SLOTS = {'S': 0x37, 's': 0x27, 'h': 0x0C, 'C': 0x2A, 'c': 0x1A, 'd': 0x0A, 'w': 0x18}
JASPER_PALETTES = [(0x37, 0x27, 0x0C), (0x2A, 0x1A, 0x0A), (0x37, 0x27, 0x1A), (0x1A, 0x0A, 0x27)]
JASPER_SPR_SLOTS = {'W': 0x30, 'p': 0x35}
JASPER_SPR_PALETTES = [(0x30, 0x35, 0x26)]

# ---------------------------------------------------------------- guanyu
GUANYU = '''
....................kGGkgg......................|
..................GkGGgkgggg....................|
................GGkkkkGggggggggg................|
..............GGGkkkkkkkkkkkkkkggg..............|
............GkkkkGGGGGGggggggggkkkkg............|
...........GGGGGGGGGGGGgggggggggggggg...........|
..........GGGGGGGkkkkkkkkkkkkkkggggggg..........|
..........kkkkkkkGGGGGGggggggggkkkkkkk..........|
.........GGGGGGGGGGGGGGgggggggggggggggg.........|
.........GGGGGGGGGGGGGGgggggggggggggggg.........|
.........GGGGGGGGGGGGGGgggggggggggggggg.........|
.........kkkkkkkkkkkkkkkkkkkkkkkkkkkkkk.........|
.........kGGGGGGGGGGGGGGggggggggggggggk.........|
.........kGGGkkkkkkkkkkkkkkkkkkkkkgggk..........|
.........kGGkRRRRRRRRRRRRRRRRRRRRRRkggk.........|
.........kGGkRRkkkkkkRRRRRRkkkkkkRRkggk.........|
.............RRRRRkkkkRRRRkkkkRRRRR.............|
...........LLLkLLLLLLLLLLRRRRRRRRkRRR...........|
...........LRLLkkkkkkLLLLRRkkkkkkRRRR...........|
...........LRLLLLkkkLLLLLRRRkkkRRRRRR...........|
...........LLLLLLLLLLLRLRRRRRRRRRRRRR...........|
...........LRkLLLLLLLLLRRRRRRRRRRRkRR...........|
.............kLLLRLLLLLRLRRRRRRRRRk.............|
.............kkLLRLLLLkRRkRRRRRRRkk.............|
.............kkkLLLLLLRRRRRRRRRRkkk.............|
.............kkkkvvvvkkkkkkvvvvkkkk.............|
.............kkvkkvkkRLLLRRkkvkkvkk.............|
..............kkvkkvkkkkvkkkvkkvkk..............|
..............kkkvkvkkkkvkkkvkvkkk..............|
...............kkvkkvkkkvkkvkkvkk...............|
...............kkkvkvkkvkkkvkvkkk...............|
................kkkvkvkvkkvkvkkk................|
....CCCcccccccCkxkkxkkxkkxkkxkkxkCccccdddddd....|
..CCCcccccccccCkxkkxkkkxxkkkxkkxkCccccccdddddd..|
.CCCccccccccccCkxkkxkkkxxkkkxkkxkCcccccccdddddd.|
CCCccccccccccccCkkkxxkkxxkkxxkkkCcccccccccdddddd|
CCCccccccccccccCkkkkxkkxxkkxkkkkCcccccccccdddddd|
CCCccccccccccccCkxkkxkkxxkkxkkxkCcccccccccdddddd|
CCCcccccccccccccCkkkxkkxxkkxkkkCccccccccccdddddd|
CCCcccccccccccccCkkkxkkkkkkxkkkCccccccccccdddddd|
CCCcccdcccccccccCkkkxkkkkkkxkkkCccccccccckdddddd|
CCCcccdccccccccccCkkxxkkkkxxkkCcccccccccckdddddd|
CCCcccdccccccccccCkkkxkkkkxkkkCcccccccccckdddddd|
CCCccccdcccccccccCkkkxkkkkxkkkCccccccccckcdddddd|
CCCccccdccccccccccCkkxkkkkxkkCcccccccccckcdddddd|
CCCccccdccccccccccCkkxkkkkxkkCcccccccccckcdddddd|
CCCcccccdcccccccccCkkxkkkkxkkCccccccccckccdddddd|
CCCcccccdccccccccccCkxxkkxxkCcccccccccckccdddddd|
CCCcccccdccccccccccCkkxkkxkkCcccccccccckccdddddd|
CCCccccccdcccccccccCkkxkkxkkCccccccccckcccdddddd|
CCCccccccdccccccccccCkxkkxkCcccccccccckcccdddddd|
CCCccccccdccccccccccCkxkkxkCcccccccccckcccdddddd|
CCCcccccccdcccccccccCkxkkxkCccccccccckccccdddddd|
CCCcccccccdcccccccccCkxxxxkCccccccccckccccdddddd|
CCCcccccccdcccccccccCkkxxkkCccccccccckccccdddddd|
CCCccccccccdccccccccCkkxxkkCcccccccckcccccdddddd|
'''
GUANYU_SPR = '''
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
................................................|
'''
GUANYU_SLOTS = {'L': 0x26, 'R': 0x16, 'v': 0x0C, 'x': 0x0C, 'G': 0x2A, 'g': 0x1A, 'C': 0x2A, 'c': 0x1A, 'd': 0x0A}
GUANYU_PALETTES = [(0x26, 0x16, 0x0C), (0x2A, 0x1A, 0x16), (0x2A, 0x1A, 0x0A), (0x2A, 0x1A, 0x0C)]
GUANYU_SPR_SLOTS = {'W': 0x30}
GUANYU_SPR_PALETTES = [(0x30,)]

PORTRAITS = {
    'jeff': (JEFF, JEFF_SPR, JEFF_SLOTS, JEFF_PALETTES, JEFF_SPR_SLOTS, JEFF_SPR_PALETTES),
    'erin': (ERIN, ERIN_SPR, ERIN_SLOTS, ERIN_PALETTES, ERIN_SPR_SLOTS, ERIN_SPR_PALETTES),
    'josh': (JOSH, JOSH_SPR, JOSH_SLOTS, JOSH_PALETTES, JOSH_SPR_SLOTS, JOSH_SPR_PALETTES),
    'jasper': (JASPER, JASPER_SPR, JASPER_SLOTS, JASPER_PALETTES, JASPER_SPR_SLOTS, JASPER_SPR_PALETTES),
    'guanyu': (GUANYU, GUANYU_SPR, GUANYU_SLOTS, GUANYU_PALETTES, GUANYU_SPR_SLOTS, GUANYU_SPR_PALETTES),
}

# the 龍門武林 cast lives in its own file
import nes_longmen  # noqa: E402
PORTRAITS.update(nes_longmen.PORTRAITS)

# 三國志 霸王之路: Jeff as main general + the stage generals
import nes_sango  # noqa: E402
PORTRAITS.update(nes_sango.PORTRAITS)


def pic(cid):
    bg, spr, slots, pals, sslots, spals = PORTRAITS[cid]
    p = nes.Pic(nes.parse(bg, W, H, cid), slots, pals, sprite=nes.parse(spr, W, H, cid + ' sprite'),
                sprite_slots=sslots, sprite_palettes=spals, name=cid)
    p.check()            # raises if a Famicom rule is broken
    return p


def portrait(cid):
    return pic(cid).image()
