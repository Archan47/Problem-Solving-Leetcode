class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        original = arr[:]
        arr.sort()
        rank = 1
        res = []
        items = {}
        for num in arr:
            if num not in items:
                items[num] = rank
                rank += 1
        for num in original:
            res.append(items[num])
        return res
        