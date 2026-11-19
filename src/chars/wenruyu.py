"""溫如玉 Wen Ruyu - clerk of the Alliance treasury. Drawn in the 8-bit `nes` style only (src/nes_longmen3.py)."""

FACTION = 'longmen'
KIND = 'person'
META = dict(
    id='wenruyu',
    name={'zh': '溫如玉', 'en': 'Wen Ruyu'},
    style_name={'zh': '書辦', 'en': 'Clerk'},
    title={'zh': '盟庫書辦', 'en': 'Clerk of the Alliance Treasury'},
    bio={'zh': '錢萬里身邊的書辦，青衫一領，衣領上總沾著一點墨。說話輕聲細語，開口前先道一聲「失禮了」；帳本抱在胸前，字寫得比誰都工整。', 'en': "Qian Wanli's clerk, in a plain green gown with a spot of ink always on the collar. He speaks softly and begins with “pardon me”; the ledger is always held to his chest, and his hand is the neatest of anyone's."},
    weapon={'zh': '帳本與毛筆', 'en': 'Ledger and brush'},
)


def variants():
    from nes_variant import NESVariant
    return [NESVariant('wenruyu')]
