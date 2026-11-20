"""Golden-bone General goldbone - a common foe of Longmen Quest II (tier 6). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
GROUP = 'longmen2Foes'
META = dict(
    id='goldbone',
    name={'zh': '金骨將', 'en': 'Golden-bone General'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 6 階小怪', 'en': 'Tier 6 common foe'},
    bio={'zh': '骨頭鍍了金的骷髏將軍，守在萬妖塔頂層。', 'en': "A skeleton general with gilded bones, guarding the tower's upper floors."},
    habitat={'zh': '萬妖塔', 'en': 'The Tower of Ten Thousand Beasts'},
    tier=6,
    base='skeleton_black',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('goldbone')]
