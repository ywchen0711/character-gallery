"""龍門武林 (Longmen Wulin) cast in the 8-bit `nes` style: hand-typed 48x56 portraits and 16x24 field sprites.

Same rules as nes_portraits.py / nes_sprites.py. A row written 'N:content' is N backdrop pixels then the content,
padded with backdrop to 48 (see nes.parse). Colours are 2C02 palette indexes; nes.Pic.check() proves the
Famicom rules (one 3-colour sub-palette per 16x16 area, max 4; sprite overlays 3 colours per 8x8 tile).
"""

# ---------------------------------------------------------------- 奕叡 Yi Rui
# indigo robe over a white inner robe, a blue headband whose ties fly behind him, a high tail through a silver ring,
# sword brows; the ring-pommel saber on his back shows over his right shoulder
YIRUI = '''
......................khhk......................|
.....................khhhhk.....................|
.....................khhhhk.....................|
.....................kkkkkk.....................|
....................khhhhhhk....................|
................kkkkhhkhhkhhkkkk................|
..............kkhhhhhkhhhhkhhhhhkk..............|
.............khhhhhkhhhhhhhhkhhhhhk.............|
............khhhhhkhhhhhhhhhhkhhhhhk............|
............khhhhkhhhhhhhhhhhhkhhhhk............|
...........khhhhkhhhhhhhhhhhhhhkhhhhk.kkkkk.....|
...........khhhkhhhhhhhhhhhhhhhhkhhhkbbbbbbkk...|
...........kbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbk..|
...........kbbbbbbbbbbbbbbbbbbbbbbbbbbkkkkkkkk..|
...........khSSSSSSSSSSSSSSSSSSSSSShkbbbbbbbk...|
...........khSSSSSSSSSSSSSSSSSSSSSShkkkkkkkk....|
..........khhSSSSSSSSSSSSSSSSSSSssshhk..........|
..........khhSkkkSSSSSSSSSSSSSSkkkshhk..........|
..........khhSSkkkkkSSSSSSSSkkkkksshhk..........|
..........khhSSSSSkkkSSSSSSkkkSSssshhk..........|
..........khhSSSSSSSSSSSSSSSSSSSssshhk..........|
..........khkSSSkkkkkSSSSSSkkkkkSsskhk..........|
..........kSsSSSSSkkSSSSSSSSkkSSsssskk..........|
..........kSsSSSSSkkSSSSSSSSkkSSsssskk..........|
..........kSkSSSSSSSSSSSsSSSSSSSssskhk..........|
..........khhSSSSSSSSSSSsSSSSSSsssshhk..........|
..........khhSSSSSSSSSSSssSSSSSsssshhk..........|
..........khhkSSSSSSSSSkskSSSSsssskhhk..........|
..........khhkSSSSSSSSSSSSSSSSsssskhhk..........|
..........khh.kSSSSSSkkkkkkSSssssk.hhk..........|
..........khh..kSSSSSSSssSSSssssk..hhk..........|
..........khh...kSSSSSSSSSSssssk...hhk..........|
...kkkk...kkk....kSSSSSSSSssssk....kkk..........|
..kwwwwk..........kkSSSSsssskk..................|
..kwkkwk...........kkkkkkkkkk...................|
..kwkkwk...........kssssssssk...................|
..kwwwwk...........kSSssssssk...................|
...kCck............kSSSsssssk...................|
...kcCk......kCCckSSkSSSSsskSSkccck.............|
..kwwwwwwkkCCCcccckSSkSSsskSSkccccccck..........|
.......kCCCcccccccckSSkSskSSkccccccccccck.......|
.....kCCCccccccccccckSSkkSSkcccccccccccccck.....|
...kCCCccccccccccccccckSSkcccccccccccccccccck...|
..kCCccccccccccccccccckSSkccccccccccccccccccck..|
.kCCccccccccccccccccckSSkccccccccccccccccccccck.|
CCccccccCkcccccccccckSSkcccccccccccccckccccccccc|
CCccccccCkcccccccccckSSkcccccccccccccckccccccccc|
CCccccccCkccccccccckSSkccccccccccccccckccccccccc|
CCcccccCkcccccccccckSSkcccccccccccccccckcccccccc|
CCcccccCkccccccccckSSkccccccccccccccccckcccccccc|
CccccccckccccccccckSSkccccccccccccccccckcccccccc|
CccccccckcccccccckSSkcccccccccccccccccckcccccccc|
CccccccckcccccccckSSkcccccccccccccccccckcccccccc|
CcccccckcccccccckSSkcccccccccccccccccccckccccccc|
CcccccckcccccccckSSkcccccccccccccccccccckccccccc|
CcccccckcccccccckSSkcccccccccccccccccccckccccccc|
'''
YIRUI_SPR = '''
.
.
.
22:WWWW
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
17:W..W......W..W
'''
YIRUI_SLOTS = {'S': 0x37, 's': 0x27, 'h': 0x0C, 'b': 0x11, 'C': 0x12, 'c': 0x02, 'w': 0x10}
YIRUI_PALETTES = [(0x37, 0x11, 0x0C), (0x37, 0x27, 0x0C), (0x37, 0x27, 0x02), (0x12, 0x02, 0x10)]
YIRUI_SPR_SLOTS = {'W': 0x30}
YIRUI_SPR_PALETTES = [(0x30,)]

