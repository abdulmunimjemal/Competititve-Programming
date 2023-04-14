class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        nums = list(nums)
        result = []
        for i in range(len(l)):
            is_arith = True
            lower_limit = l[i]
            upper_limit = r[i]
            sub_array = sorted(nums[lower_limit:upper_limit + 1])
            if len(sub_array) == 1:
                result.append(True)
                continue
            else:
                difference = sub_array[1] - sub_array[0]
                for j in range(len(sub_array) - 1):
                    if sub_array[j+1] - sub_array[j] != difference:
                        is_arith = False
                        break
            result.append(is_arith)
        
        return result