class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        combined = sorted(nums1 + nums2)
        n = len(combined)
        mid = n // 2
        if n % 2 == 1:     
            return float(combined[mid])
        else:                   
            return (combined[mid - 1] + combined[mid]) / 2