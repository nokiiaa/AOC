import re
from math import copysign
from functools import cmp_to_key

def day15(data):
  sign = lambda x: int(copysign(1, x)) if x else 0
  md = lambda x1, y1, x2, y2: abs(x1 - x2) + abs(y1 - y2)
  ed = lambda x1, y1, x2, y2: (x1 - x2) ** 2 + (y1 - y2) ** 2
  sensors = []
  for line in data.splitlines():
    xs, ys, xb, yb = map(int, re.findall('-*\d+', line))
    sensors.append((xs, ys, xb, yb, md(xs, ys, xb, yb)))
  def puzzle(part):
    ans = 0
    for y in (range(4000001) if part == 2 else [2000000]):
      intervals, beacons = [], set()
      for (xs, ys, xb, yb, dist) in sensors:
        hw = max(-1, dist - abs(ys - y))
        beacons.add((xb, yb))
        if hw > -1: intervals.append((xs - hw, xs + hw))
      if intervals:
        intervals.sort(key=cmp_to_key(lambda a, b: sign(a[0] - b[0])))
        i = 0
        if part == 1:
          while i < len(intervals):
            flag = 0
            for b in beacons:
              if b[1] == y and intervals[i][0] <= b[0] <= intervals[i][1]:
                r = []
                if intervals[i][0] < b[0]: r.append((intervals[i][0], b[0] - 1))
                if intervals[i][1] > b[0]: r.append((b[0] + 1, intervals[i][1]))
                intervals = intervals[:i] + r + intervals[i+1:]
                flag = 1
            if not flag:
              i += 1
        output = [intervals[0]]
        for i in range(1, len(intervals)):
          top = output[-1]
          if top[1] < intervals[i][0]:
            output.append(intervals[i])
          elif top[1] <= intervals[i][1]:
            output.pop()
            output.append((top[0], intervals[i][1]))
        if part == 1:
         for i in output:
            ans += max(0, i[1] - i[0] + 1)
        elif part == 2:
          if len(output) == 1:
            if output[0][0] == 1:
              ans = (0, y)
            elif output[0][1] == 3999999:
              ans = (3999999, y)
          elif len(output) == 2:
            if output[0][1] + 2 == output[1][0]:
              ans = (output[0][1] + 1, y)
    if part == 2:
      ans = ans[0] * 4000000 + ans[1]
    return ans
  return puzzle(1), puzzle(2)