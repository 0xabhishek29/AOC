import collections


def read_input(filename="input.txt"):
    grid = []

    with open(filename, "r") as f:
        for i in f.read().split('\n'):
            grid.append(list(i))
        
    return grid
    
    
def solve(inputs):
    grid = inputs

    m, n = len(grid), len(grid[0])
    seen = [[0] * n for _ in range(m)]
    q = collections.deque()
    res = 0

    for x in range(m):
        for y in range(n):
            if grid[x][y] == '@':
                nei = 0
                t = []

                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        nx, ny = x + dx, y + dy

                        if x == nx and y == ny:
                            continue
                            
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '@':
                            nei += 1
                            t.append((nx, ny))
            
                if nei < 4:
                    seen[x][y] = 1
                    res += 1
                    q += t
    
    while q:
        x, y = q.popleft()

        if seen[x][y] == 1:
            continue

        nei = 0
        t = []

        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy

                if x == nx and y == ny:
                    continue
                    
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '@' and seen[nx][ny] == 0:
                    nei += 1
                    t.append((nx, ny))
    
        if nei < 4:
            seen[x][y] = 1
            res += 1
            q += t
            
    return res


inputs = read_input()
print(solve(inputs))