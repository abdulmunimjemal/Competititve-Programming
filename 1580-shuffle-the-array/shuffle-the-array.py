class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = [0]*(2*n)
        curr = 0
        for i in range(n):
            result[curr] = nums[i]
            curr+=1
            result[curr] = nums[i+n]
            curr+=1
        return result


        