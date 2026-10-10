class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        seen = {0: 1}
        currentSum = 0
        count = 0
        for i in range(len(nums)):
            currentSum += nums[i]
            diff = currentSum - k
            if diff in seen:
                count += seen[diff]
            seen[currentSum] = seen.get(currentSum, 0) + 1

        return count
        