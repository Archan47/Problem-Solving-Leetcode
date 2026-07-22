class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        count = 1
        for i in range(len(chars)):
            if i < len(chars) - 1 and chars[i] == chars[i+1]:
                count += 1
            else:
                chars[write] = chars[i]
                write += 1
                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1
                count = 1
        return write