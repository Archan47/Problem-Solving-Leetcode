class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        else:
            ans = word
            for i in range(len(word)):
                if word[i] == ch:
                    ans = word[:i+1][::-1] + word[i+1:]
                    break
            return ans 

        