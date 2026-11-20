"""墨無涯 Mo Wuya - Sect master. Drawn in the 8-bit `nes` style only (src/nes_longmen4.py, portrait in src/nes_longmen4_busts.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmen2'
META = dict(
    id='mowuya',
    name={'zh': '墨無涯', 'en': 'Mo Wuya'},
    style_name={'zh': '馭妖宗主', 'en': 'Master of the Beastbinder Sect'},
    title={'zh': '宗主', 'en': 'Sect master'},
    bio={'zh': '馭妖宗的宗主，手持萬妖鈴。二十年前妖禍奪走了他的妹妹，他發誓要讓天下的妖物都聽話。', 'en': 'Master of the Beastbinder Sect, bearer of the Bell of Ten Thousand Beasts. A beast raid took his sister twenty years ago, and he swore every creature would obey.'},
    weapon={'zh': '鈴杖', 'en': 'Bell staff'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('mowuya')]
