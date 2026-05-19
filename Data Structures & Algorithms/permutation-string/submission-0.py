class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        freqs1 = {}
        freqs2 = {}
        for c in range(len(s1)):
            freqs1[s1[c]] = 1 + freqs1.get(s1[c], 0)
        for r in range(len(s2)):
            freqs2[s2[r]] = 1 + freqs2.get(s2[r], 0)
            if r-l+1 > len(s1):
                freqs2[s2[l]] -= 1
                if freqs2[s2[l]] == 0:
                    del freqs2[s2[l]]
                l += 1
            if r-l+1 == len(s1):
                if freqs2 == freqs1:            
                    return True
        return False
            
            
            
