class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = '123456789'
        minLen = len(str(low))
        maxLen = len(str(high))
        res = []
        for length in range(minLen,maxLen+1):
            for start in range(len(digits) - length + 1):
                num = int(digits[start:start + length])
                if low <= num <= high:
                    res.append(num)
        return res