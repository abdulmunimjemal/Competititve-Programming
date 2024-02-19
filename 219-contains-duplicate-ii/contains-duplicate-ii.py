class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in hash_map and abs(i - hash_map[num]) <= k: return True
            hash_map[num] = i
        return False