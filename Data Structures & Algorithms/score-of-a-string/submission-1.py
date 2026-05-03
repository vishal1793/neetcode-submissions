class Solution:
    def scoreOfString(self, s: str) -> int:
        prev = ord(s[0])
        result = 0
        index = 1
        while index < len(s):
            if ord(s[index]) > prev:
                result += (ord(s[index]) - prev)
                prev = ord(s[index])
                index += 1
            else:
                result += (prev - ord(s[index]))
                prev = ord(s[index])
                index += 1

        return result
                