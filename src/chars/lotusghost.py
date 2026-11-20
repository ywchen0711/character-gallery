"""Lotus Pond Ghost lotusghost - a common foe of Longmen Quest II (tier 3). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
GROUP = 'longmen2Foes'
META = dict(
    id='lotusghost',
    name={'zh': '蓮池鬼', 'en': 'Lotus Pond Ghost'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 3 階小怪', 'en': 'Tier 3 common foe'},
    bio={'zh': '舊宅蓮池裡的女鬼，頭頂荷葉，會唱一首誰也聽不懂的歌。', 'en': "A ghost of an old mansion's lotus pond, a leaf on her head, singing a song no one understands."},
    habitat={'zh': '蘇家舊宅與碧波湖', 'en': 'The old Su mansion and Green Wave Lake'},
    tier=3,
    base='drowned',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('lotusghost')]
