class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0
        while i < j:
            h = min(height[j], height[i])
            w = j - i
            area = h * w
            max_area = max(max_area, abs(area))
            if height[j] < height[i]:
                j -= 1
            else:
                i += 1
        return max_area