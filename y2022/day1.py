def day1(data):
  sums = sorted(sum(int(y) for y in x.split('\n')) for x in data.split('\n\n'))
  return sums[-1], sum(sums[-3:])