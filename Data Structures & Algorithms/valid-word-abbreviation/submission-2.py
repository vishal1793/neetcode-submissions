class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w_index = 0
        a_index = 0
        while w_index < len(word) and a_index < len(abbr):
            if abbr[a_index].isdigit():
                if abbr[a_index] == '0':
                    return False
                num = 0
                while a_index < len(abbr) and abbr[a_index].isdigit():
                    num = num * 10 + int(abbr[a_index])
                    a_index += 1
                
                w_index += num
            
            else:
                if word[w_index] != abbr[a_index]:
                    return False

                w_index += 1
                a_index += 1
                
            
        return (w_index == len(word)) and (a_index == len(abbr))