"""Bandit Archer archer - a common foe (tier 2). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='archer',
    name={'zh': '山賊弓手', 'en': 'Bandit Archer'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 2 階小怪', 'en': 'Tier 2 common foe'},
    bio={'zh': '躲在山壁上放冷箭的弓手。', 'en': 'An archer who hides on the cliff face and looses arrows from cover.'},
    habitat={'zh': '丘陵、河岸與山寨', 'en': 'Hills, riverbanks and bandit forts'},
    tier=2,
    base='archer',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('archer')]
