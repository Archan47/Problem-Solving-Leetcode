class Solution:
    def reverseVowels(self, s: str) -> str:
        stringList = list(s)
        l = []
        vowels = "aeiou"
        for v in range(len(stringList)):
            if stringList[v].lower() in vowels:
                l.append(stringList[v])
        for ch in range(len((stringList))):
            if stringList[ch].lower() in vowels:
                stringList[ch] = l[-1]
                l.pop()
        return ''.join(stringList)
        