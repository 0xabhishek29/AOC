def solve():
    N = 1279         # number of lines of input
    inp = []
    tmp = []

    for _ in range(N):
        t = input().split()
        if not t:
            continue
        if t[0] == 'Button':
            tmp.append(int(t[2][2 : -1]))
            tmp.append(int(t[3][2 : ]))
        elif t[0] == 'Prize:':
            tmp.append(int(t[1][2 : -1]))
            tmp.append(int(t[2][2 : ]))
            inp.append(tmp)
            tmp = []

    
    def solve_linear_equations(ax, ay, bx, by, target_x, target_y):
        target_x += 10000000000000
        target_y += 10000000000000

        equation1 = [ax, bx, target_x]
        equation2 = [ay, by, target_y]

        equation1 = [i * ay for i in equation1]
        equation2 = [i * ax for i in equation2]

        t1 = equation1[1] - equation2[1]
        t2 = equation1[2] - equation2[2]
        
        nb = t2 / t1

        if nb - int(nb) != 0:
            return -1, -1

        na = (equation1[2] - equation1[1] * nb) / equation1[0]

        if na - int(na) != 0:
            return -1, -1
        
        return na, nb
    
    res = 0
    
    for idx in range(len(inp)):
        r1, r2 = solve_linear_equations(*inp[idx])
        if r1 != -1:
            res += 3*r1 + r2
    
    return res


print(solve())