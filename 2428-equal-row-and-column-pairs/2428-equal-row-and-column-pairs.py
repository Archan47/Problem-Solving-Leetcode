class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowCount = Counter(tuple(row) for row in grid)
        count = 0
        for i in range(len(grid)):
            column = tuple(row[i] for row in grid)
            count += rowCount[column]
        return count
        