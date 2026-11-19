"""Tree Sprite treesprite - a common foe (tier 2). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='treesprite',
    name={'zh': '樹精', 'en': 'Tree Sprite'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 2 階小怪', 'en': 'Tier 2 common foe'},
    bio={'zh': '老樹樁成了精，用樹根走路，枝葉一甩就打人。', 'en': 'An old stump come alive; it walks on its roots and swats with its branches.'},
    habitat={'zh': '丘陵、河岸與山寨', 'en': 'Hills, riverbanks and bandit forts'},
    tier=2,
    base='treesprite',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('treesprite')]
