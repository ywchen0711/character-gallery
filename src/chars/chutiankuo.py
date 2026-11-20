"""楚天闊 Chu Tiankuo - Swordsman. Drawn in the 8-bit `nes` style only (src/nes_longmen4.py, portrait in src/nes_longmen4_busts.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmen2'
META = dict(
    id='chutiankuo',
    name={'zh': '楚天闊', 'en': 'Chu Tiankuo'},
    style_name={'zh': '屢敗屢戰', 'en': 'The Undefeated Loser'},
    title={'zh': '劍客', 'en': 'Swordsman'},
    bio={'zh': '立志要當天下第一劍客的年輕人，在每一座城鎮向奕叡挑戰，每輸一次就在小冊子上記一筆。他不知道自己的父親是誰。', 'en': 'A young man set on becoming the greatest swordsman under heaven. He challenges Yi Rui in every town and writes each defeat in a little book. He does not know who his father really is.'},
    weapon={'zh': '天闊劍', 'en': 'Sky-wide sword'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('chutiankuo')]
