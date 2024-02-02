class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = Counter(nums)
        sorted_table = {k:v for k, v in sorted(freq_table.items(), key=lambda item: item[1])}
        return list(sorted_table.keys())[-k:]
        