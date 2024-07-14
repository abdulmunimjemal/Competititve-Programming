class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1, l2 = nums[:n], nums[n:]
        result = [0] * (2 * n)
        for i in range(n):
            result[2*i] = l1[i]
            result[2*i + 1] = l2[i]
        return result
