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
    N = 140
    grid = []

    for _ in range(N):
        grid.append(input())

    def check(x, y):
        res = 0

        for dx in range(-1, 2):
            for dy in range(-1, 2):
                k = 1
                nx, ny = x + dx, y + dy
                
                while 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == pat[k]:
                    nx += dx
                    ny += dy
                    k += 1
                    if k == 4:
                        break
                
                res += k == 4
        
        return res

    n = len(grid)
    m = len(grid[0])
    pat = 'XMAS'
    res = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'X':
                res += check(i, j)
    
    return res


print(solve())
# for _ in range(int(input())):
#     print(solve())
#     # print('YES' if solve() else 'NO')