def solve():
    N = 500         # number of lines of input
    positions_and_velocities = []
    n = m = 0

    for _ in range(N):
        t = input().split()
        px, py = list(map(int, t[0][2 : ].split(',')))
        vx, vy = list(map(int, t[1][2 : ].split(',')))
        n = max(n, py + 1)
        m = max(m, px + 1)
        positions_and_velocities.append([px, py, vx, vy])


    def move(ps_and_vs):
        for i in range(len(ps_and_vs)):
            px, py, vx, vy = ps_and_vs[i]
            ps_and_vs[i] = [(px + vx) % m, (py + vy) % n, vx, vy]
    
    def find_in_grid(ps_and_vs, to_find):
        grid = [['.'] * m for _ in range(n)]

        for px, py, _, _ in ps_and_vs:
            grid[py][px] = 'X'

        for i in range(n):
            grid[i] = ''.join(grid[i])
        
        return any(to_find in row for row in grid)

    for t in range(10000):
        move(positions_and_velocities)
        if find_in_grid(positions_and_velocities, 'XXXXXXXXX'):
            return t + 1

    return -1


print(solve())