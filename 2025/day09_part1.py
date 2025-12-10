def read_input(filename="input.txt"):
    positions = []

    with open(filename, "r") as f:
        for i in f.read().split('\n'):
            positions.append(tuple(map(int, i.split(','))))
    
    return positions

    
def solve(inputs):
    positions = inputs

    n = len(positions)
    res = 0

    for i in range(n):
        x1, y1 = positions[i]
        for j in range(i + 1, n):
            x2, y2 = positions[j]
            res = max(res, (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))

    return res


inputs = read_input()
print(solve(inputs))