class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                start = stack[-1]
                s = s[:start] + s[start:i+1][::-1] + s[i+1:]
                stack.pop()
        return s.replace('(', '').replace(')', '')