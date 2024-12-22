import collections


def read_input():
    N = 2474
    nums = []

    for _ in range(N):
        nums.append(int(input()))
    
    return nums


def solve(inputs):

    def next_secret_number(secret_number):
        new_secret_number = ((secret_number * 64) ^ secret_number) % mod
        new_secret_number = ((new_secret_number // 32) ^ new_secret_number) % mod
        new_secret_number = ((new_secret_number * 2048) ^ new_secret_number) % mod
        return new_secret_number

    nums = inputs
    mod = 16777216
    seen = collections.defaultdict(int)
    
    initial = 0
    prices = [nums[initial] % 10]
    diffs = [0]
    iterations = 2000

    for i in range(iterations):
        nums[initial] = next_secret_number(nums[initial])
        prices.append(nums[initial] % 10)
        diffs.append(prices[-1] - prices[-2])

        if i >= 3:
            prices.pop(0)
            diffs.pop(0)
            diffs_tuple = tuple(diffs)
            if diffs_tuple not in seen:
                seen[diffs_tuple] = prices[-1]
    
    for idx in range(len(nums)):
        if idx == initial:
            continue

        local_seen = set()
        prices = [nums[idx] % 10]
        diffs = [0]

        for i in range(iterations):
            nums[idx] = next_secret_number(nums[idx])
            prices.append(nums[idx] % 10)
            diffs.append(prices[-1] - prices[-2])

            if i >= 3:
                prices.pop(0)
                diffs.pop(0)
                diffs_tuple = tuple(diffs)
                if diffs_tuple not in local_seen:
                    local_seen.add(diffs_tuple)
                    seen[diffs_tuple] += prices[-1]
    
    return max(seen.values())


inputs = read_input()
print(solve(inputs))