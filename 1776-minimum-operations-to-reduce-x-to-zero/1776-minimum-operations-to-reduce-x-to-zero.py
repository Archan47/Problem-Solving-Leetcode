class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        left = curr = 0
        longest = -1
        for right, num in enumerate(nums):
            curr += num
            while left <= right and curr > target:
                curr -= nums[left]
                left += 1
            if curr == target:
                longest = max(longest, right - left + 1)

        return -1 if longest == -1 else len(nums) - longest
