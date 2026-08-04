class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memory = {}
        def maxDiff(left,right):
            if left == right:
                return nums[left]
            if (left,right) in memory:
                return memory[(left, right)] 
            
            chooseLeft = nums[left] - maxDiff(left + 1, right)
            chooseRight = nums[right] - maxDiff(left, right - 1)

            memory[(left, right)] = max(chooseLeft, chooseRight)
            return memory[(left, right)]
        return maxDiff(0, len(nums) - 1) >= 0