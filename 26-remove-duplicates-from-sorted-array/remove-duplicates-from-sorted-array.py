class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length-1):
            if nums[i] == nums[i+1]:
                nums[i] = 101
                length -= 1
        # push -101 to the end
        nums.sort()
        return length
        