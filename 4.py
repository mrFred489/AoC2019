from collections import *
import itertools
import random
import sys
import re

x, y = 158126, 624574

digits = [str(i) for i in range(10)]

def check(x):
    if list(x) == sorted(x):
        for d in digits:
            for j in range(6, 1, -1):
                if d*j in x:
                    # print(d*j)
                    if j == 2:
                        return True
                    break
    return False


















# def check2(x):
#     b = False
#     if list(x) == sorted(x):
#         for j in range(1, 6):
#             if x[j-1] == x[j] and not b:
#                 b = not b
#             if x[j-1] == x[j]:
#     # print(b, bsaved)
#     return b


print("111112", check("111112")) # False
print("111122", check("111122")) # True
print("111222", check("111222")) # False
print("112222", check("112222")) # True
print("122222", check("122222")) # False
print("123456", check("123456")) # False
print("112233", check("112233")) # True
print("123444", check("123444")) # False
print("124445", check("124445")) # False
print("111111", check("111111")) # False
print("111122", check("111122")) # True


count = 0
for i in range(x, y+1):
    istr = str(i)
    b = check(istr)
    count += int(b)

print(count)
