import collections


def solve():
    N = 140         # number of lines of input
    garden = []

    for _ in range(N):
        garden.append(input())


    def inside(x, y):
        return 0 <= x < n and 0 <= y < m

    def bfs(x, y):
        char = garden[x][y]
        q = collections.deque( [(x, y)] )
        corners = area = 0

        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                area += 1

                for d in range(4):
                    dx, dy = directions[d]
                    dx2, dy2 = directions[(d + 1) % 4]

                    nx, ny = x + dx, y + dy
                    ok1 = inside(nx, ny) and garden[nx][ny] == char

                    if ok1:
                        if seen[nx][ny] == 0:
                            q.append( (nx, ny) )
                            seen[nx][ny] = 1

                    # check if (x, y) is a corner
                    nx2, ny2 = x + dx2, y + dy2
                    ok2 = inside(nx2, ny2) and garden[nx2][ny2] == char

                    if not ok1 and not ok2:
                        corners += 1
                    if ok1 and ok2:
                        if garden[x][y] == garden[nx][ny] == garden[nx2][ny2]:
                            nx3, ny3 = x + dx + dx2, y + dy + dy2       # diagonal
                            if garden[nx3][ny3] != garden[x][y]:
                                corners += 1

        return corners, area
    
    res = 0
    n, m = len(garden), len(garden[0])
    seen = [[0] * m for _ in range(n)]
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i in range(n):
        for j in range(m):
            if seen[i][j] == 0:
                seen[i][j] = 1
                c, a = bfs(i, j)
                res += c * a
    
    return res


print(solve())