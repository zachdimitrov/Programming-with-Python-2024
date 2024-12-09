def calc_sum(nums, idx):
    if idx == len(nums) - 1:
        return nums[idx]
    return nums[idx] + calc_sum(nums, idx + 1)

n = [int(n) for n in input().split()]

print(calc_sum(n, 0))
