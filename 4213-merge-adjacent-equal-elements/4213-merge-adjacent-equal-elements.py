class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
       
        i = 0
        while i < len(nums)-1:
            j = i + 1
            if nums[i] == nums[j]:
                nums[i] = nums[i] + nums[j]
                nums.pop(j)
                i = max(0, i - 1)
            else:
                i+=1
        return nums
            
            

        