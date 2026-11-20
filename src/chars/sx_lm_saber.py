"""啟程刀客 Setting-out Saber - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sectsUnique'
META = dict(
    id='sx_lm_saber',
    name={'zh': '啟程刀客', 'en': 'Setting-out Saber'},
    style_name={'zh': '龍門的刀', 'en': 'The Blade of Longmen'},
    title={'zh': '龍門刀莊的刀客', 'en': 'Saber of the Longmen Saber Manor'},
    bio={'zh': '深藍衣、藍頭帶，和奕叡一樣背著環首刀。龍門刀莊的弟子出門，總說「第一刀，從腳下開始」。', 'en': 'Indigo robe, blue headband and a ring-pommel saber like Yi Rui. Disciples of the Longmen Saber Manor always say: the first cut starts at your feet.'},
    weapon={'zh': '環首刀', 'en': 'Ring-pommel saber'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_lm_saber')]
