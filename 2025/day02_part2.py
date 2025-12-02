def read_input(filename="input.txt"):
    id_ranges = []

    with open(filename, "r") as f:
        t = f.readline().split(',')
        for i in t:
            s, e = i.split('-')
            id_ranges.append((s, e))
        
    return id_ranges
    
    
def solve(inputs):
    id_ranges = inputs

    res = 0

    for s, e in id_ranges:
        hm = set()
        v1, v2 = int(s), int(e)

        for mlt in range(2, 11):
            t = 1
            num = int(str(t) * mlt)

            while num <= v2:
                if v1 <= num <= v2:
                    hm.add(num)
                t += 1
                num = int(str(t) * mlt)
        
        res += sum(hm)
    
    return res

inputs = read_input()
print(solve(inputs))