class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        rev = []
        stringList = list(s)
        for i in range(0,len(stringList), 2*k):
            rev = stringList[i:i + k]
            rev.reverse()
            stringList[i:i + k] = rev
        return ''.join(stringList)
        