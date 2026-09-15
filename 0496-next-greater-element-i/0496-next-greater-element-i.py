class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            i = nums2.index(num)
            j = i + 1
            while j < len(nums2):
                if nums2[j] > num:
                    ans.append(nums2[j])
                    break
                j += 1
            if j == len(nums2):
                ans.append(-1)
        return ans