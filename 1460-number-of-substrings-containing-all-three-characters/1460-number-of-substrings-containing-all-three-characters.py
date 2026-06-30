class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        a = b = c = 0
        left = 0

        for right in range(n):
            if s[right] == 'a':
                a += 1
            elif s[right] == 'b':
                b += 1
            else:
                c += 1

            while a and b and c:
                count += (n - right)
                if s[left] == 'a':
                    a -= 1
                elif s[left] == 'b':
                    b -= 1
                else:
                    c -= 1
                left += 1

        return count