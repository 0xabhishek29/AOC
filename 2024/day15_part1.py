def solve():
    N = 71         # number of lines of input
    grid = []
    movements = []

    for _ in range(N):
        t = input()
        if not t:
            continue
        if t[0] == '#':
            grid.append(list(t))
        else:
            movements.append(t)
    movements = ''.join(movements)

    
    def move(x, y, movement):
        dx, dy = directions[movement]
        nx, ny = x + dx, y + dy

        match grid[nx][ny]:
            case '#':
                return x, y
            case '.':
                return nx, ny
            case 'O':
                while grid[nx][ny] == 'O':
                    nx += dx
                    ny += dy
                
                match grid[nx][ny]:
                    case '#':
                        return x, y
                    case '.':
                        nx2, ny2 = x + dx, y + dy
                        grid[nx2][ny2] = '.'
                        nx2 += dx
                        ny2 += dy

                        while grid[nx2][ny2] != '.':
                            grid[nx2][ny2] = 'O'
                            nx2 += dx
                            ny2 += dy

                        grid[nx2][ny2] = 'O'
                        return x + dx, y + dy
    
    n, m = len(grid), len(grid[0])
    directions = {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1)
    }

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '@':
                grid[i][j] = '.'
                cur_x, cur_y = i, j
                break

    for movement in movements:
        cur_x, cur_y = move(cur_x, cur_y, movement)

    res = 0
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'O':
                res += 100*i + j

    return res


print(solve())