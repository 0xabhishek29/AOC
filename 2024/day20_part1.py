import time
import sys
sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')


import collections
import functools
import itertools
import math
import heapq
import bisect


def read_input():
    N = 141
    racetrack = []

    for _ in range(N):
        racetrack.append(input())
    
    return racetrack


def solve(inputs):

    def inside(x, y):
        return 0 <= x < n and 0 <= y < m

    def bfs(skip_x = -1, skip_y = -1):
        q = collections.deque( [(cur_x, cur_y)] )
        seen = set()
        d = -1
        
        while q:
            d += 1
            for _ in range(len(q)):
                x, y = q.popleft()

                if (x, y) == (target_x, target_y):
                    return d
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if inside(nx, ny) and (nx, ny) not in seen:
                        if (nx, ny) == (skip_x, skip_y):
                            q.append((nx, ny))
                            seen.add((nx, ny))
                            continue
                        if racetrack[nx][ny] != '#':
                            q.append((nx, ny))
                            seen.add((nx, ny))

    racetrack = inputs
    n, m = len(racetrack), len(racetrack[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    for i in range(n):
        for j in range(m):
            if racetrack[i][j] == 'S':
                cur_x, cur_y = i, j
            if racetrack[i][j] == 'E':
                target_x, target_y = i, j

    res = 0
    og = bfs()
    
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if racetrack[i][j] == '#':
                # ok = 0
                # for dx, dy in directions:
                #     nx, ny = i + dx, j + dy

                #     if racetrack[nx][ny] == '.':
                #         ok = 1
                
                # if ok:
                r = bfs(i, j)
                if og - r >= 100:
                    res += 1

    return res


inputs = read_input()

_start_time = time.perf_counter()
res = solve(inputs)
_end_time = time.perf_counter()

print(res)
print('finished in', _end_time - _start_time, 'seconds')