class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        res = []
        freq = Counter(nums)
        for item , count in freq.items():
            count = min(count , k)
            for i in range(count):
                res.append(item)
        return res
        