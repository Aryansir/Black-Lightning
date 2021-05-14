# Copyright (C) 2021 KeinShin@Github.

import sys
import os
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from pathlib import Path
a=Path('exconfig.py').is_file()


if a:
    from exconfig import variable as Variable
else:
    from Config.utils import Variable


Variable  = Variable



