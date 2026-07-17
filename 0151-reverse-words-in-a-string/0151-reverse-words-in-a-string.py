class Solution:
    def reverseWords(self, s: str) -> str:
        stringList = []
        stringList.extend(s.split())
        res = []
        i = 0
        while i != len(stringList):
            res.append(stringList[-1])
            stringList.pop()
        return ' '.join(res)