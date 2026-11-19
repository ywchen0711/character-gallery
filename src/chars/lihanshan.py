"""厲寒山 Li Hanshan - the Soul-Severing Blade of the Blood Saber Sect. Drawn in the 8-bit `nes` style only (src/nes_longmen3.py)."""

FACTION = 'longmen'
KIND = 'person'
META = dict(
    id='lihanshan',
    name={'zh': '厲寒山', 'en': 'Li Hanshan'},
    style_name={'zh': '斷魂刀', 'en': 'Soul-Severing Blade'},
    title={'zh': '血刀門門主', 'en': 'Master of the Blood Saber Sect'},
    bio={'zh': '血刀門的門主，人稱「斷魂刀」。高瘦，白髮向後束起，暗紅長袍，手上一柄血紅的長彎刀。九斬之下不留人，平生最恨一個「輸」字。', 'en': 'Master of the Blood Saber Sect, called the Soul-Severing Blade. Tall and gaunt, white hair tied back, a dark red robe and a long curved blade the colour of blood. Nobody is left standing after his nine cuts, and the word he hates most is “lose”.'},
    weapon={'zh': '血色長彎刀', 'en': 'Blood-red curved blade'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('lihanshan')]
