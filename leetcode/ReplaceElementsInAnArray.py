class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        position = {nums[i]:i for i in range(len(nums))}
        for operation in operations:
            pos = position[operation[0]]
            nums[pos] = operation[1]
            position[operation[1]] = pos
        return nums
            
# Problem: Space Complexity should be improved