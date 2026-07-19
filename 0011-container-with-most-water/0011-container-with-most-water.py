class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        maxWater = 0
        while left < right:
            width = right - left
            currentHeight = min(height[left], height[right])
            currentWater = width * currentHeight
            maxWater = max(currentWater, maxWater)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxWater