import functools


def read_input(filename="input.txt"):
    joltage_ratings = []

    with open(filename, "r") as f:
        for i in f.read().split('\n'):
            joltage_ratings.append(list(map(int, i)))
        
    return joltage_ratings
    
    
def solve(inputs):
    joltage_ratings = inputs

    res = 0
    inf = float('inf')
    pow10 = [1] * 12

    for i in range(1, 12):
        pow10[i] = pow10[i - 1] * 10

    for joltage_rating in joltage_ratings:
        n = len(joltage_rating)
        
        @functools.cache
        def dp(i, rem):
            if rem == 0:
                return 0
            if i >= n:
                return -inf
            
            r1 = dp(i + 1, rem)
            r2 = joltage_rating[i] * pow10[rem - 1] + dp(i + 1, rem - 1)
            return max(r1, r2)
        
        res += dp(0, 12)
    
    return res


inputs = read_input()
print(solve(inputs))