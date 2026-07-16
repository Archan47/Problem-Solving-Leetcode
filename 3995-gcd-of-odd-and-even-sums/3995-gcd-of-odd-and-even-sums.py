class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even = 0
        odd =  0
        for i in range(1,n+1):
            num = 2 * i
            even += num
        for j in range(1,n+1):
            num = 2 * j - 1
            odd += num
        return math.gcd(even,odd)
        