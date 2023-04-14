from collections import Counter
# As the saying goes, DON'T REINVENT THE WHEEL
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums).most_common(k)
        r = []
        for x in c:
            r.append(x[0])
        return r

