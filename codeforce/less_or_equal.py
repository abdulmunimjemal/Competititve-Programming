def solve(n, k, nums):
    nums.sort() 

    if k == 0:
        if nums[0] == 1:
            return -1
        else:
            return nums[0] - 1
    else:
        if k == n:
            return nums[k - 1]
        else:
            if nums[k - 1] != nums[k]:
                return nums[k - 1]
            else:
                return -1

# Input
n, k = map(int, input().split())
nums = list(map(int, input().split()))

# Solve
result = solve(n, k, nums)
print(result)
