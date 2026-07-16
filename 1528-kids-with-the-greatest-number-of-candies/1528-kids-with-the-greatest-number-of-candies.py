class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        res = []
        for c in range(len(candies)):
            if candies[c] + extraCandies >= maxCandy:
                res.append(True)
            else:
                res.append(False)
        return res
        