class Solution:
    def decodeString(self, s: str) -> str:
        intStack = []
        strStack = []
        number = 0
        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)
            elif ch == '[':
                intStack.append(number)
                number = 0
                strStack.append(ch)
            elif ch == ']':
                newString = ""
                while strStack[-1]  != '[':
                    newString = strStack.pop() + newString
                strStack.pop()
                digit = intStack.pop()
                strStack.append(digit * newString)
            else:
                strStack.append(ch)
        return ''.join(strStack)
