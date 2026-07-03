class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if len(stack) == 0:
                stack.append(ch)
                continue
            if stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
        