"""Thunder Sprite thundersprite - a common foe (tier 4). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='thundersprite',
    name={'zh': '雷精', 'en': 'Thunder Sprite'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 4 階小怪', 'en': 'Tier 4 common foe'},
    bio={'zh': '暴雨夜裡打轉的小雷團，碰一下渾身發麻。', 'en': 'A little ball of thunder that spins on stormy nights; one touch leaves you numb.'},
    habitat={'zh': '古墓、沼澤與高塔', 'en': 'Old tombs, marshes and towers'},
    tier=4,
    base='windsprite',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('thundersprite')]
