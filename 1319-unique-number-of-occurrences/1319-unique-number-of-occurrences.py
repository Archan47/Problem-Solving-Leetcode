from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        if len(freq.values()) == len(set(freq.values())):
            return True
        else:
            return False
    


        