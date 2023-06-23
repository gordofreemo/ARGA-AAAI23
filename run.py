import os

for x in os.walk('./dataset/evaluation/'):
  if not (os.path.isfile(f'./solutions/correct/solutions_{x}') or os.path.isfile(f'./solutions/incorrect/solutions_{x}')):
    continue
  os.system(f'python3 main.py {x} evaluation')