class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [k for k, f in Counter(nums).most_common(k)]