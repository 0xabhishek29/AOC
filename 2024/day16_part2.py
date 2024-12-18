import collections
import heapq


def solve():
    N = 141         # number of lines of input
    grid = []

    for _ in range(N):
        grid.append(input())

    
    n, m = len(grid), len(grid[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    INF = pow(10, 20)
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                cur_x, cur_y = i, j
            if grid[i][j] == 'E':
                target_x, target_y = i, j
    
    def minimum_score(cur_x, cur_y):
        seen = set()
        done = set()

        def traverse_back(x, y, d):
            if (x, y, d) in done:
                return
            done.add((x, y, d))
            seen.add((x, y))
            for nx, ny, nd in prev[x, y, d]:
                traverse_back(nx, ny, nd)

        dist = collections.defaultdict(lambda: INF)
        dist[cur_x, cur_y, 1] = 0
        prev = collections.defaultdict(list)
        hp = [(0, cur_x, cur_y, 1)]

        while hp:
            w, x, y, d = heapq.heappop(hp)

            if w != dist[x, y, d]:
                continue

            if x == target_x and y == target_y:
                traverse_back(x, y, d)

            for nd in d - 1, d + 1, d:
                nd_mod = nd % 4
                dx, dy = directions[nd_mod]
                nx, ny = x + dx, y + dy

                if grid[nx][ny] != '#':
                    nw = abs(d - nd) * 1000 + 1
                    t = w + nw

                    if t == dist[nx, ny, nd_mod]:
                        prev[nx, ny, nd_mod].append((x, y, d))

                    if t < dist[nx, ny, nd_mod]:
                        prev[nx, ny, nd_mod] = [(x, y, d)]
                        dist[nx, ny, nd_mod] = t
                        heapq.heappush(hp, (t, nx, ny, nd_mod))

        return len(seen)
    
    return minimum_score(cur_x, cur_y)


print(solve())