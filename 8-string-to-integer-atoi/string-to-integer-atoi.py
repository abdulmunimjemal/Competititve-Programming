class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Remove leading and trailing whitespace
        s = s.strip()
        if not s:
            return 0
        
        # Handle sign
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]  # Skip the sign character
        elif s[0] == '+':
            s = s[1:]  # Skip the sign character
        
        # Convert characters to integer
        result = 0
        for char in s:
            if not char.isdigit():
                break  # Stop at the first non-digit character
            result = result * 10 + int(char)
        
        # Apply sign and check integer limits
        result *= sign
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result