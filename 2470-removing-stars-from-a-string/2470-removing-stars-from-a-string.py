class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in range(len(s)):
            if len(stack) == 0:
                stack.append(s[ch])
                continue
            elif s[ch] == "*":
                stack.pop()
            else:
                stack.append(s[ch])
        return ''.join(stack)

        