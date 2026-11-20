"""開山弟子 Founder - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sects'
META = dict(
    id='sx_founder',
    name={'zh': '開山弟子', 'en': 'Founder'},
    style_name={'zh': '背著包袱的開山人', 'en': 'The One with the Bundle'},
    title={'zh': '開宗立派的先鋒', 'en': 'Vanguard of a new sect'},
    bio={'zh': '背著包袱、拄著竹杖，走到哪裡就在哪裡立起門派的旗子。包袱裡是師父給的半部秘笈和三天的乾糧。', 'en': 'A bundle on his back and a bamboo stick in hand: wherever he stops, a new sect raises its banner. The bundle holds half a manual from his master and three days of dry rations.'},
    weapon={'zh': '竹杖', 'en': 'Bamboo stick'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_founder')]
