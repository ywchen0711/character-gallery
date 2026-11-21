"""醫者 Physician - 龍門戰記 (Longmen Tactics). Drawn in the 8-bit `nes` style (src/nes_tactics.py, portrait in src/nes_tactics_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'tacticsJobs'
META = dict(
    id='sx_physician',
    name={'zh': '醫者', 'en': 'Physician'},
    style_name={'zh': '懸壺濟世', 'en': 'A Gourd for the World'},
    title={'zh': '走方郎中', 'en': 'A travelling physician'},
    bio={'zh': '綠袍郎中，腰間掛著一個藥葫蘆。金針、湯藥和一點內力，走到哪裡就醫到哪裡。', 'en': 'A physician in green with a medicine gourd at the hip. Golden needles, herbs and a little inner strength, healing wherever the road goes.'},
    weapon={'zh': '藥葫蘆與金針', 'en': 'Medicine gourd and golden needles'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_physician')]
