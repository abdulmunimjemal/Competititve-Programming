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
                stack.append(vocab[i])
            else:
                if not stack or stack.pop() != i: return False
        return not stack
        