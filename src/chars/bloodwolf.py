"""Blood Wolf bloodwolf - a common foe (tier 3). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='bloodwolf',
    name={'zh': '血狼', 'en': 'Blood Wolf'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 3 階小怪', 'en': 'Tier 3 common foe'},
    bio={'zh': '吃過人血的狼，毛色轉成暗紅，眼睛發黃光，比灰狼凶十倍。', 'en': 'A wolf that has tasted human blood; its coat has turned dark red and its eyes glow yellow.'},
    habitat={'zh': '山洞、古廟與斷崖', 'en': 'Caves, old temples and cliffs'},
    tier=3,
    base='wolf',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('bloodwolf')]
