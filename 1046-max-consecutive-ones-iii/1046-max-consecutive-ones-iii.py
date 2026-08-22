class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0 
        zeroCount = 0
        maxLen = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zeroCount += 1
            while zeroCount > k:
                if nums[i] == 0:
                    zeroCount -= 1
                i += 1
            currLen = j - i + 1
            maxLen = max(maxLen, currLen)
        return maxLen
        

        


        