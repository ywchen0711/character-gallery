"""Jade Toad jadetoad - a common foe of Longmen Quest II (tier 5). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
GROUP = 'longmen2Foes'
META = dict(
    id='jadetoad',
    name={'zh': '玉蟾', 'en': 'Jade Toad'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 5 階小怪', 'en': 'Tier 5 common foe'},
    bio={'zh': '通體碧綠的玉蟾，肚子裡全是銀子，一見人就跑。', 'en': 'A toad of green jade with a belly full of silver; it runs from anyone.'},
    habitat={'zh': '南疆與北地，偶爾出沒', 'en': 'Now and then in the south and the north'},
    tier=5,
    base='stonetoad',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('jadetoad')]
