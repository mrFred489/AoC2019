from collections import *
import itertools
import random
import sys
import re

f = open("1.txt").read().split("\n")

def computation(x):
    return int(int(x)/3) - 2

def computation_rec(x):
    val = computation(x)
    if val > 0:
        return x + computation_rec(val)
    return x


ftest1 = [2]
ftest2 = [1969]    # 966
ftest3 = [100756]  # 50346

fuel = [computation(x) for x in f if x != ""]
print("part1", sum(fuel))
# print(fuel)
fuel = map(computation_rec, fuel)

print("part 2", sum(fuel))