YISHUO = '''
...............k........k.......k...............|
...............kk......khk.....kk...............|
...........k...khk....khhk....khk...k...........|
...........kk..khhk..khhhhk..khhk..kk...........|
...........khk.khhhkkhhhhhhkkhhhk.khk...........|
...........khhkkhhhhhhhhhhhhhhhhkkhhk...........|
..........kkhhhhhhhhhhhhhhhhhhhhhhhhkk..........|
..........khhhhhhhhhhhhhhhhhhhhhhhhhhk..........|
..........kbbbbbbbbbbbbbbbbbbbbbbbbbbkkkkk......|
..........kbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbk.....|
..........kbbbbbbbbbbbbbbbbbbbbbbbbbbkbkbbbk....|
..........khhhhhhhhhhhhhhhhhhhhhhhhhhkk.kkk.....|
..........khhhSShhhSSShhhhSSShhhSShhhk..........|
..........khhSSSShSSSSShhSSSSShSSSShhk..........|
..........khSSSkkkkSSSSSSSSSSkkkkSSShk..........|
..........khSSSSSSSSSSSSSSSSSSSSSSSShk..........|
..........khSSSSkkkkSSSSSSSSkkkkSssshk..........|
..........kSSSSSSkkSSSSSSSSSSkkSSssssk..........|
..........kSSSSSSkkSSSSSSSSSSkkSSssssk..........|
..........kSSSSSSkkSSSSSSSSSSkkSsssssk..........|
..........kkSSSSSSSSSSSSSSSSSSSSsssskk..........|
..........khSSSSSSSSSSSSsSSSSSSSsssshk..........|
..........khSSSSSSSkSSSssSSSSSSssssshk..........|
..........khSSSSSSSSSSSSSSSSSSSssssshk..........|
...........kSSSSSSSkSSSSSSkSSsssssk.............|
...........kSSSSSSSSkkkkkkSSSsssssk.............|
............kSSSSSSSSSssSSSSsssssk..............|
.............kSSSSSSSSSSSSsssssk................|
..............kkSSSSSSSSsssskk..................|
................kkkSSSSsssskkk..................|
...................kkkkkkkkkk...................|
...................kSSssssssk...................|
...................kSSssssssk...................|
...................kSSSsssssk...................|
.............kCCckSSkSSSSsskSSkccck.............|
..........kCCCcccckSSkSSsskSSkccccccck..........|
........kCCCcccccckSSkSskSSkccccccccck..........|
......kCCCccccccccckSSkkSSkcccccccccccck........|
....kCCCcccccccccccccckSSkcccccccccccccccck.....|
...kCCcccccccccccccccckSSkcccccccccccccccccck...|
..kCCcccccccccccccccckSSkcccccccccccccccccccck..|
.kCCccccccccccccccccckSSkccccccccccccccccccccck.|
CCccccccccccccccccccckSSkcccccccccccckcccccccccc|
CCccccccccccccccccccckSSkccccccccccccckccccccccc|
CCcccckkkkkccccccccckSSkcccccccccccccckccccccccc|
CCcckkwwwwwkkccccccckSSkcccccccccccccckccccccccc|
CCckkwwwwwwwkkccccckSSkccccccccccccccckccccccccc|
CCkkkwwkkkwwkkkcccckSSkccccccccccccccckccccccccc|
CckkwwkkkkkwwkkccckSSkccccccccccccccccckcccccccc|
CkkwwwkkkkkwwwkkcckSSkccccccccccccccccckcccccccc|
CkwwwwwkkkwwwwwkckSSkcccccccccccccccccckcccccccc|
CkwwwwwwwwwwwwwkckSSkcccccccccccccccccckcccccccc|
CkkwwwwwwwwwwwkkkSSkccccccccccccccccccckcccccccc|
CkkkwwwwkwwwwkkkkSSkcccccccccccccccccccckccccccc|
CkkwwwwkkkwwwwkkkSSkcccccccccccccccccccckccccccc|
CckwwwkkkkkwwwkckSSkcccccccccccccccccccckccccccc|
'''

YISHUO_SPR = '''
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
16:W..W........W..W
.
.
.
.
.
15:pp..............pp
15:pp..............pp
'''
YISHUO_SLOTS = {'S': 0x37, 's': 0x27, 'h': 0x0C, 'b': 0x16, 'C': 0x26, 'c': 0x16, 'w': 0x30}
YISHUO_PALETTES = [(0x37, 0x16, 0x0C), (0x37, 0x27, 0x0C), (0x37, 0x27, 0x16), (0x26, 0x16, 0x30)]
YISHUO_SPR_SLOTS = {'W': 0x30, 'p': 0x35}
YISHUO_SPR_PALETTES = [(0x30, 0x35, 0x26)]

