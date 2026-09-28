class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        dictionary = {}
        for i in range(len(nums)):
            dictionary[i] = nums[i]
        chosen = sorted(dictionary, key=dictionary.get, reverse=True)[:k]
        chosen.sort()

        return [dictionary[i] for i in chosen]
        