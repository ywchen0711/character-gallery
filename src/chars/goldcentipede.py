"""Golden Centipede goldcentipede - a common foe (tier 4). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='goldcentipede',
    name={'zh': '金頭蜈蚣', 'en': 'Golden Centipede'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 4 階小怪', 'en': 'Tier 4 common foe'},
    bio={'zh': '金黃色的大蜈蚣，練毒的人拿牠泡酒。', 'en': 'A great golden centipede that poison-masters steep in wine.'},
    habitat={'zh': '古墓、沼澤與高塔', 'en': 'Old tombs, marshes and towers'},
    tier=4,
    base='centipede',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('goldcentipede')]
