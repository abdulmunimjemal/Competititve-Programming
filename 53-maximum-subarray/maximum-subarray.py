class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        n = len(nums)
        i = 0
        while i < n:
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
            curr_sum = max(0, curr_sum)
            i += 1
        return max_sum