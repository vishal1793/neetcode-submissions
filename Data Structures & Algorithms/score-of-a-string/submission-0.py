class Solution:
    def scoreOfString(self, s: str) -> int:
        prev = 0
        result = 0
        for index, char in enumerate(s):
            if ord(char) > prev and index != 0:
                result += (ord(char) - prev)
                prev = ord(char)
            elif prev > ord(char) and index != 0:
                result += (prev - ord(char))
                prev = ord(char)
            else:
                prev = ord(char)
        

        return result
                