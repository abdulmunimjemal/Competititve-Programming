# O(n^2) solution

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for val in nums1:
            index = None
            for j in range(len(nums2)):
                if nums2[j] == val:
                    index = j
                    break
            for k in range(index, len(nums2)):
                if nums2[k] > val:
                    index = nums2[k]
                    break
                else:
                    index = -1
            result.append(index)
        return result

# O(n + m ) solution using monotonic stacks
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, index, res = [], {n:i for i, n in enumerate(nums1)}, [-1] * len(nums1)
        for num in nums2:
            while stack and num > stack[-1]:
                res[index[stack.pop()]] = num
            if num in nums1:
                stack.append(num)  
        return res