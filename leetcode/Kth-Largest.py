class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(num) for num in nums]
        nums.sort()
        nums = nums[::-1]
        index = k - 1
        return str(nums[index])