import sys
sys.setrecursionlimit(10 ** 7)
import functools
import math


def solve():
    N = 1279         # number of lines of input
    inp = []
    tmp = []

    for _ in range(N):
        t = input().split()
        if not t:
            continue
        if t[0] == 'Button':
            tmp.append(int(t[2][2 : -1]))
            tmp.append(int(t[3][2 : ]))
        elif t[0] == 'Prize:':
            tmp.append(int(t[1][2 : -1]))
            tmp.append(int(t[2][2 : ]))
            inp.append(tmp)
            tmp = []

    
    @functools.cache
    def min_traverse(cur_x, cur_y, idx):
        if cur_x > target_x or cur_y > target_y:
            return math.inf
        if cur_x == target_x and cur_y == target_y:
            return 0
        
        r1 = 3 + min_traverse(cur_x + ax, cur_y + ay, idx)
        r2 = 1 + min_traverse(cur_x + bx, cur_y + by, idx)
        return min(r1, r2)
    
    res = 0
    
    for idx in range(len(inp)):
        ax, ay, bx, by, target_x, target_y = inp[idx]
        r = min_traverse(0, 0, idx)
        if r != math.inf:
            res += r
    
    return res


print(solve())