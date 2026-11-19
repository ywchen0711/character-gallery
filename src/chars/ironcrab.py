"""Iron Crab ironcrab - a common foe (tier 4). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='ironcrab',
    name={'zh': '鐵甲蟹', 'en': 'Iron Crab'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 4 階小怪', 'en': 'Tier 4 common foe'},
    bio={'zh': '殼像鐵甲一樣灰亮的老螃蟹，躲在沼澤的爛泥裡。', 'en': 'An old crab whose shell shines grey like armour; it lurks in the marsh mud.'},
    habitat={'zh': '古墓、沼澤與高塔', 'en': 'Old tombs, marshes and towers'},
    tier=4,
    base='crab',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('ironcrab')]
