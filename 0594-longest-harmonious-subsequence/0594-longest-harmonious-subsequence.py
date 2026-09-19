class Solution:
    def findLHS(self, nums: list[int]) -> int:
        ans = 0
        count = Counter(nums)
        for item, freq in count.items():
            if item + 1 in count:
                ans = max(ans , freq + count[item + 1])
        return ans