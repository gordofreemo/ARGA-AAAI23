import os
import sys

x = sys.argv[1]
if not (os.path.isfile(f'./solutions/correct/solutions_{x}') or os.path.isfile(f'./solutions/incorrect/solutions_{x}')):
  exit(1)
os.system(f'python main.py {x} evaluation')