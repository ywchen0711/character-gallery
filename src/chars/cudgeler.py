"""Black Wind Cudgeler cudgeler - a common foe (tier 2). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='cudgeler',
    name={'zh': '黑風棍手', 'en': 'Black Wind Cudgeler'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 2 階小怪', 'en': 'Tier 2 common foe'},
    bio={'zh': '黑風寨的老手，棍子上纏著鐵釘。', 'en': 'A seasoned Black Wind bandit whose cudgel is wrapped with iron nails.'},
    habitat={'zh': '丘陵、河岸與山寨', 'en': 'Hills, riverbanks and bandit forts'},
    tier=2,
    base='lackey',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('cudgeler')]
