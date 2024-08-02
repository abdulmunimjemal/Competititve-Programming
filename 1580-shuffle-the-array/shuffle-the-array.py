class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first_half, last_half = nums[:n], nums[n:]
        result = [0] * 2 * n
        for i in range(n): # 2n and 2n+1
            result[2*i] = first_half[i]
            result[2*i + 1] = last_half[i]
        return result
        