"""奕碩 Yi Shuo - Yi Rui's younger brother, a boy whose weapon is a football. Drawn in the 8-bit `nes` style only (src/nes_longmen.py)."""

FACTION = 'longmen'
META = dict(
    id='yishuo',
    name={'zh': '奕碩', 'en': 'Yi Shuo'},
    style_name={'zh': '弟弟', 'en': 'Little brother'},
    title={'zh': '旋風少俠', 'en': 'The Whirlwind Kid'},
    bio={'zh': '奕叡的弟弟，從小不愛拿刀，只愛踢球。紅頭帶、朱紅短褂，人中右邊有一顆痣，球從不離腳。看到不公平的事，總是先衝再想。', 'en': 'Yi Rui’s little brother, who never cared for blades, only for kicking a ball. Red headband, vermilion jacket, a mole just right of the groove under his nose (his own right), and the ball never far from his feet. When he sees something unfair he charges first and thinks later.'},
    weapon={'zh': '足球', 'en': 'Football'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('yishuo')]
