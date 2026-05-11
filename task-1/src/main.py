import time
import os
from datetime import datetime

time.sleep(2)

output = f'task-1 ran successfully - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
print(output)

os.makedirs('output', exist_ok=True)
with open('output/result.txt', 'w') as f:
    f.write(output + '\n')
