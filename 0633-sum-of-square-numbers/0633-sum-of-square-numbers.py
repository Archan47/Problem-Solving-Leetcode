class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = 0
        while (right + 1) * (right + 1) <= c:
            right += 1
        while left <= right:
            ans = left * left + right * right 
            if ans == c:
                return True
            elif ans < c:
                left += 1
            else:
                right -= 1
        return False
        