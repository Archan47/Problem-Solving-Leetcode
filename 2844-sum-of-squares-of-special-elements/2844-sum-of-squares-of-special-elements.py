class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        for num in range(len(nums)):
            if n % (num+1) == 0:
                total += nums[num] * nums[num]
        return total