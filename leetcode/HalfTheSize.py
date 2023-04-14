from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq_map = Counter(arr).most_common(len(arr))
        half = len(arr) // 2
        output = 0
        tracker = 0
        for x in freq_map:
            freq = x[1]
            output += 1
            tracker = tracker + freq
            if tracker >= half:
                break
        return output