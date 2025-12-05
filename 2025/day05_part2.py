import collections


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

    hm = collections.defaultdict(int)
    res = 0

    for s, e in ranges:
        hm[s] += 1
        hm[e + 1] -= 1

    prev = val = lastval = 0
    
    for cur in sorted(hm):
        val += hm[cur]

        if lastval != 0:
            res += cur - prev

        prev = cur
        lastval = val

    return res


inputs = read_input()
print(solve(inputs))