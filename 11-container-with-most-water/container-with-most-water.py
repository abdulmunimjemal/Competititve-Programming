class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = float("-inf")

        while i < j:
            w = j - i
            h = min(height[i], height[j])
            max_area = max(max_area, w * h)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max_area
        