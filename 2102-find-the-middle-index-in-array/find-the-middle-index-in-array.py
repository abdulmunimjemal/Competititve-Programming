class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * n
        total = 0
        for i in range(n):
            total += nums[i]
            prefix_sum[i] = total
        total = sum(nums)

        for i in range(n):
            left_sum = prefix_sum[i-1] if i != 0 else 0
            right_sum = total - left_sum - nums[i]
            if left_sum == right_sum: return i

        return -1
        