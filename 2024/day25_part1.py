import time
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


import collections
import functools
import itertools
import math
import heapq
import bisect


def read_input():
    N = 3999
    locks = []
    keys = []
    tmp = []

    for _ in range(N):
        t = input()
        if not t:
            if tmp[0][0] == '#':
                locks.append(tmp)
            else:
                keys.append(tmp)
            tmp = []
            continue
        tmp.append(t)
    
    if tmp[0][0] == '#':
        locks.append(tmp)
    else:
        keys.append(tmp)
    
    return locks, keys


def solve(inputs):
    locks, keys = inputs

    def get_pin_heights(nums):
        res = []

        for i in zip(*nums):
            res.append(i.count('#') - 1)
        
        return res
    

    locks_pin_heights = [get_pin_heights(lock) for lock in locks]
    keys_pin_heights = [get_pin_heights(key) for key in keys]
    res = 0

    for lock_pin_heights in locks_pin_heights:
        for key_pin_heights in keys_pin_heights:
            res += all(i + j <= 5 for i, j in zip(lock_pin_heights, key_pin_heights))

    return res


inputs = read_input()

_start_time = time.perf_counter()
res = solve(inputs)
_end_time = time.perf_counter()

print(res)
print('finished in', _end_time - _start_time, 'seconds')