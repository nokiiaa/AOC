def day8(data):
  data = [list(map(int, x[::])) for x in data.splitlines()]
  w, h = len(data[0]), len(data)
  p1, p2 = 0, 0
  for i in range(h):
    for j in range(w):
      def core(arr, rev=False):
        gen = [x >= data[i][j] for x in arr]
        count = 0
        for k in gen[::-1] if rev else gen:
          count += 1
          if k: break
        return len(gen) == 0 or not any(gen), count
      a, e = core(data[i][:j], True)
      b, f = core(data[i][j+1:])
      c, g = core([s[j] for s in data[:i]], True)
      d, h = core([s[j] for s in data[i+1:]])
      p1 += int(a or b or c or d)
      p2 = max(p2, e * f * g * h)
  return p1, p2