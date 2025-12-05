import bisect


def read_input(filename="input.txt"):
    with open(filename, "r") as f:
        blocks = f.read().split('\n\n')
    
    ranges = []

    for i in blocks[0].splitlines():
        s, e = i.split('-')
        ranges.append((int(s), int(e)))
    
    ids = list(map(int, blocks[1].splitlines()))
        
    return ranges, ids
    
    
def solve(inputs):
    ranges, ids = inputs

    res = 0

    ranges.sort()
    ids.sort()

    s1 = e1 = 0

    for s2, e2 in ranges:
        s1 = max(s1, s2)
        e1 = max(e1, e2)

        res += bisect.bisect_right(ids, e1) - bisect.bisect_left(ids, s1)

        s1 = e1

    return res


inputs = read_input()
print(solve(inputs))