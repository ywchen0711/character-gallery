"""名匠 Master Smith - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sectsPeople'
META = dict(
    id='sx_smith',
    name={'zh': '名匠', 'en': 'Master Smith'},
    style_name={'zh': '鐵爐邊的人', 'en': 'The One by the Forge'},
    title={'zh': '鑄劍名匠', 'en': 'A master swordsmith'},
    bio={'zh': '赤膊、皮圍裙、一把大鐵鎚。江湖上叫得出名字的好劍，一半出自他的爐子。', 'en': 'Bare arms, a leather apron and a great iron hammer. Half the named swords of the jianghu came out of his forge.'},
    weapon={'zh': '鐵鎚', 'en': 'Iron hammer'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_smith')]
