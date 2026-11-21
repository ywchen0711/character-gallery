"""Re-export only the redrawn Longmen cast (src/nes2_*.py; their main `nes` art plus the previous art as `nes_old`)
and merge them into chars/index.json, leaving every other character untouched. A full
`python tools/export.py` + `export_sects.py` + `export_tactics.py` run gives the same files.

    python -P tools/export_nes2.py
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'src'))
sys.path.insert(0, os.path.join(ROOT, 'src', 'chars'))

import export_ids  # noqa: E402
from nes_variant import nes2_ids  # noqa: E402

if __name__ == '__main__':
    export_ids.main(sorted(nes2_ids()))
