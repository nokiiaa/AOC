from operator import add, sub
from math import trunc

def day9(data):
  def simulate(n):
    positions = []
    table = {'L': (-1,0), 'R': (1,0), 'U': (0,1), 'D': (0,-1)}
    knots = [(0,0) for i in range(n)]
    for op in data.splitlines():
      d, o = op.split(' ')
      for i in range(int(o)):
        knots[n-1] = tuple(map(add, knots[n-1], table[d]))
        for j in reversed(range(1, n)):
          diff = tuple(map(sub, knots[j], knots[j-1]))
          if sum(c**2 for c in diff) > 2:
            knots[j-1] = tuple(map(sub, knots[j], [trunc(c/2) for c in diff]))
            if j == 1 and knots[0] not in positions:
              positions.append(knots[0])
    return len(positions)
  return simulate(2), simulate(10)