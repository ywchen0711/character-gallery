"""文醜 Wen Chou - an enemy general of 三國志 霸王之路 (stage: 延津之戰). Drawn in the 8-bit `nes` style only (src/nes_sango.py)."""

FACTION = 'sango'
META = dict(
    id='wenchou',
    name={'zh': '文醜', 'en': 'Wen Chou'},
    style_name={'zh': '河北名將', 'en': 'Champion of Hebei'},
    title={'zh': '延津之戰・河北名將', 'en': 'The Battle of Yanjin - Champion of Hebei'},
    bio={'zh': '與顏良齊名的袁軍猛將，尖頂鐵盔、齜牙怒目、一把長槍。性子比顏良更兇，一心要替兄弟報仇。', 'en': "Yan Liang's equal in Yuan Shao's army: a spiked iron helmet, bared teeth, glaring eyes and a spear. Fiercer than his comrade, and set on avenging him."},
    weapon={'zh': '長槍', 'en': 'Spear'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('wenchou')]
