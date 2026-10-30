class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_s = {}
        freq_t = {}
        for x in s:
            freq_s[x] = freq_s.get(x, 0) + 1
        for x in t:
            freq_t[x] = freq_t.get(x, 0) + 1
        return True if freq_s == freq_t else False
        
