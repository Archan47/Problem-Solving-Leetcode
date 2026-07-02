class Solution:
    def minLength(self, s: str) -> int:
        stk = []
        for ch in s:
            if len(stk) == 0:
                stk.append(ch)
                continue
            if stk[-1] + ch == 'AB':
                stk.pop()
            elif stk[-1] + ch == 'CD':
                stk.pop()
            else:
                stk.append(ch)
        return len(stk)
    



        