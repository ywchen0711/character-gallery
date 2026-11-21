"""道士 Daoist - 龍門戰記 (Longmen Tactics). Drawn in the 8-bit `nes` style (src/nes_tactics.py, portrait in src/nes_tactics_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'tacticsJobs'
META = dict(
    id='sx_daoist',
    name={'zh': '道士', 'en': 'Daoist'},
    style_name={'zh': '符劍', 'en': 'Talisman Sword'},
    title={'zh': '畫符的道士', 'en': 'A talisman-drawing Daoist'},
    bio={'zh': '黃道袍、髮髻上頂著一頂小金冠，手中一把貼著黃符的桃木劍。火、雷、冰、風四符，蓄氣越久越厲害。', 'en': 'A yellow Daoist robe, a little gold crown on the topknot and a peachwood sword with a yellow talisman. Fire, thunder, frost and gale talismans, stronger the longer they are charged.'},
    weapon={'zh': '桃木劍與符籙', 'en': 'Peachwood sword and talismans'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_daoist')]
