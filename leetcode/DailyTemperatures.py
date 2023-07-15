class Solution:
    def dailyTemperatures(self, temp):
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

        
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        answer = [0] * len(temp)
        stack = [] # [temp, index]
        
        for current_index, current_temp in enumerate(temp):
            while stack and current_temp > stack[-1][0]:
                last_temp, last_index = stack.pop()
                answer[last_index] = (current_index - last_index)
            stack.append([current_temp, current_index])
        return answer

        

