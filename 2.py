from collections import *
import itertools
import random
import sys
import re

f = open("2.txt").read().strip("\n").split(",")
teststack1 = [1,0,0,0,99]
teststack2 = [2,3,0,3,99]
teststack3 = [2,4,4,5,99,0]
teststack4 = [1,1,1,4,99,5,6,0,99]


stack = [int(x) for x in f]
# stack = teststack4

# 99: exit
# 1 x y z: save ((lookup x) + (lookup y)) in z
# 2 x y z: save ((lookup x) * (lookup y)) in z

operators = {
    1: (lambda x, y: x + y),
    2: (lambda x, y: x * y)
}

def operator(op, val1, val2):
    return op(val1, val2)


def compute(stack, pos):
    if stack[pos] == 99:
        return stack
    x, y, z, w = stack[pos: pos+4]
    stack[w] = operator(operators[x], stack[y], stack[z])
    return stack

stack[1] = 12
stack[2] = 2
pos = 0

while pos < len(stack) and stack[pos] != 99:
    stack = compute(stack, pos)
    pos += 4

print(stack)
print(stack[0])
