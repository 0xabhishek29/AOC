import collections
import functools
import itertools
import math
import heapq
import bisect


def solve():
    N = 56         # number of lines of input
    grid = []

    for _ in range(N):
        grid.append(list(map(int, input())))


    @functools.cache
    def dfs(x, y):
        if grid[x][y] == 9:
            return 1
        
        res = 0

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == grid[x][y] + 1:
                res += dfs(nx, ny)
        
        return res
    
    res = 0
    n, m = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    res = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                res += dfs(i, j)
    
    return res

print(solve())
# for _ in range(int(input())):
#     print(solve())
#     # print('YES' if solve() else 'NO')