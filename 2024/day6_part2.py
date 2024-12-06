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

    
    def get_visited_positions(start_x, start_y):
        curX, curY = start_x, start_y
        visited = [[0] * m for _ in range(n)]
        d = 0

        for _ in range(n*m*4):
            visited[curX][curY] = 1
            dx, dy = directions[d]
            nx, ny = curX + dx, curY + dy

            if not (0 <= nx < n and 0 <= ny < m):
                return visited

            if lab_map[nx][ny] == '#':
                d = (d + 1) % 4
            else:
                curX, curY = nx, ny
    
    def can_place_obstacle(obstacle_x, obstacle_y):
        curX, curY = start_x, start_y
        seen = set()
        d = 0

        for _ in range(n*m*4):
            dx, dy = directions[d]
            nx, ny = curX + dx, curY + dy

            if not (0 <= nx < n and 0 <= ny < m):
                return 0

            if lab_map[nx][ny] == '#' or (nx == obstacle_x and ny == obstacle_y):
                d = (d + 1) % 4
                if (curX, curY, d) in seen:
                    return 1
                seen.add((curX, curY, d))
            else:
                curX, curY = nx, ny
    
    res = 0
    n, m = len(lab_map), len(lab_map[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i in range(n):
        for j in range(m):
            if lab_map[i][j] == '^':
                start_x, start_y = i, j
                break
    
    visited = get_visited_positions(start_x, start_y)
    
    for x in range(n):
        for y in range(m):
            if visited[x][y] and can_place_obstacle(x, y):
                res += 1
        
    return res

print(solve())
# for _ in range(int(input())):
#     print(solve())
#     # print('YES' if solve() else 'NO')