class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            num = nums[mid]
            if target > num:
                left = mid + 1
            elif target < num:
                right = mid - 1
            else:
                return mid
        return left

        