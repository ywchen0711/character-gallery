"""素衣劍尼 White-robed Sword Nun - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sectsUnique'
META = dict(
    id='sx_cy_nun',
    name={'zh': '素衣劍尼', 'en': 'White-robed Sword Nun'},
    style_name={'zh': '慈雲一劍', 'en': 'One Sword of Mercy Cloud'},
    title={'zh': '慈雲庵的劍尼', 'en': 'Sword nun of the Mercy Cloud Nunnery'},
    bio={'zh': '白頭巾、淡粉衣，劍法柔中帶剛。打完仗，總是第一個替受傷的人包紮。', 'en': 'A white hood and pale pink robes; her swordplay is soft with steel inside. After a fight she is always first to bind the wounded.'},
    weapon={'zh': '長劍', 'en': 'Long sword'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_cy_nun')]
