# Mathematical Approach (Solved May 15, 2023)
class Solution:
    def reverse(self, x: int) -> int:
        positive = True
        if x < 0:
            positive = False
            x = x * -1
        reversed = int(str(x)[::-1]) if positive else -1*int(str(x)[::-1])
        if reversed > 2**31 - 1 or reversed < -2**31:
            return 0
        return reversed