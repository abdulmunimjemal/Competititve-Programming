class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # using prefix sum
        n = len(nums)
        left_product = [1]*n
        right_product = [1]*n

        # let us calculate the left product
        for i in range(1, n):
            left_product[i] = left_product[i-1] * nums[i-1]
        
        for j in range(n-2,-1,-1):
            right_product[j] = right_product[j+1] * nums[j+1]
        return [left_product[i] * right_product[i] for i in range(n)]
