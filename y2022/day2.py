import math

def day2(data):
  score1, score2 = 0, 0
  cmp = lambda a, b: (((a-b)//2 if abs(a-b) == 2 else b-a) + 1) * 3
  for x in data.splitlines():
    X, Y = x.split()
    X = ord(X) - ord('A') + 1
    Y = ord(Y) - ord('X') + 1
    score1 += cmp(X, Y) + Y
    score2 += (Y-1)*3 + [i for i, v in enumerate(cmp(X,z) for z in range(1,4)) if v == (Y-1)*3][0] + 1
  return score1, score2