XIAOTIAN = '''
................................................|
................................................|
....kk....................................kk....|
....kgk............k.....................kgk....|
....kggk..kk......khk...............kk..kggk....|
.....kggkkgk.....kkWhkkkhhkkkkk.....kgkkggk.....|
.....kgggkgk...kkWWhhhhkhhhhhhhkk...kgkgggk.....|
......kggkk...kWWhhhhhhkhhhhhhkhhk...kkggk......|
.......kgggk.kWhhhWhhhhkhhhhhhhkhhk.kgggk.......|
........kgggkWhhhWhhhhhkhhhhhhhhkhhkgggk........|
.........kgggkhhWhhhhhhkhhhhhhhhhkkgggk.........|
..........kgggkWhhhhhhhkhhhhhhhhhkgggk..........|
.........kWkggkhhhhhhhhkhhhhhhhhhkggkhk.........|
........kWhkgggggkWkgggggggggkhkggggkhhk........|
........kWhkgggggkWkgggggggggkhkggggkhhk........|
........kWhhhkkkkkkkWhkkkkkkkhkkkkkhhhhk........|
........kWhhhkSSSSSWkSSSSSSSShkhhkhhhhk.........|
........kWhhhkSkkSSSSSSSSSSSSSSkkhkhhhhk........|
........kWhhhkSShkkkSSSSSSSSkkkhhhkhhhhk........|
........kWhhhkSSSShkkkSSSSkkkhSShhkhhhhk........|
........kWhhhkSkkkkkSSSSSSSSkkkkkhkhhhhk........|
........kWhhhkSSWkkkkSSSSSSkkkkWhhkhhhhk........|
........kWhhhkSSSSSSSSSSSSSSSSSSShkhhhhk........|
........kWhhhkSSSSSSSSSShSSSSSSSShkhhhhk........|
........kWhhhkSSSSSSSSSShSSSSSSShhkhhhhk........|
........kWhhhkSSSSSSSSSShhSSSSSShhkhhhhk........|
........kWhhhkSSSSSSSSkhhkSSSSSShhkhhhhk........|
........kWhhhkSSSSSSSSSSSSSSSSSShhkhhhhk........|
........kWhhhkkSSSSSSSSSSSSkSSShhkkhhhhk........|
........kWhhhk.kSSSSkkkkkkkSSShhk.khhhhk........|
........kWhhhk..kSSSSShhSSSSShhk..khhhhk........|
........kWkhkk...kSSSSSSSSSShhk...kkhkhk........|
.........k.k......kkSSSSSSSSkk......k.k.........|
....................kkkkkkkk....................|
...................kSSSSSSSSk...................|
...................kSSSSSSkkk...................|
................kgggkSSSSSSkgggk................|
...............kggggkSSSSSSkggggk...............|
.............kkkgkgggrrrrrrgggkkkkk.............|
..kk......kkkkkkkkkgggrrrrgggkkkkkkkkk..........|
.......grgkkkgkkkkkkgggrrgggkkkgkkkkkggrg.......|
.....grrrgkkkkkkkkkkkggkkggkkkkkkkkkkkgrrdg.....|
...grdrrrggkkkkkgkkkkkkggkkkgkkkkkgkkkgrrdrrg...|
..grrdrrrgkkkkkkkkkkkkkggkkkkkkkkkkkkkgrrdrrrg..|
.grrrdrrrgkkkgkkkkkgkkggkgkkkkkgkkkkkggrrdrrrdg.|
rdrrrdrrrgkkkkkkkkkkkggkkkkkkkkkkkkkkkgrrdrrrdrr|
rdrrrdrrrggkkkkkgkkkkggkkkkkgkkkkkgkkkgrrdrrrdrr|
rdrrrdrrrgkkkkkkkkkkggkkkkkkkkkkkkkkkkgrrdrrrdrr|
rdrrrdrrgkkkkgkkkkkkggkkkgkkkkkgkkkkkgkgrdrrrdrr|
rdrrrdrrgkkkkkkkkkkggkkkkkkkkkkkkkkkkkkgrdrrrdrr|
rdrrrdrrgkgkkkkkgkkggkgkkkkkgkkkkkgkkkkgrdrrrdrr|
rdrrrdrrgkkkkkkkkkggkkkkkkkkkkkkkkkkkkkgrdrrrdrr|
rdrrrdrrgkkkkgkkkkggkkkkkgkkkkkgkkkkkgkgrdrrrdrr|
rdrrrdrgkkkkkkkkkggkkkkkkkkkkkkkkkkkkkkkgdrrrdrr|
rdrrrdrgkkgkkkkkkggkkkgkkkkkgkkkkkgkkkkkgdrrrdrr|
rdrrrdrgkkkkkkkkkggkkkkkkkkkkkkkkkkkkkkkgdrrrdrr|
'''

XIAOTIAN_SPR = '''
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
23:rr
23:rr
.
.
.
.
.
.
.
16:dddd......dddd
'''
XIAOTIAN_SLOTS = {'S': 0x37, 'h': 0x10, 'W': 0x30, 'g': 0x28, 'r': 0x16, 'd': 0x06}
XIAOTIAN_PALETTES = [(0x30, 0x10, 0x28), (0x37, 0x10, 0x30), (0x37, 0x16, 0x28), (0x28, 0x16, 0x06)]
XIAOTIAN_SPR_SLOTS = {'W': 0x30, 'r': 0x16, 'd': 0x06}
XIAOTIAN_SPR_PALETTES = [(0x30, 0x16, 0x06)]

BAIXIAN = '''
................................................|
................................................|
..................kkkkkkkkkkkk..................|
.................kGGGGGGGGGGkk..................|
.................kGGGGGGGGGkkk..................|
.................kGGGGGGGGGkkk..................|
..............kkkkkkkkkkkkkkkkkkkk..............|
..............khhhhhhhhhGGGGGGGGGk..............|
..............khGGGGGGGGkGGGGGGGkk..............|
..............khGGGGGGGGkGGGGGGGkk..............|
..............khGGGGGGGGkGGGGGGGkk..............|
..............khGGGGGGGGkGGGGGGGkk..............|
.............khhhhhhhhhhhhhhhhhhhhk.............|
.............kkkkkkkkkkkkkkkkkkkkkk.............|
............kGGSSSSSSSSSSSSSSSSSSGGk............|
............kGGSSSSSSSSSSSSSSSSSSGGk............|
...........kGGSSSSSSSSSSSSSSSSSSssGGk...........|
...........kGGSSSkkkkSSSSSSkkkkSssGGk...........|
...........kGGSSSSSSSSSSSSSSSSSSssGGk...........|
...........kGkSSSSkkSSSSSSSSkkSSsskGk...........|
...........kSsSsSkSSkSSSSSSkSSkSssskk...........|
...........kSsSSSSSSSSSSsSSSSSSSssskk...........|
...........kGkSSSSSSSSSSsSSSSSSssskGk...........|
...........kGGSSSSSSSSSSsSSSSSSsssGGk...........|
...........kGGSSSSSSSSSkssSSSSSsssGGk...........|
...........kGGSSSSSSSSSSSSSSSSSsssGGk...........|
...........kGGSSSSSSSGGGGGGSSSSsssGGk...........|
...........kGGSSSSSSGGkkkkGGSSSsssGGk...........|
...........kGGSSSSSGSSSSSSSSGSSsssGGk...........|
............kk.kSSSSSSSkkSSSSSssskkk............|
................kSSSSSGGGGSSSssk................|
.................kSSSSGGGGSSssk.................|
..................kSSSGGGGSSSk..................|
...................kkSGGGGSkk......kkkkk........|
....................kkkGGkkk......kSSSSSk.......|
...................kSSkGGkSSk.....kkkkkkk.......|
...................kSSSkkSSSk.....kwwwwwk.......|
...................kSSSSSSSSk.....kwwwwwk.......|
.............kLLLkSSkSSSSSSkSSkGLLkwwwwwk.......|
..........kLLLLLLLkSSkSSSSkSSkGGLLkSwwwSk.......|
.......kLLLLLLLLLLLkSSkSSkSSkGGGLkkSSSSSkk......|
.....kLLLLLLLLLLLLLLkSSkkSSkGGGGkLkkkkkkkLk.....|
...kLLLLLLLLLLLLLLLLLLkSSkGGGGGGkLLLLLLLLLLkk...|
..kLLLLLLLLLLLLLLLLLLLkSSkGGGGGGkLLLLLLLLLLLkk..|
.kLLLLLLLLLLLLLLLLLLLkSSkGGGGGGGLkLLLLLLLLLLLkk.|
LLLLLLLLLkLLLLLLLLLLkSSkGGGGGGGGLkLLLLLLLLLLLLkL|
LLLLLLLLLkLLLLLLLLLLkSSkGGGGGGGGLLkLLLLLLLLLLLkL|
LLLLLLLLLkLLLLLLLLLkSSkGGGGGGGGGLLkLLLLLLLLLLLkL|
LLLLLLLLkLLLLLLLLLLkSSkGGGGGGGGGLLkLLLLLLLLLLLLk|
LLLLLLLLkLLLLLLLLLkSSkGGGGGGGGGGLLLkLLLLLLLLLLLk|
LLLLLLLLkLLLLLLLLLkSSkGGGGGGGGGGLLLkLLLLLLLLLLLk|
LLLLLLLLkLLLLLLLLkSSkGGGGGGGGGGGLLLkLLLLLLLLLLLk|
LLLLLLLLkLLLLLLLLkSSkGGGGGGGGGGGLLLkLLLLLLLLLLLk|
LLLLLLLkLLLLLLLLkSSkGGGGGGGGGGGGLLLkLLLLLLLLLLLk|
LLLLLLLkLLLLLLLLkSSkGGGGGGGGGGGGLLLkLLLLLLLLLLLk|
LLLLLLLkLLLLLLLLkSSkGGGGGGGGGGGGLLLkLLLLLLLLLLLk|
'''

