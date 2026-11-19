"""Living Training Dummy dummy - a common foe (tier 1). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='dummy',
    name={'zh': '木人樁', 'en': 'Living Training Dummy'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 1 階小怪', 'en': 'Tier 1 common foe'},
    bio={'zh': '武館裡被打了一萬次的木人樁，終於決定還手。', 'en': 'A training dummy struck ten thousand times in the martial hall that has finally decided to hit back.'},
    habitat={'zh': '村外田野與山林小徑', 'en': 'Fields and forest paths outside the villages'},
    tier=1,
    base='dummy',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('dummy')]
