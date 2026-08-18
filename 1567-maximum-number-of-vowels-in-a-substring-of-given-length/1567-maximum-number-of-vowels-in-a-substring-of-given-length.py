class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        n = len(s)
        current_window = s[:k]
        vowels = "aeiou"
        for ch in current_window:
            if ch in vowels:
                count += 1
        maxCount = count
        for ch in range(k,n):
            current_window = current_window[1:] + s[ch]
            if s[ch-k] in vowels:
                count -= 1
            if s[ch] in vowels:
                count += 1
            if count > maxCount:
                maxCount = count
        return maxCount
        