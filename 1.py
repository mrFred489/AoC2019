from collections import *
import itertools
import random
import sys
import re

f = open("1.txt").read().split("\n")

ftest = [100756]

fuel = [int(int(x)/3) - 2 for x in f if x != ""]
print("part1", sum(fuel))
fuels = [fuel]
counter = 10
while fuels[-1] > 0:
    addfuel = int(fuels[-1]/int(3)) - 2
    print(addfuel)
    if addfuel > 0:
        fuels.append(addfuel)
    else:
        break
    # counter -= 1

print(fuels)
print("part 2", sum(fuels))
