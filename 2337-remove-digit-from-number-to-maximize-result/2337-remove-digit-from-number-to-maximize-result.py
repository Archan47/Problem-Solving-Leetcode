class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = 0
        for i in range(len(number)):
            if number[i] == digit:
                comp = number[ : i] + number[i+1: ]
                comp = int(comp)
                if comp > res:
                    res = comp
        return str(res)
                 
        