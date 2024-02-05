class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # two pointers
        array_1 = nums[:n]
        array_2 = nums[n:]

        result = []
        for i in range(len(array_1)):
            result.append(array_1[i])
            result.append(array_2[i])
        return result


        