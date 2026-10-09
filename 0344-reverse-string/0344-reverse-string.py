class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        res = s.copy()
        i = len(res) - 1
        j = 0
        while i >= 0:
            s[j] = res[i]
            i -= 1
            j += 1
        return s
        