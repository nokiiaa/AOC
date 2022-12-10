from math import trunc

def day9(data):
  def simulate(n):
    positions = [(0, 0)]
    table = {'L': (-1,0), 'R': (1,0), 'U': (0,1), 'D': (0,-1)}
    knots = [(0, 0) for i in range(n)]
    for op in data.splitlines():
      d, o = op.split(' ')
      dx, dy = table[d]
      for i in range(int(o)):
        knots[n-1] = (knots[n-1][0] + dx, knots[n-1][1] + dy)
        for j in reversed(range(1, n)):
          diff = (knots[j][0] - knots[j-1][0], knots[j][1] - knots[j-1][1])
          if diff[0] ** 2 + diff[1] ** 2 > 2:
            knots[j-1] = (knots[j][0] - trunc(diff[0]/2), knots[j][1] - trunc(diff[1]/2))
            if j == 1 and knots[0] not in positions:
              positions.append(knots[0])
    return len(positions)
  return simulate(2), simulate(10)