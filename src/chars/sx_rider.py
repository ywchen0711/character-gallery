"""馬隊 Riders - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sects'
META = dict(
    id='sx_rider',
    name={'zh': '馬隊', 'en': 'Riders'},
    style_name={'zh': '馬上的刀', 'en': 'A Blade on Horseback'},
    title={'zh': '門派的騎手', 'en': "The sect's rider"},
    bio={'zh': '騎一匹棕馬，紅衣皮盔，跑起來像一陣風。肖像是騎手本人，身邊是他的馬。', 'en': 'On a brown horse in red with a leather helmet, gone like a gust of wind. The portrait shows the rider with his horse beside him.'},
    weapon={'zh': '馬刀與韁繩', 'en': 'Saber and reins'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_rider')]
