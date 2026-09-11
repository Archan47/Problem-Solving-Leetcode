class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        res = set(())
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if (i == j or j == k or k == i):
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k] * 1
                    if ( num >= 100) and (num % 2 == 0):
                        res.add(num)
        return len(res)

