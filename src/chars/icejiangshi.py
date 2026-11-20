"""Frozen Jiangshi icejiangshi - a common foe of Longmen Quest II (tier 5). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
GROUP = 'longmen2Foes'
META = dict(
    id='icejiangshi',
    name={'zh': '冰屍', 'en': 'Frozen Jiangshi'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 5 階小怪', 'en': 'Tier 5 common foe'},
    bio={'zh': '凍在冰窟裡百年的殭屍，被鈴聲吵醒了。', 'en': 'A jiangshi frozen in the caves for a century, woken by the bell.'},
    habitat={'zh': '冰魄窟', 'en': 'The Ice Soul Caves'},
    tier=5,
    base='jiangshi_bronze',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('icejiangshi')]
