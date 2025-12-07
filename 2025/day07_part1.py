def read_input(filename="input.txt"):
    with open(filename, "r") as f:
        manifold = f.read().split('\n')
    
    return manifold

    
def solve(inputs):
    manifold = inputs

    m = len(manifold)
    res = 0
    hm = set( [manifold[0].index('S')] )
    
    for i in range(1, m):
        nhm = set()

        for j in hm:
            if manifold[i][j] == '^':
                res += 1
                nhm.add(j - 1)
                nhm.add(j + 1)
            else:
                nhm.add(j)
        
        hm = nhm

    return res 


inputs = read_input()
print(solve(inputs))