import heapq


def read_input(filename="input.txt"):
    positions = []

    with open(filename, "r") as f:
        for i in f.read().split('\n'):
            positions.append(tuple(map(int, i.split(','))))
    
    return positions

    
def solve(inputs):
    positions = inputs

    def distance(position1, position2):
        x1, y1, z1 = position1
        x2, y2, z2 = position2
        return pow(x1 - x2, 2) + pow(y1 - y2, 2) + pow(z1 - z2, 2)
    
    hp = []
    n = len(positions)
    
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(positions[i], positions[j])
            heapq.heappush(hp, (d, i, j))
    
    par = list(range(n))
    rank = [1] * n
    comp = n

    def find(n1):
        n2 = n1
        while n1 != par[n1]:
            n1 = par[n1]
        while n2 != n1:
            p = par[n2]
            par[n2] = n1
            n2 = p
        return n1
    
    def union(n1, n2):
        nonlocal comp
        p1, p2 = find(n1), find(n2)
        if p1 == p2:
            return
        if rank[p1] < rank[p2]:
            p1, p2 = p2, p1
        par[p2] = p1
        rank[p1] += rank[p2]
        comp -= 1

    while hp:
        _, i, j = heapq.heappop(hp)
        union(i, j)
        if comp == 1:
            return positions[i][0] * positions[j][0]


inputs = read_input()
print(solve(inputs))