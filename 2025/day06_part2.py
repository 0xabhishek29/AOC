def read_input(filename="input.txt"):
    worksheet = []

    with open(filename, "r") as f:
        for i in f.read().split('\n'):
            worksheet.append(i)
    
    return worksheet[ : -1], worksheet[-1].split()

    
def solve(inputs):
    problems, operators = inputs

    res = j = 0
    op = operators[j]

    def reset_r(op):
        return 0 if op == '+' else 1
    
    r = reset_r(op)

    for i in zip(*problems):
        t = ''.join(i).strip()

        if not t:
            res += r
            j += 1
            op = operators[j]
            r = reset_r(op)
            continue

        num = int(t)

        if op == '+':
            r += num
        else:
            r *= num
   
    return res + r


inputs = read_input()
print(solve(inputs))