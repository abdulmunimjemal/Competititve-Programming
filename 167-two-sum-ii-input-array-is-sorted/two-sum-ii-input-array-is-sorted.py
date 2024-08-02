class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1

        while i < j:
            curr_sum = nums[i] + nums[j]
            if curr_sum > target:
                j -= 1
            elif curr_sum < target :
                i += 1
            else:
                return [i+1, j+1]

            
        