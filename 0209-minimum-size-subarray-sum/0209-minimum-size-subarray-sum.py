class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currentSum = 0
        minWindow = float('inf')
        low = 0
        high = 0
        while high < len(nums):
            currentSum += nums[high]
            high += 1
            while currentSum >= target:
                currentWindowSize = high - low
                minWindow = min(minWindow,currentWindowSize)
                currentSum -= nums[low]
                low += 1
        return 0 if minWindow == float('inf') else minWindow

        # prefix = [0]
        # for num in nums:
        #     prefix.append(prefix[-1] + num)
        # ans = float('inf')
        # n = len(nums)
        # for i in range(n):
        #     need = prefix[i] + target
        #     left = i + 1
        #     right = n
        #     while left <= right:
        #         mid = (left + right) // 2
        #         if prefix[mid] >= need:
        #             ans = min(ans,mid - i)
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        # return 0 if ans == float('inf') else ans       