from collections import *
import itertools
import random
import sys
import re

x, y = 158126, 624574

doubles = [str(i + 10*i) for i in range(10)]


count = 0
for i in range(x, y+1):
    if len([d for d in doubles if d in str(i)]) > 0:
        if list(str(i)) == sorted(str(i)):
            count += 1

print(count)
