"""暗器手 Dart Thrower - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sects'
META = dict(
    id='sx_hidden',
    name={'zh': '暗器手', 'en': 'Dart Thrower'},
    style_name={'zh': '袖裡乾坤', 'en': 'A World in the Sleeve'},
    title={'zh': '暗器高手', 'en': 'Master of hidden weapons'},
    bio={'zh': '灰頭巾、紫衣，袖子裡藏著九枚飛鏢。出手之前，你連他抬手都看不見。', 'en': 'Grey hood, violet clothes, nine darts hidden in the sleeves. You will not even see the hand move.'},
    weapon={'zh': '飛鏢', 'en': 'Throwing darts'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_hidden')]
