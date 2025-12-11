import collections
import functools


def read_input(filename="input.txt"):
    graph = collections.defaultdict(list)

    with open(filename, "r") as f:
        for device_output in f.read().split('\n'):
            s, edges = device_output.split(':')
            for neighbor in edges.split():
                graph[s].append(neighbor)
    
    return graph


def solve(inputs):
    graph = inputs
    
    @functools.cache
    def dfs(cur):
        if cur == 'out':
            return 1
        return sum(dfs(neighbor) for neighbor in graph[cur])
    
    return dfs('you')


inputs = read_input()
print(solve(inputs))