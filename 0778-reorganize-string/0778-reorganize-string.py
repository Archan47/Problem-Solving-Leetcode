class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        res = []
        while freq:
            found = False
            for ch, count in freq.most_common():
                if not res or res[-1] != ch:
                    res.append(ch)
                    freq[ch] -= 1
                    found = True
                    if freq[ch] == 0:
                        del freq[ch]
                    break
            if not found:
                return ""
        return ''.join(res)
