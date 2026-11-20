"""弟子 Disciple - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sects'
META = dict(
    id='sx_disciple',
    name={'zh': '弟子', 'en': 'Disciple'},
    style_name={'zh': '紮白頭帶的新弟子', 'en': 'The New Disciple'},
    title={'zh': '門派的根基', 'en': 'The root of every sect'},
    bio={'zh': '每天天沒亮就起來紮馬步、練棍法。白頭帶是入門那天師兄綁上的。', 'en': 'Up before dawn every day for horse stance and staff drills. A senior brother tied the white headband on him the day he joined.'},
    weapon={'zh': '齊眉棍', 'en': 'Brow-height staff'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_disciple')]
