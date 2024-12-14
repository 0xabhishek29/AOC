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


    def move(px, py, vx, vy, t):
        return (px + t*vx) % m, (py + t*vy) % n
    
    def find_in_grid_after_t(positions_and_velocities, to_find, t):
        grid = [['.'] * m for _ in range(n)]
        
        for px, py, vx, vy in positions_and_velocities:
            final_x, final_y = move(px, py, vx, vy, t)
            grid[final_y][final_x] = 'X'

        return any(to_find in ''.join(row) for row in grid)

    for t in range(n * m):
        if find_in_grid_after_t(positions_and_velocities, 'XXXXXXXXX', t + 1):
            return t + 1

    return -1


print(solve())