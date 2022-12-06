def day6(data):
  return ([i for i in range(n,len(data)) if len(set(data[i-n:i])) == n][0] for n in (4, 14))