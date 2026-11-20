"""Beastbinder Acolyte acolyte - a common foe of Longmen Quest II (tier 2). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
GROUP = 'longmen2Foes'
META = dict(
    id='acolyte',
    name={'zh': '馭妖宗徒', 'en': 'Beastbinder Acolyte'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 2 階小怪', 'en': 'Tier 2 common foe'},
    bio={'zh': '馭妖宗的門徒，腰掛銅鈴，搖一下鈴，身邊的妖物就紅了眼。', 'en': 'A disciple of the Beastbinder Sect. One shake of the bell at his belt and every creature nearby sees red.'},
    habitat={'zh': '鈴音寺與馭妖宗的據點', 'en': "The Bell Temple and the sect's strongholds"},
    tier=2,
    base='sorcerer',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('acolyte')]
