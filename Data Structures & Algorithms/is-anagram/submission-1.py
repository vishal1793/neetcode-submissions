class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        dict_s = dict()
        dict_t = dict()
        for i in range(len(s)):
            dict_s[s[i]] = dict_s.get(s[i], 0) + 1
            dict_t[t[i]] = dict_t.get(t[i], 0) + 1
    
        for key in dict_s:
            if dict_s[key] != dict_t.get(key, 0):
                return False
        
        return True

        