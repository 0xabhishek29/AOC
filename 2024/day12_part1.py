import collections


def solve():
    N = 140         # number of lines of input
    garden = []

    for _ in range(N):
        garden.append(input())


    def bfs(x, y):
        char = garden[x][y]
        q = collections.deque( [(x, y)] )
        perimeter = area = 0

        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                area += 1

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < n and 0 <= ny < m and garden[nx][ny] == char:
                        if seen[nx][ny] == 0:
                            q.append( (nx, ny) )
                            seen[nx][ny] = 1
                    else:
                        perimeter += 1
        
        return perimeter, area
    
    res = 0
    n, m = len(garden), len(garden[0])
    seen = [[0] * m for _ in range(n)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for i in range(n):
        for j in range(m):
            if seen[i][j] == 0:
                seen[i][j] = 1
                p, a = bfs(i, j)
                res += p * a

    return res


print(solve())