class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in range(len(s)):
            if len(s) == 0:
                stack.append(s[ch])
                continue
            if s[ch] == "*":
                stack.pop()
            else:
                stack.append(s[ch])
        return ''.join(stack)
        
        