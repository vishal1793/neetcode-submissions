class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","").replace("!", "").replace(".", "").replace(",", "").replace("?", "").replace("'", "").replace(":", "").replace(";", "").lower()
        start = 0
        end = len(s) - 1

        while (start < end):
            if ord(s[start]) != ord(s[end]):
                return False
            
            start += 1
            end -= 1

        return True

            
        