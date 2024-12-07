from collections import *
from functools import *
from itertools import *
from math import inf, factorial, isqrt, sqrt, gcd, ceil, floor, log2, log, log10, perm, comb
from heapq import *
from bisect import *


def solve():
    N = 850         # number of lines of input
    calibration_equations = []

    for _ in range(N):
        t = input().split(':')
        calibration_equations.append( (int(t[0]), list(map(int, t[1].split()))) )


    def is_possible(i, cur_val):
        if cur_val > test_value:
            return 0
        if i >= len(nums):
            return cur_val == test_value
        
        r1 = is_possible(i + 1, cur_val + nums[i])
        r2 = is_possible(i + 1, cur_val * nums[i])
        r3 = is_possible(i + 1, int(str(cur_val) + str(nums[i])))

        return r1 or r2 or r3
    
    res = 0

    for test_value, nums in calibration_equations:
        if is_possible(1, nums[0]):
            res += test_value

    return res
                

print(solve())
# for _ in range(int(input())):
#     print(solve())
#     # print('YES' if solve() else 'NO')