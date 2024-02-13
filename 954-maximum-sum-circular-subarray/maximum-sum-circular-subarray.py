class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        total_sum = sum(nums)
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            max_sum = max(curr_sum, max_sum)
            curr_sum = max(0, curr_sum)
        
        min_sum = nums[0]
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            min_sum = min(min_sum, curr_sum)
            curr_sum = min(0, curr_sum)

        max_circular = total_sum - min_sum

        return max(max_sum, max_circular) if max_circular != 0 else max_sum
