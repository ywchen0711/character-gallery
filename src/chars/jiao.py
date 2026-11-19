"""江蛟 the River Jiao. An original monster in the 8-bit `nes` style (src/nes_beasts_art.py)."""

FACTION = 'beast'
KIND = 'monster'
META = dict(
    id='jiao',
    name={'zh': '江蛟', 'en': 'River Jiao'},
    style_name={'zh': '水妖', 'en': 'Water serpent'},
    title={'zh': '寒江深潭之主', 'en': 'Lord of the Deep Pool'},
    bio={'zh': '還沒化成龍的蛟，青綠鱗甲、淡黃腹甲，頭上一對短角和長鬚。藏在江心最深的潭底，一翻身就掀起大浪，渡船常被牠攪翻。', 'en': 'A jiao that has not yet become a dragon: green-teal scales, a pale yellow belly, two short horns and long whiskers. It hides in the deepest pool mid-river, and when it turns over the waves rise and ferries capsize.'},
    habitat={'zh': '大江的深潭與急流', 'en': 'Deep pools and rapids of the great river'},
)


def variants():
    from nes_beasts import BeastVariant
    return [BeastVariant('jiao')]
