"""陣法師 Formation Master - 龍門戰記 (Longmen Tactics). Drawn in the 8-bit `nes` style (src/nes_tactics.py, portrait in src/nes_tactics_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'tacticsJobs'
META = dict(
    id='sx_strategist',
    name={'zh': '陣法師', 'en': 'Formation Master'},
    style_name={'zh': '八卦陣', 'en': 'Eight Trigrams'},
    title={'zh': '布陣的人', 'en': 'A layer of battle arrays'},
    bio={'zh': '灰袍黑冠，手搖一把白羽扇。八卦陣守，北斗陣攻。', 'en': 'A grey robe, a dark cap and a white feather fan. The Eight Trigrams to guard, the Big Dipper to strike.'},
    weapon={'zh': '羽扇', 'en': 'Feather fan'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_strategist')]
