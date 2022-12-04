import os, sys
from aocd.models import Puzzle

os.environ['AOC_SESSION'] = open('session.txt').read()

year, day = sys.argv[1:]

puzzle = Puzzle(year=int(year), day=int(day))

p1, p2 = getattr(__import__(f'y{year}'), 'day' + day)(puzzle.input_data)

print('Part 1:', p1)
print('Part 2:', p2)