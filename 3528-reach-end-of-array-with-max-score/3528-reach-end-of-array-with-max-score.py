class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        maxScore = 0
        maxVal = nums[0]
        for i in range(len(nums)-1):
            maxVal = max(maxVal, nums[i])
            maxScore += maxVal
        return maxScore
        