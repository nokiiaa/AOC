import re

def day10(data):
  cycles, x, ans = 1, 1, 0
  def check(c):
    d, m = divmod(c - 20, 40)
    D, M = divmod(c - 1, 40)
    if c < 40*6 + 1:
      print('#' if x-1 <= M <= x+1 else '.', end=('\n' if M==39 else ''))
    if m == 0 and 0 <= d <= 5:
      return c * x
    return 0
  check(cycles)
  for l in data.splitlines():
    try:
      inc = int(re.findall('-*\d+', l)[0])
      ans += check(cycles + 1)
      x += inc
      ans += check(cycles + 2)
      cycles += 2
    except:
      cycles += 1
      ans += check(cycles)
  return ans, ans