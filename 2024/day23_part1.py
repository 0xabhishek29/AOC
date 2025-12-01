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
    N = 3380
    edges = []

    for _ in range(N):
        edges.append(input().split('-'))
    
    return edges


def solve(inputs):
    edges = inputs

    graph = collections.defaultdict(set)

    for i, j in edges:
        graph[i].add(j)
        graph[j].add(i)

    res = set()
    
    for first_node in graph:
        if 't' != first_node[0]:
            continue
        for second_node in graph[first_node]:
            for third_node in graph:
                if third_node != first_node and third_node != second_node:
                    if third_node in graph[first_node] and third_node in graph[second_node]:
                        res.add(tuple(sorted([first_node, second_node, third_node])))
    
    return len(res)


inputs = read_input()

_start_time = time.perf_counter()
res = solve(inputs)
_end_time = time.perf_counter()

print(res)
print('finished in', _end_time - _start_time, 'seconds')