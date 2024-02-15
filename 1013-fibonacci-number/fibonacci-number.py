class Solution:
    def fib(self, n: int) -> int:
        context = {0:0, 1:1}
        def find(n, context=context):
            if n in context:
                return context[n]
            return find(n-1, context) + find(n-2, context)
        return find(n)