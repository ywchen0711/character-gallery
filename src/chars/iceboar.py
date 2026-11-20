"""Snowbristle Boar iceboar - a common foe of Longmen Quest II (tier 5). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
GROUP = 'longmen2Foes'
META = dict(
    id='iceboar',
    name={'zh': '雪鬃豬', 'en': 'Snowbristle Boar'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 5 階小怪', 'en': 'Tier 5 common foe'},
    bio={'zh': '鬃毛結滿冰霜的野豬，衝起來像一座小冰山。', 'en': 'A boar whose bristles are thick with frost; it charges like a small iceberg.'},
    habitat={'zh': '北地雪原', 'en': 'The northern snowfields'},
    tier=5,
    base='boar_iron',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('iceboar')]
