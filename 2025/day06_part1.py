def read_input(filename="input.txt"):
    worksheet = []

    with open(filename, "r") as f:
        for i in f.read().split('\n'):
            t = i.split()
            worksheet.append(list(map(int, t)) if t[0].isdecimal() else t)
    
    return worksheet
    
    
def solve(inputs):
    worksheet = inputs

    res = 0

    for problem in zip(*worksheet):
        op = problem[-1]

        if op == '+':
            res += sum(problem[ : -1])
        else:
            t = 1

            for i in problem[ : -1]:
                t *= i
            
            res += t
    
    return res


inputs = read_input()
print(solve(inputs))