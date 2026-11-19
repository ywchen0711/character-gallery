"""屠千秋 Tu Qianqiu - master of the Netherworld Sect. Drawn in the 8-bit `nes` style only (src/nes_longmen2.py)."""

FACTION = 'longmen'
META = dict(
    id='tuqianqiu',
    name={'zh': '屠千秋', 'en': 'Tu Qianqiu'},
    style_name={'zh': '教主', 'en': 'Sect Master'},
    title={'zh': '幽冥教教主', 'en': 'Master of the Netherworld Sect'},
    bio={'zh': '幽冥教的教主，身形清瘦，臉色蒼白，一頭長髮黑如墨，只有一綹雪白。半張臉藏在銀色鬼面之下，深紫長袍，頸上一串白骨念珠，手中白骨扇輕搖。說話總是不急不徐，客客氣氣；聽過他說話的人，大多再也沒說過話。', 'en': 'Master of the Netherworld Sect: lean and pale, his long hair ink-black but for one snow-white lock. Half his face is hidden under a silver ghost mask; he wears a deep violet robe and a string of bone beads, and idly waves a fan of white bone. He speaks unhurried and always politely. Most who have heard him speak never spoke again.'},
    weapon={'zh': '白骨扇', 'en': 'Bone fan'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('tuqianqiu')]
