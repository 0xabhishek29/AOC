def read_input(filename="input.txt"):
    rotations = []

    with open(filename, "r") as f:
        for t in f:
            rotations.append((t[0], int(t[1 : ])))
    
    return rotations

def solve(inputs):
    rotations = inputs

    res = 0
    cur = 50

    for d, val in rotations:
        if d == 'L':
            cur = (cur - val) % 100
        else:
            cur = (cur + val) % 100
        
        if cur == 0:
            res += 1
    
    return res


inputs = read_input()
print(solve(inputs))