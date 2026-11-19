"""Wind Sprite windsprite - a common foe (tier 2). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='windsprite',
    name={'zh': '風精', 'en': 'Wind Sprite'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 2 階小怪', 'en': 'Tier 2 common foe'},
    bio={'zh': '山口的一陣旋風，捲著落葉，笑嘻嘻地掀人帽子。', 'en': 'A whirlwind in the mountain pass full of leaves that giggles and steals hats.'},
    habitat={'zh': '丘陵、河岸與山寨', 'en': 'Hills, riverbanks and bandit forts'},
    tier=2,
    base='windsprite',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('windsprite')]
