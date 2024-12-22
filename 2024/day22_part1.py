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
    
    for i in range(len(nums)):
        for _ in range(2000):
            nums[i] = next_secret_number(nums[i])

    return sum(nums)


inputs = read_input()
print(solve(inputs))