from shapely import Polygon


def read_input(filename="input.txt"):
    positions = []

    with open(filename, "r") as f:
        for i in f.read().split('\n'):
            positions.append(tuple(map(int, i.split(','))))
    
    return positions


def solve(inputs):
    positions = inputs

    n = len(positions)
    res = 0
    poly = Polygon(positions)

    for i in range(n):
        x1, y1 = positions[i]
        for j in range(i + 1, n):
            x2, y2 = positions[j]
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

            if area <= res:
                continue

            mnx = min(x1, x2)
            mxx = max(x1, x2)
            mny = min(y1, y2)
            mxy = max(y1, y2)

            if poly.covers(Polygon([(mnx, mny), (mnx, mxy), (mxx, mxy), (mxx, mny)])):
                res = max(res, area)

    return res


inputs = read_input()
print(solve(inputs))