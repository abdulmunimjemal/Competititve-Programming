class Solution:
    def hIndex(self, citations: List[int]) -> int:
        hindex = 0
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] > i:
                hindex += 1
            else:
                break
        return hindex