class Solution:
    def processStr(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == "#":
                stack.extend(stack)
            elif ch == "%":
                stack.reverse()
            elif ch == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)