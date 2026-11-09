class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {}
        freq2 = {}
        for ch in s1:
            freq2[ch] = freq2.get(ch, 0) + 1
        
        l = 0
        for r in range(len(s2)):
            freq1[s2[r]] = freq1.get(s2[r], 0) + 1

            if (r - l + 1) > len(s1):
                freq1[s2[l]] -= 1
                if freq1[s2[l]] == 0:
                    del freq1[s2[l]]
                
                l += 1

            if freq1 == freq2:
                return True
        
        return False
        
            