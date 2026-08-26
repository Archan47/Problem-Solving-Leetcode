class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0
        ans = []
        for ch in s:
            if ch == ')':
                count -= 1
            if count != 0:
                ans.append(ch)
            if ch == '(':
                count += 1
        return ''.join(ans)

         