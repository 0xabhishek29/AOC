import collections


def read_input(filename="input.txt"):
    lights = []
    buttons = []
    joltages = []

    with open(filename, "r") as f:
        for s in f.read().split('\n'):
            t1 = s.index(']')
            light = s[1 : t1]
            t2 = s.index('{')
            t3 = []

            for i in s[t1 + 2 : t2 - 1].split():
                button = list(map(int, i[1 : -1].split(',')))
                t3.append(button)

            joltage = list(map(int, s[t2 + 1 : -1].split(',')))

            lights.append(light)
            buttons.append(t3)
            joltages.append(joltage)
    
    return lights, buttons, joltages


def solve(inputs):
    lights, buttons, _ = inputs

    def bitmap(s):
        n = len(s)
        return sum(1 << (n - idx - 1) for idx, i in enumerate(s) if i == '#')

    def min_presses(light, button):
        n = len(light)
        target = bitmap(light)
        q = collections.deque( [target] )
        seen = set( [target] )
        res = -1

        while q:
            res += 1
            for _ in range(len(q)):
                cur = q.popleft()

                if cur == 0:
                    return res

                for b in button:
                    ncur = cur
                    for i in b:
                        ncur ^= 1 << (n - i - 1)
                    if ncur not in seen:
                        q.append(ncur)
                        seen.add(ncur)

    n = len(lights)
    return sum(min_presses(lights[i], buttons[i]) for i in range(n))


inputs = read_input()
print(solve(inputs))