"""Deadwood Sprite deadwood - a common foe (tier 4). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='deadwood',
    name={'zh': '枯木精', 'en': 'Deadwood Sprite'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 4 階小怪', 'en': 'Tier 4 common foe'},
    bio={'zh': '吸乾了整片林子的枯樹精，葉子全是枯黃色。', 'en': 'A withered tree sprite that has drained a whole wood dry; every leaf is dead brown.'},
    habitat={'zh': '古墓、沼澤與高塔', 'en': 'Old tombs, marshes and towers'},
    tier=4,
    base='treesprite',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('deadwood')]
