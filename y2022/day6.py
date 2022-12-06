def day6(data):
  return ((lambda n: next(i+n for i in range(len(data)-n) if len(set(data[i:i+n])) == n))(n) for n in (4, 14))