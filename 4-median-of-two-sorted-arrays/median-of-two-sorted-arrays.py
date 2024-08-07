class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        i, j = 0, 0
        m1, m2 = 0, 0
        for c in range(0, (n + m) // 2 + 1):
            m2 = m1
            if i < n and j < m:
                if nums1[i] > nums2[j]:
                    m1 = nums2[j]
                    j += 1
                else:
                    m1 = nums1[i]
                    i += 1
            elif i < n:
                m1 = nums1[i]
                i += 1
            elif j < m:
                m1 = nums2[j]
                j += 1

        if (n + m) % 2 == 1:
            return m1
        return (m1 + m2) / 2
