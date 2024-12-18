import heapq


def solve():
    N = 141         # number of lines of input
    grid = []

    for _ in range(N):
        grid.append(input())

    
    n, m = len(grid), len(grid[0])
    INF = pow(10, 20)
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                cur_x, cur_y = i, j
            if grid[i][j] == 'E':
                target_x, target_y = i, j
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dist = [[INF] * m for _ in range(n)]
    dist[cur_x][cur_y] = 0
    hp = [(0, cur_x, cur_y, 1)]

    while hp:
        w, x, y, d = heapq.heappop(hp)

        if w != dist[x][y]:
            continue

        for nd in d - 1, d + 1, d:
            nd_mod = nd % 4
            dx, dy = directions[nd_mod]
            nx, ny = x + dx, y + dy

            if grid[nx][ny] != '#':
                nw = abs(d - nd) * 1000 + 1
                if w + nw < dist[nx][ny]:
                    dist[nx][ny] = w + nw
                    heapq.heappush(hp, (dist[nx][ny], nx, ny, nd_mod))

    return dist[target_x][target_y]


print(solve())