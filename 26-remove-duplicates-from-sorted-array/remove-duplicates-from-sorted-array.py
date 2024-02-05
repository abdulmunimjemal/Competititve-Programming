class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # two pointers
        i, j = 0, 1
        
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i+1] = nums[j]
                i+=1
                j+=1
        return i + 1
        