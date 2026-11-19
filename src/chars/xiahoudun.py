"""夏侯惇 Xiahou Dun - an enemy general of 三國志 霸王之路 (stage: 博望坡). Drawn in the 8-bit `nes` style only (src/nes_sango.py)."""

FACTION = 'sango'
META = dict(
    id='xiahoudun',
    name={'zh': '夏侯惇', 'en': 'Xiahou Dun'},
    style_name={'zh': '獨眼將軍', 'en': 'The one-eyed general'},
    title={'zh': '博望坡・獨眼將軍', 'en': 'Bowang Slope - The one-eyed general'},
    bio={'zh': '曹操的族弟兼大將，左眼戴著黑眼罩、滿臉黑鬍，鐵甲藍纓。脾氣剛烈，衝鋒總在最前面。', 'en': "Cao Cao's kinsman and general, with a black patch over his left eye, a full black beard and iron armour with blue lacing. Hot-tempered, always first into the charge."},
    weapon={'zh': '長槍', 'en': 'Spear'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('xiahoudun')]
