import shutil
from pathlib import Path

task_dir = Path(__file__).resolve().parent.parent
shutil.copy(
        task_dir / "input" / "2_clean" / "data.csv",
        task_dir / "output"
)
