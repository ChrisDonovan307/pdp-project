#!/usr/bin/env python3

import os
import shutil
from glob import glob

changed = os.environ.get("PDP_CHANGED")
files = changed.splitlines() if changed is not None else glob("input/*.csv")

for path in files:
    shutil.copy(path, "output")
