# class Solution:
#     def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
#         stack = []
#         i = 0 # pop index

#         for x in pushed:
#             stack.append(x)
#             while stack and stack[-1] == popped[i]:
#                 i += 1
#                 stack.pop()
#         return len(stack) == 0

from collections import deque
pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
 
def check(pushed, popped):
    i = j = 0
    while pushed[i] != popped[j]:
        i += 1

print(check(pushed, popped))