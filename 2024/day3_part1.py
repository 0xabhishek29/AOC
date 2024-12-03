import sys
from collections import *
from functools import *
from itertools import *
from math import inf, factorial, isqrt, sqrt, gcd, ceil, floor, log2, log, log10, perm, comb
from heapq import *
from bisect import *
import re


def readIntArr():
    return list(map(int, input().split()))


def readArr():
    return input().split()


def solve():    
    res = 0

    for s in sys.stdin:
        pat = 'mul\((\d{1,3}),(\d{1,3})\)'
        muls = re.findall(pat, s)

        for x, y in muls:
            if 1 <= len(x) <= 3 and 1 <= len(y) <= 3:
                res += int(x) * int(y)
            
    return res


print(solve())
# for _ in range(int(input())):
#     print(solve())
#     # print('YES' if solve() else 'NO')