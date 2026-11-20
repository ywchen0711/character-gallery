"""Bellfire bellfire - a common foe of Longmen Quest II (tier 6). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
GROUP = 'longmen2Foes'
META = dict(
    id='bellfire',
    name={'zh': '鈴火', 'en': 'Bellfire'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 6 階小怪', 'en': 'Tier 6 common foe'},
    bio={'zh': '萬妖塔裡飄蕩的鬼火，隨著鈴聲忽明忽暗。', 'en': 'A ghost flame drifting in the tower, flickering with every peal.'},
    habitat={'zh': '萬妖塔', 'en': 'The Tower of Ten Thousand Beasts'},
    tier=6,
    base='wisp_nether',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('bellfire')]
