class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedList = sorted(score, reverse=True)
        hashSet = {}
        for num in range(len(sortedList)):
            hashSet[sortedList[num]] = num + 1
        ans = []
        for num in score:
            rank = hashSet[num]
            if rank == 1:
                ans.append("Gold Medal")
            elif rank == 2:
                ans.append("Silver Medal")
            elif rank == 3:
                ans.append("Bronze Medal")
            else:
                ans.append(str(rank))
        return ans

        