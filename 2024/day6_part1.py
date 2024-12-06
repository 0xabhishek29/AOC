from collections import *
from functools import *
from itertools import *
from math import inf, factorial, isqrt, sqrt, gcd, ceil, floor, log2, log, log10, perm, comb
from heapq import *
from bisect import *


def solve():
    N = 130         # number of lines of input
    lab_map = []

    for _ in range(N):
        lab_map.append(input())


    def move(x, y, direction):
        match direction:
            case 0:
                x -= 1
            case 1:
                y += 1
            case 2:
                x += 1
            case 3:
                y -= 1
        
        return x, y

    res = set()
    n, m = len(lab_map), len(lab_map[0])
    
    for i in range(n):
        for j in range(m):
            if lab_map[i][j] == '^':
                x, y = i, j
                break

    direction = 0

    while 0 <= x < n and 0 <= y < m:
        res.add((x, y))
        nx, ny = move(x, y, direction)

        if 0 <= nx < n and 0 <= ny < m and lab_map[nx][ny] == '#':
            direction = (direction + 1) % 4
        else:
            x, y = nx, ny

    return len(res)


print(solve())
# for _ in range(int(input())):
#     print(solve())
#     # print('YES' if solve() else 'NO')