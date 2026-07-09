class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        ans = float('inf')
        n = len(nums)
        for i in range(n):
            need = prefix[i] + target
            left = i + 1
            right = n
            while left <= right:
                mid = (left + right) // 2
                if prefix[mid] >= need:
                    ans = min(ans, mid - i)
                    right = mid - 1
                else:
                    left = mid + 1
        return 0 if ans == float('inf') else ans
        