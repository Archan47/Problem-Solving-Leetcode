class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        matched = []
        i = 0
        minLength = min(len(word) for word in strs)
        while i < minLength:
            mismatch = False
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    mismatch = True
                    break
            if mismatch:
                break
            matched.append(strs[0][i])
            i += 1
        return ''.join(matched)