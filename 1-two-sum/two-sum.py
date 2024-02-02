class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = dict()
        for i in range(len(nums)):
            value = target - nums[i]
            if value in hash_table and hash_table[value] != i:
                return [hash_table[value], i]
            else:
                hash_table[nums[i]] = i
        return []
        