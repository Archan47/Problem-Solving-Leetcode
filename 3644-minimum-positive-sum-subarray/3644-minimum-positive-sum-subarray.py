class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        currentSum = 0
        minSum = float('inf')
        for size in range(l,r+1):
            for w in range(len(nums) - size + 1):
                currentWindow = nums[w:w+size]
                currentSum = sum(currentWindow)
                if currentSum <= 0:
                    continue
                minSum = min(currentSum, minSum)
        return -1 if minSum == float('inf') else minSum

        