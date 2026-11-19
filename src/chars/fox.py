"""九尾狐 the Nine-Tailed Fox Spirit. An original monster in the 8-bit `nes` style (src/nes_beasts_art.py)."""

FACTION = 'beast'
KIND = 'monster'
META = dict(
    id='fox',
    name={'zh': '九尾狐', 'en': 'Nine-Tailed Fox'},
    style_name={'zh': '妖狐', 'en': 'Fox spirit'},
    title={'zh': '千年狐仙', 'en': 'Thousand-Year Fox'},
    bio={'zh': '修行千年的金毛狐狸，身後九條尾巴像扇子一樣展開，尾尖燃著雪白的狐火。眼睛細長帶紅，會讓迷路的旅人一直在原地打轉。', 'en': 'A golden fox with a thousand years of cultivation, nine tails fanned out behind it, pale fox-fire burning at their tips. Its long red eyes can keep a lost traveller walking in circles all night.'},
    habitat={'zh': '月夜的竹林與古墳', 'en': 'Bamboo groves and old graves on moonlit nights'},
)


def variants():
    from nes_beasts import BeastVariant
    return [BeastVariant('fox')]
