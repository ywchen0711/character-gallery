"""Wild Boar wildboar - a common foe (tier 1). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='wildboar',
    name={'zh': '山豬', 'en': 'Wild Boar'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 1 階小怪', 'en': 'Tier 1 common foe'},
    bio={'zh': '低頭就衝的山豬，獠牙能把籬笆整排挑翻。', 'en': 'A boar that charges head-down; its tusks can toss a whole fence aside.'},
    habitat={'zh': '村外田野與山林小徑', 'en': 'Fields and forest paths outside the villages'},
    tier=1,
    base='boar',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('wildboar')]
