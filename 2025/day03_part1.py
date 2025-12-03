import itertools


def read_input(filename="input.txt"):
    joltage_ratings = []

    with open(filename, "r") as f:
        for i in f.read().split('\n'):
            joltage_ratings.append(list(map(int, i)))
        
    return joltage_ratings
    
    
def solve(inputs):
    joltage_ratings = inputs

    res = 0

    for joltage_rating in joltage_ratings:
        mxs = list(itertools.accumulate(joltage_rating[ : : -1], max))[ : : -1]
        t = 0
        
        for i in range(len(joltage_rating) - 1):
            t = max(t, joltage_rating[i] * 10 + mxs[i + 1])
        
        res += t
    
    return res


inputs = read_input()
print(solve(inputs))