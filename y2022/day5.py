import re

def day5(data):
  def run(order):
    crates = [[] for i in range(9)]
    flag = 1
    for line in data.splitlines():
      if any(map(str.isdigit, line)):
        if not flag:
          n, src, dst = map(int, re.findall('\d+', line))
          crates[dst-1] += crates[src-1][-n:][::order]
          crates[src-1] = crates[src-1][:-n]
        flag = 0
      else:
        for i, c in filter(lambda x: x[1] != ' ', enumerate(line[1::4])):
          crates[i].insert(0, c)
    return ''.join(c[-1] for c in crates)
  return run(-1), run(1)