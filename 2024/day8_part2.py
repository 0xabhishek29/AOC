import collections
import functools
import itertools
import math
import heapq
import bisect


def solve():
    N = 50         # number of lines of input
    antenna_map = []

    for _ in range(N):
        antenna_map.append(input())

    
    def is_inside(x, y):
        return 0 <= x < n and 0 <= y < m

    n, m = len(antenna_map), len(antenna_map[0])
    res = [[0 for _ in range(m)] for _ in range(n)]
    antennas = collections.defaultdict(list)

    for i in range(n):
        for j in range(m):
            if antenna_map[i][j] != '.':
                antennas[antenna_map[i][j]].append((i, j))
    
    for points in antennas.values():
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x0, y0 = points[i]
                x1, y1 = points[j]

                nx, ny = x0, y0
                while is_inside(nx, ny):
                    res[nx][ny] = 1
                    nx += x0 - x1
                    ny += y0 - y1

                nx, ny = x1, y1
                while is_inside(nx, ny):
                    res[nx][ny] = 1
                    nx += x1 - x0
                    ny += y1 - y0
 
    return sum(sum(row) for row in res)


print(solve())
# for _ in range(int(input())):
#     print(solve())
#     # print('YES' if solve() else 'NO')