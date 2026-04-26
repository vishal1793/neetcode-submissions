class Solution:
    def isValid(self, s: str) -> bool:
        valid_symbols = {")":"(", "]":"[", "}":"{"}
        stack = []
        for char in s:
            if char in valid_symbols:
                if not stack:
                    return False
                elif valid_symbols[char] != stack.pop():
                    return False
            else:
                stack.append(char)

        return len(stack) == 0
        