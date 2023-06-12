class Solution:
    def removeKdigits(self, numbers: str, max_len: int) -> str:
        stack = []

        for num in numbers:
            while stack and max_len > 0:
                if stack[-1] > num:
                    stack.pop()
                    max_len -= 1
                else:
                    break
            if stack or num is not '0':
                stack.append(num)
        if max_len:
            stack = stack[:-max_len]
        
        return ''.join(stack) or '0'