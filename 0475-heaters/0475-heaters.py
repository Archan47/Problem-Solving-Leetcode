class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        dist = []
        for house in houses:
            idx = bisect_left(heaters, house)
            leftSide = float('inf')
            rightSide = float('inf')
            if idx > 0:
                leftSide = house - heaters[idx-1]
            if idx < len(heaters):
                rightSide = heaters[idx] - house
            nearest = min(leftSide, rightSide)
            
            dist.append(nearest)
        return max(dist)

        