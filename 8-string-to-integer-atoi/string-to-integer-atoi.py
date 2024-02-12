class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip() 
        if not s:
            return 0
        sign = 1
        i = 0
        if s[0] == '-': # negative sign
            sign = -1
            i = 1
        elif s[0] == '+':
            i = 1
        result = 0
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        return max(-2**31, min(sign * result, 2**31 - 1))
