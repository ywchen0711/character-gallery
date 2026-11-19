"""柳寒煙 Liu Hanyan - Mistress of the Cold River Pavilion. Drawn in the 8-bit `nes` style only (src/nes_longmen.py)."""

FACTION = 'longmen'
META = dict(
    id='liuhanyan',
    name={'zh': '柳寒煙', 'en': 'Liu Hanyan'},
    style_name={'zh': '寒江閣主', 'en': 'Pavilion mistress'},
    title={'zh': '寒江閣主', 'en': 'Mistress of the Cold River Pavilion'},
    bio={'zh': '寒江閣的閣主。高髻銀簪，白衣淡藍，一柄細劍。待人冷淡、疑心很重，劍出時霜飛雪落；但欠下的人情，她一定會還。', 'en': 'Mistress of the Cold River Pavilion. A high knot of hair with a silver pin, white over pale blue, and a slender sword. Cool and slow to trust, her sword brings frost and snow when it is drawn; but a debt she owes, she always repays.'},
    weapon={'zh': '細劍', 'en': 'Slender sword'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('liuhanyan')]
