# Favoring Time Complexity
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ordered = sorted(nums)
        result = []
        for num in nums:
            result.append(ordered.index(num))
        return result

# Favoring Space Complexity: Beats 100% Python3 Submissions in Space Complexity

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * len(nums)
        index = len(nums)
        for i in range(index):
            counter = 0
            num = nums[i]
            for second_num in nums:
                if second_num < num:
                    counter += 1
            count[i] = counter
        return count
    
# Future: Middle Ground