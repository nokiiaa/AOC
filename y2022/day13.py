from math import copysign
from functools import cmp_to_key, reduce
from operator import mul

def day13(data):
  def compute(n):
    packets = [tuple(eval(y) for y in x.splitlines()) for x in data.split('\n'*2)] if n==1 else [eval(y) for y in data.splitlines() if y]
    if n == 2: packets.extend([[[2]], [[6]]])
    copysignz = lambda x: copysign(1, x) if x else 0 
    def compare(a, b):
      if isinstance(a, int) and isinstance(b, int):
        return copysignz(a - b)
      a = [a] if isinstance(a, int) else a
      b = [b] if isinstance(b, int) else b
      for i in range(min(len(a), len(b))):
        c = compare(a[i], b[i])
        if c:
          return c
      return copysignz(len(a) - len(b))
    if n == 1:
      return sum(i+1 for i, p in enumerate(packets) if compare(*p) == -1)
    else:
      packets = sorted(packets, key=cmp_to_key(compare))
      return reduce(lambda x,y: x*y, (packets.index([[x]]) + 1 for x in (2, 6)))
  return compute(1), compute(2)