class Solution:
    def secondHighest(self, s: str) -> int:
        first_max = -1
        second_max = -1
        for ch in range(len(s)):
            digit = 0
            if s[ch].isdigit():
                digit = int(s[ch])
                if digit > first_max:
                    second_max = first_max
                    first_max = digit
                elif first_max > digit > second_max:
                    second_max = digit
        return second_max 

               
        


        