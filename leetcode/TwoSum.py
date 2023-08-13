class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {nums[i]:i for i in range(len(nums))}

        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hashmap and hashmap[compliment] != i:
                return [i, hashmap[compliment]]