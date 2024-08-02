class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            num = nums[i] 
            if num in hashmap:
                return [i, hashmap[num]]
            hashmap[target - num] = i