import collections
import functools
import itertools
import math
import heapq
import bisect


def solve():
    # N = 50         # number of lines of input
    disk_map = input()


    def get_result(s, addition):
        res = []
        
        for i in range(len(s)):
            for block_id, size in addition[i]:
                res += [str(block_id)] * size

            block_id, size = s[i]

            if block_id == -1:
                block_id = '.'
            res += [str(block_id)] * size

        return sum(idx * int(i) for idx, i in enumerate(res) if i.isdigit())

    s = []
    t = 0

    for idx, i in enumerate(disk_map):
        if idx % 2 == 0:
            s.append( [t, int(i)] )
            t += 1
        else:
            s.append( [-1, int(i)] )

    addition = collections.defaultdict(list)

    for right in range(len(s) - 1, -1, -2):
        block_id, size = s[right]

        for left in range(1, right, 2):
            _, siz = s[left]

            if siz >= size:
                s[left] = [-1, siz - size]
                addition[left].append( [block_id, size] )
                s[right] = [-1, size]
                break

    return get_result(s, addition)


print(solve())
# for _ in range(int(input())):
#     print(solve())
#     # print('YES' if solve() else 'NO')