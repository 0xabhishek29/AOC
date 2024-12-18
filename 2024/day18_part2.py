import collections


def solve():
    N = 3450         # number of lines of input
    points = []

    for _ in range(N):
        x, y = list(map(int, input().split(',')))
        points.append((x, y))


    def shortest_path_after_t_fallen_bytes(t):
        grid = [[0] * m for _ in range(n)]

        for i, j in points[ : t]:
            grid[j][i] = 1
        
        q = collections.deque( [(0, 0)] )
        d = -1

        while q:
            d += 1
            for _ in range(len(q)):
                x, y = q.popleft()

                if x == n - 1 and y == m - 1:
                    return d

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                        grid[nx][ny] = 2
                        q.append((nx, ny))
        
        return -1

    n = m = 71
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    l, r = 0, N

    while l < r:
        mid = (l + r) // 2

        if shortest_path_after_t_fallen_bytes(mid) == -1:
            r = mid
        else:
            l = mid + 1

    return points[l - 1]


print(solve())