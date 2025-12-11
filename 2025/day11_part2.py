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
    def dfs(cur, dac, fft):
        if cur == 'out' and dac and fft:
            return 1
        
        res = 0
        dac = 1 if cur == 'dac' else dac
        fft = 1 if cur == 'fft' else fft

        for kid in graph[cur]:
            res += dfs(kid, dac, fft)
        
        return res
    
    return dfs('svr', 0, 0)


inputs = read_input()
print(solve(inputs))