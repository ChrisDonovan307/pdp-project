import shutil
from glob import glob

for path in glob("input/model/*.csv"):
    shutil.copy(path, "output")
