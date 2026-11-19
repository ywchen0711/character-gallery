"""Bamboo-hat Assassin assassin - a common foe (tier 3). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='assassin',
    name={'zh': '斗笠刺客', 'en': 'Bamboo-hat Assassin'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 3 階小怪', 'en': 'Tier 3 common foe'},
    bio={'zh': '斗笠垂紗遮住臉的刺客，反手握著短刀。', 'en': 'An assassin with a veil hanging from his bamboo hat and a short blade held reversed.'},
    habitat={'zh': '山洞、古廟與斷崖', 'en': 'Caves, old temples and cliffs'},
    tier=3,
    base='assassin',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('assassin')]
