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
    
    upper_left_quadrant = upper_right_quadrant = lower_left_quadrant = lower_right_quadrant = 0

    for px, py, vx, vy in positions_and_velocities:
        final_x, final_y = move(px, py, vx, vy, 100)
        if final_y < n // 2:
            if final_x < m // 2:
                upper_left_quadrant += 1
            elif final_x > m // 2:
                upper_right_quadrant += 1
        elif final_y > n // 2:
            if final_x < m // 2:
                lower_left_quadrant += 1
            elif final_x > m // 2:
                lower_right_quadrant += 1
        
    return upper_left_quadrant * upper_right_quadrant * lower_left_quadrant * lower_right_quadrant


print(solve())