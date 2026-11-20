"""莫記得 Mo Jide - Doctor. Drawn in the 8-bit `nes` style only (src/nes_longmen4.py, portrait in src/nes_longmen4_busts.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmen2'
META = dict(
    id='mojide',
    name={'zh': '莫記得', 'en': 'Mo Jide'},
    style_name={'zh': '藥王鬼手', 'en': 'The Ghost-handed Healer'},
    title={'zh': '大夫', 'en': 'Doctor'},
    bio={'zh': '蘇河城的大夫，看病不收錢，說收了也會忘。其實他什麼都記得——他是馭妖宗的藥王鬼手。', 'en': "The doctor of Suhe who treats for free, saying he would only forget the fee. In truth he remembers everything: he is the Beastbinder Sect's Ghost-handed Healer."},
    weapon={'zh': '藥箱', 'en': 'Medicine box'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('mojide')]
