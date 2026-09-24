class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        ans = [pref[0]]
        for i in range(len(pref)-1):
            ans.append(pref[i] ^ pref[i+1])
        return ans