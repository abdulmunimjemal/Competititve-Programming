class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        step, n, total = 1, len(arr), 0
        prefix_sum = [0] * n
        for i in range(n):
            total += arr[i]
            prefix_sum[i] += total

        odd_sum = 0
        while step <= n:
            partial_sum = 0
            i = 0
            while i <= n-step:
                initial_sum = prefix_sum[i-1] if i > 0 else 0
                final_sum = prefix_sum[i+step-1]
                partial_sum += (final_sum - initial_sum)
                i += 1
            step += 2
            odd_sum += partial_sum
        return odd_sum