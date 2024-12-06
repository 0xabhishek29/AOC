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

    res = 0
    n, m = len(lab_map), len(lab_map[0])

    def traverse(start_x, start_y, obstacle_x = -1, obstacle_y = -1):
        x, y = start_x, start_y
        res = [[0] * m for _ in range(n)]
        seen = set()
        direction = 0

        while 0 <= x < n and 0 <= y < m:
            res[x][y] = 1
            nx, ny = move(x, y, direction)

            if 0 <= nx < n and 0 <= ny < m and (lab_map[nx][ny] == '#' or (nx == obstacle_x and ny == obstacle_y)):
                direction = (direction + 1) % 4
                if obstacle_x != -1 and obstacle_y != -1 and (x, y, direction) in seen:
                    return 1, 0
                seen.add((x, y, direction))
            else:
                x, y = nx, ny

        return 0, res

    for i in range(n):
        for j in range(m):
            if lab_map[i][j] == '^':
                start_x, start_y = i, j
                break
    
    visited = traverse(start_x, start_y)[1]
    
    for x in range(n):
        for y in range(m):
            if visited[x][y] and traverse(start_x, start_y, x, y)[0]:
                res += 1
        
    return res


print(solve())
# for _ in range(int(input())):
#     print(solve())
#     # print('YES' if solve() else 'NO')