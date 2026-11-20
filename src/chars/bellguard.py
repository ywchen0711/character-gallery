"""Bell Guard bellguard - a common foe of Longmen Quest II (tier 5). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
GROUP = 'longmen2Foes'
META = dict(
    id='bellguard',
    name={'zh': '鈴衛', 'en': 'Bell Guard'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 5 階小怪', 'en': 'Tier 5 common foe'},
    bio={'zh': '馭妖宗的護衛，金邊斗笠下戴著面罩，出手又快又狠。', 'en': 'A guard of the Beastbinder Sect: a gold-rimmed hat, a mask, quick and merciless.'},
    habitat={'zh': '赤焰窟、冰魄窟與萬妖塔', 'en': 'The Red Flame Caves, the Ice Soul Caves and the tower'},
    tier=5,
    base='assassin',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('bellguard')]
