class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        res = []
        freq = Counter(nums)
        for item, count in freq.items():
            if count != 1:
                continue
            res.append(item)
        return res
        