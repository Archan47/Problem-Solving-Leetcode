class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mx = max(nums)
        mn = min(nums)
        maxPos = 0
        minPos = 0
        for i in range(len(nums)):
            if nums[i] == mx:
                maxPos = i
            if nums[i] == mn:
                minPos = i 
        left = max(maxPos, minPos) + 1
        right = len(nums) - min(maxPos, minPos)
        bothsides = (min(maxPos, minPos) + 1) + (len(nums) - max(maxPos, minPos))

        return min(left, right, bothsides)     