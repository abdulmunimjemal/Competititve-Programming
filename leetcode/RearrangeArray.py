class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        index = range(1, len(nums), 2)
        nums.sort()
        for i in index:
            nums[i], nums[i-1] = nums[i-1], nums[i]
        return nums