class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda i : i[0])
        output = [nums[0]]
        count = 0
        for start, end in nums[1: ]:
            last = output[-1][1]
            if start <= last:
                output[-1][1] = max(last, end)
            else:
                output.append([start, end])
        for start, end in output:
            count += end - start + 1
        return count 

        