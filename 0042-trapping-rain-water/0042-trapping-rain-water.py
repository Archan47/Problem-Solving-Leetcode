class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        lMax, rMax = 0, 0
        ans = 0
        while l < r:
            lMax = max(lMax, height[l])
            rMax = max(rMax, height[r])
            if lMax < rMax:
                ans += lMax - height[l]
                l += 1
            else:
                ans += rMax - height[r]
                r -= 1
        return ans
        