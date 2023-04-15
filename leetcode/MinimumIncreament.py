class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        steps = 0
        nums.sort()
        for i in range(1, len(nums)):  # consider the first item to be unique
            if nums[i] <= nums[i - 1]:  
                diff = +1 + (nums[i-1] - nums[i])
                steps += diff
                nums[i] = nums[i-1] + 1
        return steps