BAIXIAN_SPR = '''
.
'''
BAIXIAN_SLOTS = {'S': 0x37, 's': 0x27, 'G': 0x00, 'h': 0x10, 'L': 0x10, 'w': 0x17}
BAIXIAN_PALETTES = [(0x00, 0x10, 0x37), (0x37, 0x27, 0x00), (0x37, 0x10, 0x00), (0x37, 0x17, 0x10)]
BAIXIAN_SPR_SLOTS = {}
BAIXIAN_SPR_PALETTES = []

LIUHANYAN = '''
....................kkkkkkkk....................|
..................kkhhhhhhhhkk..................|
.................khhhhhhhhhhhhk.................|
.................khhhhhhhhhkhhk.................|
..................khhhhhhhkhhk..................|
.................kkkkkkkkkkkkkk.................|
...............kkhhhhhhhkkhhhhhhhkk.............|
..............khhhhhhhhhkhhhhhhhhhhk............|
.............khhhhhhhhhhkhhhhhhhhhhhk...........|
............khhhhhhhhhhhkhhhhhhhhhhhhk..........|
...........khhhhhhhhhhhhkhhhhhhhhhhhhhk.........|
...........khhhhhhhhhhhkSkhhhhhhhhhhhhk.........|
..........khhhhhhhhhhkSSSkhhhhhhhhhhhhk.........|
..........khhhhhhhhkSSSSSSkkhhhhhhhhhhhk........|
..........khhhhhhkSSSSSSSSSSSkkhhhhhhhhk........|
..........khhhhkkSSSSSSSSSSSSSSSkkhhhhhk........|
..........khhhkSSSSSSSSSSSSSSSSsskhhhk..........|
..........khhhkSkkkkSSSSSSSSkkkkskhhhk..........|
..........khhhkSSSSSkSSSSSSkSSSsskhhhk..........|
..........khhhkSSSSSSSSSSSSSSSSsskhhhk..........|
..........khhhkkkkkkkSSSSSSkkkkkkkhhhk..........|
..........khhhkSSSkkSkSSSSkSkkSsskhhhk..........|
..........khhhkSSSkkSSSSSSSSkkSsskhhhk..........|
..........khhhkSSSSSSSSSsSSSSSSsskhhhk..........|
..........khhhkSSSSSSSSSsSSSSSSsskhhhk..........|
..........khhhkSSSSSSSSSssSSSSssskhhhk..........|
..........khhhkSSSSSSSSSSSSSSSssskhhhk..........|
..........khhhkSSSSSSSkkkkSSSSssskhhhk..........|
..........khhhkSSSSSSSSSSSSSSsssskhhhk..........|
..........khhhhkSSSSSSSSSSSSsssk.hhhhk..........|
..........khhhh.kSSSSSSSSSSsssk..hhhhk..........|
..........khhhh..kSSSSSSSSsssk...hhhhk..........|
..........khhhh...kkSSSSSSkk.....hhhhk..........|
..........khhhh.....kkkkkkkk.....hhhhk..........|
...kkkk...khhhh.....kSSSSSSk.....hhhhk..........|
..kWWWWk..khhhh.....kSSSSSSk.....hhhhk..........|
..kWkkWk..khhhh.....kSSSSSSk.....hhhhk..........|
..kWWWWk..khhhh...kWWkSSSSkWWk...hhhhk..........|
...kBBk...khhhh.kWWWWkSSSSkWWWWk.hhhhk..........|
...kBBk.kWkhhhhkWWWWWkBSSBkWWWWWkhhhhkWk........|
...kkkkkWWkhhhhWWWWWWWkBBkWWWWWWWhhhhkWWk.......|
.kWWWWWWWWkhhhhWWWWWWWWkkWWWWWWWWhhhhkWWWWk.....|
BBWWWWWWWkhhhhhkWWWkBBBBBBBBkkWWkhhhhhkWWWWBBBBB|
BBWWWWWWWkhhhhhkWWWkBBBBBBBBkWWWkhhhhhkWWWWBBBBB|
BBWWWWWWWkhhhhhkWWWkBBBBBBBkWWWWkhhhhhkWWWWBBBBB|
BBWWWWWWWkhhhhhkWWkBBBBBBBkWWWWWkhhhhhkWWWWBBBBB|
BBWWWWWWWkhhhhhkWWkBBBBBBkWWWWWWkhhhhhkWWWWBBBBB|
BBWWWWWWWkhhhhhkWWkBBBBBkWWWWWWWkhhhhhkWWWWBBBBB|
BBWWWWWWWkhhhhhkWkBBBBBkWWWWWWWWkhhhhhkWWWWBBBBB|
BBWWWWWWWkhhhhhkWkBBBBkWWWWWWWWWkhhhhhkWWWWBBBBB|
BBWWWWWWWWkhhhhhkWWWWkWWWWWWWWWWkhhhhhkWWWWBBBBB|
BBWWWWWWWWkhhhhhkWWWkWWWWWWWWWWWkhhhhhkWWWWBBBBB|
BBWWWWWWWWkhhhhhkWWkWWWWWWWWWWWWkhhhhhkWWWWBBBBB|
BBWWWWWWWWkhhhhhkWkWWWWWWWWWWWWWkhhhhhkWWWWBBBBB|
BBWWWWWWWWkhhhhhkkWWWWWWWWWWWWWWkhhhhhkWWWWBBBBB|
BBWWWWWWWWkhhhhhkWWWWWWWWWWWWWWWkhhhhhkWWWWBBBBB|
'''

