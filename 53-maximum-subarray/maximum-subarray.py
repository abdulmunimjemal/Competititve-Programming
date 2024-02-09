class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]  # constraints: nums.length is at least 1
        curr_sum = 0 

        for num in nums:
            curr_sum += num
            max_sum = max(curr_sum, max_sum)
            curr_sum = max(0, curr_sum) 

        
        return max_sum