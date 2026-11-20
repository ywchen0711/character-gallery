"""霍天下 Huo Tianxia - Wanderer. Drawn in the 8-bit `nes` style only (src/nes_longmen4.py, portrait in src/nes_longmen4_busts.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmen2'
META = dict(
    id='huotianxia',
    name={'zh': '霍天下', 'en': 'Huo Tianxia'},
    style_name={'zh': '天下第一吹', 'en': 'The Greatest Boaster'},
    title={'zh': '江湖客', 'en': 'Wanderer'},
    bio={'zh': '自稱天下第一的大俠，誰做了什麼大事，他就說是自己做的。真打起來，總是被人綁著。', 'en': 'A self-styled great hero who claims every deed anyone does. When there is real fighting, he usually ends up tied up.'},
    weapon={'zh': '紅披風', 'en': 'Red cape'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('huotianxia')]
