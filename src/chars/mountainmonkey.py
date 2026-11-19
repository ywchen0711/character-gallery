"""Mountain Monkey mountainmonkey - a common foe (tier 1). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='mountainmonkey',
    name={'zh': '山猴', 'en': 'Mountain Monkey'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 1 階小怪', 'en': 'Tier 1 common foe'},
    bio={'zh': '拿樹枝當棍子的山猴，最愛搶旅人的乾糧。', 'en': "A mountain monkey with a stick for a club that loves to snatch travellers' food."},
    habitat={'zh': '村外田野與山林小徑', 'en': 'Fields and forest paths outside the villages'},
    tier=1,
    base='monkey',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('mountainmonkey')]
