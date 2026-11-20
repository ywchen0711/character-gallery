"""斥候 Scout - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sects'
META = dict(
    id='sx_scout',
    name={'zh': '斥候', 'en': 'Scout'},
    style_name={'zh': '斗笠下的眼睛', 'en': 'Eyes under the Straw Hat'},
    title={'zh': '探路的人', 'en': 'The pathfinder'},
    bio={'zh': '戴著寬邊斗笠，腳程比馬快，看過的山路都記在心裡。一把短刀只用來砍藤蔓。', 'en': 'Under a wide straw hat, faster on foot than a horse, he remembers every mountain path he has walked. His short knife is only for cutting vines.'},
    weapon={'zh': '短刀', 'en': 'Short knife'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_scout')]
