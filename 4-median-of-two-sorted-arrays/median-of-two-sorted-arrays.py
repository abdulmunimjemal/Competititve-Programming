class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_arr = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sorted_arr.append(nums1[i])
                i += 1
            else:
                sorted_arr.append(nums2[j])
                j += 1
        
        while i < len(nums1):
            sorted_arr.append(nums1[i])
            i += 1
        
        while j < len(nums2):
            sorted_arr.append(nums2[j])
            j += 1
        
        return self.getMedian(sorted_arr)
    
    def getMedian(self, arr):
        n = len(arr)
        if n % 2 == 0:
            return (arr[n//2] + arr[n//2 - 1])/2
        return arr[n//2] 