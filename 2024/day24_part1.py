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
    N = 313
    wires = {}
    equations = {}
    equations_start = 0

    for _ in range(N):
        t = input().split()
        if not t:
            equations_start = 1
            continue

        if not equations_start:
            wires[t[0][ : -1]] = int(t[-1])
        else:
            n1, func, n2, _, n3 = t
            equations[n3] = [n1, func, n2]
    
    return wires, equations


def solve(inputs):
    wire_values, equations = inputs

    def get_topo_order():
        q = collections.deque([node for node in wire_values if node not in indeg])
        res = []

        while q:
            cur = q.popleft()
            res.append(cur)

            for nei in graph[cur]:
                indeg[nei] -= 1

                if indeg[nei] == 0:
                    q.append(nei)
        
        return res
    
    def calc(a, b, func):
        match func:
            case 'AND':
                return a & b
            case 'OR':
                return a | b
            case 'XOR':
                return a ^ b

    graph = collections.defaultdict(list)
    indeg = collections.defaultdict(int)

    for n3 in equations:
        n1, _, n2 = equations[n3]
        graph[n1].append(n3)
        graph[n2].append(n3)
        indeg[n3] += 2

    topo_order = get_topo_order()

    for n3 in topo_order:
        if n3 in equations:
            n1, func, n2 = equations[n3]
            wire_values[n3] = calc(wire_values[n1], wire_values[n2], func)

    res = []

    for i in sorted(wire_values):
        if i[0] == 'z':
            res.append(str(wire_values[i]))

    return int(''.join(res[ : : -1]), 2)


inputs = read_input()

_start_time = time.perf_counter()
res = solve(inputs)
_end_time = time.perf_counter()

print(res)
print('finished in', _end_time - _start_time, 'seconds')