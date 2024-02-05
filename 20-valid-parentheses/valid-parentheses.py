class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        vocab = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            else:
                if not stack: return False
                if vocab[stack.pop()] != i: return False
        return not stack
        