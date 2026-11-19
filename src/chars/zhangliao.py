"""張遼 Zhang Liao - an enemy general of 三國志 霸王之路 (stage: 合肥之戰). Drawn in the 8-bit `nes` style only (src/nes_sango.py)."""

FACTION = 'sango'
META = dict(
    id='zhangliao',
    name={'zh': '張遼', 'en': 'Zhang Liao'},
    style_name={'zh': '曹軍名將', 'en': "Cao Cao's great general"},
    title={'zh': '合肥之戰・曹軍名將', 'en': "The Battle of Hefei - Cao Cao's great general"},
    bio={'zh': '曹操帳下名將，白纓藍盔、短鬚沉穩。以少擊眾、臨危不亂，打得敵軍聞名喪膽。', 'en': "One of Cao Cao's finest generals: a blue helmet with a white plume, a neat beard and a steady gaze. Calm under pressure, he wins against the odds."},
    weapon={'zh': '長戟', 'en': 'Halberd'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('zhangliao')]