LIUHANYAN_SPR = '''
.
.
23:YyG
24:yG
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
19:W..........W
.
.
.
.
.
23:rr
'''
LIUHANYAN_SLOTS = {'S': 0x37, 's': 0x27, 'h': 0x0C, 'W': 0x30, 'B': 0x31}
LIUHANYAN_PALETTES = [(0x37, 0x0C, 0x30), (0x37, 0x27, 0x0C), (0x37, 0x30, 0x31), (0x30, 0x31, 0x0C)]
LIUHANYAN_SPR_SLOTS = {'W': 0x30, 'r': 0x26, 'Y': 0x30, 'y': 0x2C, 'G': 0x2C}
LIUHANYAN_SPR_PALETTES = [(0x30, 0x26, 0x2C)]

KUCHAN = '''
..kkkkk.........................................|
.kWWWWWk........................................|
kWkkkkkWk.......................................|
kWk...kWk.......................................|
kWkkkkkWk.........kkkkkkkkkkkk..................|
.kWWsWWk........kkSSWWSSSSSSsssk................|
..kkskk........kSSWWWSSSSSSSsskkk...............|
...ksk........kSSWWSSSSSSSSSSssskk..............|
...ksk.......kSSWSSSSSSSSSSSSSssskk.............|
...ksk.......kSSSSSSSSSSSSSSSSssssk.............|
...ksk......kSSSSSSSSSSSSSSSSSSssssk............|
...ksk......kSSSSSSSSSSSSSSSSSSssssk............|
...ksk......kSSSSSSSSSSSSSSSSSSssssk............|
...ksk......kSSSSSSSSSSSSSSSSSSssssk............|
...ksk......kSSSssSSSSSSSSSssSSssssk............|
...ksk......kSSSSSSSSSSSSSSSSSSssssk............|
...ksk.....kSSWWWWWSSSSSSSSWWWWWsssSk...........|
...ksk.....kSWWkkWWWSSSSSSWWWkkWWssSk...........|
...ksk.....kSWSSSSWWSSSSSSWWSSSSWssSk...........|
...ksk.....kSWSSkkSSSSSSSSSSkkSSWssSk...........|
...ksk.....ksWSkSSkSSSSSSSSkSSkSWsssk...........|
...ksk.....ksWSSSSSSSSssSSSSSSSSWsssk...........|
...ksk.....ksSsSSSSSSSssSSSSSSSsWsssk...........|
...ksk.....kSSSsSSSSSssssSSSSSssSssSk...........|
...ksk.....kSSSSSSSSkSsssSkSSSSSsssSk...........|
...ksk.....kSSSSSSWWWWWWWWWWWWSSsssSk...........|
...ksk.....kSSSSWWWWWkkkkWWWWWWSsssSk...........|
...ksk.....kSSSWWWWWWWWWWWWWWWWWWssSk...........|
...ksk.....kSSWWWWWWWWWWWWWWWWWWWWsSk...........|
...ksk.....kSkWWWWWWWWWWWWWWWWWWWWkSk...........|
...ksk.....kSkWWWWWWWWWWWWWWWWWWWWkSk...........|
...ksk.....kSkkWWWWWWWWWWWWWWWWWWkkSk...........|
...kok........kokWWWWWWWWWWWWWWkrk..............|
...kok....kooooobWWWWWWWWWWWWWWkbkrrrk..........|
...kok.kooooooookWWWWWWWWWWWWWWkrrrrrrrrk.......|
...kokooooooooookWWWWWWWWWWWWWWkrrrrrrrrrrk.....|
...kokoooooooookrbWWWWWWWWWWWWkbkrrrrrrrrrrrk...|
..kkokooooooookrrkWWWWWWWWWWWWkrrrbrrrrrrbrrrk..|
.kokokooooooookrrbkWWWWWWWWWWkrbkrbrrrrrrbrrrrk.|
oookokoooooookrrrrkWWWWWWWWWWkrrrrbrrrrrrbrrrrrr|
oookokooooookrrrrrbkWWWWWWWWkrbkrrbrrrrrrbrrrrrr|
oookokoooookrrrrrrrkWWWWWWWWkrrrrrbrrrrrrbrrrrrr|
oookokoooookrrrrrrrbkWWWWWWkrbkrrrbrrrrrrbrrrrrr|
oookokooookrrrrrrrrrrkWWWWkrrrrrrrbrrrrrrbrrrrrr|
oookokoookrrrrrrrrrrrbkWWkrbbbbbbbbbbbbbbbbbbbbb|
oookokookrrrrrrrrrrrrrbkbkbkrrrrrrbrrrrrrbrrrrrr|
oookokookrrrrrrrrrrrrrrrrrrrrrrrrrbrrrrrrbrrrrrr|
oookokokrrrrrrrrrrrrrrrrrrrrrrrrrrbrrrrrrbrrrrrr|
oookokkrrrrrrrrrrrrrrrrrrrrrrrrrrrbrrrrrrbrrrrrr|
oookokrrrrrrrrrrrrrrrrrrrrrrrrrrrrbrrrrrrbrrrrrr|
oookokrrrrrrrrrrrrrrrrrrrrrrrrrrrrbrrrrrrbrrrrrr|
oookokrrrrrrrrrrrrrrrrrrrrrrrrrrrrbrrrrrrbrrrrrr|
oookokrrrrrrrrrrrrrrrrrrrrrbbbbbbbbbbbbbbbbbbbbb|
ookkokrrrrrrrrrrrrrrrrrrrrrrrrrrrrbrrrrrrbrrrrrr|
ookkokrrrrrrrrrrrrrrrrrrrrrrrrrrrrbrrrrrrbrrrrrr|
okrkokrrrrrrrrrrrrrrrrrrrrrrrrrrrrbrrrrrrbrrrrrr|
'''

