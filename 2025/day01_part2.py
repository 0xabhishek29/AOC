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
        v = val % 100

        if d == 'L':
            prev = cur
            cur -= v
            if prev != 0 and cur <= 0:
                res += 1
            cur %= 100
        else:
            prev = cur
            cur += v
            if prev != 0 and cur >= 100:
                res += 1
            cur %= 100
        
        if val >= 100:
            res += val // 100

    return res

inputs = read_input()
print(solve(inputs))