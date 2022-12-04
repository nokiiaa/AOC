try:
  for n in range(1, 25+1):
    exec(f'from .day{n} import day{n}')
except:
  pass