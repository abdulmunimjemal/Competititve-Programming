class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = set("/*-+")
        for token in tokens:
            if token in operations:
                num_2 = stack.pop()
                num_1 = stack.pop()
                value = int(eval(f"{num_1}{token}{num_2}"))
                stack.append(value)
            else:
                stack.append(int(token))
        return stack[-1]

        