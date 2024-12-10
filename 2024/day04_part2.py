from collections import *
from functools import *
from itertools import *
from math import inf, factorial, isqrt, sqrt, gcd, ceil, floor, log2, log, log10, perm, comb
from heapq import *
from bisect import *


def readIntArr():
    return list(map(int, input().split()))


def readArr():
    return input().split()


def solve():
    N = 140         # number of lines of input
    grid = []

    for _ in range(N):
        grid.append(input())

    def check(x, y):
        cnt = 0

        for t in -1, 1:
            x1, y1 = x - 1, y + t
            x2, y2 = x + 1, y - t
            if grid[x1][y1] + grid[x2][y2] in ['MS', 'SM']:
                cnt += 1

        return cnt >= 2

    n = len(grid)
    m = len(grid[0])
    res = 0
    
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if grid[i][j] == 'A':
                res += check(i, j)
    
    return res


print(solve())
# for _ in range(int(input())):
#     print(solve())
#     # print('YES' if solve() else 'NO')