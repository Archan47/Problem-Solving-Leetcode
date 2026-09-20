class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        count = 0
        for i in range(len(intervals)-1):
            if intervals[i+1][0] < intervals[i][1]:
                count += 1
                intervals[i+1][1] = min(intervals[i+1][1], intervals[i][1])
        return count
        