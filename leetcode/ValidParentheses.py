class Solution:
    def isValid(self, s: str) -> bool:
        valid = { '(': ')', '[': ']', '{': '}' }
        stack = []
        if len(s) % 2 != 0:
            return 
        
        for p in s:
            if p in valid.keys():
                stack.append(p)
            elif p in valid.values():
                if len(stack) == 0:
                    return False
                else:
                    if p != valid.get(stack.pop()):
                        return False
        return len(stack) == 0