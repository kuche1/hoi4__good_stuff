#! /usr/bin/env python3

# ruff: noqa: E402

# generally the target is to extend everything till 1950

import sys
from pathlib import Path

HERE = Path(__file__).parent

sys.path.append(str(HERE))
from extend_land_doctorine import extend_land_doctorine
from extend_industry import extend_industry
from extend_air_doctorine import extend_air_doctorine
from extend_artillery import extend_artillery
del sys.path[-1]

extend_land_doctorine(HERE / 'gucci_land_doctorine.txt', 18)
extend_industry      (HERE / 'gucci_industry.txt'      ,  7)
extend_air_doctorine (HERE / 'gucci_air_doctorine.txt' , 12)
extend_artillery     (HERE / 'gucci_artillery.txt'     ,  7)
