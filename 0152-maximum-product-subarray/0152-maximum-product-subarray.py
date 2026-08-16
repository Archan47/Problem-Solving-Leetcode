class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1
        suffix = 1
        n = len(nums)
        res = float('-inf')
        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            prefix *= nums[i]
            suffix *= nums[n - i - 1]
            res = max(res,prefix, suffix)
        return res
        