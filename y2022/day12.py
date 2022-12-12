from operator import add
import sys
import itertools

def day12(data):
  data = [[ord(c) - ord('a') for c in x] for x in data.splitlines()]
  find = lambda p: next((i, x.index(p)) for i, x in enumerate(data) if p in x)
  w, h = len(data[0]), len(data)
  start = find(ord('S') - ord('a'))
  end = find(ord('E') - ord('a'))
  data[start[0]][start[1]] = 0
  data[end[0]][end[1]] = 25

  def puzzle(n):
    graph, dist, prev, queue = {}, {}, {}, []
  
    for y in range(h):
      for x in range(w):
        graph[(y, x)] = []
        def add(Y, X):
          if 0<=Y<h and 0<=X<w:
            a, b = data[y][x], data[Y][X]
            if n == 2: a, b = b, a
            return a >= b - 1
        coords = [(y, x - 1), (y, x + 1), (y - 1, x), (y + 1, x)]
        for c in coords:
          if add(*c):
            graph[(y, x)].append(c)
        dist[(y, x)] = 1e9
        prev[(y, x)] = None
        queue.append((y, x))
  
    dist[start if n==1 else end] = 0
  
    while queue:
      u = min(queue, key=lambda k: dist[k])
      queue.remove(u)
      for v in graph[u]:
        if v in queue:
          alt = dist[u] + 1
          if alt < dist[v]:
            dist[v] = alt
            prev[v] = u
  
    return dist[end] if n==1 else min(dist[k] for k in dist.keys() if not data[k[0]][k[1]])
  return puzzle(1), puzzle(2)