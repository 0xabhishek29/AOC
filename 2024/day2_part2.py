import sys
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

    def check(nums):
        n = len(nums)
        return all(1 <= nums[i + 1] - nums[i] <= 3 for i in range(n - 1)) or all(1 <= nums[i] - nums[i + 1] <= 3 for i in range(n - 1))

    res = 0

    for line in sys.stdin:
        nums = list(map(int, line.split()))
        n = len(nums)

        for i in range(n):
            if check(nums[ : i] + nums[i + 1 : ]):
                res += 1
                break

    return res


print(solve())
# for _ in range(int(input())):
#     print(solve())
#     # print('YES' if solve() else 'NO')