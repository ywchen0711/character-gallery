"""Bell of Ten Thousand Beasts greatbell - a common foe of Longmen Quest II (tier 6). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
GROUP = 'longmen2Foes'
META = dict(
    id='greatbell',
    name={'zh': '萬妖鈴', 'en': 'Bell of Ten Thousand Beasts'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 6 階小怪', 'en': 'Tier 6 common foe'},
    bio={'zh': '馭妖宗的至寶。三魄歸位時，一響能讓天下妖物發狂。', 'en': "The Beastbinder Sect's treasure. With its three souls in place, one peal drives every creature mad."},
    habitat={'zh': '萬妖塔頂・鈴心殿', 'en': "The Hall of the Bell's Heart, atop the tower"},
    tier=6,
    base='greatbell',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('greatbell')]
