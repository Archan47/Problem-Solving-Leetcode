class Solution:
    def sumAndMultiply(self, n: int) -> int:
        arr = []
        total = 0
        item = ''
        for digit in str(n):

            if int(digit) == 0:
                continue
            else:
                total += int(digit)
                item += str(digit)
        if item == "":    
            return 0
        final = int(item) * total
        return final

        