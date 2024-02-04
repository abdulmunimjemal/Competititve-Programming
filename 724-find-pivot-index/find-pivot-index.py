class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum, n = sum(nums), len(nums)
        prefix_sum = [0] * n
        total = 0
        for i in range(n):
            total += nums[i]
            prefix_sum[i] = total
        for i in range(n):
            left_sum = prefix_sum[i-1] if i != 0 else 0
            right_sum = total_sum - prefix_sum[i] 
            if left_sum == right_sum:
                return i
        return -1
        