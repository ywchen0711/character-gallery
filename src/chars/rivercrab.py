"""River Crab rivercrab - a common foe (tier 1). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='rivercrab',
    name={'zh': '河蟹', 'en': 'River Crab'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 1 階小怪', 'en': 'Tier 1 common foe'},
    bio={'zh': '河岸邊橫著走的大螃蟹，鉗子能夾斷竹竿。', 'en': 'A big crab that sidles along the riverbank; its claws can snap a bamboo pole.'},
    habitat={'zh': '村外田野與山林小徑', 'en': 'Fields and forest paths outside the villages'},
    tier=1,
    base='crab',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('rivercrab')]
