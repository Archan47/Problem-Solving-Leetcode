class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(string):
            stack = []
            for ch in range(len(string)):
                if string[ch] == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(string[ch])
            return stack
        
        return process(s) == process(t)
        