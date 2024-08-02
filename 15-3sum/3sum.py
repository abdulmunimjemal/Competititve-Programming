class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        answers = []
        for k in range(N-2):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i, j = k + 1, N-1
            while i < j:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum > 0:
                    j -= 1
                elif curr_sum < 0:
                    i += 1
                else:
                    answers.append((nums[i],nums[j],nums[k]))
                    while i < j and nums[i] == nums[i+1]:
                        i += 1
                    while i < j and nums[j] == nums[j-1]:
                        j -= 1
                    i += 1
                    j -= 1
        return answers


        