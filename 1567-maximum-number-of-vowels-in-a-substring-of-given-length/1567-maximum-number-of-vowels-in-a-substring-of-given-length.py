class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        n = len(s)
        currentWindow = s[:k]
        vowels = "aeiou"
        for ch in currentWindow:
            if ch in vowels:
                count += 1
        maxVowels = count
        for ch in range(k,n):
            currentWindow = currentWindow[1:] + s[ch]
            if s[ch -k] in vowels:
                count -= 1
            if s[ch] in vowels:
                count += 1
            if count > maxVowels:
                maxVowels = count
        return maxVowels
        