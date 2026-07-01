class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        currentSum = sum(nums[:k])
        maxSum = currentSum
        maxAvg = maxSum / k
        for i in range(k,n):
            currentSum = currentSum - nums[i-k] + nums[i]
            if currentSum > maxSum:
                maxSum = currentSum
                maxAvg = maxSum / k
        return maxAvg