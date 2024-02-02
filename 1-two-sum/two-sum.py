class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {
            num: i for i, num in enumerate(nums)
        }
        for i in range(len(nums)):
            value = target - nums[i]
            if value in hash_table and hash_table[value] != i:
                return [hash_table[value], i]
        return []
        