KUCHAN_SPR = '''
.
'''
KUCHAN_SLOTS = {'S': 0x37, 's': 0x27, 'W': 0x30, 'o': 0x27, 'r': 0x16, 'b': 0x07}
KUCHAN_PALETTES = [(0x37, 0x27, 0x30), (0x30, 0x16, 0x07), (0x27, 0x16, 0x07)]
KUCHAN_SPR_SLOTS = {}
KUCHAN_SPR_PALETTES = []

PORTRAITS = {
    'yirui': (YIRUI, YIRUI_SPR, YIRUI_SLOTS, YIRUI_PALETTES, YIRUI_SPR_SLOTS, YIRUI_SPR_PALETTES),
    'yishuo': (YISHUO, YISHUO_SPR, YISHUO_SLOTS, YISHUO_PALETTES, YISHUO_SPR_SLOTS, YISHUO_SPR_PALETTES),
    'xiaotian': (XIAOTIAN, XIAOTIAN_SPR, XIAOTIAN_SLOTS, XIAOTIAN_PALETTES, XIAOTIAN_SPR_SLOTS, XIAOTIAN_SPR_PALETTES),
    'baixian': (BAIXIAN, BAIXIAN_SPR, BAIXIAN_SLOTS, BAIXIAN_PALETTES, BAIXIAN_SPR_SLOTS, BAIXIAN_SPR_PALETTES),
    'liuhanyan': (LIUHANYAN, LIUHANYAN_SPR, LIUHANYAN_SLOTS, LIUHANYAN_PALETTES, LIUHANYAN_SPR_SLOTS, LIUHANYAN_SPR_PALETTES),
    'kuchan': (KUCHAN, KUCHAN_SPR, KUCHAN_SLOTS, KUCHAN_PALETTES, KUCHAN_SPR_SLOTS, KUCHAN_SPR_PALETTES),
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
HEIGHTS = {}

# 奕叡: topknot through a silver ring, blue headband with flying ties, indigo robe, saber hilt over the shoulder
SPRITES['yirui'] = dict(pal=dict(k=0x0F, S=0x37, c=0x12), front=G('''
.......kk.......
......kSSk......
.....kkkkkk.....
...kkkkkkkkkk...
..kkkkkkkkkkkk..
..kcccccccccccck
..kSSSSSSSSSSkcc
..kSkkSSSSkkSk..
..kSSkSSSSkSSk..
.kkSSSSSSSSSSk..
kSkkSSSkkSSSk...
kkk.kkSSSSkk....
.kkkkccSSccckk..
.kccccckSccccck.
.kcckcccckcckck.
.kcckccckccckck.
.kcckkkkkkkkkck.
.kSSkcccccccSSk.
..kkkcccccccck..
...kcccccccck...
...kcccckcccck..
...kkkkk.kkkkk..
...kkkkk..kkk...
.........kkkk...
'''), side=G('''
.......kSk......
......kkkkk.....
...kkkkkkkkk....
..kkkkkkkkkkk...
cckcccccccccck..
.ckkkkkkkkkSSk..
.kkkkkkkkSSSSk..
.kkkkkkSkSSkSk..
.kkkkkkSSSSkSSk.
.kkkkkkkSSSSSSk.
..kkkkkSSSSkkk..
..kSkkkSSSSSk...
..kSk.kkSSkk....
...kkcccSSk.....
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
.......kSk......
......kkkkk.....
...kkkkkkkkk....
..kkkkkkkkkkk...
cckcccccccccck..
.ckkkkkkkkkSSk..
.kkkkkkkkSSSSk..
.kkkkkkSkSSkSk..
.kkkkkkSSSSkSSk.
.kkkkkkkSSSSSSk.
..kkkkkSSSSkkk..
..kSkkkSSSSSk...
..kSk.kkSSkk....
...kkcccSSk.....
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
'''))

# 奕碩 (a boy): spiky hair rising above a thin headband with long flying ties, an orange cross-collared jacket
# with a black sash, a mole dot on the cheek, his football at his feet
SPRITES['yishuo'] = dict(pal=dict(k=0x0F, S=0x37, c=0x27), front=G('''
..k..k..k..k....
..kk.kk.kk.kk...
..kkkkkkkkkkkk..
..kkkkkkkkkkkkcc
..kcccccccccckc.
..kSSSSSSSSSSk..
..kSkkSSSSkkSk..
..kSkkSSSSkkSk..
..kSSSSkkSkSSk..
...kSSSSSSSSk...
....kkkkkkkk....
..kkccSSkcccck..
.kcckccSkccckck.
.kSSkkkkkkkkkSSk
..kkkcckcccckk..
....kcccckcck...
....kkkkk.kkk.kk
....kkkk..kkkkSk
..............kk
'''), side=G('''
...k..k.k.......
...kk.kk.kk.....
..kkkkkkkkkk....
..kkkkkkkkkkk...
cc.kcccccccck...
.cckkkkkkkkSk...
...kkkkkkSSSk...
..kkkkkSkSkSk...
..kkkkkSSSkSSk..
..kkkkkSSkSSSk..
...kkkkSSSSkk...
....kccSScck....
...kcccSkccck...
...kkkkkkkkSSk..
...kcccccck.....
..kcck..kcck....
.kcck...kcck.kk.
.kkkk...kkkkkSSk
kkkk.....kkk.kk.
'''), side2=G('''
...k..k.k.......
...kk.kk.kk.....
..kkkkkkkkkk....
..kkkkkkkkkkk...
cc.kcccccccck...
.cckkkkkkkkSk...
...kkkkkkSSSk...
..kkkkkSkSkSk...
..kkkkkSSSkSSk..
..kkkkkSSkSSSk..
...kkkkSSSSkk...
....kccSScck....
...kcccSkccck...
...kkkkkkkkSSk..
...kcccccck.....
....kccccck.....
....kcccck...kk.
....kkkkkk..kSSk
....kkkkkk...kk.
'''))

# 冷笑天: silver hair (white), gold horns and a black robe trimmed in gold, a long cape behind
SPRITES['xiaotian'] = dict(pal=dict(k=0x0F, S=0x30, c=0x28), front=G('''
.c............c.
.kc..kkkkkk..ck.
..kckSSSSSSkck..
..kccccccccccck.
..kSSSSSSSSSSSk.
.kSkSkkSSkkSkSk.
.kSkSSkSSkSSkSk.
.kSkSSSSSSSSkSk.
.kSkSSSSSSSSkSk.
.kSkkSSkkkSkkSk.
.kSSkkSSSSkkSSk.
..kSk.kSSk.kSk..
.kkkkckSSkckkkk.
kkkkkkckkckkkkkk
kkckkkkckkkkkckk
kkckkkkkckkkkckk
kkckkkkkckkkkckk
kkSSkkkkkckkSSkk
kkkkkckkkkckkkkk
kkkkkckkkkkckkkk
kkkkkckkkkkckkkk
.kkkkkkkk.kkkkk.
..kkkkkk...kkkk.
.........kkkk...
'''), side=G('''
..c.............
..kc............
...kc.kkkkk.....
....kckSSSSkk...
...kSSkSSSSSSk..
..kSSSSSSSSSSSk.
..kSSSSSkkkkkk..
.kSSSSSkSSSkSk..
.kSSkSSkSSSkSSk.
.kSSkSSkSSSSSSk.
.kSSSkSkSSSkkk..
.kSSSkSkkSSSk...
.kSSSSSSkkkk....
.kSSSSkkcckk....
.kSSSkkkkkckk...
.kSSkkkkkkckk...
.kkkkkkkkkcSSk..
.kkkkkkkkkkkk...
.kkkcccccccck...
.kkkkkkkkkkk....
.kkkkk..kkkkk...
kkkkk....kkkkk..
kkkk......kkkkk.
kkk........kkkkk
'''), side2=G('''
..c.............
..kc............
...kc.kkkkk.....
....kckSSSSkk...
...kSSkSSSSSSk..
..kSSSSSSSSSSSk.
..kSSSSSkkkkkk..
.kSSSSSkSSSkSk..
.kSSkSSkSSSkSSk.
.kSSkSSkSSSSSSk.
.kSSSkSkSSSkkk..
.kSSSkSkkSSSk...
.kSSSSSSkkkk....
.kSSSSkkcckk....
.kSSSkkkkkckk...
.kSSkkkkkkckk...
.kkkkkkkkkcSSk..
.kkkkkkkkkkkk...
.kkkcccccccck...
.kkkkkkkkkk.....
..kkkkkkkk......
..kkkkkkkk......
...kkkkkkk......
...kkkkkkkk.....
'''))

# 白先生: black square scholar's cap, grey goatee, grey scholar's robe with long sleeves
SPRITES['baixian'] = dict(pal=dict(k=0x0F, S=0x37, c=0x10), front=G('''
....kkkkkkkk....
....kcckkkkk....
....kkkkkkkk....
...kkkkkkkkkk...
...kccccccccck..
...kkkkkkkkkkk..
..kcSSSSSSSSck..
..kcSkSSSSkScS..
..kSkSkSSkSkSk..
..kSSSSSSSSSSk..
..kSSkkkkkkSSk..
...kSSSkkSSSk...
....kSSkkSSk....
...kkkkSSkkkk...
..kcccckScckcck.
.kccccckcccckcck
.kccccckccccckck
.kcccckcccccckck
.kcccckcccccckck
.kkkkkkcccccccck
..kkcccccccccck.
..kcccccccccccck
..kcccccckccccck
..kkkkkkkkkkkkk.
'''), side=G('''
................
....kkkkkkk.....
....kcckkkk.....
....kkkkkkk.....
...kkkkkkkkk....
..kkkkkkkkkSk...
..kkkkkkkSSSSk..
..kkkkkSkSSkSk..
..kkkkkSSSSkSSk.
..kkkkkkSSSSSSk.
...kkkkSSSSkkk..
....kkkSSSSccck.
.....kkSSSkcck..
....kcccSSkck...
...kccccccck....
...kccccckcck...
...kccccckccck..
...kccccckccck..
...kccccckkkkk..
..kcccccccccck..
..kccccccccccck.
.kcccccccccccck.
.kkkkkkkkkkkkkk.
.kkk.......kkkk.
'''), side2=G('''
................
....kkkkkkk.....
....kcckkkk.....
....kkkkkkk.....
...kkkkkkkkk....
..kkkkkkkkkSk...
..kkkkkkkSSSSk..
..kkkkkSkSSkSk..
..kkkkkSSSSkSSk.
..kkkkkkSSSSSSk.
...kkkkSSSSkkk..
....kkkSSSSccck.
.....kkSSSkcck..
....kcccSSkck...
...kccccccck....
...kccccckcck...
...kccccckccck..
...kccccckccck..
...kccccckkkkk..
...kcccccccck...
...kcccccccck...
...kcccccccck...
...kkkkkkkkkk...
.....kkkkkk.....
'''))

# 柳寒煙: a high bun, long black hair down her back, a white-and-pale-blue robe to the ground, a slim sword
SPRITES['liuhanyan'] = dict(pal=dict(k=0x0F, S=0x37, c=0x31), front=G('''
......kkkk......
.....kkkkkk.....
......kkkk......
....kkkkkkkk....
...kkkkkkkkkk...
..kkkkkSSkkkkk..
..kkkkSSSSkkkk..
..kkkSSSSSSkkk..
..kkSkkSSkkSkk..
..kkSSkSSkSSkk..
..kkkSSSSSSkkk..
..kkkkSSSSkkkk..
..kkkkkSSkkkkk.k
..kkkcccSccckkkS
.kkkcccckcccckk.
.kkcckccckckcck.
.kkcckcccckkcck.
..kSSkcccccckSSk
..kkkcccccccckk.
...kccccckcccck.
...kcccckccccck.
..kcccckccccccck
..kkkkkkkkkkkkk.
....kkk...kk....
'''), side=G('''
......kkkk......
.....kkkkkk.....
......kkkk......
....kkkkkkkk....
...kkkkkkkkkk...
..kkkkkkkkkSSk..
..kkkkkkkSSSSk..
..kkkkkkSSSkSk..
..kkkkkkSSSkSSk.
..kkkkkkkSSSSSk.
..kkkkkkSSSSkk..
..kkkkkkkSSSk...
..kkkkkkkSSk....
..kkkkkcccSck...
..kkkkcccccck...
..kkkkccccckck..
..kkkkccccckSSk.
...kkkcccccSkk..
...kkkccccccSk..
..kcccccccccck..
..kccccccccccck.
.kcccccccccccck.
.kkkkkkkkkkkkkk.
.kkk.......kkkk.
'''), side2=G('''
......kkkk......
.....kkkkkk.....
......kkkk......
....kkkkkkkk....
...kkkkkkkkkk...
..kkkkkkkkkSSk..
..kkkkkkkSSSSk..
..kkkkkkSSSkSk..
..kkkkkkSSSkSSk.
..kkkkkkkSSSSSk.
..kkkkkkSSSSkk..
..kkkkkkkSSSk...
..kkkkkkkSSk....
..kkkkkcccSck...
..kkkkcccccck...
..kkkkccccckck..
..kkkkccccckSSk.
...kkkcccccSkk..
...kkkccccccSk..
...kccccccccck..
...kcccccccck...
...kcccccccck...
...kkkkkkkkkk...
.....kkkkkk.....
'''))

# 苦禪: bald, long white beard and brows, saffron robe, prayer beads, a staff with a ring at the top
SPRITES['kuchan'] = dict(pal=dict(k=0x0F, S=0x37, c=0x27), front=G('''
.kkk............
kSkSk...........
kSkSk.kkkkkk....
.kSk.kSSSSSSk...
..k.kSSSSSSSSk..
..k.kSSSSSSSSk..
..kkSSkSSSSkSSk.
..kkSSSSSSSSSSk.
..k.kSkSSSSkSk..
..k.kSSSSSSSSk..
..k.kSSSSSSSSk..
..kkkSSSSSSSSk..
..kckkSSSSSSkkk.
.kccckkSSSSkkcck
.kcckckkSSkkckck
.kSSkcckkkkcckck
..kkkcccckcccck.
..k.kcccckccccck
..k.kcccccccccck
..k.kcccccckccck
..k.kccccckcccck
..k.kkkkkkkkkkkk
..k..kkkk..kkkk.
..k.............
'''), side=G('''
.............kkk
............kSkS
............kSkS
.....kkkkk...kSk
...kkSSSSSkk..k.
..kSSSSSSSSSk.k.
..kSSSSSSSSSSkk.
.kSSSSSSSSkkSkk.
.kSSkSSSSSSkSSk.
.kSkSkSSSSSkSSSk
.kSSkSSSSSSSSSk.
..kSSSSSSSSSkkk.
...kkSSSSSSSk.k.
....kkSSSSSSk.k.
...kcckSSSSk..k.
...kcccckSkk..k.
...kccccckcck.k.
...kcccccckckkk.
...kcccccckSSSk.
..kccccccccckkk.
..kccccccccccck.
.kccccccccccccc.
.kkkkkkkkkkkkkk.
.kkk.......kkkk.
'''), side2=G('''
.............kkk
............kSkS
............kSkS
.....kkkkk...kSk
...kkSSSSSkk..k.
..kSSSSSSSSSk.k.
..kSSSSSSSSSSkk.
.kSSSSSSSSkkSkk.
.kSSkSSSSSSkSSk.
.kSkSkSSSSSkSSSk
.kSSkSSSSSSSSSk.
..kSSSSSSSSSkkk.
...kkSSSSSSSk.k.
....kkSSSSSSk.k.
...kcckSSSSk..k.
...kcccckSkk..k.
...kccccckcck.k.
...kcccccckckkk.
...kcccccckSSSk.
...kcccccccckk..
...kcccccccck.k.
...kcccccccck.k.
...kkkkkkkkkk.k.
.....kkkkkk...k.
'''))
HEIGHTS.update({'yirui': 24, 'yishuo': 19, 'xiaotian': 24, 'baixian': 24, 'liuhanyan': 24, 'kuchan': 24})

# the second group (the Black Wind Fort bandits and the master of the Netherworld Sect) lives in nes_longmen2.py
import nes_longmen2  # noqa: E402
PORTRAITS.update(nes_longmen2.PORTRAITS)
SPRITES.update(nes_longmen2.SPRITES)
HEIGHTS.update(nes_longmen2.HEIGHTS)

# the third group (more of the cast from the Longmen stories) lives in nes_longmen3.py
import nes_longmen3  # noqa: E402
PORTRAITS.update(nes_longmen3.PORTRAITS)
SPRITES.update(nes_longmen3.SPRITES)
HEIGHTS.update(nes_longmen3.HEIGHTS)
