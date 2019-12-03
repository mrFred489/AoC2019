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


def get_intersections(l1, l2):
    positions_l1 = set()
    x, y = 0, 0
    for c in l1:
        indices, (x, y) = generate_indices(x, y, c)
        positions_l1 = positions_l1.union(indices)
    
    positions_l2 = set()
    x, y = 0, 0
    for c in l2:
        indices, (x, y) = generate_indices(x, y, c)
        positions_l2 = positions_l2.union(indices)
    return positions_l1.intersection(positions_l2)


def part1():
    positions = get_intersections(l1, l2)
    print(min(set(map(lambda x: abs(x[0]) + abs(x[1]), positions))))


# print(positions_l1)
# print(positions_l2)
# print(len(positions_l1), len(positions_l2), len(positions))
# print(positions)
# print(min(set(map(lambda x: (abs(x[0]), abs(x[1])), positions))))
# print(sum(min(set(map(lambda x: (abs(x[0]), abs(x[1])), positions)))))
# print(min(positions))

def find_intersecting_steps(x, y, code, steps, intersections):
    numbers = range(1, int(code[1:]) + 1)
    print("code", code)
    if code[0] == "U":
        indices = map(lambda val: (x, y - val, steps+val), numbers)
    elif code[0] == "D":
        indices = map(lambda val: (x, y + val, steps+val), numbers)
    elif code[0] == "L":
        indices = map(lambda val: (x - val, y, steps+val), numbers)
    elif code[0] == "R":
        indices = map(lambda val: (x + val, y, steps+val), numbers)
    intersecting_steps = []
    indices = list(indices)
    for x, y, s in indices:
        if (x, y) in intersections:
            intersecting_steps.append((x, y, s))
    indices = list(indices)
    # print(indices)
    return indices[-1], intersecting_steps


def part2():
    intersections = get_intersections(l1, l2)
    intersecting_steps_1 = []
    x, y, steps = 0, 0, 0
    for c in l1:
        (x, y, steps), i_steps = find_intersecting_steps(x, y, c, steps, intersections)
        intersecting_steps_1 += i_steps
    
    intersecting_steps_2 = []
    x, y, steps = 0, 0, 0
    for c in l2:
        (x, y, steps), i_steps = find_intersecting_steps(x, y, c, steps, intersections)
        intersecting_steps_2 += i_steps

    all_steps = []
    for s1 in intersecting_steps_1:
        for s2 in intersecting_steps_2:
            if s1[0:-1] == s2[0:-1]:
                all_steps.append(s1[-1] + s2[-1])
    print(min(all_steps))

part2()
