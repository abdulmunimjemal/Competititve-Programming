class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        total = 0
        for g in gain:
            total += g
            highest = max(highest, total)
        return highest
