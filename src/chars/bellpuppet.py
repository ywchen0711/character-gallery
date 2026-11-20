"""Bell Puppet bellpuppet - a common foe of Longmen Quest II (tier 6). An original monster in the 8-bit `nes` style (src/nes_foes_art.py)."""

FACTION = 'foe'
KIND = 'monster'
GROUP = 'longmen2Foes'
META = dict(
    id='bellpuppet',
    name={'zh': '鈴偶', 'en': 'Bell Puppet'},
    style_name={'zh': '小怪', 'en': 'Common foe'},
    title={'zh': '第 6 階小怪', 'en': 'Tier 6 common foe'},
    bio={'zh': '掛滿銅鈴的木偶，由鈴聲牽著動。', 'en': 'A wooden puppet hung with brass bells, moved by their ringing.'},
    habitat={'zh': '萬妖塔', 'en': 'The Tower of Ten Thousand Beasts'},
    tier=6,
    base='dummy_iron',
)


def variants():
    from nes_foes import FoeVariant
    return [FoeVariant('bellpuppet')]
