class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            "/": lambda x, y: int(x / y),
            "*": lambda x, y: x * y,
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y
        }

        for token in tokens:
            if token in operations:
                num_2 = stack.pop()
                num_1 = stack.pop()
                operation = operations[token]
                value = operation(num_1, num_2)
                stack.append(value)
            else:
                stack.append(int(token))
        return stack[-1]

        