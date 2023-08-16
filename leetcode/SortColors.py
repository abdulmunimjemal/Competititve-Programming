# Current Solution: Improved Algorithm: Beats 97.5% Python3 Submissions - Aug 16 2023
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red = nums.count(0)
        white = nums.count(1)
        blue = nums.count(2)
        count = [red, white, blue]

        index = 0
        for color in range(3):
            while count[color] > 0:
                nums[index] = color
                count[color] -= 1
                index += 1


# PREVIOUS SOLUTIONS

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