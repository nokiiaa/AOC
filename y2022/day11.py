from operator import add, mul
from functools import reduce
import re

def int_in_line(l):
  return int(re.findall('\d+', l)[0])

def day11(data):
  data = data.splitlines()
  
  def compute(mode, rounds):
    monkey_items = []
    monkey_counters = []
    monkey_programs = []
    mod_product = 1
  
    for i in range(0, len(data), 7):
      monkey_items.append(list(map(int, re.findall('\d+', data[i+1]))))
      monkey_counters.append(0)
      imm = list(map(int, re.findall('\d+', data[i+2])))
      mod = int_in_line(data[i+3])
      op = add if '+' in data[i+2] else mul
      a, b = int_in_line(data[i+4]), int_in_line(data[i+5])
      mod_product *= mod
      func = (lambda x: op(x, imm[0])) if len(imm) else lambda x: op(x, x)
      monkey_programs.append((imm, mod, op, a, b, func))
    
    # In Puzzle 2, we can compute the worry levels modulo the product of the numbers in all divisibility tests.
    # (Don't know about others, but in my input, they're essentially a permutation of all primes between 2 and 19)
    # This speeds up the computation drastically.
    after_op = (lambda x: x//3) if mode else (lambda x: x % mod_product)
    
    for round in range(rounds):
      for i in range(0, len(data), 7):
        I = i//7
        imm, mod, op, a, b, func = monkey_programs[I]
        for x in monkey_items[I]:
          c = after_op(func(x))
          dest = a if not (c % mod) else b
          monkey_items[dest].append(c)
          monkey_counters[I] += 1
        monkey_items[I].clear()
    return reduce(mul, sorted(monkey_counters)[-2:])
  return compute(1, 20), compute(0, 10000)