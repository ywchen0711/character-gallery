"""血刀客 Blood Saber - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sectsUnique'
META = dict(
    id='sx_xd_blood',
    name={'zh': '血刀客', 'en': 'Blood Saber'},
    style_name={'zh': '九斬', 'en': 'Nine Cuts'},
    title={'zh': '血刀門的刀客', 'en': 'Saber of the Blood Saber Sect'},
    bio={'zh': '暗紅長袍，一把血紅的彎刀。厲寒山的門下，九斬之下不留人。', 'en': 'A dark red robe and a blood-red curved blade. A pupil of Li Hanshan: nine cuts, none spared.'},
    weapon={'zh': '血紅彎刀', 'en': 'Blood-red curved blade'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_xd_blood')]
