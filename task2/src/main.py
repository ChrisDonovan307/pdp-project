import shutil
from pathlib import Path

task_dir = Path(__file__).resolve().parent.parent
shutil.copy(
        task_dir / "input" / "task1" / "output" / "data1.csv", 
        task_dir / "output"
)
