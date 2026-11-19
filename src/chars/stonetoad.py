"""Stone Toad stonetoad - a common foe (tier 2). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='stonetoad',
    name={'zh': '石蟾', 'en': 'Stone Toad'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 2 階小怪', 'en': 'Tier 2 common foe'},
    bio={'zh': '廟門口的三足石蟾，嘴裡含著銅錢，有人偷錢就跳起來。', 'en': 'The three-legged stone toad at the temple gate with a coin in its mouth; it leaps at coin thieves.'},
    habitat={'zh': '丘陵、河岸與山寨', 'en': 'Hills, riverbanks and bandit forts'},
    tier=2,
    base='stonetoad',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('stonetoad')]
