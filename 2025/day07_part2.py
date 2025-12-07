def read_input(filename="input.txt"):
    manifold = []

    with open(filename, "r") as f:
        for idx, i in enumerate(f.read().split('\n')):
            if idx % 2 == 0:
                manifold.append(i)
            idx += 1
    
    return manifold

    
def solve(inputs):
    manifold = inputs

    m, n = len(manifold), len(manifold[0])
    s = manifold[0].index('S')
    hm = set( [s] )
    cnt = [[0] * n for i in range(m)]
    cnt[0][s] = 1
    
    for i in range(1, m):
        nhm = set()

        for j in hm:
            val = cnt[i - 1][j]

            if manifold[i][j] == '^':
                nhm.add(j - 1)
                cnt[i][j - 1] += val
                nhm.add(j + 1)
                cnt[i][j + 1] += val
            else:
                nhm.add(j)
                cnt[i][j] += val
        
        hm = nhm

    return sum(cnt[-1])


inputs = read_input()
print(solve(inputs))