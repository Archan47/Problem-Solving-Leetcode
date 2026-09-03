class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        chains = []
        for i in range(len(nums)):
            currentChain = [nums[i]]
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(chains[j]) + 1 > len(currentChain):
                        currentChain = chains[j] + [nums[i]]
            chains.append(currentChain)
        return max(chains, key=len)
