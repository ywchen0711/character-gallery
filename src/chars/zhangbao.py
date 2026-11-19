"""張寶 Zhang Bao - an enemy general of 三國志 霸王之路 (stage: 廣宗之戰). Drawn in the 8-bit `nes` style only (src/nes_sango.py)."""

FACTION = 'sango'
META = dict(
    id='zhangbao',
    name={'zh': '張寶', 'en': 'Zhang Bao'},
    style_name={'zh': '地公將軍', 'en': 'General of the Earth'},
    title={'zh': '廣宗之戰・地公將軍', 'en': 'The Battle of Guangzong - General of the Earth'},
    bio={'zh': '黃巾三兄弟之一，自稱地公將軍。黃道袍、長黑鬚，手舉紅字符紙，據說能呼風喚雨、撒豆成兵。', 'en': 'One of the three Yellow Turban brothers, the self-styled General of the Earth. A yellow Daoist robe, a long black beard and a red-script talisman held high; they say he can call wind and rain.'},
    weapon={'zh': '符咒與妖術', 'en': 'Talismans and sorcery'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('zhangbao')]
