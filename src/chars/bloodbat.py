"""Blood Bat bloodbat - a common foe (tier 3). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='bloodbat',
    name={'zh': '吸血蝠', 'en': 'Blood Bat'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 3 階小怪', 'en': 'Tier 3 common foe'},
    bio={'zh': '翅膀泛紅的大蝙蝠，專挑睡著的人下口。', 'en': 'A big red-winged bat that only bites people who are asleep.'},
    habitat={'zh': '山洞、古廟與斷崖', 'en': 'Caves, old temples and cliffs'},
    tier=3,
    base='bat',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('bloodbat')]
