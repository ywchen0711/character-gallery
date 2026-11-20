"""寒江劍姬 Cold River Swordmaid - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sectsUnique'
META = dict(
    id='sx_hj_sword',
    name={'zh': '寒江劍姬', 'en': 'Cold River Swordmaid'},
    style_name={'zh': '霜劍', 'en': 'Frost Sword'},
    title={'zh': '寒江閣的女劍客', 'en': 'Swordswoman of the Cold River Pavilion'},
    bio={'zh': '高髻銀簪、淡藍衣裳，柳寒煙的門下。細劍一出，像江面上的寒煙。', 'en': "A high bun with a silver pin and pale blue robes: one of Liu Hanyan's pupils. Her slim sword moves like mist over a cold river."},
    weapon={'zh': '細劍', 'en': 'Slim sword'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_hj_sword')]
