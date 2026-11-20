"""Ice Bat icebat - a common foe of Longmen Quest II (tier 5). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
GROUP = 'longmen2Foes'
META = dict(
    id='icebat',
    name={'zh': '冰蝠', 'en': 'Ice Bat'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 5 階小怪', 'en': 'Tier 5 common foe'},
    bio={'zh': '冰窟裡的蝙蝠，牙齒像冰錐。', 'en': 'A bat of the ice caves, teeth like icicles.'},
    habitat={'zh': '北地雪原與冰魄窟', 'en': 'The northern snowfields and the Ice Soul Caves'},
    tier=5,
    base='bat',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('icebat')]
