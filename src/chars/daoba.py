"""刀疤 Scar - second in command of the Black Wind Fort. Drawn in the 8-bit `nes` style only (src/nes_longmen2.py)."""

FACTION = 'longmen'
META = dict(
    id='daoba',
    name={'zh': '刀疤', 'en': 'Scar'},
    style_name={'zh': '二當家', 'en': 'Second Chief'},
    title={'zh': '黑風寨二當家', 'en': 'Second of the Black Wind Fort'},
    bio={'zh': '黑風寨的二當家，兩鬢剃得精光，頭頂紮個髮髻；一道長疤從眉梢斜劈到下巴，誰問起來歷，他就把大刀往地上一頓。話少，下手狠，寨裡的規矩都由他來管。', 'en': "Second chief of the Black Wind Fort, his temples shaved bare and a topknot on his crown. A long scar runs from his brow down to his jaw; ask him where it came from and he only sets his broad dao down hard on the ground. He says little, strikes hard, and keeps the fort's rules."},
    weapon={'zh': '大刀', 'en': 'Broad dao'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('daoba')]
