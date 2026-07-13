class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            if nums[i] == target:
                res.append(i)
            i += 1
        return res
        