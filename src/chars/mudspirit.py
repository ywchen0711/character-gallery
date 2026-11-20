"""Mud Spirit mudspirit - a common foe of Longmen Quest II (tier 3). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
GROUP = 'longmen2Foes'
META = dict(
    id='mudspirit',
    name={'zh': '泥靈', 'en': 'Mud Spirit'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 3 階小怪', 'en': 'Tier 3 common foe'},
    bio={'zh': '沼澤裡的泥巴聚成了形，一甩身子就濺得人滿頭泥漿。', 'en': "Swamp mud that has taken a shape. One shake and you're covered head to foot."},
    habitat={'zh': '水鄉的沼澤與毒龍沼', 'en': 'The marshes of the canal country and Poison Dragon Marsh'},
    tier=3,
    base='inkblot',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('mudspirit')]
