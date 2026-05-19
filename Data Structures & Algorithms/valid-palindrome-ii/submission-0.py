class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        while (start <= end and s[start] == s[end]):
            start += 1
            end -= 1
        
        a = start + 1
        b = end
        while (a <= b and s[a] == s[b]):
            a += 1
            b -= 1
        
        x = start
        y = end - 1
        while (x <= y and s[x]==s[y]):
            x += 1
            y -= 1
        

        return (b < a) or (y < x)