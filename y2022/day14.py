import re
from math import copysign
from operator import add, sub

def day14(data):
  def puzzle(part):
    cave_x, cave_y, y_floor = {}, {}, -1
    for i in range(1000):
      cave_x[i], cave_y[i] = {}, {}
    sign = lambda x: int(copysign(1, x)) if x else 0
    for line in data.splitlines():
      segments = list(map(int, re.findall('\d+', line)))
      for i in range(2, len(segments), 2):
        a, b = segments[i:i+2], segments[i-2:i]
        dx, dy = map(sub, a, b)
        d = (sign(dx), sign(dy))
        for j in range(abs(dx) + abs(dy) + 1):
          cave_x[b[0]][b[1]] = '#'
          cave_y[b[1]][b[0]] = '#'
          if part == 2: y_floor = max(y_floor, b[1] + 2)
          b = tuple(map(add, b, d))
    end, ans = False, 0
    while not end and not 0 in cave_x[500]:
      x, y, moved = 500, 0, 1
      while moved:
        l = list(filter(lambda k: k >= y, cave_x[x].keys())) + ([y_floor] if part == 2 else [])
        if not l:
          end = True
          ans -= 1
          break
        Y = min(l) - 1
        if Y != y:
          y = Y
        elif x - 1 not in cave_y[y + 1] and y + 1 != y_floor:
          x -= 1; y += 1
        elif x + 1 not in cave_y[y + 1] and y + 1 != y_floor:
          x += 1; y += 1
        else:
          moved = 0
      cave_x[x][y] = 'o'
      cave_y[y][x] = 'o'
      ans += 1
    return ans
  return puzzle(1), puzzle(2)