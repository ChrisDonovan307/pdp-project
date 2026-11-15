import shutil
from glob import glob

for path in glob("input/clean/*.csv"):
    shutil.copy(path, "output")
