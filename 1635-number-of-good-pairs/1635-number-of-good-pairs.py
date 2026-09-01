class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = Counter(nums)
        count = 0
        for num in freq:
            n = freq[num]
            count += (n * (n-1)) // 2
        return count
        