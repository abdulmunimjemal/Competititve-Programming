class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # for i < j, num[i] = num[j] -> good pair
        gp = 0
        for j in range(len(nums)):
            for i in range(j):
                if nums[i] == nums[j]:
                    gp += 1
        return gp