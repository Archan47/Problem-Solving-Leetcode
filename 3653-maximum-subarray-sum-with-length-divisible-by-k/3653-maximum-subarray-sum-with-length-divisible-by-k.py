class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        ans = float('-inf')
        minPrefix = [float('inf')] * k
        minPrefix[0] = 0
        for i in range(1, len(nums) + 1):
            prefixSum += nums[i - 1]
            remainder = i % k
            if minPrefix[remainder] != float('inf'):
                currentSum = prefixSum - minPrefix[remainder]
                ans = max(ans, currentSum)
            minPrefix[remainder] = min(minPrefix[remainder],prefixSum)
        return ans
        