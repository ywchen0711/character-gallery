"""暴龍掌客 Dragon Palm Brawler - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sectsUnique'
META = dict(
    id='sx_bl_palm',
    name={'zh': '暴龍掌客', 'en': 'Dragon Palm Brawler'},
    style_name={'zh': '一掌開碑', 'en': 'A Palm that Splits Steles'},
    title={'zh': '暴龍崖的掌客', 'en': 'Brawler of Tyrant Dragon Cliff'},
    bio={'zh': '赤膊、紅褲、金臂環，頭髮像刺蝟。冷笑天的手下，出掌前也學著先冷笑。', 'en': "Bare-chested in red trousers and gold armbands, hair like a hedgehog. One of Leng Xiaotian's men - he too sneers before he strikes."},
    weapon={'zh': '雙掌', 'en': 'Bare palms'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_bl_palm')]
