class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checker = set()
        left = 0
        maxCount = 0
        for right in range(len(s)):
            while s[right] in checker:
                checker.remove(s[left])
                left += 1
            checker.add(s[right])
            maxCount = max(maxCount , right - left + 1)
        return maxCount

 
        