class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num_1, num_2 = 0, 0
        i, j = len(num1), len(num2)
        for n in num1:
            num_1 = num_1 + (10**(i-1))*int(n)
            i -= 1
        for n in num2:
            num_2 = num_2 + (10**(j-1))*int(n)
            j -= 1
        return str(num_1 * num_2)