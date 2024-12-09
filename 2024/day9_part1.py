import collections
import functools
import itertools
import math
import heapq
import bisect


def solve():
    # N = 50         # number of lines of input
    disk_map = input()

    s = []
    t = 0

    for idx, i in enumerate(disk_map):
        if idx % 2 == 0:
            s += [str(t)] * int(i)
            t += 1
        else:
            s += ['.'] * int(i)

    left, right = 0, len(s) - 1

    while left < right:
        while left < right and s[left] != '.':
            left += 1
        while left < right and s[right] == '.':
            right -= 1
        
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    return sum(idx*int(i) for idx, i in enumerate(s) if i.isdigit())


print(solve())
# for _ in range(int(input())):
#     print(solve())
#     # print('YES' if solve() else 'NO')