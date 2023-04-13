class Solution:
    def sortColors(self, nums: List[int]) -> None:
        total = [0] * 3
        for num in nums:
            total[num] += 1
        result = [0] * total[0] + [1] * total[1] + [2] * total[2]
        for i in range(len(nums)):
            nums[i] = result[i] 
        
        return


"""
# This solution worked well. O(n) time complexity. 
def sortColors(nums):
    total = [0] * 3
    for num in nums:
        total[num] += 1
    nums = [0] * total[0] + [1] * total[1] + [2] * total[2]
"""