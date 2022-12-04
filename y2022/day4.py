def day4(data):
  f = lambda a,b,i: a&b if i else (a&b == a or a&b == b)
  ans = lambda i: sum(1 for p in [[[int(z) for z in y.split('-')] for y in x.split(',')] for x in data.splitlines()] if f(*(set(range(b[0],b[1]+1)) for b in p), i))
  return ans(0), ans(1)