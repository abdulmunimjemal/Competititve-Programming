class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = defaultdict(int)
        hash_map[0] = 1
        count = 0
        prefix_sum = 0

        for num in nums:
           prefix_sum += num
           target = prefix_sum - k

           if target in hash_map:
               count += hash_map[target]
           hash_map[prefix_sum] += 1
        return count
