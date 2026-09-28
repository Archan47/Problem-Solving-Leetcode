class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort(reverse=True)
        count = 0
        element = 0
        for i in range(len(nums)):
            element = nums[i]
            count += 1
            if count == k:
                break
        return element


        