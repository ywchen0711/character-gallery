"""蘇小婉 Su Xiaowan - Daughter of the Su family. Drawn in the 8-bit `nes` style only (src/nes_longmen4.py, portrait in src/nes_longmen4_busts.py)."""

FACTION = 'longmen'
KIND = 'person'
GROUP = 'longmen2'
META = dict(
    id='suxiaowan',
    name={'zh': '蘇小婉', 'en': 'Su Xiaowan'},
    style_name={'zh': '不知己逝的小姐', 'en': 'The Lady Who Forgot She Died'},
    title={'zh': '蘇家小姐', 'en': 'Daughter of the Su family'},
    bio={'zh': '二十年前死於妖禍的蘇家小姐。她不知道自己已經死了，每天在舊宅裡泡茶，等去京城學馴獸的哥哥回來。', 'en': 'The Su daughter, killed in a beast raid twenty years ago. She does not know she is dead; every day she makes tea in the old mansion and waits for her brother, who went to the capital to learn beast-taming.'},
    weapon={'zh': '團扇與青瓷杯', 'en': 'A round fan and a celadon cup'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('suxiaowan')]
