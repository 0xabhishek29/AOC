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
        l = len(s) // 2
        v1, v2 = int(s), int(e)
            
        t = int(s[ : l]) if l != 0 else 0
        num = int(str(t) * 2)

        while num <= v2:
            if v1 <= num <= v2:
                res += num
            t += 1
            num = int(str(t) * 2)
    
    return res

inputs = read_input()
print(solve(inputs))