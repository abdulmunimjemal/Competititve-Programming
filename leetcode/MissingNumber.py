# MATHEMATICAL APPROACH
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # using mathematics: their sum all of them would be n(n+1)/2
        total = (len(nums) * (len(nums)+1)) // 2
        for num in nums:
            total -= num
        return total
    
## BruteForce O(N^2) Approach
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numbers = list(range(len(nums)+1))
        for num in nums:
            numbers.remove(num)
        return numbers[0]