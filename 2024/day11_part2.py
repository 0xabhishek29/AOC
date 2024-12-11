import collections
import functools
import itertools
import math
import heapq
import bisect


def solve():
    # N = 37         # number of lines of input
    nums = list(map(int, input().split()))

    @functools.cache
    def change(num):
        if num == 0:
            return [1]
        if len(str(num)) % 2 == 0:
            t = len(str(num))
            return [int(str(num)[ : t // 2]), int(str(num)[t // 2 : ])]
        return [num * 2024]
    
    hm = collections.Counter(nums)

    for _ in range(75):
        nhm = collections.Counter()
        for cur in hm:
            for t in change(cur):
                nhm[t] += hm[cur]
        hm = nhm
    
    return sum(hm.values())


print(solve())
# for _ in range(int(input())):
#     print(solve())
#     # print('YES' if solve() else 'NO')