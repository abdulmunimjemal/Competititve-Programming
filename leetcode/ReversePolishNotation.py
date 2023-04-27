class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ['+', '-', '*', '/']
        for token in tokens:
            if not token in operations:
                stack.append(int(token))
            else:
                i, j = stack.pop(), stack.pop()
                expression = f"{j}{token}{i}"
                stack.append(int(eval(f"({expression})")))
        return stack.pop()