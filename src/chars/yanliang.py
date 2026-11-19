"""顏良 Yan Liang - an enemy general of 三國志 霸王之路 (stage: 白馬之圍). Drawn in the 8-bit `nes` style only (src/nes_sango.py)."""

FACTION = 'sango'
META = dict(
    id='yanliang',
    name={'zh': '顏良', 'en': 'Yan Liang'},
    style_name={'zh': '河北名將', 'en': 'Champion of Hebei'},
    title={'zh': '白馬之圍・河北名將', 'en': 'The Siege of Baima - Champion of Hebei'},
    bio={'zh': '袁紹帳下的河北名將，翼盔紅纓、方正大鬍、青銅金甲，手提大刀，是袁軍兩大猛將之一。', 'en': "One of Yuan Shao's two great champions of Hebei: a winged helmet with a red tassel, a square heavy beard, bronze-gold armour and a great dao."},
    weapon={'zh': '大刀', 'en': 'Great dao'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('yanliang')]
