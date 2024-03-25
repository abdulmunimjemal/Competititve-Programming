class Solution:
    def isValid(self, s: str) -> bool:
        db = {
            ')':'(',
            '}':'{',
            ']': '['
        }
        stack = []
        for i in s:
            if i in db.values():
                stack.append(i)
            else:
                if not stack or stack.pop() != db[i]: return False
        return not stack
        