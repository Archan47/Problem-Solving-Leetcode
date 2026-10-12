class Solution:
    def reverse(self, x: int) -> int:
        # Its reverse overflows; abs(x) also exceeds the 32-bit limit.
        if x == -2**31:
            return 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        rem = 0
        while x > 0:
            digit = x % 10
            if rem > 214748364 or (rem == 214748364 and digit > 7):
                return 0
            rem = rem * 10 + digit
            x = x // 10
        return sign * rem
        