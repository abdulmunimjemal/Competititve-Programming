class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums.sort(key=functools.cmp_to_key(self.compare))
        return str(int("".join(nums)))
    def compare(self, num, num2):
        sum_1 = int(num + num2)
        sum2 = int(num2 + num)
        return sum2 - sum_1 