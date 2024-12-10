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
    nums1 = []
    nums2 = []

    for line in sys.stdin:
        a, b = map(int, line.split())
        nums1.append(a)
        nums2.append(b)
    
    hm = Counter(nums2)
    return sum(i * hm[i] for i in nums1)


print(solve())
# for _ in range(int(input())):
#     print(solve())
#     # print('YES' if solve() else 'NO')