"""Skeleton Swordsman skeleton - a common foe (tier 3). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='skeleton',
    name={'zh': '骷髏劍客', 'en': 'Skeleton Swordsman'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 3 階小怪', 'en': 'Tier 3 common foe'},
    bio={'zh': '死在斷崖下的劍客，骨頭還記得怎麼出劍。', 'en': 'A swordsman who died under the cliff; his bones still remember how to strike.'},
    habitat={'zh': '山洞、古廟與斷崖', 'en': 'Caves, old temples and cliffs'},
    tier=3,
    base='skeleton',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('skeleton')]
