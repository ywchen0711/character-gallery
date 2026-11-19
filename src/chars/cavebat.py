"""Cave Bat cavebat - a common foe (tier 1). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
META = dict(
    id='cavebat',
    name={'zh': '洞蝠', 'en': 'Cave Bat'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 1 階小怪', 'en': 'Tier 1 common foe'},
    bio={'zh': '山洞裡倒掛的蝙蝠，一有火光就整群撲出來。', 'en': 'Bats that hang in caves and burst out in a swarm at the first light of a torch.'},
    habitat={'zh': '村外田野與山林小徑', 'en': 'Fields and forest paths outside the villages'},
    tier=1,
    base='bat',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('cavebat')]
