class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        answer = []
        for i in range(len(temp)-1, -1, -1):
            while stack:
                if temp[i] < temp[stack[-1]]:
                    answer.append(stack[-1]-i)
                    stack.append(i)
                    break
                else:
                    stack.pop()
            else:
                answer.append(0)
                stack.append(i)
        return answer[::-1]

        
