class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(lambda : 0)
        n = len(nums) / 2
        for num in nums:
            hashmap[num] += 1
            if hashmap[num] >= n: return num