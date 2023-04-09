class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        index = len(nums)
        for i in range(index):
            min = nums[i]
            for j in range(i, index):
                if nums[j] < nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
        result = []
        i = 0
        for num in nums:
            if num == target:
                result.append(i)
            i += 1
        return result

# Most effecient space complexity, Drawbacks: slow (selection sort)!