"""劍陣 Sword Formation - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sects'
META = dict(
    id='sx_swordform',
    name={'zh': '劍陣', 'en': 'Sword Formation'},
    style_name={'zh': '舉劍成陣', 'en': 'Swords Raised as One'},
    title={'zh': '劍陣弟子', 'en': 'A swordsman of the formation'},
    bio={'zh': '藍甲白纓，長劍高舉。七人成陣，進退如一人。', 'en': 'Blue armour, white plume, sword held high. Seven make a formation that moves like one.'},
    weapon={'zh': '長劍', 'en': 'Long sword'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_swordform')]
