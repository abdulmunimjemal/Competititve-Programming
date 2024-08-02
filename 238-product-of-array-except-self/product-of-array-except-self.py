class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        non_zero_product = 1
        number_of_zeros = 0
        zero_indexes = []
        for i in range(len(nums)):
            if nums[i] != 0:
                non_zero_product *= nums[i]
            else:
                number_of_zeros += 1
                zero_indexes.append(i)

        answer = [0] * len(nums)
        
        if number_of_zeros > 1:
            return answer
        if number_of_zeros == 1:
            answer[zero_indexes[0]] = non_zero_product
            return answer

        for i in range(len(nums)):
            answer[i] = non_zero_product // nums[i]
        return answer

        