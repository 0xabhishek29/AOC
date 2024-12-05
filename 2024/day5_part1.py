from collections import *
from functools import *
from itertools import *
from math import inf, factorial, isqrt, sqrt, gcd, ceil, floor, log2, log, log10, perm, comb
from heapq import *
from bisect import *


def solve():
    N = 1366         # number of lines of input
    page_ordering_rules = []
    page_updates = []
    flag = 1

    for _ in range(N):
        inp = input()
        
        if not inp:
            flag = 0
            continue

        if flag:
            x, y = map(int, inp.split('|'))
            page_ordering_rules.append((x, y))
        else:
            page_updates.append(list(map(int, inp.split(','))))
        

    res = 0

    def get_level(page_update):
        nodes = set(page_update)
        g = defaultdict(list)
        indeg = defaultdict(int)

        for i, j in page_ordering_rules:
            if i in nodes and j in nodes:
                g[i].append(j)
                indeg[j] += 1
        
        q = deque( [node for node in nodes if indeg[node] == 0] )
        level = {}
        d = -1
        
        while q:
            d += 1
            for _ in range(len(q)):
                cur = q.popleft()
                level[cur] = d

                for nei in g[cur]:
                    indeg[nei] -= 1
                    if indeg[nei] == 0:
                        q.append(nei)
        
        return level
    
    for page_update in page_updates:
        level = get_level(page_update)
        maxLevel = -1
        ok = 1

        for page in page_update:
            if level[page] < maxLevel:
                ok = 0
                break
            maxLevel = max(maxLevel, level[page])
        
        if ok:
            res += page_update[len(page_update) // 2]
    
    return res


print(solve())
# for _ in range(int(input())):
#     print(solve())
#     # print('YES' if solve() else 'NO')