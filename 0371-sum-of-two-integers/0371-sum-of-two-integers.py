class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while True:
            x = a & b
            y = a ^ b
            a = (x << 1) & mask
            b = y & mask
            if a == 0:
                break
        return b if b <= 0x7FFFFFFF else ~(b ^ mask)
        