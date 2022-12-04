from itertools import *
from functools import *

def day3(data):
  def run(N):
    ans = 0
    lines = data.splitlines()
    if N == 2:
      lines = list(chain(*([l[:len(l)//2], l[len(l)//2:]] for l in lines)))
    for i in range(len(lines)//N):
      o = ord(next(iter(reduce(lambda x,y: x & y, (set(s) for s in lines[i*N:(i+1)*N])))))
      ans += (o - ord('a') if o >= ord('a') else o - ord('A') + 26) + 1
    return ans
  return run(2), run(3)