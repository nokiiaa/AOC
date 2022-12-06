def day6(data):
  return ([i+n for i in range(len(data)-n) if len(set(data[i:i+n])) == n][0] for n in (4, 14))