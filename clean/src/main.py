import os
import shutil
from glob import glob

changed = os.environ.get("PDP_CHANGED_IMPORT")
files = changed.splitlines() if changed is not None else glob("input/import/*.csv")

for path in files:
    shutil.copy(path, "output")
