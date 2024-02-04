class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] * len(nums)
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            self.prefix_sum[i] += total

    def sumRange(self, left: int, right: int) -> int:
        left_sum = self.prefix_sum[left-1] if left != 0 else 0
        right_sum = self.prefix_sum[right]
        return right_sum-left_sum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)