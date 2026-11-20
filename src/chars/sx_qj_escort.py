"""金鏢隊 Golden Escort - 龍門江湖志 (Sects of Longmen). Drawn in the 8-bit `nes` style (src/nes_sects.py, portrait in src/nes_sects_busts.py)."""

FACTION = 'sects'
KIND = 'person'
GROUP = 'sectsUnique'
META = dict(
    id='sx_qj_escort',
    name={'zh': '金鏢隊', 'en': 'Golden Escort'},
    style_name={'zh': '金字招牌', 'en': 'A Golden Signboard'},
    title={'zh': '錢家商號的鏢頭', 'en': 'Escort master of the House of Qian'},
    bio={'zh': '金色鏢車、紅金鏢旗，鏢頭戴著和錢萬里一樣的瓜皮帽。車上的貨每一件都記在帳上。', 'en': "A golden cart and a red-and-gold banner; the escort master wears a melon-skin cap like Qian Wanli's. Every crate on the cart is in the ledger."},
    weapon={'zh': '金鏢旗', 'en': 'Golden banner'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('sx_qj_escort')]
