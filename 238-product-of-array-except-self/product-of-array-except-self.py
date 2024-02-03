class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        max_product = 1
        zero_indexes = []
        for i in range(len(nums)):
            num = nums[i]
            if num != 0: 
                max_product *= num
            else:
                zero_indexes.append(i)
        result = []
        for i in range(len(nums)):
            number = nums[i]
            if number != 0:
                if zero_indexes:
                    result.append(0)
                else:
                    result.append(max_product//number)
            else:
                if len(zero_indexes) > 1:
                    result.append(0)
                else:
                    result.append(max_product)
        return result
