class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        freq = Counter(s)
        values = list(freq.values())
        if len(freq) == 1:
            return values[0]
        else:
            for i in range(len(values)-1):
                return abs(values[i] - values[i+1])

        