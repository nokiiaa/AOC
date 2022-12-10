import re

def day10(data):
  cycles, x, ans = 1, 1, 0
  def check(c):
    d, m = divmod(c - 20, 40)
    D, M = divmod(c - 1, 40)
    if c < 40*6 + 1:
      print('#' if x-1 <= M <= x+1 else '.', end=('\n' if M==39 else ''))
    return c * x if m == 0 and 0 <= d <= 5 else 0
  check(cycles)
  for l in data.splitlines():
    try:
      for i in range(2):
        cycles += 1
        ans += check(cycles)
        x += int(re.findall('-*\d+', l)[i])
    except:
      pass
  return ans, ans