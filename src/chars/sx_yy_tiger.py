"""妖虎騎 Demon Tiger Rider - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sectsUnique'
META = dict(
    id='sx_yy_tiger',
    name={'zh': '妖虎騎', 'en': 'Demon Tiger Rider'},
    style_name={'zh': '騎虎', 'en': 'Riding the Tiger'},
    title={'zh': '馭妖宗的虎騎', 'en': 'Tiger rider of the Beastbinder Sect'},
    bio={'zh': '綠頭巾、綠衣，騎著一頭被萬妖鈴馴服的猛虎。肖像旁邊就是那頭虎。', 'en': 'A green hood and green robes, astride a tiger tamed by the Bell of Ten Thousand Beasts. The tiger is right beside her in the portrait.'},
    weapon={'zh': '虎', 'en': 'The tiger'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_yy_tiger')]
