"""小蓮 Xiaolian - the little apprentice of the Cold River Pavilion. Drawn in the 8-bit `nes` style only (src/nes_longmen3.py)."""

FACTION = 'longmen'
KIND = 'person'
META = dict(
    id='xiaolian',
    name={'zh': '小蓮', 'en': 'Xiaolian'},
    style_name={'zh': '小徒弟', 'en': 'Apprentice'},
    title={'zh': '寒江閣小徒弟', 'en': 'Apprentice of the Cold River Pavilion'},
    bio={'zh': '柳寒煙的小徒弟，兩個圓圓的髮髻綁著紅繩，粉紅衣裳配白領。好奇心比膽子還大，什麼門道都想偷學；也是奕碩在江湖上交到的第一個朋友，兩人一見面就踢起球來。', 'en': "Liu Hanyan's little disciple, two round buns tied with red ribbon, a pink robe with a white collar. Her curiosity is even bigger than her nerve and she wants to learn every trick she sees. Yi Shuo's first friend in the jianghu: the moment they met, they were kicking a ball together."},
    weapon={'zh': '（練劍中）', 'en': '(still learning the sword)'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('xiaolian')]
