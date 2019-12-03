from collections import *
import itertools
import random
import sys
import re

f = open("3.txt").read()
ftest1 = """R8,U5,L5,D3
U7,R6,D4,L4"""
ftest2 = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""
ftest3 = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""
# f = ftest3
l1 = f.split("\n")[0].split(",")
l2 = f.split("\n")[1].split(",")

def generate_indices(x, y, code):
    numbers = range(1, int(code[1:]) + 1)
    if code[0] == "U":
        indices = map(lambda val: (x, y - val), numbers)
    elif code[0] == "D":
        indices = map(lambda val: (x, y + val), numbers)
    elif code[0] == "L":
        indices = map(lambda val: (x - val, y), numbers)
    elif code[0] == "R":
        indices = map(lambda val: (x + val, y), numbers)
    indices = list(indices)
    return indices, indices[-1]
        

# print(generate_indices(0, 0, "U10"))
# print(generate_indices(0, 0, "D10"))
# print(generate_indices(0, 0, "L10"))
# print(generate_indices(0, 0, "R10"))




positions_l1 = set()
x, y = 0,0
for c in l1:
    indices, (x, y) = generate_indices(x, y, c)
    positions_l1 = positions_l1.union(indices)

positions_l2 = set()
x, y = 0,0
for c in l2:
    indices, (x, y) = generate_indices(x, y, c)
    positions_l2 = positions_l2.union(indices)


# print(positions_l1)
# print(positions_l2)
positions = positions_l1.intersection(positions_l2)
# print(len(positions_l1), len(positions_l2), len(positions))
# print(positions)
# print(min(set(map(lambda x: (abs(x[0]), abs(x[1])), positions))))
print(min(set(map(lambda x: abs(x[0]) + abs(x[1]), positions))))
# print(sum(min(set(map(lambda x: (abs(x[0]), abs(x[1])), positions)))))
# print(min(positions))
